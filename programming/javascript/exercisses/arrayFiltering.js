function main() {
  const numbers = [1, 2, 3, 4, 5]

  // return array
  const evenNumbers = numbers.filter((num) => num % 2 === 0)

  // return the element
  const firstNumberGreaterThan25 = numbers.find((num) => num > 25)

  // return the index
  const index = numbers.findIndex((num) => num > 25)

  // return a boolean
  const hasEvenNumber = numbers.some((num) => num % 2 === 0)
  const allEvenNumbers = numbers.every((num) => num % 2 === 0)
}

main()
