/*
    TypeScript is a programming language developed by Microsoft. 
    It is a superset of JavaScript, which means that any valid JavaScript code is also valid TypeScript code. 
    However, TypeScript extends JavaScript by adding static typing to the language. 
    This means that developers can specify the data types of variables, function parameters, and return types. 
    Some key features of TypeScript include:
*/

/*
    Static Typing:
    TypeScript allows developers to define the types of variables, function parameters, and return values. 
    This helps catch type-related errors at compile time rather than runtime, providing better code quality and improved tooling support.
*/
let age: number = 24
const firstName = 'Wesley'

/*
    Interfaces:
    TypeScript supports the use of interfaces, which allow developers to define the structure of objects. 
    This can enhance code readability and help catch potential errors during development.
*/
interface project {
  readonly id: number | string
  name: string
}

/*
    Generics:
    TypeScript supports generics, allowing developers to write more reusable and type-safe code by creating functions and data structures that work with a variety of types.
*/
let genericValue: any = 4
genericValue = 'maybe a string instead'

/*
    Compatibility:
    Since TypeScript is a superset of JavaScript, existing JavaScript code can be gradually migrated to TypeScript. 
    This allows developers to adopt TypeScript at their own pace.
*/
console.log('Hello, TypeScript!')
