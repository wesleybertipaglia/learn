import os

path = "/path/"

# Get the current working directory
os.getcwd()

# Change the current working directory
os.chdir(path)

# List the contents of a directory
os.listdir(path)

# Create a directory
os.mkdir(path)

# Remove a directory
os.rmdir(path)

# Rename a file or directory
os.rename("/src/", "/dst/")

# Check if a path exists
os.path.exists(path)

# Check if a path is a directory
os.path.isdir(path)

# Check if a path is a file
os.path.isfile(path)

# Join two or more path components
os.path.join("/path1/", "/path2/")

# Get the basename of a path
os.path.basename(path)

# Get the directory name of a path
os.path.dirname(path)

# Split the extension from a path
os.path.splitext(path)

# Get the size of a file
os.path.getsize(path)

# Get information about a file
os.stat(path)

# Execute a shell command
os.system("sudo apt update & sudo apt upgrade -y")

# Get the value of an environment variable
os.getenv("HOST")

# Set an environment variable
os.putenv("PORT", 8080)