# Loops

## For Loop

```go
for i:=0; i < 5; i++ {
    fmt.Println(i)
}
```

## For Range

```go
fruits := [3]string{"apple", "orange", "banana"}

for index, val := range fruits {
    fmt.Printf("%v\t%v\n", index, val)
}
```

## Loop Control Statements

### Break Statement

With the `break` statement we can stop the loop before it has looped through all the items.

```go
for i:=0; i < 5; i++ {
    if i == 3 {
        break
    }
    
    fmt.Println(i)
}
```

### Continue Statement

With the `continue` statement we can stop the current iteration of the loop, and continue with the next.

```go
for i:=0; i < 5; i++ {
    if i == 3 {
        continue
    }
    
    fmt.Println(i)
}
```
