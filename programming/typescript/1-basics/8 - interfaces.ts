/* interfaces */
interface robot {
  readonly id: number | string // cant change
  name: string
}

// new object from an interface
const bot: robot = {
  id: '1',
  name: 'R2D2',
}

// new class from an interface
class Person implements robot {
  id: string | number
  name: string

  constructor(id: string | number, name: string) {
    this.id = id
    this.name = name
  }
}
