# Shell Script in Linux

Shell scripts are text files that contain Linux shell commands. They allow you to automate repetitive tasks and execute commands sequentially. Shell scripts are widely used for system administration, file processing, and more.

## Basic Concepts

- **Shell**: Command-line interface that interprets and executes commands. Examples include `bash`, `sh`, `zsh`.
- **Script**: Text file containing a series of commands that the shell executes in order.

## Creating a Shell Script

1. **Creating the File**

Create a file with the `.sh` extension (optional, but recommended).
```bash
touch script.sh
```

2. **Execution Permissions**

Make the file executable.
```bash
chmod +x script.sh
```

3. **Specify the Interpreter**

Add a shebang line to the beginning of the file to specify the shell interpreter.
- For `bash`:
```bash
#!/bin/bash
```
- For `sh`:
```bash
#!/bin/sh
```

## Basic Structure

```bash
#!/bin/bash

# Comment: This is an example shell script
echo "Hello, World!"

# Defining variables
name="User"
echo "Welcome, $name!"

# Reading user input
read -p "Enter your name: " name
echo "Hello, $name!"

# Conditional Structures
if [ "$name" == "Admin" ]; then
echo "Hello, Administrator!"
else
echo "Hello, $name!"
fi

# Loops
for i in {1..5}; do
echo "Number: $i"
done

# Functions
function greeting {
echo "Hello, $1!"
}
greeting "World"
```

## Common Commands and Structures
### Comments

Comments are preceded by #.

```bash
# This is a comment
```

### Variables

Define variables without spaces around the = and access them using $.
```bash
variable="value"
echo $variable
```

### Input and Output

```bash
echo "Text" # display text
read variable # read user input
```

### Conditionals

```bash
if [ condition ]; then command fi
```

### Loops

```bash
for variable in list;
do command done
```

```bash
while [ condition ];
do command done
```

### Functions

```bash
function function_name {
command
}
function_name
```

### File Manipulation

```bash
touch file.txt
nano file.txt
```

```bash
cat file.txt # read
echo "Text" > file.txt # write
echo "Additional text" >> file.txt # append
```
### Debugging
```bash
bash -x script.sh
```

---

- [Previous](./9-monitoring.md)