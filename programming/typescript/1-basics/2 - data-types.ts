/* Data Types */
// boolean
let isDone: boolean = false

// number
let decimal: number = 6
let hex: number = 0xf00d
let binary: number = 0b1010
let octal: number = 0o744

// string
let color: string = 'blue'

// array
let listOne: number[] = [1, 2, 3]
let listTwo: Array<number> = [1, 2, 3]

// tuple
let myArray: [string, number] = ['hello', 10]

// enum
enum Color {
  Red,
  Green,
  Blue,
}
let c: Color = Color.Green

// date
let aniversary: Date = new Date('1999-02-21')

// any
let notSure: any = 4
notSure = 'maybe a string instead'

// type union
let value: string | number = 'string'
value = 10 // ok

let multTypeArray: (string | number)[] = ['test', 10]

// type aliases
type Point = { x: number; y: number }
let p: Point = { x: 10, y: 20 }

// void
function warnUser(): void {
  console.log('This is a warning message')
}

// null
let n: null = null

// undefined
let u: undefined = undefined
