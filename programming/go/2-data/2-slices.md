# Slices

## Declaring

```go
myslice1 := []int{1, 2, 3}
myslice2 := []string{"Go", "Slices", "Are", "Powerful"}
```

## Create a Slice from an Array

```go
arr1 := [6]int{10, 11, 12, 13, 14,15}
myslice := arr1[2:4]
```

## Get the Length and Capacity

```go
myslice1 := [4]int{1, 2, 3}
len(myslice1) // 3
cap(myslice1) // 4
```

## Accessing Elements

```go
arr1 := [6]int{10, 11, 12, 13, 14,15}
arr1[2]
```

## Changing Elements

```go
arr1 := [6]int{10, 11, 12, 13, 14,15}
arr1[2] = 20
```

## Appending Elements

```go
myslice1 := []int{1, 2, 3}
myslice2 := []int{4, 5, 6}  

myslice1 = append(myslice1, 20, 21) // append elements
myslice3 := append(myslice1, myslice2...) // append slices
```