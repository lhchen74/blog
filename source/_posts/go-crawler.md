---
title: Build a Web Crawler in Go
tag: go
date: 2020-03-18
---

> 转载：[Build a Web Crawler in Go](https://jdanger.com/build-a-web-crawler-in-go.html)

One of the basic tests I use to try out a new programming language is building a web crawler. I stole the idea from my colleague [Mike Lewis](https://twitter.com/MikeLewis) and I love it because it uses all the principles necessary in internet engineering: A web crawler needs to parse semi-structured text, rely on 3rd-party APIs, manage its internal state, and perform some basic concurrency.

## Starting a new project with Go

This is a tutorial that is accessible for complete beginners to the Go programming language or to web programming. All the commands you need to run are provided and all the code you need to type into the `.go` source code files is shown to you a piece at a time. Each time I introduce a new concept you’ll need to edit the same file, slowly building up functionality. When you run each version of the code Go will give you an exact error message with a line number so you’ll be able to fix any mistakes you make. If you get totally lost you can just copy straight out of the page into a new file and pick back up. If you’re new to Go I _highly_ recommend reading the excellent [Go documentation](http://golang.org/doc/) to help you make sense of what’s on this page.

Since this example requires the Go programming language you should start by installing Go:

```bash
sudo apt-get install golang  # (if you're on Linux)
brew install go  # (if you're on a Mac)
```

## Creating the ‘main’ function

Go is so fast that it’s practically a scripting language. All you need to run it is a ‘main’ package and a ‘main’ function. On my machine the following tiny program takes only 0.04 seconds to compile. Let’s create a new file and try it out:

```go
//// Put this in a new file 'crawl.go'
package main     // This is technically a perfectly
func main() {}    // valid Go program, even if a bit boring
```

Now you’re a Go programmer. Hooray! Let’s make it just slightly more interesting by turning this into a Hello World program.

```go
//// file: crawl.go
package main    // package will always be 'main' for our app.
import (        // the 'import' section is where you specify all
  "fmt"         // dependencies and 'fmt' is the package used for
)               // printing to the screen.

func main() {                   // The 'main' function is always the one that starts
  fmt.Println("I'm a gopher!")  // your program
}
```

And now let’s run it:

```bash
go run crawl.go  # run this in your terminal in whatever directory you created the file.
```

You could have executed `go build crawl.go` instead of `go run crawl.go` and it would have just compiled the file for you. The “run” command both compiles and executes it so you’ll find it turns Go into a usable scripting language (indeed, it’s faster than a lot of Ruby or Python projects).

## What’s a web crawler?

A web crawler is the portion of a search engine that scans web pages looking for links and then follows them. It would normally store the data it finds into some database where it can be useful but our version is just going to print the URLs to the screen and move along.

While not quite enterprise grade this’ll let us play with all the same concepts and see some really satisfying output as our little script wanders the web.

## Step 1. Starting from a specific page

You’ve got to start crawling from somewhere and in our program we’ll let the person who executes the crawler specify what starting page to use. This involves reading a command line argument which, in most programming languages, will be stored in a variable named something like `ARGV` and Go is no exception.

```go
//// file: crawl.go
package main

import (
  "fmt"
  "flag"        // 'flag' helps you parse command line arguments
  "os"          // 'os' gives you access to system calls
)

func main() {
  flag.Parse()         // This stuff with 'flag' converts the command line
  args := flag.Args()  // arguments to a new variable named 'args'
                       // The ':=' form means "this is a brand new variable" and
                       // a '=' here would throw an error.
                       // At this point 'args' will be either an empty list
                       // (if no command line arguments were provided) or it'll
                       // contain some string values.
  if len(args) < 1 {
    fmt.Println("Please specify start page")  // if a starting page wasn't provided as an argument
    os.Exit(1)                                // show a message and exit.
  }                                           // Note that 'main' doesn't return anything.
}
```

Now run this file by typing `go run crawl.go` and see that it yells at you because you didn’t specify a starting web page. Then try running it with an argument provided (`go run crawl.go http://news.google.com`) and it won’t show that message anymore.

## Step 2. Retrieving a page from the internet

The next thing you need is to download the page your starting URL represents so you can scan it for links. In Go there is a great http package right in the standard library. You can use the primitives Go gives you to turn your URL string into a string representing the page body.

First I’ll show you what this looks like in isolation, then we can incorporate it into our crawler. Put the following in retrieve.go:

```go
//// file: retrieve.go
package main    // Note: this is a new temporary file, not our crawl.go

import (
  "fmt"
  "net/http"    // this is the 'http' package we'll be using to retrieve a page
  "io/ioutil"   // we'll only use 'ioutil' to maek reading and printing
)               // the html page a little easier in this example.

func main() {
  resp, err := http.Get("http://6brand.com.com")  // See how we assign two variables at once here?
                                                  // That destructuring is really common
                                                  // in Go. The way you handle errors in
                                                  // Go is to expect that functions you
                                                  // call will return two things and the
                                                  // second one will be an error. If the
                                                  // error is nil then you can continue
                                                  // but if it's not you need to handle it.
  fmt.Println("http transport error is:", err)

  body, err := ioutil.ReadAll(resp.Body)  // resp.Body isn't a string, it's more like a reference
                                          // to a stream of data. So we use the 'ioutil'
                                          // package to read it into memory for us.
  fmt.Println("read error is:", err)

  fmt.Println(string(body))   // We cast the html body to a string because
}                             // Go hands it to us as a byte array
```

And run it with `go run retrieve.go`. You should see the body of [6brand.com](http://6brand.com/) printed to your screen. And if you scroll up to the top you’ll see that there were no errors (literally, err was nil) in either the transporting or reading of your http call. Yay, go you.

Let’s copy the new pieces of this code into our `crawl.go`:

```go
//// file: crawl.go
package main

import (
  "flag"          // 'flag', 'fmt' and 'os' we'll keep around
  "fmt"
  "net/http"      // 'http' will retrieve pages for us
  "io/ioutil"     // 'ioutil' will help us print pages to the screen
  "os"
)

func main() {
  flag.Parse()

  args := flag.Args()
  fmt.Println(args)
  if len(args) < 1 {
    fmt.Println("Please specify start page")
    os.Exit(1)
  }
  retrieve(args[0])  // The reason we can call 'retrieve' is because
                     // it's defined in the same package as the calling function.
}

func retrieve(uri string) {  // This func(tion) takes a parameter and the
                             // format for a function parameter definition is
                             // to say what the name of the parameter is and then
                             // the type.
                             // So here we're expecting to be given a
                             // string that we'll refer to as 'uri'
  resp, err := http.Get(uri)
  if err != nil {            // This is the way error handling typically works in Go.
    return                   // It's a bit verbose but it works.
  }
  defer resp.Body.Close()  // Important: we need to close the resource we opened
                           // (the TCP connection to some web server and our reference
                           // to the stream of data it sends us).
                           // `defer` delays an operation until the function ends.
                           // It's basically the same as if you'd moved the code
                           // you're deferring to the very last line of the func.

  body, _ := ioutil.ReadAll(resp.Body)  // I'm assigning the err to _ 'cause
                                        // I don't care about it but Go will whine
  fmt.Println(string(body))             // if I name it and don't use it
}
```

What we’ve got now is an excellent start to a web crawler. It’s able to boot, parse the URL you’ve given it, open a connection to the right remote host, and retrieve the html content.

## Step 3. Parsing hyperlinks from HTML

If you have a page of HTML you may want to use a regular expression to extract the links. Don’t. Like, [really don’t](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454). Regular expressions are not a good tool for that. The best way is, sadly, to walk through the tree structure of the page finding anchor tags and extracting `href` attributes from them. In most languages this is no fun but in Go’s standard library it’s extra not fun (though not nearly as painful as Java) and I won’t subject you to it here. I’ve encapsulated the act of pulling links from a large HTML string in [this project](https://github.com/jackdanger/collectlinks) and you’re welcome to check out the code if you’re interested.

Now let’s modify our code to extract links from whatever page is provided and print those links to the screen:

```go
//// file: crawl.go
package main

import (
  "flag"
  "fmt"
  "github.com/jackdanger/collectlinks"  // This is the little library I made for
  "net/http"                            // parsing links. Go natively allows sourcing
  "os"                                  // Github projects as dependencies. They'll be
)                                       // downloaded to $GOPATH/src/github.com/... on your
                                        // filesystem but you don't have to worry about that.
func main() {
  flag.Parse()

  args := flag.Args()
  fmt.Println(args)
  if len(args) < 1 {
    fmt.Println("Please specify start page")
    os.Exit(1)
  }

  resp, err := http.Get(args[0])
  if err != nil {
    return
  }
  defer resp.Body.Close()

  links := collectlinks.All(resp.Body)  // Here we use the collectlinks package

  for _, link := range(links) {  // 'for' + 'range' in Go is like .each in Ruby or
    fmt.Println(link)            // an iterator in many other languages.
  }                              // When we call range() on a list each iteration of the
}                                // contents will set two variables: the index and the value.
                                 // Here we don't care about the index so we set it to '_'
                                 // because if we write 'for index, link := range(links)'
                                 // Go would point out that we left 'index' unused.
```

If you run this against a simple website this’ll work fine:

```bash
go run crawl.go http://6brand.com
```

But if you try to run it against an https-secured site it may error out because it can’t validate the SSL cert. We don’t care about security in this toy app so let’s disable the SSL verification.

```go
//// file: crawl.go
package main

import (
  "crypto/tls"   // we'll import this package to get access to some
  "flag"         // low-level transport customizations
  "fmt"
  "github.com/jackdanger/collectlinks"
  "net/http"
  "os"
)

func main() {
  flag.Parse()

  args := flag.Args()
  fmt.Println(args)
  if len(args) < 1 {
    fmt.Println("Please specify start page")
    os.Exit(1)
  }

  tlsConfig := &tls.Config{                 // The &thing{a: b} syntax is equivalent to
                 InsecureSkipVerify: true,  // new(thing(a: b)) in other languages.
               }                            // It gives you a new 'thing' object (in this
                                            // case a new 'tls.Config' object) and sets the
                                            // 'a' attribute to a value of 'b'.

  transport := &http.Transport{    // And we take that tlsConfig object we instantiated
    TLSClientConfig: tlsConfig,    // and use it as the value for another new object's
  }                                // 'TLSClientConfig' attribute.

  client := http.Client{Transport: transport}  // Go typicaly gives you sane defaults (like 'http.Get')
                                               // and also provides a way to override them.

  resp, err := client.Get(args[0])  // this line is basically the same as before, only
  if err != nil {                   // we're calling 'Get' on a customized client rather
    return                          // than the 'http' package directly.
  }
  defer resp.Body.Close()

  links := collectlinks.All(resp.Body)

  for _, link := range(links) {
    fmt.Println(link)
  }
}
```

## Step 4. Concurrency

I’ve asked programming questions that required work similar to what we’re doing here in programming interviews and the step that candidates need the most help with is building some kind of queue. If you were to crawl the internet without queueing up the links you found you’d just visit the top link of every page and rapidly, in a depth-first search across the whole web, exhaust your resources without ever visiting the second link on the first page. To avoid that we need to keep some kind of queue where we put links we find in the back of it and we visit pages that we pull off the front of the queue.

In C# we’d using a `ConsumingQueue`, in Ruby we’d probably require the stdlib’s `Queue`, and in Java we’d use a `ConcurrentLinkedQueue` or something. Go gives us a great alternative: a channel. It’s kinda like a lightweight thread that abstracts away some concurrency primitives for you and functions much like a queue.

We’ll create a channel when we start the program and we’ll put our starting URL into it. Then we’ll begin to read URLs from the channel and whenever we find new URLs we’ll write them to the channel, effectively putting them into the back of our queue.

The queue will grow continuously over time because we’re putting things in faster than we take them out but we just don’t care.

```go
//// file: crawl.go
package main

import (
  "crypto/tls"
  "flag"
  "fmt"
  "github.com/jackdanger/collectlinks"
  "net/http"
  "os"
)

func main() {
  flag.Parse()

  args := flag.Args()
  fmt.Println(args)
  if len(args) < 1 {
    fmt.Println("Please specify start page")
    os.Exit(1)
  }

  queue := make(chan string)         // This gives you a new channel that
                                     // receives and delivers strings. There's nothing
                                     // more you need to do to set it up – it's
                                     // all ready to have data fed into it.

  go func() {            // saying "go someFunction()" means
                         // "run someFunction() asynchronously"
    queue <- args[0]     // This means "put args[0] into the channel".
  }()

  for uri := range queue {     // 'range' is such an effective iterator keyword
                               // that if you ask for the range of a channel it'll
                               // do an efficient, continuous blocking read of
                               // all the channel contents.

    enqueue(uri, queue)  // we pass each URL we find off to be read & enqueued
  }
}

func enqueue(uri string, queue chan string) {
  fmt.Println("fetching", uri)
  tlsConfig := &tls.Config{
    InsecureSkipVerify: true,
  }
  transport := &http.Transport{
    TLSClientConfig: tlsConfig,
  }
  client := http.Client{Transport: transport}
  resp, err := client.Get(uri)
  if err != nil {
    return
  }
  defer resp.Body.Close()

  links := collectlinks.All(resp.Body)

  for _, link := range links {
    go func() { queue <- link }() // We asynchronously enqueue what we've found
  }
}
```

The flow now is that `main` has a `for` loop reading from the channel called `queue` and `enqueue` does the HTTP retrieval and link parsing, putting the discovered links into the same queue used by `main`.

If you try running our code so far it’ll work but you’ll immediately discover two things: The World Wide Web is a messy place full of invalid links and most pages link to themselves.

So let’s add some sanity to our code.

## Step 5. Data sanitization

To properly explore the web let’s turn all of the relative links we find into absolute links.

```go
package main

import (
  "crypto/tls"
  "flag"
  "fmt"
  "github.com/jackdanger/collectlinks"
  "net/http"
  "net/url"  // We're going to use the standard library
  "os"       // to fix our URLs
)

func main() {
  flag.Parse()

  args := flag.Args()
  fmt.Println(args)
  if len(args) < 1 {
    fmt.Println("Please specify start page")
    os.Exit(1)
  }

  queue := make(chan string)

  go func() { queue <- args[0] }()

  for uri := range queue {
    enqueue(uri, queue)
  }
}

func enqueue(uri string, queue chan string) {
  fmt.Println("fetching", uri)
  transport := &http.Transport{
    TLSClientConfig: &tls.Config{
      InsecureSkipVerify: true,
    },
  }
  client := http.Client{Transport: transport}
  resp, err := client.Get(uri)
  if err != nil {
    return
  }
  defer resp.Body.Close()

  links := collectlinks.All(resp.Body)

  for _, link := range links {
    absolute := fixUrl(link, uri)      // Don't enqueue the raw thing we find,
                                       // fix it first.
    if uri != "" {                     // We'll set invalid URLs to blank strings
                                       // so let's never send those to the channel.
      go func() { queue <- absolute }()
    }
  }
}

func fixUrl(href, base string) (string) {  // given a relative link and the page on
  uri, err := url.Parse(href)              // which it's found we can parse them
  if err != nil {                          // both and use the url package's
    return ""                              // ResolveReference function to figure
  }                                        // out where the link really points.
  baseUrl, err := url.Parse(base)          // If it's not a relative link this
  if err != nil {                          // is a no-op.
    return ""
  }
  uri = baseUrl.ResolveReference(uri)
  return uri.String()                      // We work with parsed url objects in this
}                                          // func but we return a plain string.
```

Now you’re cookin’. This program will now pretty reliably walk around the web downloading and parsing pages. However, there’s still one thing we lack.

## Step 6. Avoiding Loops

Nothing so far prevents us from visiting a page that has one link pointing to itself and just looping on that single page forever. That’s dumb, let’s not fetch any page more than once.

The right data structure for keeping track of the presence or absense of things is a set. Go, like JavaScript, doesn’t have a native way of doing sets so we need to use a map (a.k.a a hash or hashmap or a dictionary) with urls as keys to keep track of which pages we’ve visited.

```go
package main

import (
  "crypto/tls"
  "flag"
  "fmt"
  "github.com/jackdanger/collectlinks"
  "net/http"
  "net/url"
  "os"
)

                                     // Putting a variable outside a function is Go's
var visited = make(map[string]bool)  // version of a global variable.
                                     // This is a map of string -> bool, so
                                     // visited["hi"] works but visited[6] doesn't.
                                     // Setting a value in a map is a simple as:
                                     //   visited["google.com"] = true
                                     // and reading is equally so:
                                     //   visited["google.com"]
func main() {
  flag.Parse()

  args := flag.Args()
  fmt.Println(args)
  if len(args) < 1 {
    fmt.Println("Please specify start page")
    os.Exit(1)
  }

  queue := make(chan string)

  go func() { queue <- args[0] }()

  for uri := range queue {
    enqueue(uri, queue)
  }
}

func enqueue(uri string, queue chan string) {
  fmt.Println("fetching", uri)
  visited[uri] = true                        // Record that we're going to visit this page
  transport := &http.Transport{
    TLSClientConfig: &tls.Config{
      InsecureSkipVerify: true,
    },
  }
  client := http.Client{Transport: transport}
  resp, err := client.Get(uri)
  if err != nil {
    return
  }
  defer resp.Body.Close()

  links := collectlinks.All(resp.Body)

  for _, link := range links {
    absolute := fixUrl(link, uri)
    if uri != "" {
      if !visited[absolute] {          // Don't enqueue a page twice!
        go func() { queue <- absolute }()
      }
    }
  }
}

func fixUrl(href, base string) (string) {
  uri, err := url.Parse(href)
  if err != nil {
    return ""
  }
  baseUrl, err := url.Parse(base)
  if err != nil {
    return ""
  }
  uri = baseUrl.ResolveReference(uri)
  return uri.String()
}
```

And now you can start at any html page you like and slowly explore the entire world wide web.

```bash
go run crawl.go http://6brand.com
```

Full source code is available [on GitHub](https://github.com/JackDanger/gocrawler) as well.
