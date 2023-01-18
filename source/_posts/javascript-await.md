---
title: await - JavaScript | MDN
tags: js
date: 2022-09-16
---

> 转载：[await - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#syntax)

The `await` operator is used to wait for a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) and get its fulfillment value. It can only be used inside an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) or a [JavaScript module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

## [Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#syntax)

```js
await expression;
```

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#parameters)

- `expression`

  A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) or any value to wait for.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#return_value)

The fulfillment value of the promise, or the expression itself's value itself if it's not a `Promise`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#exceptions)

Throws the rejection reason if the promise is rejected.

## [Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#description)

The `await` expression causes async function execution to pause until a promise is settled (that is, fulfilled or rejected), and to resume execution of the async function after fulfillment. When resumed, the value of the `await` expression is that of the fulfilled promise.

The `expression` is resolved in the same way as [`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve), which means [thenable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables) are supported, and if `expression` is not a promise, it's implicitly wrapped in a `Promise` and then resolved.

If the promise is rejected, the `await` expression throws the rejected value. The function containing the `await` expression will [appear in the stack trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#improving_stack_trace) of the error. Otherwise, if the rejected promise is not awaited or is immediately returned, the caller function will not appear in the stack trace.

An `await` splits execution flow, allowing the caller of the async function to resume execution. After the `await` defers the continuation of the async function, execution of subsequent statements ensues. If this `await` is the last expression executed by its function, execution continues by returning to the function's caller a pending `Promise` for completion of the `await`'s function and resuming execution of that caller.

Because `await` is only valid inside async functions and modules, which themselves are asynchronous and return promises, the `await` expression never blocks the main thread and only defers execution of code that actually depends on the result, i.e. anything after the `await` expression.

## [Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#examples)

### [Awaiting a promise to be fulfilled](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#awaiting_a_promise_to_be_fulfilled)

If a `Promise` is passed to an `await` expression, it waits for the `Promise` to be fulfilled and returns the fulfilled value.

```js
function resolveAfter2Seconds(x) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

async function f1() {
  const x = await resolveAfter2Seconds(10);
  console.log(x); // 10
}

f1();
```

### [Thenable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#thenable_objects)

[Thenable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables) will be fulfilled just the same.

```js
async function f2() {
  const thenable = {
    then(resolve, _reject) {
      resolve("resolved!");
    },
  };
  console.log(await thenable); // resolved!
}

f2();
```

### [Conversion to promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#conversion_to_promise)

If the value is not a `Promise`, it converts the value to a resolved `Promise`, and waits for it.

```js
async function f3() {
  const y = await 20;
  console.log(y); // 20
}

f3();
```

### [Promise rejection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#promise_rejection)

If the `Promise` is rejected, the rejected value is thrown.

```js
async function f4() {
  try {
    const z = await Promise.reject(30);
  } catch (e) {
    console.error(e); // 30
  }
}

f4();
```

### [Handling rejected promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#handling_rejected_promises)

You can handle rejected promises without a `try` block by chaining a [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) handler before awaiting the promise.

```js
const response = await promisedFunction().catch((err) => {
  console.error(err);
});
// response will be undefined if the promise is rejected
```

### [Top level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await)

You can use the `await` keyword on its own (outside of an async function) within a [JavaScript module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules). This means modules, with child modules that use `await`, wait for the child module to execute before they themselves run, all while not blocking other child modules from loading.

Here is an example of a simple module using the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and specifying await within the [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) statement. Any modules that include this will wait for the fetch to resolve before running any code.

```js
// fetch request
const colors = fetch("../data/colors.json").then((response) => response.json());

export default await colors;
```

### [Control flow effects of await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#control_flow_effects_of_await)

When an `await` is encountered in code (either in an async function or in a module), execution of all code following this is immediately paused and pushed into the [microtask queue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop). The main thread is then freed for the next task in the event loop. This happens even if the awaited value is an already-resolved promise or not a promise. For example, consider the following code:

```js
async function foo(name) {
  console.log(name, "start");
  console.log(name, "middle");
  console.log(name, "end");
}

foo("First");
foo("Second");

// First start
// First middle
// First end
// Second start
// Second middle
// Second end
```

In this case, the two async functions are synchronous in effect, because they don't contain any `await` expression. The three statements happen in the same tick. In promise terms, the function corresponds to:

```js
function foo(name) {
  return Promise.resolve().then(() => {
    console.log(name, "start");
    console.log(name, "middle");
    console.log(name, "end");
  });
}
```

However, as soon as there's one `await`, the function becomes asynchronous, and execution of following statements is deferred to the next tick.

```js
async function foo(name) {
  console.log(name, "start");
  await console.log(name, "middle");
  console.log(name, "end");
}

foo("First");
foo("Second");

// First start
// First middle
// Second start
// Second middle
// First end
// Second end
```

This corresponds to:

```js
function foo(name) {
  return Promise.resolve()
    .then(() => {
      console.log(name, "start");
      console.log(name, "middle");
    })
    .then(() => {
      console.log(name, "end");
    });
}
```

While the extra `then()` handler is not necessary and can be merged with the previous one, its existence means the code will take one extra tick to complete. The same happens for `await`. Therefore, make sure to use `await` only when necessary (to unwrap promises into their values).

### [Improving stack trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#improving_stack_trace)

Sometimes, the `await` is omitted when a promise is directly returned from an async function.

```js
async function noAwait() {
  // Some actions...

  return /* await */ lastAsyncTask();
}
```

However, consider the case where `someAsyncTask` asynchronously throws an error.

```js
async function lastAsyncTask() {
  await setTimeout(() => {}, 100);
  throw new Error("failed");
}

async function noAwait() {
  return lastAsyncTask();
}

noAwait();

// Error: failed
//    at lastAsyncTask
```

Only `lastAsyncTask` appears in the stack trace, because the promise is rejected after it has already been returned from `noAwait` — in some sense, the promise is unrelated to `noAwait`. To improve the stack trace, you can use `await` to unwrap the promise, so that the exception gets thrown into the current function. The exception will then be immediately wrapped into a new rejected promise, but during error creation, the caller will appear in the stack trace.

```js
async function lastAsyncTask() {
  await setTimeout(() => {}, 100);
  throw new Error("failed");
}

async function withAwait() {
  return await lastAsyncTask();
}

withAwait();

// Error: failed
//    at lastAsyncTask
//    at async withAwait
```

However, there's a little performance penalty coming with `return await` because the promise has to be unwrapped and wrapped again.

## Comments

```js
const getLastPost = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const data = await res.json();

  return { title: data.at(-1).title };
};
```

- promise.then

  ```js
  const lastPost = getLastPost().then((post) => console.log(post));
  console.log("end");
  
  // end
  // {title: 'at nam consequatur ea labore ea harum'}
  ```

- async wrap IIFE(Immediately Invoked Function Expression)

  ```js
  (async () => {
    const lastPost = await getLastPost();
    console.log(lastPost);
  })();
  console.log("end");
  
  // end
  // {title: 'at nam consequatur ea labore ea harum'}
  ```

- top level await

  ```js
  const lastPost = await getLastPost();
  console.log(lastPost);
  console.log("end");
  
  // {title: 'at nam consequatur ea labore ea harum'}
  // end
  ```
  
  Import in HTML need by module way.
  
  ```html
  <script type="module" defer src="script.js"></script>
  ```
  
  