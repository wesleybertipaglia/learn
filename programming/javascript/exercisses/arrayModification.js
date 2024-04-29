function main() {
  const numbers = [1, 2, 3]

  // adding elements
  numbers.push(4, 5) // end
  numbers.unshift(0) // start
  numbers.splice(2, 0, 3, 4) // specific index

  // combining arrays
  const newNumbers = numbers.concat(3, 4, [5, 6])
  const combinedNumbers = [...numbers, ...newNumbers]

  // removing elements
  const removedElementEnd = numbers.pop() // end
  const removedElementStart = numbers.shift() // start
  numbers.splice(2, 1) // specific index

  // replacing elements
  numbers[1] = 8 // specific index
  numbers.splice(2, 2, 6, 7) // specific index
}

main()
