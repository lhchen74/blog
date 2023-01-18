---
title: Escaping backtick in Markdown
tags: markdown
date: 2022-05-31
---

> 转载：[Escaping backtick in Markdown - Growing with the Web](https://www.growingwiththeweb.com/2015/06/escaping-backtick-in-markdown.html)

The backtick (also known as the grave accent or backquote) is used to start a code section in Markdown, because of this it's a little tricky to include it without triggering the code formatting in a page. This snippet demonstrates the various ways of displaying a backtick.

## Backtick outside code

To include a non-code formatted backtick it can be added by escaping it with a `\`.

```markdown
\`
```

## Backtick within code

Wrapping inline code blocks in double backticks instead of single backticks allow a backtick to be used.

```markdown
`` ` ``
```

such as \`\` \` this is a test \` \`\` will be `` `this is a test` ``

Alternatively a code block can be used, this will wrap everything in a `<pre>` however. To do this either indent 4 spaces to start a code block

```markdown
    `
```

or use fenced code blocks if supported

```markdown
​```
`
​```
```