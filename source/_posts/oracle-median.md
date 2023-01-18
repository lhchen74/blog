---
title: Oracle Calculate Median
tag: db
date: 2022/12/08
---

## Median Define

统计学上，中位数（Median），又称中央值、中值，是一个样本、种群或概率分布中之一个数值，其可将数值集合划分为数量相等的上下两部分。对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。如果观察值有偶数个，则中位数不唯一，通常取最中间的两个数值的平均数作为中位数。

一个数集中最多有一半的数值小于中位数，也最多有一半的数值大于中位数。如果大于和小于中位数的数值个数均少于一半，那么数集中必有若干值等同于中位数。

## Data Set

```sql
create table movie_ratings (
  rating number
);

insert into movie_ratings(rating) values (11);
insert into movie_ratings(rating) values (12);
insert into movie_ratings(rating) values (15);
insert into movie_ratings(rating) values (19);
insert into movie_ratings(rating) values (12);
insert into movie_ratings(rating) values (13);
insert into movie_ratings(rating) values (16);
insert into movie_ratings(rating) values (20);
```

## ROW_NUMBER() Window Function

对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。如果观察值有偶数个，则中位数不唯一，通常取最中间的两个数值的平均数作为中位数。

```sql
select avg(m.rating)
  from (select m1.rating,
               row_number() over(order by m1.rating) as row_num,
               count(*) over() as cnt
          from movie_ratings m1) m
 where m.row_num in
       (floor(cnt / 2) + 1,
        case when mod(cnt, 2) = 0 then cnt / 2 else floor(cnt / 2) + 1 end);
--14
```

```sql
--11, 12, 12, 13, 15, 16, 19, 20
select avg(m.rating)
  from (select m1.rating,
               row_number() over(order by m1.rating) as row_num1, --11, 12, 12, 13, 15, 16, 19, 20
               row_number() over(order by m1.rating desc) as row_num2, --20, 19, 16, 15, 13, 12, 12, 11
               count(*) over() as cnt
          from movie_ratings m1) m
 where row_num1 = round(cnt / 2) --13
    or row_num2 = round(cnt / 2); --15
```

## HAVING Clause

一个数集中最多有一半的数值小于中位数，也最多有一半的数值大于中位数。

```sql
--11, 12, 12, 13, 15, 16, 19, 20
select avg(m.rating)
  from (select m1.rating
          from movie_ratings m1, movie_ratings m2
         group by m1.rating
        having sum(case when m1.rating <= m2.rating then 1 else 0 end) >= count(*) / 2 --11, 12, 12, 13, 15
           and sum(case when m1.rating >= m2.rating then 1 else 0 end) >= count(*) / 2 --13, 15, 16, 19, 20
        ) m;

--14
```

## MEDIAN Function

```sql
select median(rating) from movie_ratings;
--14
```
