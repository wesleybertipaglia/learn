# Mathematics Basics: Least Common Multiple (LCM)

## 1. Definition of LCM
- **LCM (Least Common Multiple)**: The least common multiple of two or more numbers is the smallest positive integer that is divisible by each of the numbers.
- **Formula**:  
  - LCM of `a` and `b` is the smallest number that is a multiple of both `a` and `b`.  
  - **Example**:  
    - LCM of 4 and 5 is 20 because 20 is the smallest number that both 4 and 5 divide into without leaving a remainder.

---

## 2. How to Find LCM

### a) Method 1: Prime Factorization
1. **Prime Factorization**: Write each number as a product of prime factors.
2. **Take the highest power** of each prime factor that appears in any of the factorizations.
3. **Multiply** these highest powers together to find the LCM.

#### Example: LCM of 12 and 18
- Prime factorization of 12: `12 = 2² * 3`
- Prime factorization of 18: `18 = 2 * 3²`
- Take the highest powers: `2²` and `3²`
- LCM = `2² * 3² = 4 * 9 = 36`

---

### b) Method 2: Using the Relationship with GCD (Greatest Common Divisor)
- **Formula**:  
  `LCM(a, b) = (a * b) / GCD(a, b)`
- **Explanation**: The LCM of two numbers can be found by multiplying them together and dividing by their greatest common divisor (GCD).
  
#### Example: LCM of 12 and 18
- GCD of 12 and 18 is 6.
- `LCM(12, 18) = (12 * 18) / 6 = 216 / 6 = 36`

---

### c) Method 3: Listing Multiples
1. **List multiples** of each number.
2. **Find the smallest multiple** that appears in both lists.

#### Example: LCM of 4 and 6
- Multiples of 4: `4, 8, 12, 16, 20, 24, ...`
- Multiples of 6: `6, 12, 18, 24, ...`
- The smallest common multiple is 12, so `LCM(4, 6) = 12`.

---

## 3. Properties of LCM

### a) LCM is Always Greater Than or Equal to Both Numbers
- The LCM of two numbers is always equal to or greater than both of the original numbers.

#### Example:  
- `LCM(4, 6) = 12`  
  `12 ≥ 4` and `12 ≥ 6`

---

### b) LCM of Multiple Numbers
- The LCM can be extended to more than two numbers.
  - **Example**:  
    `LCM(4, 6, 8)` is the LCM of `4` and `6`, then the result is used to find the LCM with `8`.

---

### c) LCM and GCD Relationship
- **Formula**:  
  `LCM(a, b) * GCD(a, b) = a * b`
  This relationship helps in calculating the LCM efficiently if you already know the GCD.

---

### d) LCM of Consecutive Numbers
- The LCM of two consecutive numbers (e.g., 5 and 6) is simply their product because consecutive numbers are always relatively prime (GCD is 1).

---

## 4. Summary Table of LCM Methods

| Method                         | Formula / Steps                                | Example                       | Result |
|---------------------------------|-----------------------------------------------|-------------------------------|--------|
| Prime Factorization            | Take the highest powers of prime factors.    | LCM(12, 18)                   | 36     |
| Using GCD                      | `LCM(a, b) = (a * b) / GCD(a, b)`            | LCM(12, 18)                   | 36     |
| Listing Multiples              | List multiples and find the smallest common. | LCM(4, 6)                     | 12     |

---

## 5. Special Cases

- **LCM of 1 and any number**:  
  `LCM(1, x) = x` because any number is divisible by 1.

- **LCM of two numbers where one is a multiple of the other**:  
  If `a` divides `b`, then `LCM(a, b) = b`.  
  Example:  
  `LCM(5, 20) = 20` because 20 is a multiple of 5.
