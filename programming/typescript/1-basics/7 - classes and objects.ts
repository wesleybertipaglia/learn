/* Classes and Objects */

// Class
class Product {
  public productName: string // can be accessed anywhere
  private productBrand: string // can only be accessed within the class
  protected productPrice: number // can only be accessed within the class and subclasses
  productStock: number

  constructor(
    productName: string,
    productBrand: string,
    productPrice: number,
    productStock: number
  ) {
    this.productName = productName
    this.productBrand = productBrand
    this.productPrice = productPrice
    this.productStock = productStock
  }
}

// subclasses
class Drinks extends Product {
  flavor: string

  constructor(
    flavor: string,
    productName: string,
    productBrand: string,
    productPrice: number,
    productStock: number
  ) {
    super(productName, productBrand, productPrice, productStock)
    this.flavor = flavor
  }
}

// objects
const RedragonMice = new Product('Redragon Mice', 'Redragon', 20, 100)

// Object Types
type vehicle = {
  name: string
  brand: string
  type: string
}

let KawasakiJetski: vehicle = {
  name: 'Jetski',
  brand: 'Kawasaki',
  type: 'Jetski',
}
