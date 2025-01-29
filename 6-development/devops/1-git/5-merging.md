# Git Merging

## 1. What is Merging?

**Merging** in Git is the process of combining changes from one branch into another. It typically happens when you want to integrate feature development, bug fixes, or changes from multiple collaborators into a stable branch, such as `main`.

### Key Concepts:
- **Source Branch**: The branch containing the changes you want to integrate.
- **Target Branch**: The branch you want to merge changes into.
- **Merge Commit**: A special commit that records the integration of changes from both branches.

## 2. Types of Merges

### a. Fast-Forward Merge
A **fast-forward merge** occurs when the target branch has not diverged from the source branch. Git simply moves the target branch pointer forward to match the source branch, resulting in no merge commit.

```bash
# Switch to the target branch
git checkout main

# Merge the source branch (e.g., feature-branch)
git merge feature-branch
```

## 3. Workflow Example

1. **Create a New Branch**
```bash
# Create a new branch
git checkout -b feature-branch
```

2. **Work on the Branch**
```bash
# Make changes to your files
git add .
git commit -m "Add new feature"
```

3. **Push the Branch**
```bash
# Push the branch to the remote repository
git push origin feature-branch
```

4. **Switch Between Branches**
```bash
# Switch to the main branch
git checkout main
```

5. **Merge the Branch**
```bash
# Merge the feature branch into the main branch
git merge feature-branch
```

6. **Delete the Branch**
```bash
# Delete the feature branch after merging
git branch -d feature-branch
```

## 4. Merge Conflicts

**Merge conflicts** occur when Git cannot automatically merge changes between branches. This happens when the same part of a file has been modified in both branches. Resolving conflicts involves manually editing the conflicting files to choose which changes to keep.

### Steps to Resolve Merge Conflicts:

1. **Identify Conflicts**: Git will mark the conflicting files. Open them in a text editor to resolve the conflicts.

2. **Resolve Conflicts**: Edit the conflicting files to keep the desired changes. Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

3. **Add Changes**: After resolving conflicts, add the modified files to the staging area.

4. **Commit Changes**: Create a merge commit to finalize the merge process.

```bash
# Resolve conflicts in the conflicting files
# Add the modified files to the staging area
git add <file1> <file2> ...

# Commit the changes to complete the merge
git commit -m "Merge branch 'feature-branch' into main"
```

## 5. Merge Strategies

Git provides different **merge strategies** to handle conflicts and merge changes. Some common strategies include:

- **Recursive Merge**: The default strategy that handles most merge scenarios.

- **Octopus Merge**: Merges more than two branches simultaneously.

- **Resolve Merge**: Attempts to automatically resolve conflicts.

- **Ours Merge**: Keeps the changes from the current branch and ignores changes from the merged branch.

- **Subtree Merge**: Merges a subdirectory of one repository into another repository.

## 6. Merge vs Rebase

**Merging** integrates changes from one branch into another, creating a merge commit. It preserves the commit history of both branches but can result in a cluttered history.

```bash
# Merge the source branch into the target branch
git merge source-branch
```

**Rebasing** is an alternative to merging that moves the commits from one branch to another, creating a linear history. It is useful for maintaining a clean commit history but can rewrite commit IDs and cause conflicts.

```bash
# Rebase the source branch onto the target branch
git rebase target-branch
```

> **Note**: Choose between merging and rebasing based on your project's needs and collaboration workflow.

---

- [Previous](./4-branches.md)
- [Next](6-pr.md)
