# Git Repository

## 1. What is a Repository?

A **repository** (often called a "repo") in Git is a directory that contains your project's files and tracks their complete version history. It can be:

- **Local**: Resides on your computer.
- **Remote**: Hosted on a server like GitHub, GitLab, or Bitbucket.

Repositories help developers collaborate by providing a centralized place to manage code changes.

## 2. Types of Repositories

### a. Local Repository
A **local repository** is a version of the repository stored on your local machine. All your commits are first made here.

### b. Remote Repository
A **remote repository** is hosted on a remote server, allowing collaboration with other developers. It’s often hosted on platforms like GitHub, GitLab, or a private server. The remote repository is synchronized with local repositories via `git push` and `git pull`.

## 3. Basic Commands

- **Init**: To create a new local repository, you use the `git init` command. This command initializes a new Git repository in the current directory.

```bash
git init
```

- **Clone**: To get a working copy of a remote repository to your local machine, you use the `git clone` command. This command creates a full copy of the repository with its history.
  
```bash
git clone <repo-url>
```

- **Remote Add**: To add a remote repository as a new remote, you use the `git remote add` command. This command creates a new connection to a remote repository.

```bash
git remote add origin <repo-url>
```

- **Remote List**: To list all the remote repositories connected to your local repository, you use the `git remote -v` command.
```bash
git remote -v
```

- **Pull Origin**: To fetch changes from the remote repository and merge them into your local repository, you use the `git pull origin <branch-name>` command.

```bash
git pull origin main
```

- **Push Origin**: To send your local changes to the remote repository, you use the `git push origin <branch-name>` command.

```bash
git push origin main
```

- **Fork**: To create a copy of a repository in your GitHub account, you use the `Fork` button on the repository's page.

## 4. Best Practices

- **Keep a Clean History**: Make small, focused commits with clear messages.

- **Use Branches**: Work on features in separate branches to avoid conflicts.

- **Sync Regularly**: Fetch changes before pushing your own to avoid conflicts.

- **Secure Your Repository**: Protect your repository with strong passwords and two-factor authentication.

---

- [Previous](./2-configuration.md)
- [Next](./4-branches.md)
