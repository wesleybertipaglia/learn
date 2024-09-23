# Linux Monitoring

Linux monitoring is essential to track system performance, resource utilization, and detect problems before they become critical. Here are some important tools and techniques for monitoring your system.

## Basic Concepts

- **System Performance**: Measuring CPU, memory, disk, and network utilization.
- **Logs**: Files that record system events and messages, useful for diagnosing problems.
- **Processes**: Running instances of programs that consume system resources.

## Monitoring Tools

### CPU and Memory Usage

- **`top`**: Displays real-time processes and resource usage.
- Show `top`:
```bash
top
```

- **`htop`**: Interactive and visual version of `top` (may need to be installed).
- Display `htop`:
```bash
htop
```

- **`vmstat`**: Displays information about memory, processes, and system activity.
- Display memory and system information:
```bash
vmstat 1
```

- **`free`**: Displays information about system memory.
- Display memory usage:
```bash
free -h
```

### Disk Usage

- **`df`**: Displays file system usage.
- Display disk usage:
```bash
df -h
```

- **`du`**: Displays disk usage by files and directories.
- Display disk usage by directory:
```bash
du -sh /path/to/directory
```

### Network Usage

- **`ifstat`**: Displays network usage statistics. - Display network statistics:
```bash
ifstat
```

- **`nload`**: Monitors network traffic in real time.
- Display `nload`:
```bash
nload
```

- **`sar`**: Collects, reports, and saves information about system activity (part of the `sysstat` package).
- Display CPU statistics:
```bash
sar -u 1 3
```

### Log Monitoring

- **`tail`**: Displays the last lines of log files.
- Displays the last lines of the system log:
```bash
tail -f /var/log/syslog
```

- **`grep`**: Searches for text in log files.
- Search for error messages in the system log:
```bash
grep "error" /var/log/syslog
```

- **`logwatch`**: Tool for analyzing and reporting system logs.
- Display log reports:
```bash
logwatch
```

### Process Monitoring

- **`ps`**: Displays information about running processes.
- Display all processes:
```bash
ps aux
```

- **`pstree`**: Displays a tree of running processes.
- Display process tree:
```bash
pstree
```

- **`pidstat`**: Displays statistics about processes.
- Display process statistics:
```bash
pidstat 1
```

### Resource Monitoring

- **`nmap`**: Tool for exploring networks and services, and checking open ports. - Scan ports on a host:
```bash
nmap -p 1-65535 192.168.1.1
```

- **`iotop`**: Monitors disk I/O usage by processes (may need to be installed).
- Display disk I/O usage:
```bash
iotop
```

- **`dstat`**: Flexible replacement for `vmstat`, `iostat`, `netstat`, and `ifstat`.
- Display resource statistics:
```bash
dstat
```

### Service Monitoring

- **`systemctl`**: Manages services and units in systemd.
- Check the status of a service:
```bash
systemctl status service_name
```

- **`service`**: Tool for starting, stopping, and managing services (on systems that use `init`).
- Check the status of a service:
```bash
service service_name status
```

---

- [Previous](./8-security.md)
- [Next](./10-script.md)
