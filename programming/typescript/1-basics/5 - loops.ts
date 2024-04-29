/* Loops */

// for
for (let i = 0; i < 5; i++) {
  console.log(i) // 0, 1, 2, 3, 4
}

// for of
let fruits: string[] = ['apple', 'banana', 'orange']
for (let fruit of fruits) {
  console.log(fruit) // 'apple', 'banana', 'orange'
}

// for in
let person = { name: 'John', age: 30 }
for (let key in person) {
  console.log(key, person[key]) // 'name John', 'age 30'
}

// while
let count = 0
while (count < 3) {
  console.log(count) // 0, 1, 2
  count++
}

// do...while...
let x = 0
do {
  console.log(x) // 0
  x++
} while (x < 0)
