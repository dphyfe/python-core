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
