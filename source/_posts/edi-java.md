---
title: Reading EDI Data in Java
tags: edi
date: 2021-06-08
---

> 转载: [Reading EDI Data in Java - DZone Java](https://dzone.com/articles/reading-edi-data-in-java)

These days, most Java developers expect to deal with JSON to exchange data with other systems and businesses. However, what happens when JSON is not an option? It's easy to forget that there are other formats for data exchange, some of which are more difficult to handle. One such format is known as EDI. EDI itself comes in several flavors — for example, X12 and EDIFACT — so code to read it may not always be "one size fits all."

On the surface, reading EDI data seems to be a simple endeavor. A developer may see a sample file and attempt to read it using the basic string parsing APIs available in his or her programming language's standard library. Unfortunately, this may not always work and it becomes difficult to do data validation and handle the structure of the document effectively.

## What Is EDI? An Introduction

EDI is a general term that covers several standard data formats for exchanging data between businesses (or any two parties). Two of the most commonly used standards are X12 and EDIFACT. Both of these standards represent data in a sequence of named segments (which are basically records containing individual fields). For example, a simple segment might look like this:

```
SEG*SMITH*JOHN*20190101~
```

EDI also has a structure similar to XML or JSON where segments are nested within begin/end boundaries known as loops. In the example, the X12 acknowledgment exchange is shown below; the indentation is added to emphasize the structure. However, in practice, the structure is not apparent by looking at an unformatted EDI file.

```
ISA*00*          *00*          *ZZ*Receiver       *ZZ*Sender         *191031*1301*^*00501*000000001*0*P*:~
  GS*FA*ReceiverDept*SenderDept*20191031*130123*000001*X*005010X230~
    ST*997*0001~
      AK1*HC*000001~
        AK2*837*0001~
          AK3*NM1*8**8~
          AK4*8*66*7*MI~
        AK5*R*5~
      AK9*R*1*1*0~
    SE*8*0001~
  GE*1*000001~
IEA*1*000000001~
```

## Reading EDI as a Stream of Events

One option for reading EDI is to process the data as a stream of events. The [StAEDI](https://github.com/xlate/staedi) (pronounced "steady") Java library takes the same approach for EDI that the standard Java StAX API takes for processing XML — a stream of events. A simple program that only lists the names of the segments could look something like this:

```java
EDIInputFactory factory = EDIInputFactory.newFactory();
InputStream stream = new FileInputStream("my_edi_file.txt");
EDIStreamReader reader = factory.createEDIStreamReader(stream);
EDIStreamEvent event;

while (reader.hasNext()) {
  event = reader.next();

  if (event == EDIStreamEvent.START_SEGMENT) {
    System.out.println("Segment: " + reader.getText());
  }
}
```

If you are familiar with the StAX API for XML, this should look familiar. The `EDIStreamReader` is used in a loop similar to an iterator or a database result set. Each call to the `next` method will return the next data event from the EDI file. In addition to events for the start of a segment, there are events for handling:

- Beginning and end of an interchange ( `ISA` / `IEA`  in X12,  `UNB` / `UNZ`  for EDIFACT)
- Beginning and end of a message group ( `GS` / `GE`  in X12,  `UNG` / `UNE`  for EDIFACT)
- Beginning and end of a transaction ( `ST` / `SE`  in X12,  `UNH` / `UNT`  for EDIFACT)
- Beginning and end of a loop (depending on configuration)
- Beginning and end of a segment
- Beginning and end of a composite element
- Individual data elements
- Segment errors
- Data element errors

## What About Structure and Validation?

Processing EDI using [StAEDI](https://github.com/xlate/staedi) will give you only basic structure and validation (interchange, group, and transaction envelop structures). If you need to handle the structure and validation of the data within a transaction (and you probably do), a *schema* must be provided. A schema is loosely based on standard XML schema syntax and provides details on the order of segments and elements in your transaction. Additionally, constraints may be placed on the length and data type of elements.

An EDI schema for the example X12 `997`  transaction above could be defined using the following XML. The `transaction`  element and its sub-elements define the structure of the transaction. Each segment references `segmentType`  elements defined below, and each `segmentType`  references  `elementType` s and  `compositeType` s as necessary. Enumerated values for `identifier`  element types have been mostly omitted for brevity.

```xml
<schema xmlns="http://xlate.io/EDISchema/v2">
  <transaction>
    <sequence>
      <segment ref="AK1" minOccurs="1" />
      <loop code="2000" maxOccurs="999999">
        <sequence>
          <segment ref="AK2" />
          <loop code="2100" maxOccurs="999999">
            <sequence>
              <segment ref="AK3" />
              <segment ref="AK4" maxOccurs="99" />
            </sequence>
          </loop>
          <segment ref="AK5" minOccurs="1" />
        </sequence>
      </loop>
      <segment ref="AK9" minOccurs="1" />
    </sequence>
  </transaction>

  <elementType name="E0002" number="2" base="numeric" maxLength="6" />
  <elementType name="E0028" number="28" base="numeric" maxLength="9" />
  <elementType name="E0097" number="97" base="numeric" maxLength="6" />
  <elementType name="E0123" number="123" base="numeric" maxLength="6" />
  <elementType name="E0143" number="143" base="identifier" minLength="3" maxLength="3" />
  <elementType name="E0329" number="329" base="string" minLength="4" maxLength="9" />
  <elementType name="E0447" number="447" base="string" maxLength="4" />
  <elementType name="E0479" number="479" base="identifier" minLength="2" maxLength="2" />
  <elementType name="E0480" number="480" base="string" maxLength="12" />
  <elementType name="E0715" number="715" base="identifier">
    <enumeration>
      <value>A</value>
      <value>E</value>
      <value>M</value>
      <value>P</value>
      <value>R</value>
      <value>W</value>
      <value>X</value>
    </enumeration>
  </elementType>
  <elementType name="E0716" number="716" base="identifier" maxLength="3" />
  <elementType name="E0717" number="717" base="identifier">
    <enumeration>
      <value>A</value>
      <value>E</value>
      <value>M</value>
      <value>R</value>
      <value>W</value>
      <value>X</value>
    </enumeration>
  </elementType>
  <elementType name="E0718" number="718" base="identifier" maxLength="3" />
  <elementType name="E0719" number="719" base="numeric" maxLength="10" />
  <elementType name="E0720" number="720" base="identifier" maxLength="3" />
  <elementType name="E0721" number="721" base="string" minLength="2" maxLength="3" />
  <elementType name="E0722" number="722" base="numeric" maxLength="2" />
  <elementType name="E0723" number="723" base="identifier" maxLength="3" />
  <elementType name="E0724" number="724" base="string" maxLength="99" />
  <elementType name="E0725" number="725" base="numeric" maxLength="4" />
  <elementType name="E1528" number="1528" base="numeric" maxLength="2" />
  <elementType name="E1686" number="1686" base="numeric" maxLength="4" />
  <elementType name="E1705" number="1705" base="string" maxLength="35" />
  <compositeType name="C030">
    <sequence>
      <element ref="E0722" minOccurs="1" />
      <element ref="E1528" />
      <element ref="E1686" />
    </sequence>
  </compositeType>
  <segmentType name="AK1">
    <sequence>
      <element ref="E0479" minOccurs="1" />
      <element ref="E0028" minOccurs="1" />
      <element ref="E0480" />
    </sequence>
  </segmentType>
  <segmentType name="AK2">
    <sequence>
      <element ref="E0143" minOccurs="1" />
      <element ref="E0329" minOccurs="1" />
      <element ref="E1705" />
    </sequence>
  </segmentType>
  <segmentType name="AK3">
    <sequence>
      <element ref="E0721" minOccurs="1" />
      <element ref="E0719" minOccurs="1" />
      <element ref="E0447" />
      <element ref="E0720" />
    </sequence>
  </segmentType>
  <segmentType name="AK4">
    <sequence>
      <composite ref="C030" minOccurs="1" />
      <element ref="E0725" />
      <element ref="E0723" minOccurs="1" />
      <element ref="E0724" />
    </sequence>
  </segmentType>
  <segmentType name="AK5">
    <sequence>
      <element ref="E0717" minOccurs="1" />
      <element ref="E0718" />
      <element ref="E0718" />
      <element ref="E0718" />
      <element ref="E0718" />
      <element ref="E0718" />
    </sequence>
  </segmentType>
  <segmentType name="AK9">
    <sequence>
      <element ref="E0715" minOccurs="1" />
      <element ref="E0097" minOccurs="1" />
      <element ref="E0123" minOccurs="1" />
      <element ref="E0002" minOccurs="1" />
      <element ref="E0716" />
      <element ref="E0716" />
      <element ref="E0716" />
      <element ref="E0716" />
      <element ref="E0716" />
    </sequence>
  </segmentType>
</schema>
```

Using a schema while parsing an EDI file is straight-forward. As the program iterates over the event stream, the application code must provide a Schema object at the start of a transaction. **(before end of segment)**

```java
EDIInputFactory factory = EDIInputFactory.newFactory();
InputStream stream = new FileInputStream("my_edi_file.txt");
EDIStreamReader reader = factory.createEDIStreamReader(stream);

while (reader.hasNext()) {
  EDIStreamEvent event = reader.next();

  if (event == EDIStreamEvent.START_TRANSACTION) {
    SchemaFactory schemaFactory = SchemaFactory.newFactory();
    Schema txSchema = schemaFactory.createSchema(new FileInputStream("my_edi_schema.xml"));
    reader.setTransactionSchema(txSchema);
  } else {
    // Do something else with the event
  }
}
```

## Summary

Are you writing custom code to process EDI data in Java? Have you tried [StAEDI](https://github.com/xlate/staedi) and encountered an issue? Give your feedback in the comments, or open an issue on the [StAEDI](https://github.com/xlate/staedi) GitHub repository.