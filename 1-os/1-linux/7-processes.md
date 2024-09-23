# Linux Processes

In Linux, a process is a running instance of a program. Process management is crucial to the operation of the system and to the execution of programs.

## Basic Concepts

- **Process**: A running instance of a program. It includes executable code, data, and execution context.
- **PID (Process ID)**: Unique identifier for each process.
- **PPID (Parent Process ID)**: Identifier of the parent process that created the current process.
- **TID (Thread ID)**: Unique identifier for a thread within a process (on systems that support threads).

## Process States

Processes can be in several states:
- **Running (R)**: Running or ready to run.
- **Sleeping (S)**: Waiting for an event or resource.
- **Stopped (T)**: Stopped, usually by a signal. - **Zombie (Z)**: Terminated, but still has an entry in the process table, waiting for the parent process to collect its status.

## Important Commands

### Process Viewing

- **`ps`**: Displays a list of running processes.
- `ps aux` - Displays all running processes in detail.
- `ps -ef` - Another way to display all processes with additional information.

- **`top`**: Displays a dynamic list of processes in real time.
```bash
top
```

- **`htop`**: A more interactive and visual version of `top`. May need to be installed separately.
```bash
htop
```

- **`pgrep`**: Searches for processes based on criteria.
```bash
pgrep process_name
```

### Process Management

- **`kill`**: Sends a signal to a process.
- To terminate a process:
```bash
kill PID
```
- To send a forced termination signal:
```bash
kill -9 PID
```

- **`killall`**: Sends signals to all processes with a specific name.
```bash
killall process_name
```

- **`nice`**: Runs a command with an adjusted priority.
- To run a command with a lower priority:
```bash
nice -n 10 command
```

- **`renice`**: Adjusts the priority of a running process.
- To increase the priority (decrease the value):
```bash
renice -n -5 -p PID
```

### Process Creation and Manipulation

- **`fork`**: System call that creates a new process (child) from the current process (parent).
- **`exec`**: Replaces the current process image with a new image (executes a new program).
- **`wait`**: Causes a parent process to wait for a child process to finish.

### Background Processes

- **`&`**: Executes a command in the background.
```bash
command &
```

- **`jobs`**: Lists the background processes of the current user.
```bash
jobs
```

- **`fg`**: Moves a process from the background to the foreground.
```bash
fg %n
```

- **`bg`**: Resumes a suspended process and makes it run in the background.
```bash
bg %n
```

## Related Files

- **/proc/[PID]/**: Directory containing information about the process with the specific PID, such as status, memory, and open files.
- **/etc/init.d/**: Directory containing service startup scripts.
- **/etc/crontab**: Configuration file for scheduling tasks.

---

- [Previous](./5-users.md)
- [Next](./7-networking.md)
