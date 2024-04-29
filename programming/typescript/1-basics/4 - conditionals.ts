/* Conditionals */

// if
let condition: boolean = true

if (condition) {
  // Code to be executed if the condition is true
} else {
  // Code to be executed if the condition is false
}

// else
let num: number = 10
if (num > 0) {
  console.log('Positive')
} else if (num < 0) {
  console.log('Negative')
} else {
  console.log('Zero')
}

// switch
let day: number = 3
let dayString: string
switch (day) {
  case 1:
    dayString = 'Monday'
    break
  case 2:
    dayString = 'Tuesday'
    break
  case 3:
    dayString = 'Wednesday'
    break
  // ... other cases
  default:
    dayString = 'Unknown'
}

// ternary
let isRaining: boolean = true
let action: string

// Ternary operator
action = isRaining ? 'Stay indoors' : 'Go outside'

// nullish coalescing
let userInput: string | null = window.prompt('Hi, how are you?')
let username: string = userInput ?? 'defaultUsername'

// optional chaining
let user = {
  address: {
    street: '123 Main St',
    city: 'Cityville',
  },
}
let city = user?.address?.city // Safe access even if address or city is undefined/null
