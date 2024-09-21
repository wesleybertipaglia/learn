# Git History

## 1. What is Git History?

Git **history** refers to the record of all changes made in a Git repository over time. Every commit in Git represents a snapshot of the project at a specific point in time. The history helps in tracking changes, finding bugs, reviewing the development process, and understanding the evolution of the codebase.

Git history includes all commits, branches, merges, and other actions that modify the repository.

## 2. Viewing Git History

You can view the commit history using Git commands that show logs, diffs, and information about changes.

1. Git Log
The **git log** command is the primary tool to view the history of commits. It shows a list of commits in reverse chronological order (most recent first).

```bash
# standard log
git log 

# log with one-line commit messages
git log --oneline

# log with a graph of branches
git log --graph

# log with a specific number of commits
git log -n 5

# log with a specific author
git log --author="John Doe"

# log with a specific date range
git log --since="2022-01-01" --until="2022-12-31"

# log with a specific file
git log -- <file>

# log with a specific commit message
git log --grep="bug fix"
```

2. Git Short Log
The **git shortlog** command provides a summary of commits grouped by author. It shows the number of commits made by each author.

```bash
# standard shortlog
git shortlog

# with commit count
git shortlog -sn

# with commit count and email
git shortlog -sne

# with commit count and summary
git shortlog -sn --summary

# with commit count and summary for a specific file
git shortlog -sn --summary -- <file>

# with commit count and summary for a specific author
git shortlog -sn --summary --author="John Doe"

# with commit count and summary for a specific date range
git shortlog -sn --summary --since="2022-01-01" --until="2022-12-31"
```

3. Git Show
The **git show** command displays information about a specific commit, including the changes made in that commit.

```bash
git show <commit-hash>
```

4. Git Diff
The **git diff** command shows the differences between two commits, branches, or files.

```bash
git diff <commit1> <commit2>
```

5. Git Blame
The **git blame** command shows who last modified each line of a file and when.

```bash
git blame <file>
```

## 3. Git History Best Practices

- **Meaningful Commits**: Write clear and concise commit messages that explain the purpose of the changes.

- **Atomic Commits**: Make small, focused commits that address a single issue or feature.

- **Branch Naming**: Use descriptive branch names that reflect the purpose of the branch.

- **Rebase Before Merge**: Use `git rebase` to clean up your commit history before merging branches.

- **Tagging Releases**: Use Git tags to mark specific commits as releases or milestones.


---

- [Previous](./6-pr.md)

