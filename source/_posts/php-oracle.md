---
title: PHP connect Oracle
tags: php
date: 2019-10-31
---

1. install php_oci8_11g 

   - **php -i** view phpinfo, php7.4-ts-x64.

     PHP Version => 7.4.0
     Architecture => x64
     PHP Extension Build => API20190902,TS,VC15

   -  download  php_oci8_11g

      go to [PECL :: Package :: oci8 2.2.0 for Windows](https://pecl.php.net/package/oci8/2.2.0/windows) download 7.4 Thread Safe (TS) x64 .

   - config php.ini

     add  `extension=php_oci8_11g.dll` in php.ini

2. install oracle instant_client

   download oracle instant_client 11g 64bit, instant_client version must match php architecture, such as php-x64 instant_client must is x64.

3. test connection

   ```php
   <?php
   
   $conn = oci_connect('xxx', 'xxx', 'www.jbn.com:1523/DEV');
   if (!$conn) {
       $e = oci_error();
       echo $e['message'];
   }
   
   
   $stid = oci_parse($conn, 'SELECT empno, ename, job FROM scott.emp');
   oci_execute($stid);
   
   
   while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
       foreach ($row as $item) {
           echo $item . " ";
       }
       echo "\n";
   }
   ```

   

