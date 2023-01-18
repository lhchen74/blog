---
title: Write HTML, the HTML Way (Not the XHTML Way)
tags: html
date: 2022-05-19
---

> 转载：[Write HTML, the HTML Way (Not the XHTML Way) | CSS-Tricks - CSS-Tricks](https://css-tricks.com/write-html-the-html-way-not-the-xhtml-way/)

You may not use XHTML (anymore), but when you write HTML, you may be more influenced by XHTML than you think. You are very likely writing HTML, the XHTML way.

What is the XHTML way of writing HTML, and what is the HTML way of writing HTML? Let’s have a look.

In the 1990s, there was HTML. In the 2000s, there was XHTML. Then, in the 2010s, we switched back to HTML. That’s the simple story.

You can tell by the rough dates of the specifications, too: HTML "1" 1992, HTML 2.0 1995, HTML 3.2 1997, HTML 4.01 1999; XHTML 1.0 2000, XHTML 1.1 2001; "HTML5" [2007](https://en.wikipedia.org/wiki/HTML5#Timeline).

XHTML became popular when everyone believed XML and XML derivatives were the future. "XML all the things." For HTML, this had a profound effect: The effect that we learned to write it the XHTML way.

## The XHTML way of writing HTML

The XHTML way is well-documented, because XHTML 1.0 describes in great detail in its section on ["Differences with HTML 4"](https://www.w3.org/TR/xhtml1/#diffs):

- Documents must be well-formed.
- Element and attribute names must be in lower case.
- For non-empty elements, end tags are required.
- Attribute values must always be quoted.
- [Attribute minimization](https://www.w3.org/TR/xhtml1/#h-4.5) is not supported.
- Empty elements need to be closed.
- White space handling in attribute values is done according to XML.
- Script and style elements need CDATA sections.
- SGML exclusions are not possible.
- The elements with `id` and `name` attributes, like `a`, `applet`, `form`, `frame`, `iframe`, `img`, and `map`, should only use `id`.
- Attributes with pre-defined value sets are case-sensitive.
- Entity references as hex values must be in lowercase.

Does this look familiar? With the exception of marking CDATA content, as well as dealing with SGML exclusions, you probably follow all of these rules. **All of them.**

Although XHTML is dead, many of these rules have never been questioned again. Some have even been elevated to "best practices" for HTML.

That is the XHTML way of writing HTML, and its lasting impact on the field.

## The HTML way of writing HTML

One way of walking us back is to negate the rules imposed by XHTML. Let’s actually do this (without the SGML part, because HTML [isn’t based on SGML anymore](https://html.spec.whatwg.org/multipage/parsing.html#parsing)):

- Documents may not be well-formed.
- Element and attribute names may not be in lower case.
- For non-empty elements, end tags are not always required.
- Attribute values may not always be quoted.
- Attribute minimization is supported.
- Empty elements don’t need to be closed.
- White space handling in attribute values isn’t done according to XML.
- Script and style elements don’t need CDATA sections.
- The elements with `id` and `name` attributes may not only use `id`.
- Attributes with pre-defined value sets are not case-sensitive.
- Entity references as hex values may not only be in lowercase.

Let’s remove the esoteric things; the things that don’t seem relevant. This includes XML whitespace handling, CDATA sections, doubling of `name` attribute values, the case of pre-defined value sets, and hexadecimal entity references:

- Documents may not be well-formed.
- Element and attribute names may not be in lowercase.
- For non-empty elements, end tags are not always required.
- Attribute values may not always be quoted.
- Attribute minimization is supported.
- Empty elements don’t need to be closed.

Peeling away from these rules, this looks a lot less like we’re working with XML, and more like working with HTML. But we’re not done yet.

"Documents may not be well-formed" suggests that it was fine if HTML code was invalid. It was fine for XHTML to point to wellformedness because of XML’s strict error handling. But while HTML documents work even when they contain severe syntax and wellformedness issues, it’s neither useful for the professional — nor our field — to use and abuse this resilience. (I’ve argued this case before in my article, ["In Critical Defense of Frontend Development."](https://meiert.com/en/blog/critical-frontend-development/))

The HTML way would therefore not suggest "documents may not be well-formed." It would also be clear that not only end, but also start tags aren’t always required. Rephrasing and reordering, this is the essence:

- Start and end tags are not always required.
- Empty elements don’t need to be closed.
- Element and attribute names may be lower or upper case.
- Attribute values may not always be quoted.
- Attribute minimization is supported.

## Examples

How does this look like in practice? For start and end tags, be aware that [many tags](https://meiert.com/en/blog/optional-html/#toc-tags) are optional. A paragraph and a list, for example, are written like this in XHTML:

```html
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
<ul>
  <li>Praesent augue nisl</li>
  <li>Lobortis nec bibendum ut</li>
  <li>Dictum ac quam</li>
</ul>
```

In HTML, however, you can write them using only this code (which is valid):

```html
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
<ul>
  <li>Praesent augue nisl</li>
  <li>Lobortis nec bibendum ut</li>
  <li>Dictum ac quam</li>
</ul>
```

Developers also learned to write void elements, like so:

```html
<br />
```

This is something XHTML brought to HTML, but as [the slash has no effect on void elements](https://html.spec.whatwg.org/multipage/syntax.html#start-tags), you only need this:

```html
<br />
```

In HTML, you can also just write everything in all caps:

```html
<a href="https://css-tricks.com/">CSS-Tricks</a>
```

It looks like you’re yelling and you may not like it, but it’s okay to write it like this.

When you want to condense that link, HTML offers you the option to [leave out certain quotes](https://meiert.com/en/blog/optional-html/#toc-quotes):

```html
<A HREF=https://css-tricks.com/>CSS-Tricks</A>
```

As a rule of thumb, when the attribute value doesn’t contain a space or an equal sign, it’s usually fine to drop the quotes.

Finally, HTML–HTML — not XHTML–HTML — also allows to minimize attributes. That is, instead of marking an `input` element as required and read-only, like this:

```html
<input type="text" required="required" readonly="readonly" />
```

You can minimize the attributes:

```html
<input type="text" required readonly />
```

If you’re not only taking advantage of the fact that the quotes aren’t needed, but that `text` is the default for the `type` attribute here (there are more such [unneeded attribute–value combinations](https://meiert.com/en/blog/optional-html/#toc-attribute-values)), you get an example that shows HTML in all its minimal beauty:

```html
<input required readonly />
```

## Write HTML, the HTML way

The above isn’t a representation of where HTML was in the 90s. HTML, back then, was loaded with `<table>` elements for layout, packed with presentational code, largely invalid ([as it’s still today](https://meiert.com/en/blog/valid-html-2021/)), with wildly varying user agent support. Yet it’s the _essence_ of what we would have wanted to keep if XML and XHTML hadn’t come around.

If you’re open to a suggestion of what a more comprehensive, contemporary way of writing HTML could look like, I have one. (HTML is my main focus area, so I’m augmenting this by links to some of my articles.)

1. Respect syntax and semantics.
   - [Validate your HTML](https://meiert.com/en/blog/the-frontend-developer-test/), and ship only valid HTML.
2. Use the options HTML gives you, as long as you do so consistently.
   - Remember that element and attribute names may be lowercase or uppercase.
3. Keep use of HTML to the absolute minimum
   - Remember that presentational and behavioral markup is to be handled by CSS and JavaScript instead.
   - Remember that start and end tags are [not always](https://meiert.com/en/blog/optional-html/#toc-tags) required.
   - Remember that empty elements don’t need to be closed.
   - Remember that some attributes have defaults that allow [these attribute–value pairs to be omitted](https://meiert.com/en/blog/optional-html/#toc-attribute-values).
   - Remember that attribute values may [not always](https://meiert.com/en/blog/optional-html/#toc-quotes) be quoted.
   - Remember that attribute minimization is supported.

It’s not a coincidence that this resembles [the three ground rules for HTML](https://meiert.com/en/blog/rules-for-html/), that it works with the premise of [a smaller payload also leading to faster sites](https://meiert.com/en/blog/html-performance/), and that this follows [the school of minimal web development](https://meiert.com/en/blog/minimal-web-development/). None of this is new — our field could merely decide to rediscover it. Tooling is available, too: [html-minifier](https://github.com/kangax/html-minifier) is probably the most established and able to handle all HTML optimizations.

You’ve learned HTML the XHTML way. HTML isn’t XHTML. Rediscover HTML, and help shape a new, modern way of writing HTML — which acknowledges, but isn’t necessarily based on XML.
