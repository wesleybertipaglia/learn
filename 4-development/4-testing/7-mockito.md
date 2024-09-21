# Mockito

Mockito is a popular mocking framework for Java that allows developers to create and configure mock objects for unit testing. It helps simulate the behavior of complex dependencies and isolate the units being tested.

## Key Concepts

### 1. **Purpose of Mockito**

- **Mock Dependencies**: Create mock objects to simulate the behavior of complex dependencies in unit tests.
- **Isolate Units**: Ensure that tests focus on the unit being tested without relying on external systems or components.
- **Verify Interactions**: Check that specific methods are called on mock objects with the expected parameters.

### 2. **Core Features**

- **Mocking**: Create mock objects for interfaces and classes to simulate their behavior in tests.
- **Stubbing**: Define the behavior of mock objects, such as what values they should return when certain methods are called.
- **Verification**: Confirm that certain methods were called on mock objects with specific arguments.
- **Argument Matchers**: Use matchers to specify flexible conditions for method arguments.

### 3. **Core Annotations**

- **`@Mock`**: Creates a mock instance of a class or interface.
- **`@Spy`**: Creates a partial mock, allowing the real methods to be called unless stubbed.
- **`@InjectMocks`**: Automatically injects mock or spy fields into the annotated class.
- **`@Captor`**: Captures argument values passed to mocked methods for further assertions.

### 4. **Common Methods**

- **`Mockito.mock(Class<T> classToMock)`**: Creates a mock object of the specified class or interface.
- **`Mockito.when(T methodCall)`**: Stubs a method call to return a specific value or perform an action.
- **`Mockito.verify(T mock)`**: Verifies that specific interactions occurred on a mock object.
- **`Mockito.times(int wantedNumberOfInvocations)`**: Specifies the number of times a method is expected to be called.

### 5. **Best Practices**

- **Use Mock Objects Wisely**: Only mock dependencies that are complex or external to ensure tests remain meaningful and maintainable.
- **Keep Tests Focused**: Ensure tests focus on the behavior of the unit under test, rather than the implementation of mocks.
- **Verify Interactions**: Use verification to ensure that the unit under test interacts correctly with its dependencies.
- **Avoid Over-Mocking**: Over-mocking can lead to brittle tests. Use real implementations or simpler mocks when possible.
- **Use Argument Matchers Judiciously**: Employ argument matchers to make your tests more flexible and maintainable.

## Example

Consider a simple unit test for a service that calculates the total price of items in a shopping cart:

```java
import org.junit.jupiter.api.Test;
import static org.mockito.Mockito.*;

public class ShoppingCartServiceTest {

    @Test
    public void testCalculateTotalPrice() {
        // Arrange
        ShoppingCartDao dao = mock(ShoppingCartDao.class);
        when(dao.getItemsInCart()).thenReturn(new int[]{10, 20, 30});

        ShoppingCartService service = new ShoppingCartService(dao);

        // Act
        double totalPrice = service.calculateTotalPrice();

        // Assert
        assertEquals(60.0, totalPrice);
        verify(dao, times(1)).getItemsInCart();
    }

}
```

## Conclusion

Mockito is a powerful and flexible mocking framework that simplifies the process of creating and managing mock objects in Java unit tests. By allowing developers to isolate units, define behavior, and verify interactions, Mockito enhances the testing process and helps ensure code quality. Following best practices and leveraging Mockito’s features effectively can improve the reliability and maintainability of tests.
