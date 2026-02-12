import subprocess
import sys

def execute_python(filepath: str):
    result = subprocess.run(
        [sys.executable, filepath],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, result.stdout

    return False, result.stderr
