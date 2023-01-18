---
title: Oracle XML
tags: [db, xml]
date: 2020-04-30
---

## 从关系数据库生成 XML

```sql
-- create the tables
CREATE TABLE customers (
  customer_id INTEGER CONSTRAINT customers_pk PRIMARY KEY,
  first_name VARCHAR2(10) NOT NULL,
  last_name VARCHAR2(10) NOT NULL,
  dob DATE,
  phone VARCHAR2(12),
  type number
);

-- insert sample data into customers table
INSERT INTO customers (
  customer_id, first_name, last_name, dob, phone, type
) VALUES (
  1, 'John', 'Brown', '01-JAN-1965', '800-555-1211', 0
);

INSERT INTO customers (
  customer_id, first_name, last_name, dob, phone, type
) VALUES (
  2, 'Cynthia', 'Green', '05-FEB-1968', '800-555-1212', 0
);

INSERT INTO customers (
  customer_id, first_name, last_name, dob, phone, type
) VALUES (
  3, 'Steve', 'White', '16-MAR-1971', '800-555-1213', 1
);

INSERT INTO customers (
  customer_id, first_name, last_name, dob, phone, type
) VALUES (
  4, 'Gail', 'Black', NULL, '800-555-1214', 1
);

INSERT INTO customers (
  customer_id, first_name, last_name, dob, phone, type
) VALUES (
  5, 'Doreen', 'Blue', '20-MAY-1970', NULL, 1
);

-- commit the transaction
COMMIT;
```

| CUSTOMER_ID | FIRST_NAME | LAST_NAME | DOB       | PHONE        | TYPE |
| ----------- | ---------- | --------- | --------- | ------------ | ---- |
| 1           | John       | Brown     | 1/1/1965  | 800-555-1211 | 0    |
| 2           | Cynthia    | Green     | 2/5/1968  | 800-555-1212 | 0    |
| 3           | Steve      | White     | 3/16/1971 | 800-555-1213 | 1    |
| 4           | Gail       | Black     |           | 800-555-1214 | 1    |
| 5           | Doreen     | Blue      | 5/20/1970 |              | 1    |

### XMLELEMENT

```sql
SELECT XMLELEMENT(
    "customer",
    XMLELEMENT("customer_id", customer_id),
    XMLELEMENT("name", first_name || ' ' || last_name)
  ).GETSTRINGVAL() AS xml_customers
  FROM customers
 WHERE customer_id IN (1, 2);
```

| XML_CUSTOMERS                                                                 |
| ----------------------------------------------------------------------------- |
| `<customer><customer_id>1</customer_id><name>John Brown</name></customer>`    |
| `<customer><customer_id>2</customer_id><name>Cynthia Green</name></customer>` |

### XMLATTRIBUTES

```sql
SELECT XMLELEMENT(
    "customer",
    XMLATTRIBUTES(
      customer_id AS "id",
      first_name || ' ' || last_name AS "name",
      TO_CHAR(dob, 'MM/DD/YYYY') AS "dob"
    )
  ).GETSTRINGVAL() AS xml_customers
  FROM customers
 WHERE customer_id IN (1, 2);
```

| XML_CUSTOMERS                                                        |
| -------------------------------------------------------------------- |
| `<customer id="1" name="John Brown" dob="01/01/1965"></customer>`    |
| `<customer id="2" name="Cynthia Green" dob="02/05/1968"></customer>` |

### XMLFOREST

`XMLFOREST` 不会包含值为空的 Tag.

```sql
SELECT XMLELEMENT(
    "customer",
    XMLFOREST(
      customer_id AS "id",
      first_name || ' ' || last_name AS "name",
      TO_CHAR(dob, 'MM/DD/YYYY') AS "dob",
      '' AS 'empty'
    )
  ).GETSTRINGVAL() AS xml_customers
  FROM customers
 WHERE customer_id IN (1, 2);
```

| XML_CUSTOMERS                                                                    |
| -------------------------------------------------------------------------------- |
| `<customer><id>1</id><name>John Brown</name><dob>01/01/1965</dob></customer>`    |
| `<customer><id>2</id><name>Cynthia Green</name><dob>02/05/1968</dob></customer>` |

### XMLAGG

```sql
SELECT XMLELEMENT(
    "customer_in_group",
    XMLATTRIBUTES(type as "type"),
    XMLAGG(
      XMLELEMENT("name", first_name || ' ' || last_name)
    )
  ).GETSTRINGVAL() AS xml_customers
  FROM customers
 GROUP BY type;
```

| XML_CUSTOMERS                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------- |
| `<customer_in_group type="0"><name>John Brown</name><name>Cynthia Green</name></customer_in_group>`                       |
| `<customer_in_group type="1"><name>Steve White</name><name>Doreen Blue</name><name>Gail Black</name></customer_in_group>` |

### XMLCOLATTVAL

```sql
SELECT XMLELEMENT(
    "customer",
    XMLCOLATTVAL(
      customer_id AS "id",
      dob as "dob"
    )
  ).GETSTRINGVAL() AS xml_customers
  FROM customers
 WHERE customer_id in (1, 2);
```

| XML_CUSTOMERS                                                                                 |
| --------------------------------------------------------------------------------------------- |
| `<customer><column name = "id">1</column><column name = "dob">1965-01-01</column></customer>` |
| `<customer><column name = "id">2</column><column name = "dob">1968-02-05</column></customer>` |

### XMLCONCAT

```sql
SELECT XMLCONCAT(
    XMLELEMENT("name", first_name || ' ' || last_name),
    XMLELEMENT("phone", phone)
  ).GETSTRINGVAL() AS xml_customers
  FROM customers
 WHERE customer_id in (1, 2);
```

| XML_CUSTOMERS                                           |
| ------------------------------------------------------- |
| `<name>John Brown</name><phone>800-555-1211</phone>`    |
| `<name>Cynthia Green</name><phone>800-555-1212</phone>` |

### XMLPARSE

表达式前面

-   CONTENT 意味着表达式必须解析为有效的 XML 值。
-   DOCUMENT 意味着表达式必须解析为带有唯一根元素的 XML 文档。

表达式后面

-   WELLFORMED 意味着保证表达式解析为具有良好格式的 XML 文档。

```sql
SELECT XMLPARSE(
    CONTENT
    '<customer><customer_id>1</customer_id><name>John Brown</name></customer>'
    WELLFORMED
  ).GETSTRINGVAL() AS xml_customer
 FROM dual;
```

| XML_CUSTOMER                                                               |
| -------------------------------------------------------------------------- |
| `<customer><customer_id>1</customer_id><name>John Brown</name></customer>` |

### XMLPI

```sql
SELECT XMLPI(
  NAME "xml-stylesheet",
  'type="text/css" href="example.css"'
).GETSTRINGVAL() AS xml_sheet_pi
FROM dual;
```

| XML_SHEET_PI                                            |
| ------------------------------------------------------- |
| `<?xml-stylesheet type="text/css" href="example.css"?>` |

### XMLCOMMENT

```sql
SELECT XMLCOMMENT(
  'An example XML comment'
).GETSTRINGVAL() AS xml_comment
FROM dual;
```

| XML_COMMENT                     |
| ------------------------------- |
| `<!--An example XML comment-->` |

### XMLSEQUENCE

XMLSEQUENCE() 函数可以生成 XMLSequenceType 对象，XMLSequenceType 对象是 XMLType 对象的变长数组。因为 XMLSEQUENCE() 函数后返回一个变长数组，所以可以在查询的 FROM 子句中使用该函数。

```sql
SELECT VALUE(list_of_values).GETSTRINGVAL() order_values
  FROM TABLE(
    XMLSEQUENCE(
      EXTRACT(
        XMLType('<A><B>PLACED</B><B>PENDING</B><B>SHIPPED</B></A>'),
        '/A/B'
      )
    )
  ) list_of_values;
```

| ORDER_VALUES     |
| ---------------- |
| `<B>PLACED</B>`  |
| `<B>PENDING</B>` |
| `<B>SHIPPED</B>` |

### XMLSERIALIZE

将表达式的求值结果表示为字符串或 LOB (大对象)类型 XML 数据。

-   CONTENT 意味着表达式必须解析为有效的 XML 值。
-   DOCUMENT 意味着表达式必须解析为带有唯一根元素的 XML 文档。

```sql
SELECT XMLSERIALIZE(
    CONTENT XMLType('<order_status>SHIPPED</order_status>')
) AS xml_order_status
FROM DUAL;
```

| XML_ORDER_STATUS |
| ---------------- |
| `<CLOB>`         |

```sql
SELECT XMLSERIALIZE(
    CONTENT XMLType('<order_status>SHIPPED</order_status>') AS BLOB
) AS xml_order_status
FROM DUAL;
```

| XML_ORDER_STATUS |
| ---------------- |
| `<BLOB>`         |

### XMLQUERY

```sql
SELECT XMLQUERY(
    '(1, 2 + 5, "D", 100 to 102, <A>text</A>)'
    RETURNING CONTENT
) AS xml_output
FROM DUAL;
```

| XML_OUTPUT                   |
| ---------------------------- |
| 1 7 D 100 101 102<A>text</A> |

```sql
CREATE PROCEDURE create_xml_resources AS
  v_result BOOLEAN;

  -- create string containing XML for products
  v_products VARCHAR2(300):=
    '<?xml version="1.0"?>' ||
    '<products>' ||
      '<product product_id="1" product_type_id="1" name="Modern Science" price="19.95"/>' ||
      '<product product_id="2" product_type_id="1" name="Chemistry" price="30"/>' ||
      '<product product_id="3" product_type_id="2" name="Supernova" price="25.99"/>' ||
    '</products>';

  -- create string containing XML for product types
  v_product_types VARCHAR2(300):=
    '<?xml version="1.0"?>' ||
    '<product_types>' ||
      '<product_type product_type_id="1" name="Book"/>' ||
      '<product_type product_type_id="2" name="Video"/>' ||
    '</product_types>';
BEGIN
  -- create resource for products
  v_result := DBMS_XDB.CREATERESOURCE('/public/products.xml', v_products);

  -- create resource for product types
  v_result := DBMS_XDB.CREATERESOURCE('/public/product_types.xml', v_product_types);

END create_xml_resources;
/

CALL create_xml_resources();
```

XMLQUERY 从 `/public/products.xml` 资源中检索产品。

```sql
SELECT XMLQUERY(
  'for $product in doc("/public/products.xml")/products/product
   return <product name="{$product/@name}"/>'
   RETURNING CONTENT
).GETSTRINGVAL() AS xml_products
FROM dual;
```

| XML_PRODUCTS                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------- |
| `<product name="Modern Science"></product><product name="Chemistry"></product><product name="Supernova"></product>` |

XMLQUERY 从 `/public/products.xml` 和 `/public/product_types.xml` 资源中检索价格大于 20 的产品以及它们的产品类型。

```sql
SELECT XMLQUERY(
  'for $product in doc("/public/products.xml")/products/product
   let $product_type := doc("/public/product_types.xml")//product_type[@product_type_id = $product/@product_type_id]/@name
   where $product/@price > 20
   order by $product/@product_id
   return <product name="{$product/@name}" product_type="{$product_type}"/>'
   RETURNING CONTENT
).GETSTRINGVAL() AS xml_query_results
FROM dual;
```

| XML_QUERY_RESULTS                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------- |
| `<product name="Chemistry" product_type="Book"></product><product name="Supernova" product_type="Video"></product>` |

XMLQUERY 从 `/public/products.xml` 和 `/public/product_types.xml` 资源中检索产品类型，每种产品类型的产品数量和每种产品类型中产品的平均价格。

```sql
SELECT XMLQUERY(
  'for $product_type in doc("/public/product_types.xml")/product_types/product_type
   let $product := doc("/public/products.xml")//product[@product_type_id = $product_type/@product_type_id]
   return
     <product
       name="{$product_type/@name}"
       num_products="{count($product)}"
       average_price="{xs:integer(avg($product/@price))}"
       />'
   RETURNING CONTENT
).GETSTRINGVAL() AS xml_query_results
FROM dual;
```

| XML_QUERY_RESULTS                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------- |
| `<product name="Book" num_products="2" average_price="24"></product><product name="Video" num_products="1" average_price="25"></product>` |

## 将 XML 文件保存到数据库中

### 示例 XML 文件

purchase_order.xml

```xml
<?xml version="1.0"?>
<purchase_order>
  <customer_order_id>176</customer_order_id>
  <order_date>2007-05-17</order_date>
  <customer_name>Best Products 456 Inc.</customer_name>
  <street>10 Any Street</street>
  <city>Any City</city>
  <state>CA</state>
  <zip>94440</zip>
  <phone_number>555-121-1234</phone_number>
  <products>
    <product>
      <product_id>1</product_id>
      <name>Supernova video</name>
      <quantity>5</quantity>
    </product>
    <product>
      <product_id>2</product_id>
      <name>Oracle SQL book</name>
      <quantity>4</quantity>
    </product>
  </products>
</purchase_order>
```

### 创建示例 XML 模式

-   对象类型 t_product 用来表示产品。
-   嵌套表类型 t_nested_table_product，用来表示产品的嵌套表。
-   表 purchase_order，用来保存购货单。

purchase_order 中的 xml_purchase_order 类型是 XMLType，允许存储 XML 数据。

```sql
-- create the types
CREATE TYPE t_product AS OBJECT (
  product_id INTEGER,
  name VARCHAR2(15),
  quantity INTEGER
);
/

CREATE TYPE t_nested_table_product AS TABLE OF t_product;
/

-- create the table
CREATE TABLE purchase_order (
  purchase_order_id INTEGER CONSTRAINT purchase_order_pk PRIMARY KEY,
  customer_order_id INTEGER,
  order_date DATE,
  customer_name VARCHAR2(25),
  street VARCHAR2(15),
  city VARCHAR2(15),
  state VARCHAR2(2),
  zip VARCHAR2(5),
  phone_number VARCHAR2(12),
  products t_nested_table_product,
  xml_purchase_order XMLType
)
NESTED TABLE products
STORE AS nested_products;

-- create the directory (you may need to modify this line)
-- then copy purchase_order.xml to the directory and grant permission `chmod '/usr/tmp/edi/purchase_order.xml' 777`
CREATE OR REPLACE DIRECTORY XML_FILES_DIR AS '/usr/tmp/edi';
SELECT * FROM ALL_DIRECTORIES WHERE DIRECTORY_NAME = 'XML_FILES_DIR';

-- add a row to the table
INSERT INTO purchase_order (
  purchase_order_id,
  xml_purchase_order
) VALUES (
  1,
  XMLType(
    BFILENAME('XML_FILES_DIR', 'purchase_order.xml'),  -- 指向外部文件的指针
    NLS_CHARSET_ID('AL32UTF8') -- 标准 UTF-8 编码
  )
);

SELECT * FROM purchase_order;
```

| PURCHASE_ORDER_ID | CUSTOMER_ORDER_ID | ORDER_DATE | CUSTOMER_NAME | STREET | CITY | STATE | ZIP | PHONE_NUMBER | PRODUCTS       | XML_PURCHASE_ORDER |
| ----------------- | ----------------- | ---------- | ------------- | ------ | ---- | ----- | --- | ------------ | -------------- | ------------------ |
| 1                 |                   |            |               |        |      |       |     |              | `<Collection>` | `<XMLTYPE>`        |

### 从示例 XML 检索信息

EXTRACT() 函数的返回值是 XMLType 对象。

```sql
SELECT
    EXTRACT(xml_purchase_order, '/purchase_order/customer_order_id') cust_order_id,
    EXTRACT(xml_purchase_order, '/purchase_order/order_date') order_date,
    EXTRACT(xml_purchase_order, '/purchase_order/customer_name') cust_name,
    EXTRACT(xml_purchase_order, '/purchase_order/phone_number') phone_number
  FROM purchase_order
 WHERE purchase_order_id = 1;
```

| CUST_ORDER_ID | ORDER_DATE  | CUST_NAME   | PHONE_NUMBER |
| ------------- | ----------- | ----------- | ------------ |
| `<XMLTYPE>`   | `<XMLTYPE>` | `<XMLTYPE>` | `<XMLTYPE>`  |

EXTRACTVALUE() 函数的返回值是字符串。

```sql
SELECT
    EXTRACTVALUE(xml_purchase_order, '/purchase_order/customer_order_id') cust_order_id,
    EXTRACTVALUE(xml_purchase_order, '/purchase_order/order_date') order_date,
    EXTRACTVALUE(xml_purchase_order, '/purchase_order/customer_name') cust_name,
    EXTRACTVALUE(xml_purchase_order, '/purchase_order/phone_number') phone_number
  FROM purchase_order
 WHERE purchase_order_id = 1;
```

| CUST_ORDER_ID | ORDER_DATE | CUST_NAME              | PHONE_NUMBER |
| ------------- | ---------- | ---------------------- | ------------ |
| 176           | 2007-05-17 | Best Products 456 Inc. | 555-121-1234 |

检索所有商品。

```sql
SELECT
    EXTRACT(xml_purchase_order, '/purchase_order//products').GETSTRINGVAL() xml_products
  FROM purchase_order
 WHERE purchase_order_id = 1;
```

xml_products

```xml
<products>
  <product>
    <product_id>1</product_id>
    <name>Supernova video</name>
    <quantity>5</quantity>
  </product>
  <product>
    <product_id>2</product_id>
    <name>Oracle SQL book</name>
    <quantity>4</quantity>
  </product>
</products>
```

检索产品 #2.

```sql
SELECT
    EXTRACT(xml_purchase_order, '/purchase_order/products/product[2]').GETSTRINGVAL() xml_product
  FROM purchase_order
 WHERE purchase_order_id = 1;
```

检索 "Supernova video" 产品。

```sql
 SELECT
    EXTRACT(xml_purchase_order, '/purchase_order/products/product[name="Supernova video"]').GETSTRINGVAL() xml_product
  FROM purchase_order
 WHERE purchase_order_id = 1;
```

使用 EXISTSNODE() 函数检查 XML 元素是否存在，如果元素存在 EXISTSNODE() 函数返回 1，否则返回 0。

```sql
 SELECT 'EXISTS'
  FROM purchase_order
 WHERE purchase_order_id = 1
   AND EXISTSNODE(
     xml_purchase_order,
     '/purchase_order/products/product[product_id=1]') = 1;

--EXISTS
```

XMLSEQUENCE 将产品检索为 XMLType 对象的变长数组

```sql
SELECT product.column_value--.GETSTRINGVAL()
  FROM TABLE(
    SELECT
       XMLSEQUENCE(EXTRACT(xml_purchase_order, '/purchase_order//product'))
      FROM purchase_order
     WHERE purchase_order_id = 1) product;
```

| PRODUCT.COLUMN_VALUE |
| -------------------- |
| `<XMLTYPE>`          |
| `<XMLTYPE>`          |

使用 EXTRACTVALUE() 函数将产品的 product_id, name 和 quantity 检索为字符串。

```sql
SELECT
    EXTRACTVALUE(product.column_value, '/product/product_id') AS product_id,
    EXTRACTVALUE(product.column_value, '/product/name') AS name,
    EXTRACTVALUE(product.column_value, '/product/quantity') AS quantity
  FROM TABLE(
    SELECT
       XMLSEQUENCE(EXTRACT(xml_purchase_order, '/purchase_order//product'))
      FROM purchase_order
     WHERE purchase_order_id = 1) product;
```

| PRODUCT_ID | NAME            | QUANTITY |
| ---------- | --------------- | -------- |
| 1          | Supernova video | 5        |
| 2          | Oracle SQL book | 4        |

### 更新示例 XML 模式中的信息

```sql
CREATE PROCEDURE update_purchase_order(
  p_purchase_order_id IN purchase_order.purchase_order_id%TYPE
) AS
  v_count INTEGER := 1;

  -- declare a nested table to store products
  v_nested_table_products t_nested_table_product :=
    t_nested_table_product();

  -- declare a type to represent a product record
  TYPE t_product_record IS RECORD (
    product_id INTEGER,
    name VARCHAR2(15),
    quantity INTEGER
  );

  -- declare a REF CURSOR type to point to product records
  TYPE t_product_cursor IS REF CURSOR RETURN t_product_record;

  -- declare a cursor
  v_product_cursor t_product_cursor;

  -- declare a variable to store a product record
  v_product t_product_record;
BEGIN
  -- open v_product_cursor to read the product_id, name, and quantity for
  -- each product stored in the XML of the xml_purchase_order column
  -- in the purchase_order table
  OPEN v_product_cursor FOR
  SELECT
    EXTRACTVALUE(product.COLUMN_VALUE, '/product/product_id')
      AS product_id,
    EXTRACTVALUE(product.COLUMN_VALUE, '/product/name') AS name,
    EXTRACTVALUE(product.COLUMN_VALUE, '/product/quantity') AS quantity
  FROM TABLE(
    SELECT
      XMLSEQUENCE(EXTRACT(xml_purchase_order, '/purchase_order//product'))
    FROM purchase_order
    WHERE purchase_order_id = p_purchase_order_id
  ) product;

  -- loop over the contents of v_product_cursor
  LOOP
    -- fetch the product records from v_product_cursor and exit when there
    -- are no more records found
    FETCH v_product_cursor INTO v_product;
    EXIT WHEN v_product_cursor%NOTFOUND;

    -- extend v_nested_table_products so that a product can be stored in it
    v_nested_table_products.EXTEND;

    -- create a new product and store it in v_nested_table_products
    v_nested_table_products(v_count) :=
      t_product(v_product.product_id, v_product.name, v_product.quantity);

    -- display the new product stored in v_nested_table_products
    DBMS_OUTPUT.PUT_LINE('product_id = ' ||
      v_nested_table_products(v_count).product_id);
    DBMS_OUTPUT.PUT_LINE('name = ' ||
      v_nested_table_products(v_count).name);
    DBMS_OUTPUT.PUT_LINE('quantity = ' ||
      v_nested_table_products(v_count).quantity);

    -- increment v_count ready for the next iteration of the loop
    v_count := v_count + 1;
  END LOOP;

  -- close v_product_cursor
  CLOSE v_product_cursor;

  -- update the purchase_order table using the values extracted from the
  -- XML stored in the xml_purchase_order column (the products nested
  -- table is set to v_nested_table_products already populated by the
  -- previous loop)
  UPDATE purchase_order
  SET
    customer_order_id =
      EXTRACTVALUE(xml_purchase_order,
        '/purchase_order/customer_order_id'),
    order_date =
      TO_DATE(EXTRACTVALUE(xml_purchase_order,
        '/purchase_order/order_date'), 'YYYY-MM-DD'),
    customer_name =
      EXTRACTVALUE(xml_purchase_order, '/purchase_order/customer_name'),
    street =
      EXTRACTVALUE(xml_purchase_order, '/purchase_order/street'),
    city =
      EXTRACTVALUE(xml_purchase_order, '/purchase_order/city'),
    state =
      EXTRACTVALUE(xml_purchase_order, '/purchase_order/state'),
    zip =
      EXTRACTVALUE(xml_purchase_order, '/purchase_order/zip'),
    phone_number =
      EXTRACTVALUE(xml_purchase_order, '/purchase_order/phone_number'),
    products = v_nested_table_products
  WHERE purchase_order_id = p_purchase_order_id;

  -- commit the transaction
  COMMIT;
END update_purchase_order;
/


CALL update_purchase_order();
```

## Practice Example

### Generate HTML Table from DB Table

1. 多个 XMLELEMENT 可以使用 XMLFOREST 简化，但是 XMLFOREST 不会包含值为空的 Tag, 这里 po_release_number 可能为空，所以不使用 XMLFOREST。
2. 一个 PO_NUMBER 可以包含多条记录，但是只需要一个 Table  Header, 所以资料需要根据 PO 进行聚合，XMLAGG 可以连接聚合的多个记录。

```sql
select yeh.po_number,
       XMLELEMENT("table",
         XMLCONCAT(
           XMLELEMENT("tr", 
             XMLELEMENT("th", 'EDI Type'),
             XMLELEMENT("th", 'PO Number'),
             XMLELEMENT("th", 'PO Release Number'),
             XMLELEMENT("th", 'PO Date'),
             XMLELEMENT("th", 'Ship to Code'),
             XMLELEMENT("th", 'Ship to Name'),
             XMLELEMENT("th", 'Sold to Code'),
             XMLELEMENT("th", 'Sold to Name')
           ),
           XMLAGG( 
             XMLELEMENT("tr", 
               XMLELEMENT("td", yeh.edi_type),
               XMLELEMENT("td", yeh.po_number),
               XMLELEMENT("td", yeh.po_release_number),
               XMLELEMENT("td", yeh.po_date),
               XMLELEMENT("td", yea_ship.code),
               XMLELEMENT("td", yea_ship.name),
               XMLELEMENT("td", yea_sold.code),
               XMLELEMENT("td", yea_sold.name)
             )
           )
         )
       ).getStringVal() as table_str
   from ysc_edi_inbound_header  yeh,
       ysc_edi_inbound_address  yea_ship,
       ysc_edi_inbound_address  yea_sold
 where yeh.header_id = yea_ship.header_id
   and yeh.header_id = yea_sold.header_id
   and yea_ship.identifier_code = 'ST'
   and yea_sold.identifier_code = 'BY'
   and yeh.header_id = 1
 group by yeh.po_number;
```

| PO_NUMBER  | TABLE_STR                                                    |
| ---------- | ------------------------------------------------------------ |
| 2211100025 | `<table><tr><th>EDI Type</th><th>PO Number</th><th>PO Release Number</th><th>PO Date</th><th>Ship to Code</th><th>Ship to Name</th><th>Sold to Code</th><th>Sold to Name</th></tr><tr><td>855</td><td>2211100025</td><td></td><td>20211130</td><td>147</td><td>XXX TECHNOLOGIES</td><td>84</td><td>XXX TECHNOLOGIES</td></tr></table>` |

## XML namespace

使用 XMLTable 解析 XML 如果 XML 包含 namespace, 会解析不到数据。

```sql
select item.*
  from som_edi_customer_source ses,
       xmltable(
         '/Pip3A4PurchaseOrderRequest/PurchaseOrder/ProductLineItem'
          passing xmltype(ses.memo)  --memo type is clob, if memo is xmltype can direct use passing ses.memo
          columns
            cust_name varchar2(1000) path 'CustomerInformation/businessName',
            cust_po_number varchar2(1000) path 'PartnerBusiness/BusinessIdentifier'
       ) item
where ses.seq_id = p_seq_id;
```

解决方法 1：添加 xmlnamespace

```sql
select item.*
from som_edi_customer_source ses,
     xmltable(
        --xmlnamespaces('http://schemas.microsoft.com/xxx.dtd' as "ns"),
        xmlnamespaces(default 'http://schemas.microsoft.com/xxx.dtd'),
        '/Pip3A4PurchaseOrderRequest/PurchaseOrder/ProductLineItem'
        passing xmltype(ses.memo)
        columns
          cust_name varchar2(1000) path'CustomerInformation/businessName',
          cust_po_number varchar2(1000) path 'PartnerBusiness/BusinessIdentifier'
      ) item
where ses.seq_id = p_seq_id;
```

解决方法 2: 解析前先移除 namespace

```sql
function remove_namespace(p_xml_clob clob) return clob is
  l_return clob;
  l_taiwan_namespace varchar2(100) := 'xmlns="http://schemas.microsoft.com/xxx.dtd"';
  l_china_namespace  varchar2(100) := 'xmlns="http://schemas.microsoft.com/yyy.dtd"';
begin
  begin
    select replace(replace(p_xml_clob, l_china_namespace, null),
                   l_taiwan_namespace,
                   null)
      into l_return
      from dual;
  end;
  return l_return;
end remove_namespace;
```

```sql
 select item.*
  from (select seq_id, remove_namespace(memo) as memo 
          from som_edi_customer_source) ses,
       xmltable(
         '/Pip3A4PurchaseOrderRequest/PurchaseOrder/ProductLineItem'
         passing xmltype(ses.memo)
         columns
           cust_name varchar2(1000) path'CustomerInformation/businessName',
           cust_po_number varchar2(1000) path 'PartnerBusiness/BusinessIdentifier'
       ) item
where ses.seq_id = p_seq_id;
```

为生成的 XML 添加 default namespace。

`xmlattributes('microsoft.com' as "xmlns:prx")`

```sql
select (
    xmlelement("Pip3A4PurchaseOrderConfirmation",
      --add default namespace
      xmlattributes('microsoft.com' as "xmlns:prx"),
      xmlelement("PurchaseOrder",
        ( -- line loop
          select (
            xmlelement("ProductLineItem",
              xmlelement("buyerLineItem",
                xmlelement("LineNumber", sel.line_number)
              )
              xmlelement("OrderQuantity",
                xmlelement("requestedQuantity",
                  xmlelement("ProductQuantity", order_line.ordered_quantity)
                )
              )
            )
          )
           from oe_order_lines_all order_line,
                som_edi_customer_3a4_line sel
          where order_line.header_id = order_header.header_id
            and order_line.customer_line_number = sel.po_line_number
            and sel.header_id = seh.header_id
        ) as "line"
      ),
      xmlelement("requestingDocumentDateTime",
        xmlelement("DateTimeStamp", som_edi_customer_pkg.get_customer_format_date(sysdate))
      )
    )
  ).getClobVal() as "header" into l_clob_xml
from oe_order_headers_all         order_header,
     som_edi_customer_3a4_header  seh
where 1 = 1
  and order_header.cust_po_number = seh.po_number
  and seh.po_number = p_customer_po;
```

输出的 XML root element 如下:

```xml
<Pip3A4PurchaseOrderConfirmation xmlns:prx="microsoft.com">
</Pip3A4PurchaseOrderConfirmation>
```

## cx_Oracle working with XMLTYPE

> [Working with XMLTYPE — cx_Oracle 8.3.0-dev documentation](https://cx-oracle.readthedocs.io/en/latest/user_guide/xml_data_type.html)

Oracle XMLType columns are fetched as strings by default. This is currently limited to the maximum length of a `VARCHAR2` column. To return longer XML values, they must be queried as LOB values instead.

The examples below demonstrate using XMLType data with cx_Oracle. The following table will be used in these examples:

```sql
CREATE TABLE xml_table (
    id NUMBER,
    xml_data SYS.XMLTYPE
);
```

Inserting into the table can be done by simply binding a string as shown:

```python
xml_data = """<?xml version="1.0"?>
        <customer>
            <name>John Smith</name>
            <Age>43</Age>
            <Designation>Professor</Designation>
            <Subject>Mathematics</Subject>
        </customer>"""
cursor.execute("insert into xml_table values (:id, :xml)",
               id=1, xml=xml_data)
```

This approach works with XML strings up to 1 GB in size. For longer strings, a temporary CLOB must be created using [`Connection.createlob()`](https://cx-oracle.readthedocs.io/en/latest/api_manual/connection.html#Connection.createlob) and bound as shown:

```python
clob = connection.createlob(cx_Oracle.DB_TYPE_CLOB)
clob.write(xml_data)
cursor.execute("insert into xml_table values (:id, sys.xmltype(:xml))",
               id=2, xml=clob)
```

Fetching XML data can be done simply for values that are shorter than the length of a VARCHAR2 column, as shown:

```python
cursor.execute("select xml_data from xml_table where id = :id", id=1)
xml_data, = cursor.fetchone()
print(xml_data)          # will print the string that was originally stored
```

For values that exceed the length of a VARCHAR2 column, a CLOB must be returned instead by using the function `XMLTYPE.GETCLOBVAL()` as shown:

```python
cursor.execute("""
        select xmltype.getclobval(xml_data)
        from xml_table
        where id = :id""", id=1)
clob, = cursor.fetchone()
print(clob.read())
```

The LOB that is returned can be streamed or a string can be returned instead of a CLOB. See [Using CLOB and BLOB Data](https://cx-oracle.readthedocs.io/en/latest/user_guide/lob_data.html#lobdata) for more information about processing LOBs.
