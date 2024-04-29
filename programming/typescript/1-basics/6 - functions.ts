/* Functions */

// typed functions
function addNumber(x: number, y: number): number {
  return x + y
}

function sayHello(name: string): string {
  return `Hello, ${name}`
}

// void functions
function display(value: string): void {
  console.log(`String Value: ${value}`)
}

// async functions
function fetchData(callback: (data: string) => void): void {
  // Simulating asynchronous data retrieval
  setTimeout(() => {
    const data: string = 'This is the data'
    callback(data)
  }, 1000)
}

fetchData((result) => {
  console.log(result) // This is the data
})
