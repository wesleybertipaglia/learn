# Git Foundations

## 1. What is Git?
Git is a **version control system (VCS)** that helps track changes in source code during software development. It allows multiple developers to work on a project simultaneously without overwriting each other's work.

## 2. Key Concepts

### a. Repository (Repo)
A **repository** is where Git stores your project's files and the history of changes. Repos can be local (on your computer) or remote (on a server like GitHub).

### b. Commit
A **commit** is a snapshot of your code at a specific point in time. Each commit has a unique identifier (hash) and contains a message describing the changes made.

### c. Branch
A **branch** is a parallel version of the codebase. By default, Git creates a `main` branch (formerly `master`). Branches allow developers to work on features independently.

### d. Merge
**Merging** is the process of integrating changes from one branch into another.

### e. Clone
**Cloning** is copying a remote repository to your local machine to work on it.

### f. Pull
A **pull** operation fetches changes from a remote repository and integrates them into your local repo.

### g. Push
A **push** operation sends your local changes (commits) to a remote repository.

## 3. Basic Git Commands

| Command                    | Description                                              |
|----------------------------|----------------------------------------------------------|
| `git init`                  | Initializes a new Git repository                         |
| `git clone <repo>`          | Clones a repository from a remote source                 |
| `git status`                | Shows the status of your working directory               |
| `git add <file>`            | Stages changes for commit                               |
| `git commit -m "message"`   | Commits staged changes with a message                    |
| `git push`                  | Pushes local commits to a remote repository              |
| `git pull`                  | Fetches and merges changes from a remote repo            |
| `git checkout <branch>`     | Switches to a different branch                           |
| `git branch`                | Lists all branches                                       |
| `git merge <branch>`        | Merges changes from one branch into another              |
| `git log`                   | Displays commit history                                  |

## 4. Best Practices

- **Commit Frequently**: Make small, focused commits with clear messages.
- **Use Branches**: Work on features in separate branches to avoid conflicts.
- **Pull Before Push**: Always fetch changes before pushing your own.
- **Write Descriptive Messages**: Explain the purpose of each commit clearly.
- **Review Changes**: Before committing, review your changes for errors.
- **Keep Repositories Clean**: Remove unnecessary files and branches.

## 5. Git Workflow

1. **Initialize Repository**: Create a new repository or clone an existing one.
2. **Work on Files**: Modify files in your working directory.
3. **Stage Changes**: Use `git add` to stage changes for commit.
4. **Commit Changes**: Use `git commit` to save staged changes.
5. **Push Changes**: Send your commits to a remote repository.
6. **Pull Changes**: Fetch and integrate changes from the remote repo.

## 6. Git Hosting Services

Popular Git hosting services include:

- **GitHub**: Offers free public repositories and collaboration tools.
- **GitLab**: Provides both cloud-hosted and self-hosted options.
- **Bitbucket**: Supports Git and Mercurial repositories with Jira integration.

## 7. Git GUI Tools

Git GUI tools provide a graphical interface for Git operations. Some popular options are:

- **GitHub Desktop**: Simplifies Git workflows with an intuitive interface.
- **GitKraken**: Offers visual tools for branching, merging, and collaboration.
- **SourceTree**: Supports Git and Mercurial repositories with advanced features.

---

- [Next](./2-configuration.md)
