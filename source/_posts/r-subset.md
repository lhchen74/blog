---
title: Subset Data Frame Rows in R
tags: r
date: 2021-05-12
---

> 转载: [Subset Data Frame Rows in R - Datanovia](https://www.datanovia.com/en/lessons/subset-data-frame-rows-in-r/)

## Subset Data Frame Rows in R

This tutorial describes how to **subset** or extract data frame rows based on certain criteria.

In this tutorial, you will learn the following R functions from the **dplyr** package:

-   **slice**(): Extract rows by position
-   **filter**(): Extract rows that meet a certain logical criteria. For example `iris %>% filter(Sepal.Length > 6)`.
-   **filter_all**(), **filter_if**() and **filter_at**(): filter rows within a selection of variables. These functions replicate the logical criteria over all variables or a selection of variables.
-   **sample_n**(): Randomly select n rows
-   **sample_frac**(): Randomly select a fraction of rows
-   **top_n**(): Select top n rows ordered by a variable

We will also show you how to remove rows with missing values in a given column.

## Required packages

Load the `tidyverse` packages, which include `dplyr`:

```R
library(tidyverse)
```

## Demo dataset

We’ll use the R built-in iris data set, which we start by converting into a tibble data frame (tbl_df) for easier data analysis.

```R
my_data <- as_tibble(iris)
my_data
## # A tibble: 150 x 5
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          5.1         3.5          1.4         0.2 setosa
## 2          4.9         3            1.4         0.2 setosa
## 3          4.7         3.2          1.3         0.2 setosa
## 4          4.6         3.1          1.5         0.2 setosa
## 5          5           3.6          1.4         0.2 setosa
## 6          5.4         3.9          1.7         0.4 setosa
## # ... with 144 more rows
```

## Extract rows by position

-   Key R function: `slice()` [dplyr package]

```R
my_data %>% slice(1:6)
```

## Filter rows by logical criteria

-   Key R function: `filter()` [dplyr package]. Used to filter rows that meet some logical criteria.

Before continuing, we introduce logical comparisons and operators, which are important to know for filtering data.

### Logical comparisons

The “logical” comparison operators available in R are:

1. Logical comparisons
    - **<**: for less than
    - **>**: for greater than
    - **<=**: for less than or equal to
    - **>=**: for greater than or equal to
    - **==**: for equal to each other
    - **!=**: not equal to each other
    - **%in%**: group membership. For example, “value **%in%** c(2, 3)” means that value can takes 2 or 3.
    - **is.na**(): is NA
    - **!is.na**(): is not NA.
2. Logical operators
    - value == 2**|**3: means that the value equal 2 or (|) 3. value **%in%** c(2, 3) is a shortcut equivalent to value == 2**|**3.
    - **&**: means and. For example sex == “female” & age > 25

The most frequent mistake made by beginners in R is to use = instead of == when testing for equality. Remember that, when you are testing for equality, you should always use == (not =).

### Extract rows based on logical criteria

-   **One-column based criteria**: Extract rows where Sepal.Length > 7:

```R
my_data %>% filter(Sepal.Length > 7)
## # A tibble: 12 x 5
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          7.1         3            5.9         2.1 virginica
## 2          7.6         3            6.6         2.1 virginica
## 3          7.3         2.9          6.3         1.8 virginica
## 4          7.2         3.6          6.1         2.5 virginica
## 5          7.7         3.8          6.7         2.2 virginica
## 6          7.7         2.6          6.9         2.3 virginica
## # ... with 6 more rows
```

-   **Multiple-column based criteria**: Extract rows where Sepal.Length > 6.7 and Sepal.Width ≤ 3:

```R
my_data %>% filter(Sepal.Length > 6.7, Sepal.Width <= 3)
## # A tibble: 10 x 5
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          6.8         2.8          4.8         1.4 versicolor
## 2          7.1         3            5.9         2.1 virginica
## 3          7.6         3            6.6         2.1 virginica
## 4          7.3         2.9          6.3         1.8 virginica
## 5          6.8         3            5.5         2.1 virginica
## 6          7.7         2.6          6.9         2.3 virginica
## # ... with 4 more rows
```

-   **Test for equality** (==): Extract rows where Sepal.Length > 6.5 and Species = “versicolor”:

```R
my_data %>% filter(Sepal.Length > 6.7, Species == "versicolor")
## # A tibble: 3 x 5
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          7           3.2          4.7         1.4 versicolor
## 2          6.9         3.1          4.9         1.5 versicolor
## 3          6.8         2.8          4.8         1.4 versicolor
```

-   **Using OR operator** (|): Extract rows where Sepal.Length > 6.5 and (Species = “versicolor” or Species = “virginica”):

Use this:

```R
my_data %>% filter(
  Sepal.Length > 6.7,
  Species == "versicolor" | Species == "virginica"
  )
## # A tibble: 20 x 5
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          7           3.2          4.7         1.4 versicolor
## 2          6.9         3.1          4.9         1.5 versicolor
## 3          6.8         2.8          4.8         1.4 versicolor
## 4          7.1         3            5.9         2.1 virginica
## 5          7.6         3            6.6         2.1 virginica
## 6          7.3         2.9          6.3         1.8 virginica
## # ... with 14 more rows
```

Or, equivalently, use this shortcut (**%in%** operator):

```R
my_data %>% filter(
  Sepal.Length > 6.7,
  Species %in% c("versicolor", "virginica" )
  )
```

## Filter rows within a selection of variables

This section presents 3 functions - **filter_all**(), **filter_if**() and **filter_at**() - to filter rows within a selection of variables.

These functions replicate the logical criteria over all variables or a selection of variables.

Create a new demo data set from `my_data` by removing the grouping column “Species”:

```R
my_data2 <- my_data %>% select(-Species)
```

-   Select rows where all variables are greater than 2.4:

```R
my_data2 %>% filter_all(all_vars(.> 2.4))
## # A tibble: 3 x 4
##   Sepal.Length Sepal.Width Petal.Length Petal.Width
##          <dbl>       <dbl>        <dbl>       <dbl>
## 1          6.3         3.3          6           2.5
## 2          7.2         3.6          6.1         2.5
## 3          6.7         3.3          5.7         2.5
```

-   Select rows when any of the variables are greater than 2.4:

```R
my_data2 %>% filter_all(any_vars(.> 2.4))
## # A tibble: 150 x 4
##   Sepal.Length Sepal.Width Petal.Length Petal.Width
##          <dbl>       <dbl>        <dbl>       <dbl>
## 1          5.1         3.5          1.4         0.2
## 2          4.9         3            1.4         0.2
## 3          4.7         3.2          1.3         0.2
## 4          4.6         3.1          1.5         0.2
## 5          5           3.6          1.4         0.2
## 6          5.4         3.9          1.7         0.4
## # ... with 144 more rows
```

-   Vary the selection of columns on which to apply the filtering criteria. `filter_at()` takes a `vars()` specification. The following R code apply the filtering criteria on the columns Sepal.Length and Sepal.Width:

```R
my_data2 %>% filter_at(vars(starts_with("Sepal")), any_vars(. > 2.4))
## # A tibble: 150 x 4
##   Sepal.Length Sepal.Width Petal.Length Petal.Width
##          <dbl>       <dbl>        <dbl>       <dbl>
## 1          5.1         3.5          1.4         0.2
## 2          4.9         3            1.4         0.2
## 3          4.7         3.2          1.3         0.2
## 4          4.6         3.1          1.5         0.2
## 5          5           3.6          1.4         0.2
## 6          5.4         3.9          1.7         0.4
## # ... with 144 more rows
```

## Remove missing values

We start by creating a data frame with missing values. In R **NA** (Not Available) is used to represent missing values:

```R
# Create a data frame with missing data
friends_data <- data_frame(
  name = c("A", "B", "C", "D"),
  age = c(27, 25, 29, 26),
  height = c(180, NA, NA, 169),
  married = c("yes", "yes", "no", "no")
)
# Print
friends_data
## # A tibble: 4 x 4
##   name    age height married
##   <chr> <dbl>  <dbl> <chr>
## 1 A        27    180 yes
## 2 B        25     NA yes
## 3 C        29     NA no
## 4 D        26    169 no
```

Extract rows where height is NA:

```R
friends_data %>% filter(is.na(height))
## # A tibble: 2 x 4
##   name    age height married
##   <chr> <dbl>  <dbl> <chr>
## 1 B        25     NA yes
## 2 C        29     NA no
```

Exclude (drop) rows where height is NA:

```R
friends_data %>% filter(!is.na(height))
## # A tibble: 2 x 4
##   name    age height married
##   <chr> <dbl>  <dbl> <chr>
## 1 A        27    180 yes
## 2 D        26    169 no
```

In the R code above, **!is.na()** means that “we don’t want” NAs.

## Select random rows from a data frame

It’s possible to select either n random rows with the function `sample_n()` or a random fraction of rows with `sample_frac()`. We first use the function `set.seed()` to initiate random number generator engine. This important for users to 转载 the analysis.

```R
set.seed(1234)
# Extract 5 random rows without replacement
my_data %>% sample_n(5, replace = FALSE)

# Extract 5% of rows, randomly without replacement
my_data %>% sample_frac(0.05, replace = FALSE)
```

## Select top n rows ordered by a variable

Select the top 5 rows ordered by Sepal.Length

```R
my_data %>% top_n(5, Sepal.Length)
## # A tibble: 5 x 5
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          7.7         3.8          6.7         2.2 virginica
## 2          7.7         2.6          6.9         2.3 virginica
## 3          7.7         2.8          6.7         2   virginica
## 4          7.9         3.8          6.4         2   virginica
## 5          7.7         3            6.1         2.3 virginica
```

Group by the column Species and select the top 5 of each group ordered by Sepal.Length:

```R
my_data %>%
  group_by(Species) %>%
  top_n(5, Sepal.Length)
## # A tibble: 16 x 5
## # Groups:   Species [3]
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
##          <dbl>       <dbl>        <dbl>       <dbl> <fct>
## 1          5.8         4            1.2         0.2 setosa
## 2          5.7         4.4          1.5         0.4 setosa
## 3          5.7         3.8          1.7         0.3 setosa
## 4          5.5         4.2          1.4         0.2 setosa
## 5          5.5         3.5          1.3         0.2 setosa
## 6          7           3.2          4.7         1.4 versicolor
## # ... with 10 more rows
```

## Summary

In this tutorial, we introduce how to filter a data frame rows using the dplyr package:

-   Filter rows by logical criteria: `my_data %>% filter(Sepal.Length >7)`
-   Select n random rows: `my_data %>% sample_n(10)`
-   Select a random fraction of rows: `my_data %>% sample_frac(10)`
-   Select top n rows by values: `my_data %>% top_n(10, Sepal.Length)`
