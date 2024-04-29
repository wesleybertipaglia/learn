import platform

# Get the Python version
platform.python_version()

# Get the Python implementation (e.g., 'CPython', 'Jython', 'IronPython', 'PyPy')
platform.python_implementation()

# Get the system's architecture (e.g., '32bit', '64bit', 'arm64')
platform.architecture()

# Get the system's platform (e.g., 'Windows', 'Linux', 'Darwin' for macOS)
platform.system()

# Get the system's release version
platform.release()

# Get the system's node name (e.g., computer's network name)
platform.node()

# Get the system's machine type (e.g., 'x86_64', 'i386')
platform.machine()

# Get the system's processor (e.g., 'Intel(R) Core(TM) i7 CPU', 'ARMv8 Processor')
platform.processor()

# Get a concise system summary as a string
platform.platform()