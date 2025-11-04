import subprocess

# Example 3: Using run() with streaming (Python 3.7+)
print("=== Example 3: Using subprocess.run() ===")
result = subprocess.run(
    [
        "mamba",
        "run",
        "--live-stream",
        "python",
        "-c",
        """
import time
for i in range(3):
    print(f"Run output {i}")
    time.sleep(3)
""",
    ],
    # Key: Don't capture stdout/stderr
    capture_output=False,
    text=True,
)

print(f"Process exited with code: {result.returncode}")
