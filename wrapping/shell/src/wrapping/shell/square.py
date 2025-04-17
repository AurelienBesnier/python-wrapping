import subprocess


def square(x):
    return subprocess.run(["square", f"{x}"]).returncode
