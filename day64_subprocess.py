# Day 64: subprocess for my practice

import subprocess

my_result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
print(f"My stdout: {my_result.stdout}")
print(f"My returncode: {my_result.returncode}")

try:
    my_output = subprocess.check_output(["echo", "My test"], text=True)
    print(f"My check_output: {my_output.strip()}")
except subprocess.CalledProcessError as e:
    print(f"My error: {e}")

my_process = subprocess.Popen(["echo", "My popen"], stdout=subprocess.PIPE, text=True)
my_stdout, my_stderr = my_process.communicate()
print(f"My popen output: {my_stdout.strip()}")

my_result2 = subprocess.run(["python", "--version"], capture_output=True, text=True)
print(f"My python version: {my_result2.stdout.strip() or my_result2.stderr.strip()}")

my_result3 = subprocess.run(
    ["python", "-c", "print('My inline')"],
    capture_output=True,
    text=True
)
print(f"My inline output: {my_result3.stdout.strip()}")

try:
    my_timeout = subprocess.run(
        ["python", "-c", "import time; time.sleep(0.1)"],
        timeout=1,
        capture_output=True
    )
    print("My timeout succeeded")
except subprocess.TimeoutExpired:
    print("My command timed out")

my_env = {"MY_VAR": "my_value"}
my_result4 = subprocess.run(
    ["python", "-c", "import os; print(os.environ.get('MY_VAR', 'not found'))"],
    capture_output=True,
    text=True,
    env=my_env
)
print(f"My env result: {my_result4.stdout.strip()}")

my_result5 = subprocess.run(["echo", "test"], shell=False, capture_output=True, text=True)
print(f"My no shell: {my_result5.stdout.strip()}")

print("My subprocess examples complete")

# Progress: part 2/2
