---
title: Programming languages are similar
tags: other
date: 2020-06-03
---

> 转载：[GitHub - jiyinyiyong/swift-is-like-go: Comparing Swift syntax with Go's](https://github.com/jiyinyiyong/swift-is-like-go)

# BASICS

## Hello World

### Swift

```swift
print("Hello, world!")
```

### Go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
```

### C#

```c#
Console.WriteLine("Hello, world!");
```

### SCALA

```scala
println("Hello, world!")
```

## Variables And Constants

### Swift

```swift
var myVariable = 42
myVariable = 50
let myConstant = 42

let explicitDouble: Double = 70
```

### GO

```go
var myVariable = 42
myVariable = 50
const myConstant = 42

const explicitDouble float64 = 70
```

### C#

```c#
var myVariable = 42;
myVariable = 50;
const int myConstant = 42;

double explicitDouble = 70d;
```

### SCALA

```scala
var myVariable = 42
myVariable = 50
val myConstant = 42

val explicitDouble: Double = 70
```

## Type Coercion

### Swift

```swift
let label = "The width is "
let width = 94
let widthLabel = label + String(width)
```

### Go

```go
const label = "The width is "
const width = 94
var widthLabel = label + strconv.Itoa(width)
```

### C#

```c#
var label = "The width is ";
var width = 94;
var widthLabel = label + width;
```

### SCALA

```scala
val label = "The width is "
val width = 94
val widthLabel = label + width
```

## String Interpolation

### Swift

```swift
let apples = 3
let oranges = 5
let fruitSummary = "I have \(apples + oranges) " +
                   "pieces of fruit."
```

### GO

```go
const apples = 3
const oranges = 5
fruitSummary := fmt.Sprintf("I have %d pieces of fruit.", apples + oranges)
```

### C#

```c#
var apples = 3;
var oranges = 5;
var fruitSummary = $"I have {apples + oranges} " +
                   "pieces of fruit.";
```

### SCALA

```scala
val apples = 3
val oranges = 5
val fruitSummary = s"I have ${apples + oranges} " +
                   " pieces of fruit."
```

## Range Operator

### Swift

```swift
let names = ["Anna", "Alex", "Brian", "Jack"]
let count = names.count
for i in 0..count {
    print("Person \(i + 1) is called \(names[i])")
}
// Person 1 is called Anna
// Person 2 is called Alex
// Person 3 is called Brian
// Person 4 is called Jack
```

### GO

```go
names := [4]string{"Anna", "Alex", "Brian", "Jack"}
for i, value := range(names) {
    fmt.Printf("Person %v is called %v\n", (i + 1), value)
}
// Person 1 is called Anna
// Person 2 is called Alex
// Person 3 is called Brian
// Person 4 is called Jack
```

### C#

```c#
var names = new[]{"Anna", "Alex", "Brian", "Jack"};
var count = names.Count();
for (var i; i< count; i++) {
    Console.WriteLine($"Person {i + 1} is called {names[i]}");
}
// Person 1 is called Anna
// Person 2 is called Alex
// Person 3 is called Brian
// Person 4 is called Jack
```

### SCALA

```scala
val names = Array("Anna", "Alex", "Brian", "Jack")
val count = names.length
for (i <- 0 until count) {
    println(s"Person ${i + 1} is called ${names(i)}")
}
// Person 1 is called Anna
// Person 2 is called Alex
// Person 3 is called Brian
// Person 4 is called Jack
```

## Inclusive Range Operator

### Swift

```swift
for index in 1...5 {
    print("\(index) times 5 is \(index * 5)")
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

### GO

```go
for i := 1; i <= 5; i++ {
    fmt.Printf("%d times 5 is %d", i, i*5)
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

### C#

```c#
foreach (var index in Enumerable.Range(1,5)) {
    Console.WriteLine($"{index} times 5 is {index * 5}");
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

### SCALA

```scala
for (index <- 1 to 5) {
    println(s"$index times 5 is ${index * 5}")
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

# COLLECTIONS

## Arrays

### Swift

```swift
var shoppingList = ["catfish", "water",
    "tulips", "blue paint"]
shoppingList[1] = "bottle of water"
```

### GO

```go
var shoppingList = []string{"catfish", "water",
    "tulips", "blue paint"}
shoppingList[1] = "bottle of water"
```

### C#

```c#
val shoppingList = new[] { "catfish", "water",
    "tulips", "blue paint" };
shoppingList[1] = "bottle of water";
```

### SCALA

```scala
var shoppingList = Array("catfish",
    "water", "tulips", "blue paint")
shoppingList(1) = "bottle of water"
```

## Maps

### Swift

```swift
var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
]
occupations["Jayne"] = "Public Relations"
```

### GO

```go
var occupations = map[string]string{
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
}
occupations["Jayne"] = "Public Relations"
```

### C#

```c#
var occupations = new Dictionary {
            { "Malcolm", "Captain" },
            { "Kaylee", "Mechanic" }
        };
occupations["Jayne"] = "Public Relations";
```

### SCALA

```scala
var occupations = scala.collection.mutable.Map(
    "Malcolm" -> "Captain",
    "Kaylee" -> "Mechanic"
)
occupations("Jayne") = "Public Relations"
```

## Empty Collections

### Swift

```swift
let emptyArray = [String]()
let emptyDictionary = [String: Float]()
let emptyArrayNoType = []
```

### Go

```go
var (
    emptyArray []string
    emptyDictionary = make(map[interface{}]interface{})
    emptyArrayNoType []interface{}
)
```

### C#

```c#
var emptyArray = new string[0];
var emptyMap = new Dictionary<String, float>();
```

### SCALA

```scala
val emptyArray = Array[String]()
val emptyDictionary = Map[String, Float]()
val emptyArrayNoType = Array()
```

# FUNCTIONS

## Functions

### Swift

```swift
func greet(name: String, day: String) -> String {
    return "Hello \(name), today is \(day)."
}
greet("Bob", "Tuesday")
```

### Go

```go
func greet(name, day string) string {
    return fmt.Sprintf("Hello %v, today is %v.", name, day)
}

func main() {
    greet("Bob", "Tuesday")
}
```

### C#

```c#
string greet(string name, string day) {
    return $"Hello {name}, today is {day}.";
}
greet("Bob", "Tuesday");
```

### SCALA

```scala
def greet(name: String, day: String): String = {
    return s"Hello $name, today is $day."
}
greet("Bob", "Tuesday")

// IDIOMATIC
def greet(name: String, day: String): String =
    s"Hello $name, today is $day."

greet("Bob", "Tuesday")
```

## Tuple Return

### Swift

```swift
func getGasPrices() -> (Double, Double, Double) {
    return (3.59, 3.69, 3.79)
}
```

### Go

```go
func getGasPrices() (float64, float64, float64) {
    return 3.59, 3.69, 3.79
}
```

### C#

```c#
(double, double, double) GasPrices(long id)
{
    return (3.59, 3.69, 3.79);
}
```

### SCALA

```scala
def getGasPrices(): (Double, Double, Double) = {
    return (3.59, 3.69, 3.79)
}

// IDIOMATIC
def getGasPrices = (3.59, 3.69, 3.79)
```

## Variable Number Of Arguments

### Swift

```swift
func sumOf(numbers: Int...) -> Int {
    var sum = 0
    for number in numbers {
        sum += number
    }
    return sum
}
sumOf(42, 597, 12)
```

### Go

```go
func sumOf(numbers ...int) int {
    var sum = 0
    for _, number := range(numbers) {
        sum += number
    }
    return sum
}

func main() {
    sumOf(42, 597, 12)
    sumOf([]int{42, 597, 12}...)
}
```

### C#

```c#
int sumOf(params int[] args){
    var sum = 0;
    for (number in numbers) {
        sum += number;
    }
    return sum;
}
sumOf(42, 597, 12);

//can also be written
int sumOf(params int[] args)
    => args.Sum();
sumOf(42, 597, 12);
```

### SCALA

```scala
def sumOf(numbers: Int*): Int = {
    var sum = 0
    for (number <- numbers) {
        sum += number
    }
    return sum
}
sumOf(42, 597, 12)

// IDIOMATIC
Array(42, 597, 12).sum
```

## Function Type

### Swift

```swift
func makeIncrementer() -> (Int -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}
var increment = makeIncrementer()
increment(7)
```

### Go

```go
func makeIncrementer() func(int) int {
    return func (number int) int {
        return 1 + number
    }
}

func main() {
    increment := makeIncrementer()
    increment(7)
}
```

### C#

```c#
Func makeIncrementer()
    => (int number) => { return 1 + number; };

var increment = makeIncrementer();
increment(7);
```

### SCALA

```scala
def makeIncrementer(): Int => Int = {
    def addOne(number: Int): Int = {
        return 1 + number
    }
    return addOne
}
var increment = makeIncrementer()
increment(7)


// IDIOMATIC
def makeIncrementer: Int => Int =
    (number: Int) => 1 + number

var increment = makeIncrementer
increment(7)
```

## Map

### Swift

```swift
var numbers = [20, 19, 7, 12]
numbers.map({ number in 3 * number })
```

### Go

```go
mapFunc := func(slice interface{}, fn func(a interface{}) interface{}) interface{} {
    val := reflect.ValueOf(slice)
    out := reflect.MakeSlice(reflect.TypeOf(slice), val.Len(), val.Cap())
    for i := 0; i < val.Len(); i++ {
        out.Index(i).Set(
            reflect.ValueOf(fn(val.Index(i).Interface())),
        )
    }
    return out.Interface()
}
a := mapFunc([]int{1, 2, 3, 4}, func(val interface{}) interface{} {
    return val.(int) * 3
})
```

### C#

```c#
var numbers = new[]{20, 19, 7, 12};
numbers.Select(i => i*3).ToArray();
```

### SCALA

```scala
var numbers = Array(20, 19, 7, 12)
numbers.map( number => 3 * number )
```

## Sort

### Swift

```swift
sort([1, 5, 3, 12, 2]) { $0 > $1 }
```

### Go

```go
sort.Sort(sort.Reverse(sort.IntSlice([]int{1, 5, 3, 12, 2})))
```

### C#

```c#
new[]{1, 5, 3, 12, 2}
    .OrderBy(i => i);
```

### SCALA

```scala
Array(1, 5, 3, 12, 2).sortWith(_ > _)
```

## Named Arguments

### Swift

```swift
def area(width: Int, height: Int) -> Int {
    return width * height
}

area(width: 10, height: 10)
```

### Go

```

```

### C#

```c#
int Area(int width, int height) { return width * height; };
Area(width: 2, height: 3);

// This is also possible with named arguments
Area(2, height: 2);
Area(height: 3, width: 2);
```

### SCALA

```scala
def area(width: Int, height: Int): Int = {
    return width * height
}

area(width = 10, height = 10)
```

# CLASSES

## Declaration

### Swift

```swift
class Shape {
    var numberOfSides = 0
    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
}
```

### Go

```go
type Shape struct {
    numberOfSides int
}
func (p *Shape) simpleDescription() string {
    return fmt.Sprintf("A shape with %d sides.", p.numberOfSides)
}
```

### C#

```c#
class Shape {
    var numberOfSides = 0;
    string SimpleDescription()
        => $"A shape with {numberOfSides} sides.";
}
```

### SCALA

```scala
class Shape {
    var numberOfSides = 0
    def simpleDescription(): String = {
        return s"A shape with $numberOfSides sides."
    }
}


// IDIOMATIC
class Shape (var numberOfSides: Int = 0) {
    def simpleDescription =
        s"A shape with $numberOfSides sides."
}
```

## Usage

### Swift

```swift
var shape = Shape()
shape.numberOfSides = 7
var shapeDescription = shape.simpleDescription()
```

### Go

```go
var shape = new(Shape)
shape.numberOfSides = 7
var shapeDescription = shape.simpleDescription()
```

### C#

```c#
var shape = new Shape();
shape.numberOfSides = 7;
var shapeDescription = shape.SimpleDescription();
```

### SCALA

```scala
var shape = new Shape()
shape.numberOfSides = 7
var shapeDescription = shape.simpleDescription()
```

## Subclass

### Swift

```swift
class NamedShape {
    var numberOfSides: Int = 0
    var name: String

    init(name: String) {
        self.name = name
    }

    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
}

class Square: NamedShape {
    var sideLength: Double

    init(sideLength: Double, name: String) {
        self.sideLength = sideLength
        super.init(name: name)
        numberOfSides = 4
    }

    func area() -> Double {
        return sideLength * sideLength
    }

    override func simpleDescription() -> String {
        return "A square with sides of length
                \(sideLength)."
    }
}

let test = Square(sideLength: 5.2, name: "square")
test.area()
test.simpleDescription()
```

### Go

```go
type NamedShape struct {
    numberOfSides int
    name string
}
func NewNamedShape(name string) *NamedShape {
    return &NamedShape{
        name: name,
    }
}
func (p *NamedShape) SimpleDescription() string {
    return fmt.Sprintf("A shape with %d sides.", p.numberOfSides)
}

type Square struct {
    *NamedShape
    sideLength float64
}
func NewSquare(sideLength float64, name string) *Square {
    return &Square{
        NamedShape: NewNamedShape(name),
        sideLength: sideLength,
    }
}
func (p *Square) Area() float64 {
    return p.sideLength * p.sideLength
}
func (p *Square) SimpleDescription() string {
    return fmt.Sprintf("A square with sides of length %d.", p.sideLength)
}

func main() {
    a := NewSquare(5.2, "square")
    a.Area()
    a.SimpleDescription()
}
```

### C#

```c#
class NamedShape(string name) {
    var numberOfSides = 0;
    string SimpleDescription()
        => $"A shape with {numberOfSides} sides.";
}

class Square(decimal sideLength, string name) :
        NamedShape(name) {

    public Square() {
        numberOfSides = 4;
    }

    int Area()
        => sideLength*sideLength;

    override string SimpleDescription() =>
        "A square with sides of length $sideLength.";
}

val test = new Square(5.2, "square");
test.Area();
test.SimpleDescription();
```

### SCALA

```scala
class NamedShape(var name: String,
                 var numberOfSides: Int = 0) {
    def simpleDescription =
        s"A shape with $numberOfSides sides."
}

class Square(var sideLength: Double, name: String)
    extends NamedShape(name, numberOfSides = 4) {
    def area = sideLength * sideLength
    override def simpleDescription =
        s"A square with sides of length $sideLength."
}

val test = new Square(5.2, "my test square")
test.area
test.simpleDescription
```

## Checking Type

### Swift

```swift
var movieCount = 0
var songCount = 0

for item in library {
    if item is Movie {
        ++movieCount
    } else if item is Song {
        ++songCount
    }
}
```

### Go

```go
var movieCount = 0
var songCount = 0

for _, item := range(library) {
    if _, ok := item.(Movie); ok {
        movieCount++
    } else if _, ok := item.(Song); ok {
        songCount++
    }
}
```

### C#

```c#
var movieCount = 0;
var songCount = 0;

foreach (var item in library) {
    if (item.GetType() == typeof(Movie)) {
        ++movieCount;
    } else if (item.GetType() == typeof(Song)) {
        ++songCount;
    }
}
```

### SCALA

```scala
var movieCount = 0
var songCount = 0

for (item <- library) {
    if (item.isInstanceOf[Movie]) {
        movieCount += 1
    } else if (item.isInstanceOf[Song]) {
        songCount += 1
    }
}
```

## Pattern Matching

### Swift

```swift
let nb = 42
switch nb {
    case 0...7, 8, 9: print("single digit")
    case 10: print("double digits")
    case 11...99: print("double digits")
    case 100...999: print("triple digits")
    default: print("four or more digits")
}
```

### C#

```c#
var nb = 42;
switch (nb)
{
    case int r when (1 <= r && r <= 9):
        Console.WriteLine("single digit");
        break;
    case 10:
        Console.WriteLine("double digits");
        break;
    case int r when (11 <= r && r <= 99):x
        Console.WriteLine("double digits");
        break;
    case int r when (100 <= r && r <= 999):
        Console.WriteLine("triple digits");
        break;
    default:
        Console.WriteLine("four or more digits");
}
```

### SCALA

```scala
var movieCount = 0
var songCount = 0

for (item <- library) {
  item match {
    case movie: Movie =>
      movieCount += 1
      println(s"Movie: '${movie.name}', dir. ${movie.director}")
    case song: Song =>
      songCount += 1
      println(s"Song: '${song.title}'")
  }
}
```

## Downcasting

### Swift

```swift
for object in someObjects {
    let movie = object as Movie
    print("Movie: '\(movie.name)', dir. \(movie.director)")
}
```

### Go

```go
for object := range someObjects {
    movie := object.(Movie)
    fmt.Printf("Movie: '%s', dir. %s", movie.name, movie.director)
}
```

### C#

```c#
for (current in someObjects) {
    if ((current as Movie) != null) {
        Console.WriteLine($"Movie: '{(current as Movie).name}'," +
        $"dir. {(current as Movie).director}")
    }
}
```

### SCALA

```scala
for (obj <- someObjects) {
    val movie = obj.asInstanceOf[Movie]
    println(s"Movie: '${movie.name}', dir. ${movie.director}")
}
```

## Protocol

### Swift

```swift
protocol Nameable {
    func name() -> String
}

func f<T: Nameable>(x: T) {
    print("Name is " + x.name())
}
```

### Go

```go
type Nameabler interface {
    func Name() string
}

func F(x Nameabler) {
    fmt.Println("Name is " + x.Name())
}
```

### C#

```c#
public interface Nameable {
    string Name();
}

void F(Nameable x) {
    Console.WriteLine("Name is " + x.Name());
}
```

### SCALA

```scala
trait Nameable {
    def name(): String
}

def f[T <: Nameable](x: T) = {
    println("Name is " + x.name())
}
```

## Extensions

### Swift

```swift
extension Double {
    var km: Double { return self * 1_000.0 }
    var m: Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}
let oneInch = 25.4.mm
print("One inch is \(oneInch) meters")
// prints "One inch is 0.0254 meters"
let threeFeet = 3.ft
print("Three feet is \(threeFeet) meters")
// prints "Three feet is 0.914399970739201 meters"
```

### Go

```go
type double float64

func (d double) km() double { return d * 1000 }
func (d double) m() double  { return d }
func (d double) cm() double { return d / 100 }
func (d double) mm() double { return d / 1000 }
func (d double) ft() double { return d / 3.28084 }

func main() {
    var oneInch = double(25.4).mm()
    fmt.Printf("One inch is %v meters\n", oneInch)
    // prints "One inch is 0.0254 meters"

    var threeFeet = double(3).ft()
    fmt.Printf("Three feet is %v meters\n", threeFeet)
    // prints "Three feet is 0.914399970739201 meters"
}
```

### C#

```c#
public static double mm(this double value)
{
    return value / 1000;
}

public static double ft(this double value)
{
    return value / 3.28084;
}

var oneInch = 25.4.mm();
Console.WriteLine($"One inch is {oneInch} meters")
// prints "One inch is 0.0254 meters"
var threeFeet = 3.0.ft();
Console.WriteLine($"Three feet is {threeFeet} meters")
// prints "Three feet is 0.914399970739201 meters"
```

### SCALA

```scala
object Extensions {
    implicit class DoubleUnit(d: Double) {
        def km: Double = { return d * 1000.0 }
        def m: Double = { return d }
        def cm: Double = { return d / 100.0 }
        def mm: Double = { return d / 1000.0 }
        def ft: Double = { return d / 3.28084 }
    }
}

import Extensions.DoubleUnit

val oneInch = 25.4.mm
println(s"One inch is $oneInch meters")
// prints "One inch is 0.0254 meters"
val threeFeet = 3.ft
println(s"Three feet is $threeFeet meters")
// prints "Three feet is 0.914399970739201 meters"


// IDIOMATIC
object Extensions {
    implicit class DoubleUnit(d: Double) {
        def km = d * 1000.0
        def m = d
        def cm = d / 100.0
        def mm = d / 1000.0
        def ft = d / 3.28084
    }
}

import Extensions.DoubleUnit

val oneInch = 25.4.mm
println(s"One inch is $oneInch meters")
// prints "One inch is 0.0254 meters"
val threeFeet = 3.ft
println(s"Three feet is $threeFeet meters")
// prints "Tree feet is 0.914399970739201 meters"
```
