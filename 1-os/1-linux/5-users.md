# Users and User Groups

In Linux, user and group management is essential for system administration and controlling access to files and resources. Here are the main concepts and commands related to users and groups.

## Basic Concepts

- **User**: Entity that can authenticate to the system and execute processes. Each user has a unique identifier called UID (User ID).
- **Group**: Set of users that share permissions and resources. Each group has a unique identifier called GID (Group ID).

## Commands

### User Management

#### User Information

- `whoami`: Displays the current username.

```bash
whoami
```

- `id`: Displays the current user's UID, GID, and groups.

```bash
id
```

- `finger username`: Displays detailed information about a user.

```bash
finger username
```

- `cat /etc/passwd`: Displays information about all users on the system.

```bash
cat /etc/passwd
```

#### User Creation

- `adduser` / `useradd`: Adds a new user to the system.

```bash
sudo adduser username
```

> `adduser` is more interactive, while `useradd` is more basic and requires additional options for configuration.

#### User Deletion

- `deluser` / `userdel`: Removes a user from the system.

```bash
sudo deluser username
```
> `userdel` is less interactive, while `deluser` can offer additional options.

#### Modify User Properties

- `usermod -l new_username old_username`: Changes the username of a user.

```bash
sudo usermod -l new_username old_username
```

- `usermod -p password username`: Changes the password of a user.

```bash
sudo usermod -p password username
```

- `passwd`: Changes the password of the current user.

```bash
passwd
```

- `passwd username`: Changes the password of a specific user.

```bash
sudo passwd username
```

#### Modify User Groups

- `usermod -g new_group username`: Changes the primary group of a user.

```bash
sudo usermod -g new_group username
```

- `usermod -aG additional_group username`: Adds a user to an additional group.

```bash
sudo usermod -aG additional_group username
```


### Group Management

#### Group Information

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

#### Group Creation

- `addgroup` / `groupadd`: Adds a new group to the system.

```bash
sudo addgroup groupname
```

> `addgroup` is more interactive, while `groupadd` is more basic and requires additional options for configuration.

#### Group Deletion

- `delgroup` / `groupdel`: Removes a group from the system.

```bash
sudo delgroup groupname
```

> `groupdel` is less interactive, while `delgroup` can offer additional options.

#### Modify Group Properties

- `groupmod -n new_group old_group`: Changes the name of a group.

```bash
sudo groupmod -n new_group old_group
```

- `gpasswd -a username groupname`: Adds a user to a group.

```bash
sudo gpasswd -a username groupname
```

- `gpasswd -d username groupname`: Removes a user from a group.

```bash
sudo gpasswd -d username groupname
```

## Related Files

- **/etc/passwd**: File that contains information about users, such as their name, UID, GID, and home directory.
- **/etc/shadow**: File that contains information about user passwords and expiration policies.
- **/etc/group**: File that contains information about groups and their members.

---

- [Previous](./4-permissions.md)
- [Next](./6-processes.md)