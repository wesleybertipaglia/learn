# Linux Permissions

In Linux, the permissions system controls access to files and directories. Each file and directory has permissions associated with it, defining who can read, write, or execute the contents.

## User Types

There are three main types of users in Linux:

1. **Owner**: The user who created the file or directory.
2. **Group**: A group of users who have specific permissions for the file or directory.
3. **Others**: All other users on the system.

## Permission Structure

Permissions are displayed in the format `rwx`, where:

- **r (4)** - Read permission
- **w (2)** - Write permission
- **x (1)** - Execute permission

Each permission can be represented by it letter of it corresponding octal value.

## Viewing Permissions

Permissions can be viewed using the `ls -l` command:
```bash
ls -l
```

The output will be something like:
```bash
-rwxr-xr--
```

Here, `-rwxr-xr--` means:
- **-**: File type (e.g. `-` for regular file, `d` for directory)
- **rwx**: Permissions for owner
- **r-x**: Permissions for group
- **r--**: Permissions for others

## Modifying Permissions

Permissions can be changed using the `chmod` command:

### Symbolic Mode

You can add or remove permissions using letters:

- **+**: Add permission
- **-**: Remove permission
- **=`**: Set permission

And you can specify the user type:

- **u**: Owner
- **g**: Group
- **o**: Others

> If you don't specify a user type, it will apply to all users.

Examples:
- Add execute permission for owner:
```bash
chmod u+x file
```
- Remove write permission for the group:
```bash
chmod g-w file
```
- Set read and write permissions for everyone:
```bash
chmod a+rw file
```

### Octal Mode

Permissions can also be specified using numbers:
- **4**: Read
- **2**: Write
- **1**: Execute

Permissions are represented as a combination of these numbers:
- **7**: Read (4) + write (2) + execute (1)
- **6**: Read (4) + write (2)
- **5**: Read (4) + execute (1)
- **4**: Read (4)
- **3**: Write (2) + execute (1)
- **2**: Write (2)
- **1**: Execute (1)

Examples:
- Set read, write, and execute permissions for the owner, and read only for the group and others:
```bash
chmod 744 file
```
- Set read and write permissions for everyone:
```bash
chmod 666 file
```

## Ownership

The ownership of a file or directory can be changed using the `chown` (to change the owner) and `chgrp` (to change the group) commands:

- Change both the owner and the group:
```bash
chown user:group file
```
- Change only the owner:
```bash
chown user file
```

- Change only the group:
```bash
chgrp group file
```

---

- [Previous](./3-files.md)
- [Next](./5-users.md)