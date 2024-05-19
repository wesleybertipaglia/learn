import shutil

# Copy a file from source to destination
shutil.copy("/path/", "/dest/path/")

# Copy a file and its permissions from source to destination
shutil.copy2("/path/", "/dest/path/")

# Copy a file, preserving symlinks from source to destination
shutil.copyfile("/path/", "/dest/path/")

# Copy permissions, last access time, and last modification time from source to destination
shutil.copystat("/path/", "/dest/path/")

# Recursively copy a directory and its contents to another location
shutil.copytree("/path/", "/dest/path/")

# Move a file or directory to another location
shutil.move("/path/", "/dest/path/")

# Remove a directory and its contents recursively
shutil.rmtree("/path/")

# Create a zip archive of a directory and its contents
shutil.make_archive("test", format, root_dir=None, base_dir=None)

# Extract all files from a zip archive
shutil.unpack_archive("test", extract_dir=None, format=None)

# Change the owner and group of a file or directory
shutil.chown("/path/", user=None, group=None)

# Change the permissions of a file or directory
shutil.chmod("/path/", 0664)

# Get statistics about a file or directory
shutil.stat("/path/")

# Get the size of a file or directory
shutil.disk_usage("/path/")