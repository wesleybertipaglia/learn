# Mathematics Basics: Greatest Common Divisor (GCD)

## 1. Definition of GCD
- **GCD (Greatest Common Divisor)**: The GCD of two or more numbers is the largest positive integer that divides each of the numbers without leaving a remainder.
- **Other Names**: It is also called the **greatest common factor (GCF)** or **highest common divisor (HCD)**.
  
#### Example:
- **GCD of 12 and 18**: The divisors of 12 are `{1, 2, 3, 4, 6, 12}`, and the divisors of 18 are `{1, 2, 3, 6, 9, 18}`. The common divisors are `{1, 2, 3, 6}`, and the greatest of these is `6`. Therefore, GCD(12, 18) = 6.

---

## 2. How to Find GCD

### a) **Method 1: Prime Factorization**
1. Write the prime factorizations of both numbers.
2. Identify the common prime factors.
3. Multiply the lowest powers of the common prime factors.

#### Example: GCD of 12 and 18
- Prime factorization of 12: `12 = 2² * 3`
- Prime factorization of 18: `18 = 2 * 3²`
- The common prime factors are `2` and `3`. Take the lowest powers: `2¹` and `3¹`.
- GCD = `2¹ * 3¹ = 6`.

---

### b) **Method 2: Euclidean Algorithm**
- The Euclidean algorithm involves repeated division to find the GCD.
1. Divide the larger number by the smaller number.
2. Take the remainder.
3. Divide the previous divisor by the remainder.
4. Repeat until the remainder is 0. The last non-zero remainder is the GCD.

#### Example: GCD of 12 and 18 using Euclidean algorithm
1. `18 ÷ 12 = 1` remainder `6`.
2. `12 ÷ 6 = 2` remainder `0`.
3. Since the remainder is now `0`, the GCD is the last non-zero remainder, which is `6`.

---

### c) **Method 3: Listing Divisors**
- List all divisors of each number and find the largest common divisor.

#### Example: GCD of 12 and 18
- Divisors of 12: `{1, 2, 3, 4, 6, 12}`
- Divisors of 18: `{1, 2, 3, 6, 9, 18}`
- The common divisors are `{1, 2, 3, 6}`, and the greatest common divisor is `6`.

---

## 3. Properties of GCD

### a) **GCD of 1 and Any Number**
- The GCD of `1` and any other number is always `1`.
  
#### Example:  
- `GCD(1, 5) = 1`

---

### b) **GCD of Two Prime Numbers**
- The GCD of two distinct prime numbers is always `1` since prime numbers do not share any divisors other than `1`.

#### Example:  
- `GCD(5, 7) = 1`

---

### c) **GCD is Commutative and Associative**
- **Commutative Property**: The GCD of two numbers does not depend on the order.
  - `GCD(a, b) = GCD(b, a)`
- **Associative Property**: The GCD of more than two numbers is the same regardless of how the numbers are grouped.
  - `GCD(a, b, c) = GCD(GCD(a, b), c)`

---

### d) **GCD and Divisibility**
- If `a` divides `b`, then `GCD(a, b) = a`.
  
#### Example:  
- `GCD(4, 8) = 4` because 4 divides 8 exactly.

---

### e) **GCD of Consecutive Numbers**
- The GCD of any two consecutive numbers is always `1` because consecutive numbers are always relatively prime (they do not have any common divisors other than `1`).
  
#### Example:  
- `GCD(8, 9) = 1`

---

## 4. Summary Table of GCD Methods

| Method                   | Formula / Steps                                     | Example                    | Result |
|--------------------------|-----------------------------------------------------|----------------------------|--------|
| Prime Factorization       | Find common prime factors and multiply the lowest powers. | `GCD(12, 18)`              | `6`    |
| Euclidean Algorithm       | Divide and take remainders until remainder is 0.    | `GCD(12, 18)`              | `6`    |
| Listing Divisors          | List divisors and find the greatest common divisor. | `GCD(12, 18)`              | `6`    |
| GCD of 1 and Any Number   | The GCD of 1 and any number is 1.                  | `GCD(1, 5)`                | `1`    |
| GCD of Two Prime Numbers | The GCD of two distinct primes is always 1.        | `GCD(5, 7)`                | `1`    |

---

## 5. Special Cases and Notes

- **Relatively Prime (Coprime) Numbers**: Two numbers are relatively prime (or coprime) if their GCD is `1`.
  
#### Example:
- `GCD(14, 15) = 1`, so 14 and 15 are relatively prime.

- **LCM and GCD Relationship**: The product of the LCM and GCD of two numbers is equal to the product of the numbers:
  - `LCM(a, b) * GCD(a, b) = a * b`
