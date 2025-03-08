import os
import platform
import socket
import sys

# System Information
print(f"Machine Type: {platform.machine()}")
print(f"Processor Type: {platform.processor()}")
socket.setdefaulttimeout(50)
print(f"Default socket timeout: {socket.getdefaulttimeout()} seconds")
print(f"Operating System: {os.name}")
print(f"Current Process ID: {os.getpid()}")

# File Writing with os module
file_path = "fdpractice.txt"
fd = os.open(file_path, os.O_RDWR | os.O_CREAT)
os.write(fd, b"Some string to write to the file")
os.lseek(fd, 0, 0)  # Move pointer to beginning

# Process forking (Unix only)
try:
    pid = os.fork()
    if pid == 0:
        print(f"Child Process ID: {os.getpid()}")
        content = os.read(fd, 100).decode()
        print("File Content in Child Process:", content)
        os.close(fd)
        sys.exit(0)
    else:
        print(f"Parent Process ID: {os.getpid()}")
        os.wait()
        os.close(fd)
except AttributeError:
    print("Fork is not available on this operating system (e.g., Windows). Using multiprocessing instead.")
    import multiprocessing as mp

    def child_process():
        print(f"Child Process ID: {os.getpid()}")
        content = os.read(fd, 100).decode()
        print("File Content in Child Process:", content)
        os.close(fd)

    context = mp.get_context('spawn')
    p = context.Process(target=child_process)
    p.start()
    p.join()
