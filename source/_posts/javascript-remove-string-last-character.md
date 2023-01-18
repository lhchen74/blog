---
title: How to Remove the Last Character from a String in JavaScript
tags: js
date: 2022-09-05
---

> 转载: [How to Remove the Last Character from a String in JavaScript - Mastering JS](https://masteringjs.io/tutorials/fundamentals/remove-last-character#:~:text=Nov 12%2C 2021-,To remove the last character from a string in JavaScript,length - 1)

To remove the last character from a string in JavaScript, you should use the `slice()` method. It takes two arguments: the start index and the end index. `slice()` supports negative indexing, which means that `slice(0, -1)` is equivalent to `slice(0, str.length - 1)`.

```javascript
let str = 'Masteringjs.ioF';
str.slice(0, -1); // Masteringjs.io
```

## Alternative Methods

`slice()` is generally easier, however other methods available are `substring()` and `replace()`. `substring()` does not have negative indexing, so be sure to use `str.length - 1` when removing the last character from the string. `replace()` takes either a string or a regular expression as its `pattern` argument. Using `/.$/` as the regular expression argument matches the last character of the string, so `.replace(/.$/, '')` replaces the last character of the string with an empty string.

```javascript
let str = 'Masteringjs.ioF';
str.substring(0, str.length - 1); // Masteringjs.io
str.substr(0, str.length - 1); // Masteringjs.io
str.replace(/.$/, ''); // Masteringjs.io
```

## Advanced Features

With `replace()`, you can specify if the last character should be removed depending on what it is with a regular expression. For example, suppose you want to remove the last character only if the last character is a number. You can use `.replace(/\d$/, '')` as shown below.

```javascript
// For a number, use \d$.
let str = 'Masteringjs.io0';
str.replace(/\d$/, ''); // Masteringjs.io

let str2 = 'Masteringjs.io0F';
// If the last character is not a number, it will not replace.
str.replace(/\d$/, ''); // Masteringjs.io0F;
```

## Comments from MDN

> [String.prototype.substring() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)

### The difference between substring() and substr()

There are subtle differences between the `substring()` and [`substr()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr) methods, so you should be careful not to get them confused.

- The two parameters of `substr()` are `start` and `length`, while for `substring()`, they are `start` and `end`.
- `substr()`'s `start` index will wrap to the end of the string if it is negative, while `substring()` will clamp it to `0`.
- Negative lengths in `substr()` are treated as zero, while `substring()` will swap the two indexes if `end` is less than `start`.

Furthermore, `substr()` is considered a *legacy feature in ECMAScript*, so it is best to avoid using it if possible.

```javascript
const text = 'Mozilla';
console.log(text.substring(2, 5));  // => "zil"
console.log(text.substr(2, 3));     // => "zil"
```

### Differences between substring() and slice()

The `substring()` and [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice) methods are almost identical, but there are a couple of subtle differences between the two, especially in the way negative arguments are dealt with.

The `substring()` method swaps its two arguments if `indexStart` is greater than `indexEnd`, meaning that a string is still returned. The [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice) method returns an empty string if this is the case.

```javascript
const text = 'Mozilla';
console.log(text.substring(5, 2));  // => "zil"
console.log(text.slice(5, 2));      // => ""
```

If either or both of the arguments are negative or `NaN`, the `substring()` method treats them as if they were `0`.

```javascript
console.log(text.substring(-5, 2));  // => "Mo"
console.log(text.substring(-5, -2)); // => ""
```

`slice()` also treats `NaN` arguments as `0`, but when it is given negative values it counts backwards from the end of the string to find the indexes.

```javascript
console.log(text.slice(-5, 2))   // => ""
console.log(text.slice(-5, -2))  // => "zil"
```

See the [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice) page for more examples with negative numbers.

### Replacing a substring within a string

The following example replaces a substring within a string. It will replace both individual characters and substrings. The function call at the end of the example changes the string `Brave New World` to `Brave New Web`.

```javascript
// Replaces oldS with newS in the string fullS
function replaceString(oldS, newS, fullS) {
  for (let i = 0; i < fullS.length; ++i) {
    if (fullS.substring(i, i + oldS.length) === oldS) {
      fullS = fullS.substring(0, i) + newS + fullS.substring(i + oldS.length, fullS.length);
    }
  }
  return fullS;
}

replaceString('World', 'Web', 'Brave New World');
```

Note that this can result in an infinite loop if `oldS` is itself a substring of `newS` — for example, if you attempted to replace '`World`' with '`OtherWorld`' here.

A better method for replacing strings is as follows:

```javascript
function replaceString(oldS, newS, fullS) {
  return fullS.split(oldS).join(newS);
}
```

The code above serves as an example for substring operations. If you need to replace substrings, most of the time you will want to use [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace).