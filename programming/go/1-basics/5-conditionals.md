# Conditionals

## If

```go
time := 22

if time < 10 {
    fmt.Println("Good morning.")
} else if time < 20 {
    fmt.Println("Good day.")
} else {
    fmt.Println("Good evening.")
}
```

## Switch

```go
day := 4

switch day {
    case 1:
        fmt.Println("Monday")
    case 2:
        fmt.Println("Tuesday")
    case 3:
        fmt.Println("Wednesday")
    case 4:
        fmt.Println("Thursday")
    case 5:
        fmt.Println("Friday")
    case 6:
        fmt.Println("Saturday")
    case 7:
        fmt.Println("Sunday")
    default:
        fmt.Println("Not a weekday")
}
```
