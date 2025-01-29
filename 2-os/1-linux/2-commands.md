# Basic Commands

## Directory Commands

### Navigation
- `cd [directory]`: Changes the current directory.
    - `cd ..`: Moves up one directory.
    - `cd ~`: Moves to the home directory.
    - `cd /`: Moves to the root directory.

### Listing
- `pwd`: Shows the current directory.
- `ls`: Lists files and directories.
    - `ls -l`: Lists files and directories in long format.
    - `ls -a`: Lists all files and directories, including hidden ones.
    - `ls -lh`: Lists files and directories in long format with human-readable sizes. 

### Create and Remove
- `mkdir [directory]`: Creates a new directory.
- `rmdir [directory]`: Removes an empty directory.
- `rm -r [directory]`: Removes a directory and its contents.

### Copy and Move
- `cp -r [source] [destination]`: Copies directories and their contents.
- `mv [source] [destination]`: Moves or renames directories.

### Search and Find
- `find [path] -type d`: Finds directories.
- `locate [file]`: Finds files and directories.

## File Commands

### Show Content
- `cat [file]`: Displays the contents of a file.
- `more [file]`: Displays the contents of a file one screen at a time.
- `less [file]`: Displays the contents of a file with navigation.
- `head [file]`: Displays the first lines of a file.

### Create, Remove, and Update
- `touch [file]`: Creates a new empty file.
- `rm [file]`: Removes files.
- `nano [file]`: Opens a file in the nano text editor.
- `vi [file]`: Opens a file in the vi text editor.
- `echo [text] > [file]`: Writes text to a file (overwrites).
- `echo [text] >> [file]`: Appends text to a file.

### Copy and Move
- `cp [source] [destination]`: Copies files and directories.
- `mv [source] [destination]`: Moves or renames files and directories.

### Search and Find
- `grep [pattern] [file]`: Searches for a pattern in a file.
- `find [path] -name [name]`: Finds files with a specific name.

## Permissions Commands
- `chmod [permissions] [file]`: Changes file permissions.
- `chown [user:group] [file]`: Changes the owner and group of files.
- `chgrp [group] [file]`: Changes the group of files.

## Process Commands

### Monitoring
- `ps`: Lists running processes.
    - `ps aux`: Lists all processes.
    - `ps -ef`: Lists all processes in full format.
- `top`: Shows processes in real time.
- `htop`: Shows processes in real time in an interactive way with some additional features.
- `pgrep [name]`: Lists processes by name.

### Management
- `kill [PID]`: Kills a process.
    - `kill -9 [PID]`: Forces a process to stop.
- `killall [name]`: Kills all processes with a specific name.
- `pkill [name]`: Kills processes by name.

## Network Commands

### Testing and Troubleshooting
- `ping [host]`: Checks connectivity to a host.
- `traceroute [host]`: Shows the route packets take to reach a host.
- `nslookup [host]`: Queries DNS servers for information about a host.
- `dig [host]`: Queries DNS servers for information about a host.
- `tcpdump`: Captures and analyzes network traffic.
- `nmap [host]`: Scans ports and services on a host.

### Network Configuration
- `ifconfig`: Displays information about network interfaces.
- `netstat`: Displays information about network connections.
- `ip`: Displays and modifies network interfaces.

### Remote Access
- `ssh [user@host]`: Connects to a remote host via SSH.
- `scp [file] [user@host:directory]`: Copies files to a remote host via SSH.
- `sftp [user@host]`: Transfers files to a remote host via SSH.
- `rsync [source] [destination]`: Syncs files and directories between systems.

### Tools
- `wget [URL]`: Downloads files from the web.
- `curl [URL]`: Transfers data from or to a server.

--- 

- [Previous](./1-fundamentals.md)
- [Next](./3-files.md)