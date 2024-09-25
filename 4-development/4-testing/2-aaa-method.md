# AAA Method

The AAA (Arrange, Act, Assert) method is a structured approach used in software testing, particularly in unit testing. It helps ensure that tests are clear, organized, and effective.

## Key Components

### 1. **Arrange**

- **Purpose**: Set up the test environment and prepare all necessary data and dependencies.
- **Activities**: 
  - Initialize objects and variables.
  - Configure the system or mock dependencies.
  - Prepare the input data required for the test.

### 2. **Act**

- **Purpose**: Execute the code or functionality being tested.
- **Activities**: 
  - Call the method or function under test.
  - Perform actions that are necessary to invoke the behavior being tested.

### 3. **Assert**

- **Purpose**: Verify that the outcome of the test is as expected.
- **Activities**: 
  - Compare the actual result to the expected result.
  - Check if the test conditions meet the defined criteria.
  - Report or handle discrepancies between the expected and actual results.

## Benefits

- **Clarity**: Provides a clear structure for writing and understanding tests.
- **Maintainability**: Makes it easier to modify and maintain tests over time.
- **Focus**: Helps to keep tests focused on a single behavior or outcome.

## Example

Consider a simple unit test for a function that calculates the sum of two numbers:

```python
import unittest

# Function to be tested
def add_numbers(a, b):
    return a + b

# Unit test using the AAA method
class TestAddNumbers(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        # Arrange
        num1 = 5
        num2 = 3
        expected_sum = 8

        # Act
        result = add_numbers(num1, num2)

        # Assert
        self.assertEqual(result, expected_sum)

    def test_add_negative_and_positive_number(self):
        # Arrange
        num1 = -2
        num2 = 7
        expected_sum = 5

        # Act
        result = add_numbers(num1, num2)

        # Assert
        self.assertEqual(result, expected_sum)

    def test_add_two_negative_numbers(self):
        # Arrange
        num1 = -4
        num2 = -6
        expected_sum = -10

        # Act
        result = add_numbers(num1, num2)

        # Assert
        self.assertEqual(result, expected_sum)

# Run the tests
if __name__ == '__main__':
    unittest.main()
```

---

- [Previous](./1-introduction.md)
- [Next](./3-unit-testing.md)
