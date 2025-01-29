# Linux Fundamentals

## 1. Basic Concepts

### Kernel
- The kernel is the core of the Linux operating system.
- Manages hardware and provides essential services for programs.
- Responsible for tasks such as memory management, processes, and device control.

### Shell
- The shell is the interface between the user and the kernel.
- Allows the execution of commands and scripts.
- There are several types of shells, including:
- **Bash (Bourne Again Shell)**: The most common.
- **Zsh (Z Shell)**: Offers advanced features and customizations.
- **Fish (Friendly Interactive Shell)**: Focused on usability and auto-completion.

### Desktop Environment
- Provides a visual interface for interacting with the operating system, similar to what you see on a Windows or Mac desktop.
- Includes elements such as windows, icons, menus, and toolbars.
- Examples: 
    - GNOME
    - KDE Plasma
    - XFCE
    - LXDE

### Distributions

- A Linux distribution (distro) is a complete operating system based on the Linux kernel.
- Combines the Linux kernel, system utilities, libraries, graphical environment, and software applications.
- Distributions can be tailored for different purposes, such as desktops, servers, or embedded systems.
- Examples: 
    - Ubuntu
    - Debian
    - Fedora
    - Linux Mint
    - Arch Linux    

### Flavors

- Flavors are variations of a distribution that come with different desktop environments or software configurations.
- Flavors allow users to choose the environment that best suits their needs.
- They often come with pre-installed software and configurations tailored to the desktop environment.
- For example, Ubuntu has official flavors like:
    - Kubuntu (KDE Plasma)
    - Xubuntu (XFCE)
    - Lubuntu (LXQt)

## 2. File Systems
The Linux file system organizes data and files in a hierarchical structure, where everything is represented as a file (including devices).

### Main directories:
- **/**: Root directory, where everything begins.
- **/home**: User directory.
- **/etc**: Configuration files.
- **/var**: Variable files, such as logs and cache.
- **/usr**: System programs and utilities.

### File system types:
- **ext4**: The most widely used in Linux distributions.
- **xfs**: Commonly used in servers for its scalability.
- **btrfs**: Advanced system with support for snapshots and self-healing.

## 3. Basic Commands
Common commands for browsing and manipulating files in Linux:

- **`ls`**: Lists files and directories.
- **`pwd`**: Displays the path of the current directory.
- **`cd`**: Navigates between directories.
- **`cat`**, **`less`**, **`more`**: Displays the contents of files.
- **`cp`**: Copies files/directories.
- **`mv`**: Moves or renames files/directories. 
- **`rm`**: Removes files/directories.

## 4. Package Managers
Linux uses package management systems to install, update, and remove software. Each distro has its own package manager:

### APT (Debian/Ubuntu):
- `sudo apt update`: Updates the package list.
- `sudo apt upgrade`: Updates installed packages.
- `sudo apt install <package>`: Installs a package.
- `sudo apt remove <package>`: Removes a package.

### Others:
- `pacman`: Arch Linux package manager.
- `dnf`: Fedora package manager.
- `zypper`: openSUSE package manager.
- `emerge`: Gentoo package manager.
- `apk`: Alpine Linux package manager.
- `dpkg`: Low-level package manager for Debian-based systems.
- `snap`: Universal package manager for multiple distros.
- `flatpak`: Universal package manager for multiple distros.

## 5. File Permissions
Linux uses a permission system to control who can read, write, or execute a file.

- `r` (4): Read
- `w` (2): Write
- `x` (1): Execute

### Change permissions `chmod`:

- **`chmod +x file`**: Adds execute permission.
- **`chmod -w file`**: Removes write permission.
- **`chmod u=rwx file`**: Sets user permissions to read, write, and execute.

Add, Remove or Set permissions with numbers:

- **`chmod 755 file`**: Sets permissions to `rwxr-xr-x`.
- **`chmod 644 file`**: Sets permissions to `rw-r--r--`.

### Change owner/group:
- **`chown`**: Changes the owner and group of a file.
- `sudo chown user:group file`: Sets a new owner and group.

## 6. Process Management
Processes in Linux can be monitored and managed with specific commands:

- **`ps`**: Lists running processes.
- **`top`** or **`htop`**: Monitors resource usage by processes in real time.
- **`kill`**: Sends a signal to a process, usually used to terminate a process.
- `kill <PID>`: Terminates the process with the specified ID.

## 7. Networks
Linux offers robust tools for configuring and monitoring networks:

- **`ip addr`** or **`ifconfig`**: Displays network interfaces and their details.
- **`ping`**: Tests connectivity to another host.
- **`traceroute`**: Displays the path that packets take to a destination.
- **`netstat`** or **`ss`**: Checks active network connections.

## 8. Basic Shell Scripting
Automating repetitive tasks is one of Linux's strengths through scripts.

### Basic structure of a script:
```bash
#!/bin/bash
# Simple script

echo "Hello, World!"
```

- **`chmod +x script.sh`**: Makes the script executable.
- **`./script.sh`**: Runs the script.

## 9. Basic Security
Common security tools and practices in Linux:

- **`ufw`**: Configures the firewall in a simplified way (Ubuntu).
- **`iptables`**: Manages firewall rules.
- **`selinux`**: Mandatory access control tool in distros such as CentOS and Fedora.
- **`ssh`**: Secure remote access protocol.
- **`fail2ban`**: Protects against brute-force attacks by blocking IP addresses.
- **`sudo`**: Allows users to run commands with administrative privileges.
- **`gpg`**: Encrypts and signs data and communications.

---

- [Next](./2-commands.md)