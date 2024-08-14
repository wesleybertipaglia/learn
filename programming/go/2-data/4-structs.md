# Structs

## Declare a Struct

```go
type Person struct {
  name string
  age int
  job string
  salary int
}
```

## Creating Members

```go
var pers1 Person

pers1.name = "Hege"
pers1.age = 45
pers1.job = "Teacher"
pers1.salary = 6000
```

## Pass Struct as Function Arguments

```go
package main
import ("fmt")

type Person struct {
  name string
  age int
}

func main() {
  var pers1 Person

  pers1.name = "Hege"
  pers1.age = 45

  printPerson(pers1)
}

func printPerson(pers Person) {
  fmt.Println("Name: ", pers.name)
  fmt.Println("Age: ", pers.age)
}
```
