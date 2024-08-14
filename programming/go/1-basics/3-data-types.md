# Data Types

## Boolean

```go
var mytrue bool = true
var myfalse bool = false
```

## Numbers

```go
var myint int = 5 // int
var myfloat float32 = 3.14 // float
```

## Text

```go
var mystring string = "Hi!"  // String
```

## Array

Stores multiple values of the same type in a single variable, with a fixed length

```go
var myarr1 = [3]datatype{0, 1, 2} // defined length
var myarr2 = [...]datatype{0, 1, 2} // inferred length

myarr3 := [3]datatype{0, 1, 2} // defined length
myarr4 := [...]datatype{0, 1, 2} // inferred length

myarr1[0] // accessing a value
len(myarr1) // return the length
```

## Slices

Stores multiple values of the same type in a single variable, with a flexible length

```go
myslice1 := []int{1, 2, 3}

var myarr = [3]datatype{0, 1, 2}
myslice2 := myarray[0:1] // a slice made from the array

myslice1[0] // accessing
myslice1[0] = 2 // modifying
myslice1 = append(myslice1, 20) // appending elements

len(myslice1) // return the length
cap(myslice1) // return the capacity
```
