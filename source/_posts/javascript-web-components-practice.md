---
title: Web Components Practice
tags: js
date: 2022-05-19
---

## Button Click Counter use Web Components

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Components</title>
</head>
<body>
    <script type="module" src="main.js"></script>
    
    <my-counter></my-counter>
</body>
</html>
```

```js
class Counter extends HTMLElement {
    static get observedAttributes() {
        return ["count"] // observe 'count' attribute change
    }

    get count() {
        return this.getAttribute("count") || 0
    }

    set count(value) {
        this.setAttribute("count", value);
    }

    attributeChangedCallback(attribute, oldVal, newVal) {
        if (attribute === 'count') {
            this.btn.textContent = newVal
        }
    }

    constructor() {
        super()
        this.attachShadow({mode: "open"})
        this.shadowRoot.innerHTML = `
            <button>${this.count}</button>
        `
        this.btn = this.shadowRoot.querySelector('button')
        this.btn.addEventListener("click", () => this.count++)
    }
}


customElements.define("my-counter", Counter)
```

## Use Google Lit Framework Samplify Web Components Use

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Components</title>
    <style>
        :root {
            --my-color: red;
        }
    </style>
</head>
<body>
    <script type="module" src="main.js"></script>

    <lit-counter count="1"></lit-counter>
</body>
</html>
```

```js
import {LitElement, html, css} from "https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js"

class LitCounter extends LitElement {
    static properties = {
        count: {}  // observe 'count' property change
    }

    static styles = css`
        button {
            color: var(--my-color);
        }
    `

    constructor() {
        super()
        this.count = 0
    }

    render() {
        return html`<button @click=${() => this.count++}>${this.count}</button>`
    }
}

customElements.define("lit-counter", LitCounter)
```

## Web Components UI Framework

> [carbon-web-components: Carbon Design System variant on top of Web Components](https://github.com/carbon-design-system/carbon-web-components)

>[shoelace: A forward-thinking library of web components.](https://shoelace.style/)

> [Components - UI5 Web Components](https://sap.github.io/ui5-webcomponents/playground/components)

> [Spectrum Web Components](https://opensource.adobe.com/spectrum-web-components/)

> [Kor: An open source Design System and lightweight UI Component Library.](https://kor-ui.com/introduction/welcome)

> [Fluent UI Web Components Overview | Microsoft Docs](https://docs.microsoft.com/en-us/fluent-ui/web-components/)

> [Wired Elements](https://wiredjs.com/showcase.html)

> [VSCode Webview Elements](https://bendera.github.io/vscode-webview-elements/)