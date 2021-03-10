---
title: oracle xml
tags: db
date: 2020-04-30
---

### namespace

1.使用 xmltable 解析 xml, 如果 xml 包含 namespace, 会解析不到数据

```sql
select item.*
  from som_edi_customer_source ses,
      xmltable(
        '/Pip3A4PurchaseOrderRequest/PurchaseOrder/ProductLineItem'
        passing xmltype(ses.memo)  --memo type is clob, if memo is xmltype can direct use passing ses.memo
        columns
          cust_name varchar2(1000) path'CustomerInformation/businessName',
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
  from (select seq_id, som_edi_customer_pkg.remove_namespace(memo) as memo from som_edi_customer_source) ses,
      xmltable(
        '/Pip3A4PurchaseOrderRequest/PurchaseOrder/ProductLineItem'
        passing xmltype(ses.memo)
        columns
          cust_name varchar2(1000) path'CustomerInformation/businessName',
          cust_po_number varchar2(1000) path 'PartnerBusiness/BusinessIdentifier'
      ) item
where ses.seq_id = p_seq_id;
```

2.为生成的 xml 添加 default namespace

`xmlattributes('microsoft.com' as "xmlns:prx")`

```sql
select (
    xmlelement("Pip3A4PurchaseOrderConfirmation",
      --Add default namespace
      xmlattributes('microsoft.com' as "xmlns:prx"),
      xmlelement("PurchaseOrder",
        (
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
from oe_order_headers_all          order_header,
     som_edi_customer_3a4_header   seh,
     som_edi_sercomm_information   sei
where 1 = 1
  and order_header.cust_po_number = seh.po_number
  and sei.customer_name = 'customer'
  and seh.po_number = p_customer_po;
```

输出的 xml root element 如下

```xml
<Pip3A4PurchaseOrderConfirmation xmlns:prx="microsoft.com">
</Pip3A4PurchaseOrderConfirmation>
```
