---
title: Create and Read Excel File using PHP
tags: php
date: 2019-10-30
---

> 转载：[Create and Read Excel File using PHP - TrinityTuts](https://trinitytuts.com/create-and-read-excel-file-using-php/)

In this post I will explain to you how we can create and read Excel (.xlsx||.xls) using PHP. If you miss my last post in which I explain how to [create a CSV file using PHP](https://trinitytuts.com/create-csv-and-excel-using-php/) please read that post. For this post, I am using **PhpSpreadsheet** plugin. You can use this plugin in any framework you can install this plugin using composer.

### Create Excel

**Step 1.** Using a terminal and run below command it will install in your project

```php
composer require phpoffice/phpspreadsheet
```

**Step 2.** Now include installed plugin in your file

```php
require 'vendor/autoload.php';
```

**Step 3.** Create Excel file using this plugin is very simple to please add below code and run.

```php
<?php

require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\Cell\DataValidation;

$spreadsheet = new Spreadsheet();

// ADD DATA TO SPECIFIC CELL
$spreadsheet->getActiveSheet()->setCellValue('A1', 'Hello World !');

// Create Excel file and sve in your directory
$writer = new Xlsx($spreadsheet);
$writer->save('mysheet.xlsx');
```

This code creates an excel file and add data in the cell and save.

**Step 4**. Add new sheet in your excel file use below code

```php
<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\Cell\DataValidation;

$spreadsheet = new Spreadsheet();

// ADD DATA TO SPECIFIC CELL
$spreadsheet->getActiveSheet()->setCellValue('A1', 'Hello World !');

// Create a new worksheet called "My Data"
// Attach the "My Data" worksheet as the first worksheet in the Spreadsheet object
$myWorkSheet = new \PhpOffice\PhpSpreadsheet\Worksheet\Worksheet($spreadsheet, 'My Data');
$spreadsheet->addSheet($myWorkSheet, 0);

// Create Excel file and sve in your directory
$writer = new Xlsx($spreadsheet);
$writer->save('mysheet.xlsx');
```

**Step 5.** Now if you want to array data in your excel at location use below code

```php
<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\Cell\DataValidation;

$spreadsheet = new Spreadsheet();

$arrayData = [
    ['Aneh', 'Amit', 'Ajay', 'Sanjeev'],
    ['Q1',   12,   15,   21],
    ['Q2',   56,   73,   86],
];
$spreadsheet->getActiveSheet()
    ->fromArray(
        $arrayData,  // The data to set
        NULL,        // Array values with this value will not be set
        'A1'         // Top left coordinate of the worksheet range where
    );

// Create Excel file and sve in your directory
$writer = new Xlsx($spreadsheet);
$writer->save('mysheet.xlsx');
```

**Step 6**. Now if you want to create a fixed header in your excel sheet. We use **freezePane** method to fixed header

```php
<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\Cell\DataValidation;

$spreadsheet = new Spreadsheet();

// FIXED HEADER
$spreadsheet->getActiveSheet()->freezePane('D2');

$arrayData = [
    ['Aneh', 'Amit', 'Ajay', 'Sanjeev'],
    ['Q1',   12,   15,   21],
    ['Q2',   56,   73,   86],
];
$spreadsheet->getActiveSheet()
    ->fromArray(
        $arrayData,  // The data to set
        NULL,        // Array values with this value will not be set
        'A1'         // Top left coordinate of the worksheet range where
    );

// Create Excel file and sve in your directory
$writer = new Xlsx($spreadsheet);
$writer->save('mysheet.xlsx');
```

### Read Excel

Reading spreadsheet file is very easy you need to pass sheet name if you want to specific sheet please follow below steps.

**Step 1.** In this step we can get list of sheet and name

```php
<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

$spreadsheet = new Spreadsheet();

$inputFileType = 'Xlsx';
$inputFileName = './mysheet.xlsx';

/**  Create a new Reader of the type defined in $inputFileType  **/
$reader = \PhpOffice\PhpSpreadsheet\IOFactory::createReader($inputFileType);
/**  Advise the Reader that we only want to load cell data  **/
$reader->setReadDataOnly(true);

$worksheetNames = $reader->listWorksheetNames($inputFileName);

echo '<h3>Worksheet Names</h3>';
echo '<ol>';
foreach ($worksheetNames as $worksheetName) {
    echo '<li>', $worksheetName, '</li>';
}
echo '</ol>';
```

**Step 2.** Now we can read sheet and sheet info eg. Row, Column, Cell Range

```php
<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

$spreadsheet = new Spreadsheet();

$inputFileType = 'Xlsx';
$inputFileName = './mysheet.xlsx';

/**  Create a new Reader of the type defined in $inputFileType  **/
$reader = \PhpOffice\PhpSpreadsheet\IOFactory::createReader($inputFileType);
/**  Advise the Reader that we only want to load cell data  **/
$reader->setReadDataOnly(true);

$worksheetData = $reader->listWorksheetInfo($inputFileName);

echo '<h3>Worksheet Information</h3>';
echo '<ol>';
foreach ($worksheetData as $worksheet) {
    echo '<li>', $worksheet['worksheetName'], '<br />';
    echo 'Rows: ', $worksheet['totalRows'],
         ' Columns: ', $worksheet['totalColumns'], '<br />';
    echo 'Cell Range: A1:',
    $worksheet['lastColumnLetter'], $worksheet['totalRows'];
    echo '</li>';
}
echo '</ol>';
```

**Step 3**. Read data for specific sheet use below code

```php
<?php
require 'vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

$spreadsheet = new Spreadsheet();

$inputFileType = 'Xlsx';
$inputFileName = './mysheet.xlsx';

/**  Create a new Reader of the type defined in $inputFileType  **/
$reader = \PhpOffice\PhpSpreadsheet\IOFactory::createReader($inputFileType);
/**  Advise the Reader that we only want to load cell data  **/
$reader->setReadDataOnly(true);

$worksheetData = $reader->listWorksheetInfo($inputFileName);

foreach ($worksheetData as $worksheet) {
    $sheetName = $worksheet['worksheetName'];

    echo "<h4>$sheetName</h4>";
    /**  Load $inputFileName to a Spreadsheet Object  **/
    $reader->setLoadSheetsOnly($sheetName);
    $spreadsheet = $reader->load($inputFileName);

    $worksheet = $spreadsheet->getActiveSheet();
    print_r($worksheet->toArray());
    
}
```

If you want to learn more about PhpSpreadsheet please follow their official [link](https://phpspreadsheet.readthedocs.io/).