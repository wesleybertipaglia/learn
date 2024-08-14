# Interfaces

## Declaring

```go
type Animal interface {
    Speak() string
}
```

## Implementing 

```go
type Dog struct{}

func (d Dog) Speak() string {
    return "Woof!"
}

var a Animal = Dog{}
```
