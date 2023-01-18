---
title: CSS Selector Quiz
tags: css
date: 2022-03-18
quiz: true
---

> 转载: [CSS Speedrun | Test your CSS Skills](https://css-speedrun.netlify.app/)
> 转载: [CSS selectors - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)

Enter the CSS selector, which applies to all elements with an arrow ⬅️

```html
<ul>
    <li></li> ⬅️
    <li></li>
    <li></li>
</ul>
```

1. 💡 [`li:first-child`]{.gap} {.quiz .fill}

   > The :first-child CSS pseudo-class represents the first element among a group of sibling elements.
   >
   > `li:first-child` is right for below.
   >
   > ```html
   > <ul>
   >     <li></li> ⬅️
   >     <li></li>
   >     <li></li>
   >     <ul>
   >         <li></li> ⬅️
   >         <li></li>
   >         <li></li>
   >     </ul>
   > </ul>
   > ```
   >
   > 

## Level1

```html
<div>
    <p></p> ⬅️
    <p class="foo"></p>
    <p></p> ⬅️
    <p></p> ⬅️
</div>
```

1. 💡 [`p:not(.foo)`]{.gap} {.quiz .fill}

   > The :not() CSS pseudo-class represents elements that do not match a list of selectors. Since it prevents specific items from being selected, it is known as the negation pseudo-class.

## Level2

```html
<ul>
  <li></li>
  <li></li>
  <li></li> ⬅️
  <li></li>
  <li></li> ⬅️
  <li></li>
  <li></li> ⬅️
</ul>
```

1. 💡 [`li:nth-child(2n+3)`]{.gap} {.quiz .fill}

   > The :nth-child() CSS pseudo-class matches elements based on their position among a group of siblings.
   >
   > **Functional notation <An+B>**
   > Represents elements in a list whose indices match those found in a custom pattern of numbers, defined by An+B, where:
   >
   > - A is an integer step size
   >
   > - B is an integer offset
   >
   > - n is all nonnegative integers, starting from 0
   >
   >
   >It can be read as the An+Bth element of a list.   

## Level3

```html
<div>
  <span></span> ⬅️
  <p>           ⬅️
    <a></a>
    <span></span>
  </p>
</div>
```

1. 💡 [`div > *`]{.gap} {.quiz .fill}

   > `>` direct child selector.
   >
   > `*` represent all elements.

## Level4

```html
<div>
  <span data-item="foo"></span>   ⬅️
  <span></span>
  <div>
    <span></span>
    <span data-item="bar"></span> ⬅️
    <span></span>
  </div>
</div>
```

1. 💡 [`span[data-item]`]{.gap} {.quiz .fill}

   > The CSS **attribute selector** matches elements based on the presence or value of a given attribute.

## Level5

```html
<div>
  <span></span>
  <code></code>
  <span></span>
  <p></p>
  <span></span> ⬅️
  <span></span> ⬅️
  <p></p>
  <code></code>
  <span></span> ⬅️
  <p></p>
</div>
```

1. 💡 [`p ~ span`]{.gap} {.quiz .fill}

   > The **general sibling combinator** (`~`) separates two selectors and matches *all iterations* of the second element, that are following the first element (though not necessarily immediately), and are children of the same parent [element](https://developer.mozilla.org/en-US/docs/Glossary/Element).

## Level6

```html
<form>
  <input /> ⬅️
  <input disabled />
  <input /> ⬅️
  <input /> ⬅️
  <button disabled></button>
  <button></button> ⬅️
</form>
```

1. 💡 [`:enabled`]{.gap} {.quiz .fill}

   > The **:enabled** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) represents any enabled element. An element is enabled if it can be activated (selected, clicked on, typed into, etc.) or accept focus. The element also has a disabled state, in which it can't be activated or accept focus.

## Level7

```html
<div>
  <span></span>
  <p>
    <a></a> 
    <span></span> ⬅️
  </p>
  <p>
    <span></span>
    <a></a>
    <span></span> ⬅️
    <span></span>
  </p>
  <a></a>
  <span></span>   ⬅️
</div>
```

1. 💡 [`a + span`]{.gap} {.quiz .fill}

   > The **adjacent sibling combinator** (`+`) separates two selectors and matches the second element only if it *immediately* follows the first element, and both are children of the same parent [`element`](https://developer.mozilla.org/en-US/docs/Web/API/Element).

## Level8

```html
<div id="foo">
  <div class="foo"></div>  ⬅️
  <div></div>
  <div>
    <div class="foo"></div>
    <div></div>
  </div>
  <div class="foo"></div>  ⬅️
</div>
```

1. 💡 [`#foo > .foo`]{.gap} {.quiz .fill}

   > The **child combinator** (`>`) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the direct children of elements matched by the first.

## Level9

```html
<div>
  <div>
    <span></span>
    <code></code> ⬅️
  </div>
  <div>
    <code></code>
    <span></span> 
    <code></code> ⬅️
  </div>
  <div>
    <span></span>
    <code class="foo"></code>
  </div>
  <span></span>
  <code></code>
</div>
```

1. 💡 [`div div span + code:not(.foo)`]{.gap} {.quiz .fill}

   > 

## Comments

| CSS Selector | Meaning                   |
| ------------ | ------------------------- |
| a, b         | Multiple Element Selector |
| a b          | Descendant Selector       |
| a > b        | Child Selector            |
| a ~ b        | General Sibling Selector  |
| a + b        | Adjacent Sibling Selector |
| [a=b]        | Attribute Selector        |
| a:b          | Pseudoclass Selector      |
| a::b         | Pseudoelement Selector    |

