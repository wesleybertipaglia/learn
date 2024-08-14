# Arrays

## Declaring

```go
var arr1 = [3]int{1, 2, 3} // defined size
arr2 := [3]string{"Volvo", "BMW", "Ford"} // defined size

var arr3 = [...]int{1, 2, 3} // inferred size
arr4 := [...]int{4, 5, 6, 7, 8} // inferred size
```

## Initializing

```go
arr1 := [5]int{} // not initialized
arr2 := [5]int{1, 2} // partially initialized
arr3 := [5]int{1, 2, 3, 4, 5} // fully initialized
arr4 := [5]int{1:10, 2:40} // partially initialized, with specific elements
```

## Get the Length 

```go
arr1 := [4]string{"Volvo", "BMW", "Ford", "Mazda"}
len(arr1)
```

## Accessing Elements

```go
prices := [3]int{10, 20, 30}
prices[0]
```

## Changing Elements

```go
prices := [3]int{10, 20, 30}
prices[0] = 25
```
