# Linux Groups

In Linux, groups are used to manage permissions and resources for multiple users. Each user belongs to one or more groups, which define the access rights and privileges that the user has on the system.

## Basic Concepts

- **Group**: A set of users that share permissions and resources. Each group has a unique identifier called GID (Group ID).

- **Primary Group**: The main group to which a user belongs. It is specified in the user's entry in the `/etc/passwd` file.

- **Additional Groups**: A user can belong to multiple groups, in addition to their primary group, to access shared resources and files.

- **Group Permissions**: The permissions assigned to a group on a file or directory, which determine the actions that group members can perform.

- **Group Owner**: The user who owns a group and has administrative control over it.

- **Group Membership**: The list of users who belong to a particular group.

- **Group Ownership**: A group can own files and directories, allowing all members of the group to access and modify them.


## Commands

### Group Information

- `cat /etc/group`: Displays information about all groups on the system.

```bash
cat /etc/group
```

- `groups`: Displays the groups to which the current user belongs.

```bash
groups
```

- `groups username`: Displays the groups to which a specific user belongs.

```bash
groups username
```

### Group Creation

- `addgroup` / `groupadd`: Adds a new group to the system.

```bash
sudo addgroup groupname
```

> `addgroup` is more interactive, while `groupadd` is more basic and requires additional options for configuration.

### Group Deletion

- `delgroup` / `groupdel`: Removes a group from the system.

```bash
sudo delgroup groupname
```

> `groupdel` is less interactive, while `delgroup` can offer additional options.

### Modify Group Properties

- Change the group name:

```bash
sudo groupmod -n new_group old_group
```

- Change the group owner:

```bash
sudo chown :new_group file
```

### Group Membership

- Add a user to a group:

```bash
sudo gpasswd -a username groupname
```

- Remove a user from a group:

```bash
sudo gpasswd -d username groupname
```

- Change the primary group of a user:

```bash
sudo usermod -g new_group username
```

- Add a user to an additional group:

```bash
sudo usermod -aG additional_group username
```

### Group Permissions

- Change the group ownership of a file or directory:

```bash
sudo chown :groupname file
```

- Change the group permissions of a file or directory:

```bash
sudo chmod g+rw file
```

- Change the default group permissions for new files:

```bash
umask 002
```

> The `umask` command sets the default permissions for new files created by the user.

## Related Files

- **/etc/passwd**: File that contains information about users, such as their name, UID, GID, and home directory.
- **/etc/shadow**: File that contains information about user passwords and expiration policies.
- **/etc/group**: File that contains information about groups and their members.

---

- [Previous](./4-users.md)
- [Next](./6-permissions.md)
