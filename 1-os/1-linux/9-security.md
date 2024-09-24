# Linux Security

Linux security involves protecting the system from unauthorized access, threats, and vulnerabilities. Here are some essential concepts and practices for maintaining a secure Linux system.

## Basic Concepts

- **File Permissions**: Control access to files and directories based on read, write, and execute permissions for the owner, group, and others.
- **Sudo**: Allows authorized users to execute commands as the superuser or another user.
- **Firewall**: System that controls network traffic, allowing or blocking packets based on security rules.
- **SELinux/AppArmor**: Security modules that provide policy-based access control to protect the system.

## Security Practices

### User and Group Management

- **Use `sudo` with Caution**: Grant elevated privileges only when necessary and avoid using `root` directly. - Add a user to the `sudo` group:
```bash
sudo usermod -aG sudo username
```

- **Disable Inactive Accounts**: Remove or disable user accounts that are no longer in use.
- To disable an account:
```bash
sudo usermod -L username
```

- **Manage Passwords Securely**: Use strong passwords and set expiration policies.
- Change a user's password:
```bash
sudo passwd username
```

### Access Control

- **File Permissions**: Set appropriate permissions for files and directories. - Change permissions:
```bash
chmod 700 file
```
- Change ownership:
```bash
chown user:group file
```

- **Use `umask`**: Set the file creation mask to ensure default secure permissions.
- Set `umask`:
```bash
umask 027
```

### Network Security

- **Configure a Firewall**: Use `iptables` or `nftables` to manage firewall rules. - Example of configuration with `iptables`:
```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -j DROP
```
- Example of configuration with `nftables`:
```bash
sudo nft add rule ip filter input tcp dport 22 accept
sudo nft add rule ip filter input drop
```

- **Use Intrusion Detection Tools**: Tools like `fail2ban` can block IPs with repeated login attempts.
- Install and configure `fail2ban`:
```bash
sudo apt-get install fail2ban
```

### System Security

- **Update Regularly**: Keep your system and packages up to date to protect against known vulnerabilities.
- Update the system:
```bash
sudo apt-get update
sudo apt-get upgrade
```

- **Check Logs**: Monitor system logs for suspicious activity.
- View system logs:
```bash
sudo less /var/log/syslog
sudo less /var/log/auth.log
```

- **Use SELinux or AppArmor**: Configure SELinux or AppArmor to enforce additional security policies.
- Check SELinux status:
```bash
sestatus
```
- Enable/AppArmor:
```bash
sudo systemctl enable apparmor
sudo systemctl start apparmor
```

### Backup and Recovery

- **Perform Regular Backups**: Perform frequent backups of important data to ensure recovery in case of failures or attacks. - Example of backup using `rsync`:
```bash
rsync -av /home/username /backup/home/
```

- **Test Recovery Plans**: Ensure that your backups are functional and test data recovery regularly.

## Security Tools

- **`chkrootkit`**: Checks for the presence of rootkits on the system.
- Install and run:
```bash
sudo apt-get install chkrootkit
sudo chkrootkit
```

- **`rkhunter`**: Checks for the presence of rootkits and malware.
- Install and run:
```bash
sudo apt-get install rkhunter
sudo rkhunter --check
```

---

- [Previous](./8-networking.md)
- [Next](./10-monitoring.md)
