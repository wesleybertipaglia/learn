# Linux Users

In Linux, user management is essential for system administration and controlling access to files and resources. Here are the main concepts and commands related to users.

## Basic Concepts

- **User**: Entity that can authenticate to the system and execute processes. Each user has a unique identifier called UID (User ID).

- **Superuser (root)**: Special user account with administrative privileges to perform system-wide tasks.

- **Home Directory**: Location where a user's files and settings are stored.

## Commands

### User Information

- Display the current user's username:

```bash
whoami
```

- Display the current user's ID:

```bash
id
```

- Display detailed information about a user:

```bash
finger username
```

- Display information about all users on the system:

```bash
cat /etc/passwd
```

### User Creation

- Adds a new user to the system:

```bash
# using adduser (more interactive)
sudo adduser username

# using useradd
sudo useradd username
```

### User Deletion

- Removes a user from the system:

```bash
# using deluser (more interactive)
sudo deluser username

# using userdel
sudo userdel username
```

### Modify User Properties

- Changes the username of a user:

```bash
sudo usermod -l new_username old_username
```

- Changes the password of a user:

```bash
sudo usermod -p password username
```

- Changes the password of the current user:

```bash
passwd
```

- Changes the password of a specific user:

```bash
sudo passwd username
```

### User Permissions

- Changes the owner of a file or directory:

```bash
sudo chown username:groupname file
```

- Changes the permissions of a file or directory:

```bash
sudo chmod permissions file
```

## Related Files

- **/etc/passwd**: File that contains information about users, such as their name, UID, GID, and home directory.

- **/etc/shadow**: File that contains information about user passwords and expiration policies.

- **/etc/group**: File that contains information about groups and their members.

---

- [Previous](./3-files.md)
- [Next](./5-groups.md)
