# Linux Fundamentals

## 1. Kernel, Shell, and Graphical Environment

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

### Graphical Environment
- The graphical environment provides a visual interface for interacting with the operating system, similar to what you see on a Windows or Mac desktop.
- Includes elements such as windows, icons, menus, and toolbars.
- Examples of Graphical Environments: GNOME, KDE Plasma, XFCE, LXDE.

## 2. Main Distributions

### Popular Distributions
- **Ubuntu**: Known for its ease of use and long-term support (LTS).
- **Debian**: Famous for its stability and vast package base.
- **Fedora**: Offers the latest innovations and technologies.
- **CentOS / Rocky Linux**: Derivatives of Red Hat Enterprise Linux, focused on servers and stability.
- **Arch Linux**: Focused on simplicity and control, ideal for advanced users.

## 3. File Systems
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

## 4. Basic Commands
Common commands for browsing and manipulating files in Linux:

- **`ls`**: Lists files and directories.
- **`pwd`**: Displays the path of the current directory.
- **`cd`**: Navigates between directories.
- **`cat`**, **`less`**, **`more`**: Displays the contents of files.
- **`cp`**: Copies files/directories.
- **`mv`**: Moves or renames files/directories. - **`rm`**: Removes files/directories.

## 5. Package Managers
Linux uses package management systems to install, update, and remove software. Each distro has its own package manager:

### For Debian/Ubuntu-based distributions:
- **`apt-get`** or **`apt`**: Installs, removes, and updates packages.
- `sudo apt update`: Updates the package list.
- `sudo apt upgrade`: Updates installed packages.
- `sudo apt install <package>`: Installs a package.

### For Red Hat-based distributions (Fedora/CentOS):
- **`yum`** or **`dnf`**: Manages packages on Red Hat-based distros.
- `sudo dnf install <package>`: Installs a package.
- `sudo dnf update`: Updates all packages.

### Others:
- **`pacman`**: Arch Linux package manager.
- `sudo pacman -Syu`: Synchronizes and updates the system.

## 6. File Permissions
Linux uses a permission system to control who can read, write, or execute a file.

- **`r`**: Read
- **`w`**: Write
- **`x`**: Execute

### Change permissions:
- **`chmod`**: Changes file and directory permissions.
- `chmod +x script.sh`: Gives execute permission to a file.

### Change owner/group:
- **`chown`**: Changes the owner and group of a file.
- `sudo chown user:group file`: Sets a new owner and group.

## 7. Process Management
Processes in Linux can be monitored and managed with specific commands:

- **`ps`**: Lists running processes.
- **`top`** or **`htop`**: Monitors resource usage by processes in real time.
- **`kill`**: Sends a signal to a process, usually used to terminate a process.
- `kill <PID>`: Terminates the process with the specified ID.

## 8. Networks
Linux offers robust tools for configuring and monitoring networks:

- **`ip addr`** or **`ifconfig`**: Displays network interfaces and their details.
- **`ping`**: Tests connectivity to another host.
- **`traceroute`**: Displays the path that packets take to a destination.
- **`netstat`** or **`ss`**: Checks active network connections.

## 9. Basic Shell Scripting
Automating repetitive tasks is one of Linux's strengths through scripts.

### Basic structure of a script:
```bash
#!/bin/bash
# Simple script

echo "Hello, World!"
```

- **`chmod +x script.sh`**: Makes the script executable.
- **`./script.sh`**: Runs the script.

## 10. Basic Security
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