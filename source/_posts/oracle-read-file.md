---
title: UTL_FILE - Random Access of Files
tag: db
date: 2021-05-25
---

> 转载： [ORACLE-BASE - UTL_FILE - Random Access of Files](https://oracle-base.com/articles/9i/utl_file-random-access-of-files-9i)

I was recently asked if I could read the first and last line of a file using PL/SQL. Until recently this was not possible without reading the whole file or using a Java stored procedure, but Oracle9i Release 2 supports random access of files through the `UTL_FILE` package. This article shows a simple mechanism to solve this problem using these UTL_FILE enhancements.

First we create a directory object pointing to the location of the file of interest.

```sql
CREATE OR REPLACE DIRECTORY MY_DOCS AS '/usr/users/oracle/';
SELECT * FROM ALL_DIRECTORIES WHERE DIRECTORY_NAME = 'MY_DOCS';
```

Prior to Oracle9i Release 2 I would solve this problem by reading the whole file as follows.

```sql
SET SERVEROUTPUT ON SIZE 1000000
DECLARE
  l_file         UTL_FILE.file_type;
  l_location     VARCHAR2(100) := 'MY_DOCS';
  l_filename     VARCHAR2(100) := 'temp';
  l_text         VARCHAR2(32767);
BEGIN
  -- Open file.
  l_file := UTL_FILE.fopen(l_location, l_filename, 'r', 32767);
  
  -- Read and output first line.
  UTL_FILE.get_line(l_file, l_text, 32767);
  DBMS_OUTPUT.put_line('First Line: |' || l_text || '|');

  -- Read through the file until we reach the last line.
  BEGIN
    LOOP
      UTL_FILE.get_line(l_file, l_text, 32767);
    END LOOP;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      NULL;
  END;
  
  -- Output the last line.
  DBMS_OUTPUT.put_line('Last Line : |' || l_text || '|');

  -- Close the file.
  UTL_FILE.fclose(l_file);
END;
/
```

Using the `UTL_FILE` enhancements we can now do the following.

```sql
SET SERVEROUTPUT ON SIZE 1000000
DECLARE
  l_file         UTL_FILE.file_type;
  l_location     VARCHAR2(100) := 'MY_DOCS';
  l_filename     VARCHAR2(100) := 'temp';
  l_exists       BOOLEAN;
  l_file_length  NUMBER;
  l_blocksize    NUMBER;
  l_text         VARCHAR2(32767);
BEGIN
  UTL_FILE.fgetattr(l_location, l_filename, l_exists, l_file_length, l_blocksize);

  IF l_exists THEN
    -- Open file.
    l_file := UTL_FILE.fopen(l_location, l_filename, 'r', 32767);
    
    -- Read and output first line.
    UTL_FILE.get_line(l_file, l_text, 32767);
    DBMS_OUTPUT.put_line('First Line: |' || l_text || '|');
    UTL_FILE.FSEEK (l_file, l_file_length-1);
  
    -- Step backwards through the file until we reach the start of the last line.
    FOR i IN REVERSE 0 .. l_file_length-2 LOOP
      UTL_FILE.FSEEK (l_file, NULL, -2);
      UTL_FILE.get_line(l_file, l_text, 1);
      EXIT WHEN l_text IS NULL;
    END LOOP;
    
    -- Read and output the last line.
    UTL_FILE.get_line(l_file, l_text, 32767);
    DBMS_OUTPUT.put_line('Last Line : |' || l_text || '|');
  
    -- Close the file.
    UTL_FILE.fclose(l_file);
  END IF;
END;
/
```

The `FGETATTR` procedure allows us to check that the file exists and return the file length. We then read the first line using the `GET_LINE` procedure as normal. To get the last line we need to skip to the end of the file using the `FSEEK` procedure and work backwards until we hit a line terminator. The `GET_LINE` procedure does not return line terminators so we detect it's presence by checking for the return of an empty line. We can then display the last line.

I'm not too sure about the performance of the `FSEEK` procedure. For large files it's often quicker to read the whole file which is a bit disappointing. Even so, if you need to move both backwards and forwards in the file, these enhancements may still be useful.

For more information see:

- [UTL_FILE Enhancements](https://oracle-base.com/articles/9i/utl_file-enhancements-9i)
- [Export BLOB Contents Using UTL_FILE](https://oracle-base.com/articles/9i/export-blob-9i)
- [UTL_FILE](http://docs.oracle.com/cd/E11882_01/appdev.112/e40758/u_file.htm)

补充使用  UTL_FILE  写文件。

```sql
  -- CREATE OR REPLACE DIRECTORY EDI_TEST AS '/usr/tmp/edi/test';
  -- putty login to server and cd /usr/tmp/edi/test, then touch test.html and chmod 777 test.xml
  -- write_xml_data_to_file('EDI_TEST', 'test.xml')
  PROCEDURE write_xml_data_to_file(
    p_directory VARCHAR2,
    p_file_name VARCHAR2
  ) AS
    v_file UTL_FILE.FILE_TYPE;
    v_amount INTEGER := 32767;
    v_xml_data XMLType;
    v_char_buffer VARCHAR2(32767);
  BEGIN
    -- open the file for writing of text (up to v_amount
    -- characters at a time)
    v_file := UTL_FILE.FOPEN(p_directory, p_file_name, 'w', v_amount);
    
    -- write the starting line to v_file
    UTL_FILE.PUT_LINE(v_file, '<?xml version="1.0"?>');

    -- retrieve the customers and store them in v_xml_data
    SELECT
      EXTRACT(
        XMLELEMENT(
          "emps",
          XMLAGG(
            XMLELEMENT("emp", empno || ' - ' || ename)
            ORDER BY empno
          )
        ),
        '/emps'
      )
    AS xml_emps
    INTO v_xml_data
    FROM scott.emp;

    -- get the string value from v_xml_data and store it in v_char_buffer
    v_char_buffer := v_xml_data.GETSTRINGVAL();

    -- copy the characters from v_char_buffer to the file
    UTL_FILE.PUT(v_file, v_char_buffer);

    -- flush any remaining data to the file
    UTL_FILE.FFLUSH(v_file);

    -- close the file
    UTL_FILE.FCLOSE(v_file);
  END write_xml_data_to_file;
  
end som_edi_custom_utils_pkg;
/
```

