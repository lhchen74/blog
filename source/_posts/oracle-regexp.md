---
title: The Complete Guide to Oracle REGEXP Functions
date: 2022-12-11
tags: db
---

> 转载：[The Complete Guide to Oracle REGEXP Functions - Database Star](https://www.databasestar.com/oracle-regexp-functions/)

Are you confused by Oracle regular expressions? Want to know how to use them to get the information you need for your queries? Learn all about Oracle REGEXP functions in this article.

## What is a Regular Expression?

A regular expression is a sequence of characters that allows you to search for patterns in strings or text values.

The "expression" is made up of special characters, which have their own meaning. This expression is then used in a regular expression function, and then the result is used in your query.

## Why Use Regular Expressions?

The main reason to use regular expressions is that they provide a very specific level of control over the pattern matching for your strings.

Oracle SQL has [many string functions](https://www.databasestar.com/oracle-sql-functions/) that allow you to do some comparisons. You can use [UPPER](https://www.databasestar.com/sql-upper-lower/) to find upper case values, for example, and can use a combination of LIKE and [wildcard characters](https://www.databasestar.com/sql-wildcards/) % and \_ to find certain values.

However, for more complicated checks, these functions are not enough.

This is where regular expressions come in.

They can be used to:

- Check phone number formats
- Check email address formats
- Check URLs match a specific format
- Check any other type of string value to see if it matches a desired format.

Many programming languages include regular expressions in their libraries. However, using it at the database level allows for the check to be done closer to where the data is stored, making it more efficient. It's also more consistent, which means any application that uses the data you're working with will see and require it in the same format.

## Oracle Regular Expression Functions

There are a few functions in Oracle SQL that can be used with regular expressions. They are:

- REGEXP_LIKE
- REGEXP_INSTR
- REGEXP_REPLACE
- REGEXP_SUBSTR
- REGEXP_COUNT (added in Oracle 11g)

Let's take a look at these functions in more detail.

## Oracle REGEXP_LIKE Function

The REGEXP_LIKE function searches a column for a specified pattern. It's used in a WHERE clause to check if a column matches a pattern, and if it does, then the row is included in the result set.

It's similar to the LIKE condition, but allows for regular expressions.

The syntax for the REGEXP_LIKE function is:

```
REGEXP_LIKE (source_string, pattern [, match_parameter] )
```

The parameters are:

- **source_string** (mandatory): The value that is searched in. It can be any data type of CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, or NCLOB.

- **pattern** (mandatory): This is the regular expression that you provide. It can be up to 512 bytes.

- match_parameter

  (optional): This allows you to change the default matching behaviour of the function, which can be one or more of:

  - "i": case-insensitive matching
  - "c": case-sensitive matching
  - "n": allows the "." character to match the newline character instead of any character
  - "m": treats the source_string value as multiple lines, where ^ is the start of a line and $ is the end of a line.

If you specify multiple match_parameter values that contradict each other (e.g. "ci" which matches to case-sensitive and case-insensitive), then Oracle uses the last value. In this example, it will use "i" instead of "c".

If you don't specify a match parameter, then:

- The default case sensitivity is determined by the parameter NLS_SORT.
- The period character doesn't match the newline character
- The source string is treated as a single line and not multiple lines.

## Oracle REGEXP_LIKE Examples

Let's take a look at some examples of the REGEXP_LIKE function:

### Example 1

This example uses just a source and pattern value.

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, 'W+');
```

| **TITLE** |
| --------- |
| Waterfall |
| Wishful   |
| Wellness  |

It returns these three values because they start with W and have one or more characters following them.

### Example 2

This example uses another source and pattern value. It looks for values where there are at least two consecutive "e" characters

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, 'e{2,}');
```

| **TITLE** |
| --------- |
| Tree      |
| Freedom   |

These two values have the "ee" characters within them.

### Example 3

This example looks for values that have a letter "C" in it.

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, 'C');
```

| **TITLE** |
| --------- |
| Chair     |
| Crypt     |
| QUICKLY   |

This example shows it doesn't matter if the "C" is at the start or in the middle of the string.

### Example 4

This example looks for values that have either a "V" or a "v" in it. The "i" denotes that the search is case-insensitive.

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, 'V', 'i');
```

| **TITLE**  |
| ---------- |
| Vacuum     |
| November   |
| TraVERse   |
| Undercover |
| Vain       |

It shows results that have either a "V" or a "v", at any point in the string.

### Example 5

This example shows results that have a "V", but not those that have a lowercase "v".

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, 'V', 'c');
```

| **TITLE** |
| --------- |
| Vacuum    |
| TraVERse  |
| Vain      |

### Example 6

This example shows values that have digits inside them.

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, '[[:digit:]]');
```

| **TITLE**        |
| ---------------- |
| Summer of 69     |
| The year is 2017 |
| 1955             |

It shows values that are only digits, and those that have digits inside them.

### Example 7

This example shows values that have alphabetical characters.

```sql
SELECT title
FROM regvalues
WHERE REGEXP_LIKE(title, '[[:alpha:]]');
```

]');

| **TITLE** |
| --------- |
| Box       |
| Chair     |
| Vacuum    |
| Desk      |
| Round     |
| Under     |

This also only shows a sample of values.

## Oracle REGEXP_INSTR Function

The Oracle REGEXP_INSTR function lets you search a string for a regular expression pattern, and returns a number that indicates where the pattern was found.

It's similar to the [Oracle INSTR function](https://www.databasestar.com/sql-instr/), but it handles regular expressions where INSTR does not.

The syntax for the REGEXP_INSTR function is:

```
REGEXP_INSTR (
  source_string, pattern [, position [, occurrence
  [, return_option [, match_parameter [, sub_expression ] ] ] ] ]
)
```

This looks pretty complicated! Don't worry, I'll explain it all. There are a lot of parameters here, most of which are optional.

Let's look at them and see what they do.

- **source_string** (mandatory): This is the character string that the expression is searched in. It can be any of CHAR, VARCHAR2, NCHAR, NVACHAR2, CLOB, or NCLOB.

- **pattern** (mandatory): This is the regular expression that is used to search within the source_string. It can be any of CHAR, VARCHAR, NCHAR, or NVARCHAR2, and can be up to 512 bytes.

- **position** (optional): This is the position in the source_string where the function should begin the search for the pattern. It must be a positive integer, and the default value is 1 (the search begins at the first character).

- **occurrence** (optional): This is a positive integer that indicates which occurrence of the pattern within the source_string the function should search for. The default value is 1, which means the function finds the first occurrence. If the value is greater than 1, then the function looks for the second occurrence (or further occurrences) after the first occurrence is found.

- **return_option** (optional): This lets you specify what happens when an occurrence is found. If you specify 0, which is the default, the function returns the position of the first character of the occurrence. If you specify 1, then the function returns the position of the character after the occurrence.

- match_parameter

  (optional): This allows you to change the default matching behaviour of the function, which can be one or more of:

  - "i": case-insensitive matching
  - "c": case-sensitive matching
  - "n": allows the "." character to match the newline character instead of any character
  - "m": treats the source_string value as multiple lines, where ^ is the start of a line and $ is the end of a line.

- **sub_expression** (optional): If the pattern has subexpressions, this value indicates which subexpression is used in the function. The default value is 0.

## Oracle REGEXP_INSTR Examples

Let's take a look at some examples of the Oracle REGEXP_INSTR function.

### Example 1

This example finds the position of the "ee" within a string.

```sql
SELECT title,
REGEXP_INSTR(title, 'ee') AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, 'ee') > 0;
```

| **TITLE** | **REG** |
| --------- | ------- |
| Tree      | 3       |
| Freedom   | 3       |

### Example 2

This example finds the position of a string that starts with either A, B, or C, and then has 4 alphabetical characters following it.

```sql
SELECT title,
REGEXP_INSTR(title, '[A|B|C][[:alpha:]]{4}') AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '[A|B|C][[:alpha:]]{4}') > 0;
```

| **TITLE** | **REG** |
| --------- | ------- |
| Chair     | 1       |
| Crypt     | 1       |

### Example 3

This example finds the position of strings that have two vowels in a row.

```sql
SELECT title,
REGEXP_INSTR(title, '[aeiou]{2,}') AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '[aeiou]{2,}') > 0;
```

| **TITLE**        | **REG** |
| ---------------- | ------- |
| Chair            | 3       |
| Vacuum           | 4       |
| Round            | 2       |
| Superficial      | 9       |
| Suspicious       | 7       |
| Tree             | 3       |
| breakfast        | 3       |
| Freedom          | 3       |
| Helium           | 4       |
| Laundromat       | 2       |
| Exclaim          | 5       |
| Vain             | 2       |
| The year is 2017 | 6       |

As you can see, the REGEXP_INSTR value is different for each row depending on where the two vowels start.

### Example 4

This example shows the position of values where there are two vowels in a row, after position 4.

```sql
SELECT title,
REGEXP_INSTR(title, '[aeiou]{2,}', 4) AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '[aeiou]{2,}', 4) > 0;
```

| **TITLE**        | **REG** |
| ---------------- | ------- |
| Vacuum           | 4       |
| Superficial      | 9       |
| Suspicious       | 7       |
| Helium           | 4       |
| Exclaim          | 5       |
| The year is 2017 | 6       |

### Example 5

This example shows the position of the second occurrence in a string where there is a vowel after position 5.

```sql
SELECT title,
REGEXP_INSTR(title, '[aeiou]', 5, 2) AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '[aeiou]', 5, 2) > 0;
```

| **TITLE**        | **REG** |
| ---------------- | ------- |
| Superficial      | 9       |
| Suspicious       | 7       |
| Designate        | 9       |
| Hawkeye          | 7       |
| Laundromat       | 9       |
| Mathematical     | 7       |
| Exclaim          | 6       |
| Undercover       | 9       |
| Xylophone        | 9       |
| Zucchini         | 8       |
| Summer of 69     | 8       |
| The year is 2017 | 7       |

### Example 6

This example shows the position of the second occurrence in a string where there is a vowel after position 5, but shows the position at the end of the value that was found.

```sql
SELECT title,
REGEXP_INSTR(title, '[aeiou]', 5, 2, 1) AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '[aeiou]', 5, 2) > 0;
```

| **TITLE**        | **REG** |
| ---------------- | ------- |
| Superficial      | 10      |
| Suspicious       | 8       |
| Designate        | 10      |
| Hawkeye          | 8       |
| Laundromat       | 10      |
| Mathematical     | 8       |
| Exclaim          | 7       |
| Undercover       | 10      |
| Xylophone        | 10      |
| Zucchini         | 9       |
| Summer of 69     | 9       |
| The year is 2017 | 8       |

### Example 7

This example shows the position of values that have an A, B, C, D, or E, followed by a vowel, using a case-insensitive search.

```sql
SELECT title,
REGEXP_INSTR(title, '[A|B|C|D|E][aeiou]', 1, 1, 0, 'i') AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '[A|B|C|D|E][aeiou]', 1, 1, 0, 'i') > 0;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | 1       |
| Chair       | 3       |
| Vacuum      | 3       |
| Desk        | 1       |
| Under       | 3       |
| Dismiss     | 1       |
| Superficial | 8       |
| Suspicious  | 6       |
| Tree        | 3       |
| breakfast   | 3       |
| Designate   | 1       |

Only some of the values are shown here. "breakfast' is shown because the search is case-insensitive, so it doesn't matter that it has lowercase values.

### Example 8

This example shows values that have an A, B, or C, followed by a vowel, and finds the position of the vowel.

```sql
SELECT title,
REGEXP_INSTR(title, '([ABC])([aeiou])', 1, 1, 0, 'i', 2) AS reg
FROM regvalues
WHERE REGEXP_INSTR(title, '([ABC])([aeiou])', 1, 1, 0, 'i') > 0;
```

| **TITLE**    | **REG** |
| ------------ | ------- |
| Box          | 2       |
| Chair        | 4       |
| Vacuum       | 4       |
| Superficial  | 9       |
| Suspicious   | 7       |
| November     | 7       |
| October      | 6       |
| Laundromat   | 3       |
| Mathematical | 11      |
| Exclaim      | 6       |
| Undercover   | 7       |
| Vain         | 3       |

## Oracle REGEXP_REPLACE Function

The Oracle REGEXP_REPLACE function is used to search a string for a regular expression and replace it with other characters.

It's an extension of the [standard Oracle REPLACE function](https://www.databasestar.com/oracle-replace/), but REPLACE does not support regular expressions where REGEXP_REPLACE does.

The syntax for this function is:

```
REGEXP_REPLACE (source_string, pattern
[, replace_string [, position [, occurrence [, match_parameter ] ] ] ]
)
```

Let's take a look at each of these parameters:

- **source_string** (mandatory): This is the string to be searched in for this function. It is usually a character value and can be any of CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, or NCLOB.

- **pattern** (mandatory): This is the regular expression and is used to search within the source_string. It can be any of CHAR, VARCHAR2, NCHAR, or NVARCHAR2, and can be up to 512 bytes.

- **replace_string** (optional): This is a value that is used to replace the occurrences of the pattern within the source_string. It can be any of CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, or NCLOB. This replace_string can contain backreferences to subexpressions in the pattern by using backslashes (\), which I will show you in the examples below.

- **position** (optional): This is the position in the source_string where the function should begin the search for the pattern. It must be a positive integer, and the default value is 1 (the search begins at the first character).

- **occurrence** (optional): This is a positive integer that indicates which occurrence of the pattern within the source_string the function should search for. The default value is 1, which means the function finds the first occurrence. If the value is greater than 1, then the function looks for the second occurrence (or further occurrences) after the first occurrence is found.

- match_parameter

  (optional): This allows you to change the default matching behaviour of the function, which can be one or more of:

  - "i": case-insensitive matching
  - "c": case-sensitive matching
  - "n": allows the "." character to match the newline character instead of any character
  - "m": treats the source_string value as multiple lines, where ^ is the start of a line and $ is the end of a line.

The return value is a VARCHAR2 if the source_string is not a CLOB or NCLOB, and CLOB if it is.

## Oracle REGEXP_REPLACE Examples

Let's see some examples of the REGEXP_REPLACE function.

### Example 1

This example removes all occurrences of two consecutive vowels.

```sql
SELECT title,
REGEXP_REPLACE(title, '[a|e|i|o|u]{2,}') AS reg
FROM regvalues;
```

| **TITLE**   | **REG**   |
| ----------- | --------- |
| Box         | Box       |
| Chair       | Chr       |
| Vacuum      | Vacm      |
| Desk        | Desk      |
| Round       | Rnd       |
| Under       | Under     |
| Waterfall   | Waterfall |
| Dismiss     | Dismiss   |
| Superficial | Superficl |
| Suspicious  | Suspics   |

As you can see, the "ai" in "Chair" was removed, but "Box" remained the same, because "Box" only has one consecutive vowel.

### Example 2

This example replaces two consecutive vowels with two dashes.

```sql
SELECT title,
REGEXP_REPLACE(title, '[a|e|i|o|u]{2,}', '--') AS reg
FROM regvalues;
```

| **TITLE**   | **REG**    |
| ----------- | ---------- |
| Box         | Box        |
| Chair       | Ch–r       |
| Vacuum      | Vac–m      |
| Desk        | Desk       |
| Round       | R–nd       |
| Under       | Under      |
| Waterfall   | Waterfall  |
| Dismiss     | Dismiss    |
| Superficial | Superfic–l |
| Suspicious  | Suspic–s   |

### Example 3

This example replaces two consecutive vowels of the same vowel with two dashes.

```sql
SELECT title,
REGEXP_REPLACE(title, '([a|e|i|o|u])\1', '--') AS reg
FROM regvalues;
```

| **TITLE**   | **REG**     |
| ----------- | ----------- |
| Box         | Box         |
| Chair       | Chair       |
| Vacuum      | Vac–m       |
| Desk        | Desk        |
| Round       | Round       |
| Under       | Under       |
| Waterfall   | Waterfall   |
| Dismiss     | Dismiss     |
| Superficial | Superficial |
| Suspicious  | Suspicious  |

As you can see, "Vacuum" had the "uu" replaced, but "Chair" did not, as the vowels in "Chair" are not the same.

### Example 4

This example replaces any digits in the string with a + and then the digit.

```sql
SELECT title,
REGEXP_REPLACE(title, '([[:digit:]])', '+\1') AS reg
FROM regvalues;
```

| **TITLE**        | **REG**              |
| ---------------- | -------------------- |
| Yeti             | Yeti                 |
| Zucchini         | Zucchini             |
| Summer of 69     | Summer of +6+9       |
| The year is 2017 | The year is +2+0+1+7 |
| 1955             | +1+9+5+5             |

### Example 5

This example replaces any vowel character followed by any letter from "a" to "m", starting from position 4, with two dashes.

```sql
SELECT title,
REGEXP_REPLACE(title, '[a|e|i|o|u][a-m]', '--', 4) AS reg
FROM regvalues;
```

| **TITLE**   | **REG**   |
| ----------- | --------- |
| Box         | Box       |
| Chair       | Chair     |
| Vacuum      | Vacu–     |
| Desk        | Desk      |
| Round       | Round     |
| Under       | Under     |
| Waterfall   | Waterf–l  |
| Dismiss     | Dismiss   |
| Superficial | Superf—-l |
| Suspicious  | Susp–ious |

### Example 6

This example replaces the second occurrence of any vowel character followed by any letter from "a" to "m", starting from position 1, with two dashes.

```sql
SELECT title,
REGEXP_REPLACE(title, '[a|e|i|o|u][a-m]', '--', 1, 2) AS reg
FROM regvalues;
```

| **TITLE**   | **REG**    |
| ----------- | ---------- |
| Box         | Box        |
| Chair       | Chair      |
| Vacuum      | Vacu–      |
| Desk        | Desk       |
| Round       | Round      |
| Under       | Under      |
| Waterfall   | Waterfall  |
| Dismiss     | Dismiss    |
| Superficial | Superfic–l |
| Suspicious  | Suspicious |

### Example 7

This example replaces more than one consecutive capitalised letter with an underscore, starting from position 2.

```sql
SELECT title,
REGEXP_REPLACE(title, '[A-Z]+', '_', 2, 1, 'c') AS reg
FROM regvalues;
```

| **TITLE**    | **REG**      |
| ------------ | ------------ |
| Mathematical | Mathematical |
| Press        | Press        |
| QUICKLY      | Q\_          |
| Roger        | Roger        |
| Simple       | Simple       |

## Oracle REGEXP_SUBSTR Function

The Oracle REGEXP_SUBSTR function allows you to search for a string inside another string, using regular expressions.

It's similar to the REGEXP_INSTR function, but instead of returning the position of the string, it returns the substring. One of the uses is to [split a string into separate rows](https://www.databasestar.com/sql-split-string/).

It extends the [SUBSTR function](https://www.databasestar.com/oracle-substr/) but allows the user of regular expressions.

The function returns a VARCHAR2 or CLOB data type, depending on what has been provided as an input.

The syntax of the REGEXP_SUBSTR function is:

```
REGEXP_SUBSTR (
source_string, pattern [, position [, occurrence [, match_parameter ] ] ]
)
```

The parameters for this function are:

- **source_string** (mandatory): This is the string to be searched inside of. It is usually the larger of the two parameters, and is usually a character value and can be any of CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, or NCLOB.

- **pattern** (mandatory): This is the regular expression and is used to search within the source_string. It can be any of CHAR, VARCHAR2, NCHAR, or NVARCHAR2, and can be up to 512 bytes.

- **position** (optional): This is the position in the source_string where the function should begin the search for the pattern. It must be a positive integer, and the default value is 1 (the search begins at the first character).

- **occurrence** (optional): This is a positive integer that indicates which occurrence of the pattern within the source_string the function should search for. The default value is 1, which means the function finds the first occurrence. If the value is greater than 1, then the function looks for the second occurrence (or further occurrences) after the first occurrence is found.

- match_parameter

  (optional): This allows you to change the default matching behaviour of the function, which can be one or more of:

  - "i": case-insensitive matching
  - "c": case-sensitive matching
  - "n": allows the "." character to match the newline character instead of any character
  - "m": treats the source_string value as multiple lines, where ^ is the start of a line and $ is the end of a line.

## Oracle REGEXP_SUBSTR Examples

Let's take a look at some examples of the REGEXP_SUBSTR function.

### Example 1

This example finds a substring that matches two consecutive vowels.

```sql
SELECT title,
REGEXP_SUBSTR(title, '[a|e|i|o|u]{2,}') AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | (null)  |
| Chair       | ai      |
| Vacuum      | uu      |
| Desk        | (null)  |
| Round       | ou      |
| Under       | (null)  |
| Waterfall   | (null)  |
| Dismiss     | (null)  |
| Superficial | ia      |
| Suspicious  | iou     |

It returns the substring that was found, and NULL for all other records.

### Example 2

This example finds all consecutive vowels in a string that are the same, and returns NULL for those that don't have consecutive vowels that are the same.

```sql
SELECT title,
REGEXP_SUBSTR(title, '([a|e|i|o|u])\1') AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | (null)  |
| Chair       | (null)  |
| Vacuum      | uu      |
| Desk        | (null)  |
| Round       | (null)  |
| Under       | (null)  |
| Waterfall   | (null)  |
| Dismiss     | (null)  |
| Superficial | (null)  |
| Suspicious  | (null)  |
| Tree        | ee      |

### Example 3

This example finds substrings that contain one or more digits.

```sql
SELECT title,
REGEXP_SUBSTR(title, '[[:digit:]]+') AS reg
FROM regvalues;
```

| **TITLE**        | **REG** |
| ---------------- | ------- |
| Xylophone        | (null)  |
| Yeti             | (null)  |
| Zucchini         | (null)  |
| Summer of 69     | 69      |
| The year is 2017 | 2017    |
| 1955             | 1955    |

### Example 4

This example finds substrings that have a vowel followed by a letter from "a" to "m", starting from position 4.

```sql
SELECT title,
REGEXP_SUBSTR(title, '[a|e|i|o|u][a-m]', 4) AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | (null)  |
| Chair       | (null)  |
| Vacuum      | um      |
| Desk        | (null)  |
| Round       | (null)  |
| Under       | (null)  |
| Waterfall   | al      |
| Dismiss     | (null)  |
| Superficial | ic      |
| Suspicious  | ic      |

### Example 5

This example finds the second occurrence of substrings that have a vowel followed by a letter from "a" to "m".

```sql
SELECT title,
REGEXP_SUBSTR(title, '[a|e|i|o|u][a-m]', 1, 2) AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | (null)  |
| Chair       | (null)  |
| Vacuum      | um      |
| Desk        | (null)  |
| Round       | (null)  |
| Under       | (null)  |
| Waterfall   | (null)  |
| Dismiss     | (null)  |
| Superficial | ia      |
| Suspicious  | (null)  |

### Example 6

This example finds substrings that contain one or more consecutive capital letters starting from position 2.

```sql
SELECT title,
REGEXP_SUBSTR(title, '[A-Z]+', 2, 1, 'c') AS reg
FROM regvalues;
```

| **TITLE**    | **REG** |
| ------------ | ------- |
| Mathematical | (null)  |
| Press        | (null)  |
| QUICKLY      | UICKLY  |
| Roger        | (null)  |
| Simple       | (null)  |
| TraVERse     | VER     |
| Exclaim      | (null)  |

## Oracle REGEXP_COUNT

The Oracle REGEXP_COUNT function finds the number of times a pattern occurs in a particular string. It returns an integer which indicates the number of times it was found. If no matches are found, it returns 0.

The REGEXP_COUNT function is a new function in Oracle 11g. It works in a similar way to REGEXP_INSTR.

The syntax of this function is:

```
REGEXP_COUNT (source_string, pattern [, position [, match_parameter ] ] ] )
```

The parameters for this function are:

- **source_string** (mandatory): This is the string to be searched inside of. It is usually a character value and can be any of CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, or NCLOB.

- **pattern** (mandatory): This is the regular expression and is used to search within the source_string. It can be any of CHAR, VARCHAR2, NCHAR, or NVARCHAR2, and can be up to 512 bytes.

- **position** (optional): This is the position in the source_string where the function should begin the search for the pattern. It must be a positive integer, and the default value is 1 (the search begins at the first character).

- match_parameter

  (optional): This allows you to change the default matching behaviour of the function, which can be one or more of:

  - "i": case-insensitive matching
  - "c": case-sensitive matching
  - "n": allows the "." character to match the newline character instead of any character
  - "m": treats the source_string value as multiple lines, where ^ is the start of a line and $ is the end of a line.
  - "x": ignores whitespace characters. By default, any whitespace characters will match.

The REGEXP_COUNT function ignores subexpressions in the pattern. This means any brackets used to create subexpression patterns are ignored and the pattern is treated as a single expression.

## Oracle REGEXP_COUNT Examples

Here are some examples of the REGEX_COUNT function.

### Example 1

This example finds the number of occurrences that contain two consecutive vowels.

```sql
SELECT title,
REGEXP_COUNT(title, '[a|e|i|o|u]{2,}') AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | 0       |
| Chair       | 1       |
| Vacuum      | 1       |
| Desk        | 0       |
| Round       | 1       |
| Under       | 0       |
| Waterfall   | 0       |
| Dismiss     | 0       |
| Superficial | 1       |
| Suspicious  | 1       |

### Example 2

This example finds the number of occurrences that contain vowels.

```sql
SELECT title,
REGEXP_COUNT(title, '[a|e|i|o|u]') AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | 1       |
| Chair       | 2       |
| Vacuum      | 3       |
| Desk        | 1       |
| Round       | 2       |
| Under       | 1       |
| Waterfall   | 3       |
| Dismiss     | 2       |
| Superficial | 5       |
| Suspicious  | 5       |

### Example 3

This example finds the number of occurrences that contain digits.

```sql
SELECT title,
REGEXP_COUNT(title, '[[:digit:]]') AS reg
FROM regvalues;
```

| **TITLE**        | **REG** |
| ---------------- | ------- |
| Wishful          | 0       |
| Wellness         | 0       |
| Xylophone        | 0       |
| Yeti             | 0       |
| Zucchini         | 0       |
| Summer of 69     | 2       |
| The year is 2017 | 4       |
| 1955             | 4       |

### Example 4

This example finds the number of occurrences that contain vowels, starting from position 3.

```sql
SELECT title,
REGEXP_COUNT(title, '[a|e|i|o|u]', 3) AS reg
FROM regvalues;
```

| **TITLE**   | **REG** |
| ----------- | ------- |
| Box         | 0       |
| Chair       | 2       |
| Vacuum      | 2       |
| Desk        | 0       |
| Round       | 1       |
| Under       | 1       |
| Waterfall   | 2       |
| Dismiss     | 1       |
| Superficial | 4       |
| Suspicious  | 4       |

### Example 5

This example finds the number of occurrences that contain a capital letter, starting from position 2.

```sql
SELECT title,
REGEXP_COUNT(title, '[A-Z]', 2, 'c') AS reg
FROM regvalues;
```

| **TITLE**    | **REG** |
| ------------ | ------- |
| Mathematical | 0       |
| Press        | 0       |
| QUICKLY      | 6       |
| Roger        | 0       |
| Simple       | 0       |
| TraVERse     | 3       |
| Exclaim      | 0       |
| Undercover   | 0       |
| Vain         | 0       |

## Function Syntax Summary

As you may have noticed, the REGEXP functions have a lot of similar parameters. This table highlights how the parameters are the same between each function.

| **Parameter**   | **REGEXP\_ LIKE** | **REGEXP\_ INSTR** | **REGEXP\_ SUBSTR** | **REGEXP\_ REPLACE** | **REGEXP\_ COUNT** |
| --------------- | ----------------- | ------------------ | ------------------- | -------------------- | ------------------ |
| source_string   | Yes               | Yes                | Yes                 | Yes                  | Yes                |
| pattern         | Yes               | Yes                | Yes                 | Yes                  | Yes                |
| replace_string  | No                | No                 | No                  | Yes                  | No                 |
| position        | No                | Yes                | Yes                 | Yes                  | Yes                |
| occurrence      | No                | Yes                | Yes                 | Yes                  | No                 |
| return_option   | No                | Yes                | No                  | No                   | No                 |
| match_parameter | Yes               | Yes                | Yes                 | Yes                  | Yes                |
| sub_expression  | No                | Yes                | No                  | No                   | No                 |

## Oracle Regular Expression Patterns

Regular expressions are a sequence of characters that are used to search another string.

Each of the characters inside a regular expression has a specific meaning.

There are characters called "metacharacters", which are used to specify the rules used for searching a character or set of characters.

I'll show some examples of these being used shortly, but first I'll show you what these characters are.

This table shows the metacharacters used in Oracle.

| **Metacharacter Syntax** | **Operator Name**                     | **Description**                                                                                                                                   |
| ------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| .                        | Any Character: Dot                    | Matches any character                                                                                                                             |
| +                        | One or More: Plus Quantifier          | Matches one or more occurrences of the preceding subexpression                                                                                    |
| ?                        | Zero or One: Question Mark Quantifier | Matches zero or one occurrence of the preceding subexpression                                                                                     |
| \*                       | Zero or More: Star Quantifier         | Matches zero or more occurrences of the preceding subexpression                                                                                   |
| {m}                      | Interval: Exact Count                 | Matches exactly m occurrences of the preceding subexpression                                                                                      |
| {m,}                     | Interval: At Least Count              | Matches at least m occurrences of the preceding subexpression                                                                                     |
| {m,n}                    | Interval: Between Count               | Matches at least m, but not more than n occurrences of the preceding subexpression                                                                |
| [ … ]                    | Matching Character List               | Matches any character in list …                                                                                                                   |
| [^ … ]                   | Non-Matching Character List           | Matches any character not in list …                                                                                                               |
| \|                       | Or                                    | Matches either character each side of this symbol                                                                                                 |
| ( … )                    | Subexpression or Grouping             | Treat expression … as a unit. The subexpression can be a string of literals or a complex expression containing operators.                         |
| \n                       | Backreference                         | Matches the nth preceding subexpression, where n is an integer from 1 to 9.                                                                       |
| \                        | Escape Character                      | Treat the subsequent metacharacter in the expression as a literal.                                                                                |
| ^                        | Beginning of Line Anchor              | Match the subsequent expression only when it occurs at the beginning of a line.                                                                   |
| $                        | End of Line Anchor                    | Match the preceding expression only when it occurs at the end of a line.                                                                          |
| [:class:]                | POSIX Character Class                 | Match any character belonging to the specified character class. Can be used inside any list expression.                                           |
| [.element.]              | POSIX Collating Sequence              | Specifies a collating sequence to use in the regular expression. The element you use must be a defined collating sequence, in the current locale. |
| [=character=]            | POSIX Character Equivalence Class     | Match characters having the same base character as the character you specify.                                                                     |

Let's take a look at some examples of using regular expression patterns.

### Basic Example

This example is the simplest match you can get with a regular expression.

If you provide a pattern of 'abc', with no metacharacters, you will find the sequence 'abc'.

- Pattern: 'abc'
- Matches: 'abc'
- Does not match: 'abd', 'ab'

### Match Any Single Character

The dot or period character '.' will match any single character in your string.

So, if you're looking for an 'ab' followed by any single character, then a 'd', you will use a pattern of 'ab.d'.

- Pattern: 'ab.d'
- Matches: 'abcd', 'abad', 'abbd', 'ab9d'
- Does not match: 'abd', 'ababd'

### Match Any One or More Characters

The plus character '+' will match any single or multiple occurrences of the previous expression or character.

For example, to find one or more occurrences of the letter 'e', you would use the pattern 'e+'.

- Pattern: 'e+'
- Matches: 'e', 'ee', 'eee', 'eeeeeeeee'
- Does not match: 'aaa', 'each', 'eaea'

### Match Zero or One Character

The question mark character '?' will match zero or one, and only one, occurrence of the previous expression or character.

It's helpful for specifying optional characters.

For example, to find a character string 'abcd' where the 'c' may or may not be there, you would use the pattern 'abc?d'.

- Pattern: 'abc?d'
- Matches: 'abcd', 'abd'
- Does not match: 'acd', 'cabd'

### Match Zero or More Characters

The asterisk character '\*' allows you to match zero or more occurrences of the previous expression or character.

For example, to find a character string that starts with 'a' and ends in 'b', you could use the pattern 'a\*b'.

- Pattern: 'a\*b'
- Matches: 'acedb', 'ab', 'aeb'
- Does not match: 'abcd', 'ba', 'abcde'

### Match an Exact Number of Characters

The exact count operator for regular expressions is written as a single digit inside curly braces {}. This finds the exact number of occurrences of the preceding character or expression.

For example, to find expressions matching 'eeeeee' you would use a pattern of 'e{6}'.

- Pattern: 'e{6}'
- Matches: 'eeeeee'
- Does not match: 'eee', 'e6'

### Match At Least a Number of Characters

The at least count operator for regular expressions is written as a single digit and a comma inside curly braces {}. This finds occurrences where at least the specified number of preceding characters or expressions are found.

For example, to find if the character 'd' occurs at least 4 times, you would use a pattern of 'd{4,}'.

- Pattern: 'd{4,}'
- Matches: 'dddd', 'ddddd', 'ddddddd'
- Does not match: 'ddd', 'd4', 'd'

### Match a Number of Characters Between Two Counts

The between count operator for regular expressions can be used to find occurrences of a specified value within a range. This is done by specifying the lower and upper bounds of the range, separated by a comma, inside curly braces {}.

For example, to find where the character 'g' occurs between 3 and 5 times, you would use a pattern of 'g{3,5}'.

- Pattern: 'g{3,5}'
- Matches: 'ggg', 'gggg', 'ggggg'
- Does not match: 'gg', 'goooo', 'ggegge'

### Match a Character List

To match a list of characters, you can specify a pattern of characters inside square brackets []. This will find any occurrences of any of the specified characters.

For example, to find where either the 'a', 'e', or 'o' character exists, you would use a pattern of [aeo].

- Pattern: [aeo]
- Matches: 'alpha', 'egg', 'orange'
- Does not match: 'dig', 'why', 'xbzpgws'

### Non-Matching Character List

To match against a list of characters you don't want to match, you can specify a non-matching list. This is done by specifying a ^ character inside a character list.

Characters that do not match any of the characters in your square brackets are returned by the match.

For example, to exclude strings with 'm' and 'p' in them from your results, use a pattern of [^mp].

- Pattern: [^mp]
- Matches: 'mpera', 'wamplne'
- Does not match: 'mp'

### Range Operator

To match on a range of characters, you can use the '-' symbol between two characters inside square brackets []. This will find occurrences of any character between the two characters.

For example, to find values that contain any character between 'a' and 'e', you would use the pattern of [a-e].

- Pattern: [a-e]
- Matches: 'alpha', 'end' 'bubble'
- Does not match: 'zip', 'mug', 'up'

### Or Operator

To specify an alternative to a character or expression, you can use the pipe character '|' as an OR expression.

For example, to match the value 'a' or 'e', you can use the pattern of 'a|e'.

- Pattern: 'a|e'
- Matches: 'a', 'e'
- Does not match: 'w', 'c'

### Subexpression or Grouping

You can use subexpressions to group characters you want to find as a whole. You do this by enclosing them in round brackets ().

For example, to find the optional value of 'un' followed by the characters 'col', you can use the pattern of '(un)?col'.

- Pattern: '(un)?col'
- Matches: 'col', 'uncol'
- Does not match: 'un', 'ununcolcol'

### Backreference

The backreference feature allows you to search for a repeated expression. This is done by specifying subexpressions, and then using a backslash '\' and a number, where the number is from 1-9 and indicates the number of the subexpression.

This will be explained further with examples later in this article.

For example, to find repeated expressions of either 'aa' or 'bb', you can use a pattern of '(aa|bb)\1'.

- Pattern: '(aa|bb)\1'
- Matches: 'aaaa', 'bbbb'
- Does not match: 'abab', 'aa', 'bb'

### Escape Character

The escape character can be used to search for a character that is usually used for a meta character. For example, you can search of \* or + characters by putting an escape character before this character, such as '\*'

- Pattern: '\*'
- Matches: 'awe\*po'
- Does not match: 'awepo', 'abc'

### Beginning of Line Anchor

To find the occurrence of a string that only occurs at the beginning of a line, use the caret '^' operator. For example, to find expressions where the letter 'B' appears at the beginning of a line, use a pattern of '^B'.

- Pattern: '^B'
- Matches: 'Big', 'Beyond'
- Does not match: 'At the Big', 'ABC is easy'

### End of Line Anchor

The end of line character of a dollar sign '$' allows you to search for an expression that occurs only at the end of a line.

For example, to find expressions where the letter 'e' occurs at the end of a line, use a pattern of 'e$'.

- Pattern: 'e$'
- Matches: 'three', 'septe'
- Does not match: 'abcdef', 'fourteen'

### POSIX Character Class

The POSIX Character Class operator lets you search for an expression that matches a POSIX character class.

POSIX character classes are a standard set of values that represent other values. They are represented by a keyword enclosed in a colon ':' and two sets of square braces [[]].

The full list of POSIX character classes is:

| **POSIX Class** | **Similar To** | **Definition**                                                        |
| --------------- | -------------- | --------------------------------------------------------------------- |
| [:upper:]       | [A-Z]          | uppercase letters                                                     |
| [:lower:]       | [a-z]          | lowercase letters                                                     |
| [:alpha:]       | [A-Za-z]       | upper- and lowercase letters                                          |
| [:digit:]       | [0-9]          | digits                                                                |
| [:xdigit:]      | [0-9A-Fa-f]    | hexadecimal digits                                                    |
| [:alnum:]       | [A-Za-z0-9]    | digits, upper- and lowercase letters                                  |
| [:punct:]       |                | punctuation (all graphic characters except letters and digits)        |
| [:blank:]       | [ \t]          | space and TAB characters only                                         |
| [:space:]       | [ \t\n\r\f\v]  | blank (whitespace) characters                                         |
| [:cntrl:]       |                | control characters                                                    |
| [:graph:]       | [^ [:cntrl:]]  | graphic characters (all characters which have graphic representation) |
| [:print:]       | [[:graph] ]    | graphic characters and space                                          |

So, for example, to find where there are at least four upper case characters, use a pattern of '[[:upper:]]{4,}'.

- Pattern: '[[:upper:]]{4,}'
- Matches: 'ABCDE', 'WHYEPAFdce'
- Does not match: 'AbCdEfGhIj', 'EPOfjnvkdfvnPO'

### POSIX Collating Sequence

The POSIX collating sequence operator lets you specify a collating sequence in your regular expression. This operator is a value inside two dots '..' and double square braces [[]].

For example, to find the collating sequence of 'ch' in your strings, then you would use a value of '[[.ch.]]'.

- Pattern: '[[.ch.]]'
- Matches: 'chabc'
- Does not match: 'cdefg'

### POSIX Character Equivalence Class

The POSIX character equivalence class allows you to find characters in the current locale that are equivalent characters. This allows you to search for characters with and without accents, for example, depending on the locale.

For example, to find strings that contain an equivalent of 'e', use the pattern of '[[=e=]]'.

Pattern: '[[=e=]]'

Matches: 'west', 'café'

Does not match: 'window', garçon'
