function main() {
  // objects
  const person = {
    firstName: 'John',
    lastName: 'Doe',
    age: 30,
  }
  const { firstName, lastName, age } = person

  // arrays
  const colors = ['red', 'green', 'blue']
  const [firstColor, secondColor, thirdColor] = colors
  const [red, , blue] = colors
  const [redColor, ...restColors] = colors

  // strings
  const meal = 'Chicken Tacos'
  const [flavor, food] = meal.split(' ')
}

main()
