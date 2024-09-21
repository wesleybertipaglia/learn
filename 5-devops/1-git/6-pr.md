# Pull Requests

## 1. What is a Pull Request?

A **Pull Request (PR)** is a feature in Git-based collaboration platforms like GitHub, GitLab, or Bitbucket. It allows developers to notify others about changes they have made to a repository, request feedback, or propose that their changes be merged into the main codebase.

Pull requests facilitate code review, discussion, and collaboration before merging a feature branch into the target branch (e.g., `main` or `develop`).

## 2. Why Use Pull Requests?

- **Code Review**: Pull requests enable other developers to review the code for quality, security, and correctness before merging.
- **Collaboration**: PRs serve as a communication tool between team members, allowing for discussion and feedback on proposed changes.
- **History and Tracking**: A pull request records all the changes, comments, and decisions made, providing a clear history of why a certain change was introduced.

## 3. Pull Request Workflow

1. Create a Branch
Create a new branch for your feature or fix and commit changes to it.

```bash
git checkout -b feature-branch
# Make changes and commit
git add <file>
git commit -m "Add new feature"
```

2. Push the Branch
Push the branch to the remote repository to share your changes with others.

```bash
git push origin feature-branch
```

3. Create a Pull Request
On the collaboration platform (e.g., GitHub), create a pull request from your feature branch to the target branch (e.g., `main`).

4. Review and Discuss
Team members review your changes, provide feedback, and discuss the proposed changes.

5. Make Changes
If necessary, make changes based on the feedback received and push them to the same branch.

```bash
# Make changes and commit
git add <file>
git commit -m "Address feedback"
git push origin feature-branch
```

6. Merge the Pull Request
Once the changes are approved, merge the pull request into the target branch.

7. Delete the Branch
After merging, delete the feature branch to keep the repository clean.

```bash
git branch -d feature-branch
```

## 4. Best Practices

- **Small Pull Requests**: Keep pull requests small and focused on a single feature or fix.

- **Descriptive Titles and Descriptions**: Use clear and descriptive titles and descriptions to explain the purpose of the pull request.

- **Request Reviews**: Assign reviewers to your pull requests to ensure thorough code review.

- **Address Feedback Promptly**: Respond to feedback and make necessary changes promptly to keep the process moving.

- **Automate Tests**: Set up automated tests to run on pull requests to catch issues early.

- **Use Templates**: Create pull request templates to standardize the information provided in pull requests.

- **Follow Coding Standards**: Ensure that the code in the pull request follows the project's coding standards.

- **Keep Discussions Constructive**: Provide constructive feedback and engage in discussions respectfully.


---

- [Previous](./5-merging.md)
- [Next](7-history.md)
