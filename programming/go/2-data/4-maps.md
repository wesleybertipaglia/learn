# Maps

## Creating Maps

```go
var a = map[string]string{"brand": "Ford", "model": "Mustang"}
b := map[string]int{"Oslo": 1, "Bergen": 2, "Trondheim": 3}
```

## Creating Maps with make() Function

```go
var a = make(map[string]string)

a["brand"] = "Ford"
a["model"] = "Mustang"
a["year"] = "1964"
```

## Accessing Elements

```go
var a = map[string]string{"brand": "Ford", "model": "Mustang"}
a["brand"]
```

## Modifing Elements

```go
var a = make(map[string]string)
a["brand"] = "Ford"
```

## Removing Elements

```go
var a = map[string]string{"brand": "Ford", "model": "Mustang"}
delete(a,"brand")
```

## Iterate Over Maps

```go
a := map[string]int{"one": 1, "two": 2, "three": 3, "four": 4}

for k, v := range a {
    fmt.Printf("%v : %v, ", k, v)
}
```