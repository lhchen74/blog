---
title: ISO 8601 the better date format
tags: other
date: 2021-03-19
---

> 转载: [ISO 8601: the better date format](https://kirby.kevinson.org/blog/iso-8601-the-better-date-format/)

If you haven’t been living under a rock, you’ve probably heard that there are different date formats in the world such as the American one (mm/dd/yyyy) and the European one (dd.mm.yyyy). If you’re smart enough, you’ve probably also noticed that the American one makes no sense and is just awful. A simple conclusion that many people draw out of this is that the European format is the best one, however I don’t think this is true. If you’re one of these people who think so, I’m here to (hopefully) change your mind by introducing you to a lesser-known date format called ISO 8601.

## Basics

As you can see by the “ISO” part in the format’s name, it’s an actual standard written by the International Organization for Standardization. It defines many cool things like a way to write time intervals, which can be useful for writing portable software, and a calendar where the year is separated not by months but by weeks, which is used in finances, but here we’re only interested in the basics. Simplified, the core date format looks like this:

```
yyyy-mm-dd hh:mm:ss
```

Yup, that’s about it. You write the year, the month, the day, and then the time exactly like it’s done in other date formats. There’s nothing extraordinary, so you can learn it in 2 minutes.

## Why it’s better

### It’s unambigous

This is the main reason the standard was written and why people still use it. Other date formats can be diffucult to tell apart. For example, consider this date:

```
02-03-04
```

When you read it out of context, you have absolutely no idea what’s going on there. Is `02` here the day or the month? You just can’t know unless the day in the date is greater than 12, in which case it just can’t be a month:

```
30-03-04
```

This day-month ambiguity is a really common problem, which often occurs online. People just write down their dates in whatever date format they know without even thinking that other people can interpret it in different ways.

ISO 8601 doesn’t have this problem as it’s always obvious which part is the day and which is the month because of the uniqueness of the format:

```
2004-03-02
```

### It’s more strict

While other date formats usually don’t provide strict requirements on how to write something, ISO 8601 is an exception. Here there’s only one correct way to write a date, which is not only useful for computers to parse, but also helpful for humans to avoid confusion with other formats and improve readability. Here are some of the restrictions:

- The elements in the date are always separated by a hyphen. Not many date formats use this delimiter, and this also can be useful when using dates inside filenames as slashes are usually not accepted in them.
- The elements are always padded to the maximum number of digits. This not only makes all of the dates look equally nice, but also, coupled with other quirks of this format, allows the files with the date in the name to be sorted just by the filename.
- The year is always written in the full form. This makes the format unique when written down and eliminates [the year 2000 problem](https://en.wikipedia.org/wiki/Year_2000_problem) in any forms that it can take. For example, when writing down birthdays, it always makes it obvious which century we’re talking about.
- The time is always written in the 24 hour format, so there can be no confusion about what half of the day something happened in.

### It makes more sense

On the first glance, it seems like the European format is about as logical as it can get - days go into months and months go into years:

```
18.12.2002
---------> Elements
```

However, this ignores a very important characteristic of numbers - endianness. Consider a regular number, for example:

```
69420
<---- Digits
```

As you can see the digits here do the opposite of what elements do in the European format. When the leftmost element of something is the most valuable, we call it big endian.

Thus, the European format is little endian while the numbers in it are big endian:

```
18.12.2002
<- <- <--- Digits
---------> Elements
```

And the American format just makes no sense:

```
12/18/2002
<- <- <--- Digits
?????????? Elements
```

And, as you can see, ISO 8601 is completely consistent in this regard as everything is big endian:

```
2002-12-18
<--- <- <- Digits
<--------- Elements
```

The situation becomes even worse if you consider time because it is big endian, like ISO 8601, thus doesn’t work with any other date format:

```
18.12.2002 23:03:59
<- <- <--- <- <- <- Digits
---------> <------- Elements

12/18/2002 23:03:59
<- <- <--- <- <- <- Digits
?????????? <------- Elements

2002-12-18 23:03:59
<--- <- <- <- <- <- Digits
<--------- <------- Elements
```

If you’re still having trouble visualizing all of this in your head, look at [this Reddit post](https://www.reddit.com/r/ISO8601/comments/ln33j2/datetime_format_by_region_visualised_v3_thanks/).

### It’s standardized and actively used

If you think that ISO 8601 is a silly thing that someone in their basement made up and no one actually uses, think again because that can’t be further from the truth:

- The fact that it’s standardized says at least something. Does your favorite format has a neat several hundred page document where it’s described in extreme detail and that is internationally recognized? Also the standard is quite far from being dead - after being published in 1988 it was updated in 1991, 2000, 2004, and 2019.
- As I already mentioned, the standard is actively used in IT. Almost everything that is used by software and somehow involves a written numerical date format already speaks ISO 8601.
- yyyy-mm-dd has been adapted or used since the beginning as a national date format by many countries such as Canada, Sweden, and Japan. See [this article](https://en.wikipedia.org/wiki/Date_format_by_country) for more details.

## Frequently asked questions

### Why not use a format like 01-Jan-2020?

It doesn’t have any of the nice features ISO 8601 has and doesn’t work well internationally (i.e. assumes the person you’re communicating with knows knows English). If you think the latter is not a problem, imagine how you would feel feel if you had to read a date someone wrote in their native language that you don’t understand:

```
01-Янв-2020
```

### yyyy-mm-dd looks weird

The only reason why it does to you is because you’re not used to it. After a little bit of practice, it’ll be even less weird than your favorite date format.

### Maybe the European date format is better because the elements are in the order of relevance?

First of all, the claim that the order of relevance is little endian is quite questionable. The only situation when you can say that for certain is when we’re talking about events occuring on a day-to-day basis, however I can think of numerous cases when the year and the month are more relevant:

- Article publication date
- Historical event
- Personal event that happened a long time ago
- Someone’s birthday
- Random database entry

Second, the order of relevance is actually irrelevant. Even if the order of relevance was this way, you’re not reading the dates out loud, so there’s no need for them to be ordered a certain way. If you’re not interested in the year, you just skip it and read the end of the date just like you would do when reading time while not being interested in the hour.

## Conclusion

In my opinion, ISO 8601 seems clearly superior to other date formats when it comes to international communication (such as posting things online), and as you can see, I have enough reasons to say so. While the format certainly has an audience, it’s unfortunate that it’s not as big as it could be. By writing this article, I hope I made you at least think about different date formats and be more careful when it comes to making people understand what date you’re talking about.