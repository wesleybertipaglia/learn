# System Testing

System testing is a high-level testing phase that focuses on validating the complete and integrated software system. The goal is to ensure that the entire system meets specified requirements and functions correctly in a real-world environment.

## Key Concepts

### 1. **Purpose of System Testing**

- **Verify System Behavior**: Ensure that the entire system operates according to the specified requirements and use cases.
- **Validate End-to-End Functionality**: Confirm that all integrated components and modules work together seamlessly to deliver the expected results.
- **Identify Issues**: Detect any defects or inconsistencies in the system’s overall behavior and performance.
- **Ensure Compliance**: Verify that the system adheres to regulatory, security, and performance standards.

### 2. **Types of System Testing**

- **Functional Testing**: Validates that the system performs its intended functions correctly based on the requirements.
- **Non-Functional Testing**: Assesses aspects such as performance, usability, reliability, and security.
- **Regression Testing**: Ensures that recent changes or additions to the system have not adversely affected existing functionality.
- **Acceptance Testing**: Verifies that the system meets business requirements and is ready for deployment or release.

### 3. **System Testing Approaches**

- **Black-Box Testing**: Focuses on testing the system’s outputs based on various inputs without knowledge of the internal workings.
- **White-Box Testing**: Involves testing internal structures or logic of the system.
- **Gray-Box Testing**: Combines elements of both black-box and white-box testing to cover more comprehensive test scenarios.

### 4. **Challenges in System Testing**

- **Complexity**: Managing and coordinating tests for a complete and integrated system can be complex and resource-intensive.
- **Environment Configuration**: Ensuring that the test environment accurately reflects the production environment.
- **Test Data Management**: Handling and managing data across different system components.
- **Scope and Coverage**: Ensuring comprehensive test coverage across all system functionalities and integration points.

### 5. **Best Practices**

- **Develop Clear Test Plans**: Create detailed test plans and test cases that cover all functional and non-functional requirements.
- **Use Realistic Test Data**: Ensure that test data is representative of real-world scenarios and use cases.
- **Automate Where Possible**: Implement test automation to streamline repetitive testing tasks and improve efficiency.
- **Conduct Regular Testing**: Perform system testing regularly throughout the development lifecycle to identify and address issues early.
- **Collaborate with Stakeholders**: Work closely with development, QA, and business teams to ensure comprehensive testing and alignment with requirements.

## Example

Consider a system test for a user service that creates and retrieves user information from a repository while sending notifications. The test verifies that the user creation and retrieval functions work correctly and that the notification service is triggered as expected.

```python
import unittest

# Mock classes to simulate the UserRepository and NotificationService
class UserRepository:
    """Simulates a repository that stores and retrieves user data."""
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_info):
        self.users[user_id] = user_info

    def get_user(self, user_id):
        return self.users.get(user_id)

class NotificationService:
    """Simulates a notification service that sends notifications."""
    def __init__(self):
        self.notifications = []

    def send_notification(self, message):
        self.notifications.append(message)

# The UserService interacts with the UserRepository and NotificationService
class UserService:
    def __init__(self, user_repo, notification_service):
        self.user_repo = user_repo
        self.notification_service = notification_service

    def create_user(self, user_id, user_info):
        self.user_repo.add_user(user_id, user_info)
        self.notification_service.send_notification(f"User {user_id} created!")

    def retrieve_user(self, user_id):
        return self.user_repo.get_user(user_id)

# System Test Case
class TestUserServiceSystem(unittest.TestCase):
    
    def setUp(self):
        # Set up repository and notification service
        self.user_repo = UserRepository()
        self.notification_service = NotificationService()
        self.user_service = UserService(self.user_repo, self.notification_service)

    def test_create_and_retrieve_user(self):
        # Test user creation
        user_id = "user123"
        user_info = {"name": "John Doe", "email": "john@example.com"}
        
        self.user_service.create_user(user_id, user_info)
        
        # Verify user is added to the repository
        retrieved_user = self.user_service.retrieve_user(user_id)
        self.assertEqual(retrieved_user, user_info)
        
        # Verify that the notification was sent
        self.assertIn(f"User {user_id} created!", self.notification_service.notifications)

    def test_user_not_found(self):
        # Test retrieving a non-existing user
        user_id = "non_existent_user"
        retrieved_user = self.user_service.retrieve_user(user_id)
        
        # Assert the user does not exist
        self.assertIsNone(retrieved_user)

# Run the system tests
if __name__ == '__main__':
    unittest.main()
```

---

- [Previous](./4-integration-testing.md)
- [Next](./6.py-test.md)
