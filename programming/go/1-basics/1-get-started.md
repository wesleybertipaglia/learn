# Get Started

## Install GO

```bash
wget https://go.dev/dl/go[version].linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go[version].linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```

## Write Your First Program

1. Write your code

```go
package main
import ("fmt")

func main() {
  fmt.Println("Hello World!")
}
```

2. Compile your code

```go
go build -o hello
```

3. Running your program

```go
./hello
```
