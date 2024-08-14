# Syntax

## Comments

```go
// single line comment

/* 
    Multiple line comment
*/
```

## Variables

```go
var mystring1 string = "John" // string
var mystring2 = "Jane" // inferred -> string
myint := 2 // inferred -> int
```

## Functions

```go
func myFunction() {
}

myFunction() // call the function
```

### Function Parameters

```go
func myFunction(x int, y int) {
}
```

### Function Return

```go
func myFunction(x int, y int) int {
    return x + y
}
```

## Output 

```go
import ("fmt")

fmt.Print("Hello, World")
fmt.Println("Hello,", "World") // a new line is a added between arguments and a /n is added at the end
fmt.Printf("i has value: %v and type: %T\n", 10, 10) // formated print, %v print the value and %T print the type
```

## Input

```go
import ("fmt")

var x, y int

fmt.Print("Type a number: ")
fmt.Scan(&x)

fmt.Print("Type two numbers: ")
fmt.Scanln(&x, &y) // it stops scanning for inputs at a newline

fmt.Print("Type two numbers: ")
fmt.Scanf("%v %v",&x, &y) // receives the inputs and stores them based on the determined formats for its arguments
```
