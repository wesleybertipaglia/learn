function main() {
  const fruits = ['banana', 'apple', 'orange', 'grape']
  const numbers = [3, 1, 2, 10]

  // ascending
  fruits.sort()
  numbers.sort((a, b) => a - b) // for numbers

  // descending
  numbers.reverse()
}

main()
