# Git Branches

## 1. What is a Branch?

A **branch** in Git represents an independent line of development in a repository. It allows you to work on different versions of a project simultaneously, such as adding new features or fixing bugs, without affecting the main codebase.

The default branch in Git is usually called `main` (formerly `master`), but you can create and switch between branches to work on different parts of the project independently.

## 2. Why Use Branches?

- **Parallel Development**: Developers can work on different features or fixes at the same time without interfering with each other.
- **Isolated Environments**: Changes made in one branch do not affect others until they are merged.
- **Version Control**: Branches make it easy to manage different versions or releases of a project.

## 3. Key Branching Concepts

### a. Main Branch (Default Branch)
The **main branch** (often named `main`) is the central branch that contains the official, stable version of the project. 

### b. Feature Branch
A **feature branch** is a branch created for developing a specific feature or fix. Once the feature is complete, the branch is typically merged back into the `main` branch.

### c. Branching Strategy
A **branching strategy** defines how branches are created, merged, and managed. Common strategies include:

- **Feature branching**: Each feature is developed in its own branch.
- **Git Flow**: A structured workflow that uses different branches like `develop`, `release`, and `hotfix`.

### d. Merging
**Merging** integrates changes from one branch into another, usually from a feature branch back into the `main` branch after development is complete.

### e. Rebasing
**Rebasing** is another way to integrate changes from one branch into another by moving or combining commits, often used to maintain a cleaner commit history.

## 4. Common Branch Commands

| Command                             | Description                                                 |
|-------------------------------------|-------------------------------------------------------------|
| `git branch`                        | Lists all local branches                                    |
| `git branch <branch-name>`          | Creates a new branch                                        |
| `git checkout <branch-name>`        | Switches to an existing branch                              |
| `git checkout -b <branch-name>`     | Creates and switches to a new branch                        |
| `git merge <branch-name>`           | Merges the specified branch into the current branch         |
| `git branch -d <branch-name>`       | Deletes a branch locally                                    |
| `git push origin <branch-name>`     | Pushes a branch to the remote repository                    |
| `git pull origin <branch-name>`     | Pulls the latest changes from a remote branch               |

## 5. Workflow Example

1. **Create a New Branch**  
To create a new branch and switch to it:
```bash
   git checkout -b feature-xyz
```

2. **Work on the Branch**  
Make changes to your files and commit them:
```bash
   git add .
   git commit -m "Add new feature"
```

3. **Push the Branch**
To push the branch to the remote repository:
```bash
   git push origin feature-xyz
```

4. **Switch Between Branches**
To switch between branches:
```bash
   git checkout main
```

5. **Merge the Branch**
To merge the feature branch into the main branch:
```bash
   git checkout main
   git merge feature-xyz
```

6. **Delete the Branch**
After merging, delete the feature branch:
```bash
   git branch -d feature-xyz
```

## 6. Best Practices

- **Use Descriptive Names**: Name branches based on the feature or fix being developed.
- **Keep Branches Small**: Focus on one feature per branch to simplify development and review.
- **Regularly Update Branches**: Fetch changes from the main branch to keep feature branches up to date.
- **Review Changes Before Merging**: Ensure that the changes in a branch are tested and reviewed before merging.
- **Delete Merged Branches**: Remove feature branches after merging to keep the repository clean.

---

- [Previous](./3-repositories.md)
- [Next](./5-merging.md)
