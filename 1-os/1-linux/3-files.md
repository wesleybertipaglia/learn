# Linux File System

The Linux file system organizes and manages files and directories on the system. Here are some of the main concepts and components:

## Types

- **Ext4**: The default file system for many Linux distributions, known for its stability and performance.
- **XFS**: Designed for high performance and scalability.
- **Btrfs**: Provides advanced features such as snapshots and integrity control.
- **FAT32**: Commonly used on removable devices and supported by many operating systems.

## Basic Structure

- **Root**: The main directory of the system, represented by `/`.
- **Main Directories**:
- `/bin` - Contains essential binaries for the system.
- `/boot` - Initialization files, such as the kernel.
- `/dev` - Device files.
- `/etc` - System configuration files.
- `/home` - Users' home directories.
- `/lib` - Essential system libraries and binaries.
- `/media` - Mount points for removable devices.
- `/mnt` - Mount points for temporary file systems.
- `/opt` - Optional software and additional packages.
- `/proc` - Virtual file system that provides information about the kernel and processes.
- `/root` - Home directory of the superuser (root).
- `/sbin` - Binaries essential for system administration.
- `/srv` - Data about services provided by the system.
- `/sys` - Virtual file system that exposes kernel information and configuration.
- `/tmp` - Temporary files.
- `/usr` - User data and applications, such as binaries, libraries, and documentation.
- `/var` - Variable data, such as logs and caches.

## Mounting and Unmounting

- **Mounting**: The process of making a file system accessible at a mount point. Using the `mount` command:
```bash
mount /dev/sdXn /mount/point
```

- **Unmounting**: The process of removing the file system from the mount point. Using the umount command:
```bash
umount /mount/point
```
---

- [Previous](./2-commands.md)
- [Next](./4-permissions.md)