# Day 72: pip and packages for my practice

import subprocess
import sys

def my_run_pip(args):
    """My helper to run pip commands"""
    my_result = subprocess.run(
        [sys.executable, "-m", "pip"] + args,
        capture_output=True,
        text=True
    )
    return my_result.stdout, my_result.stderr

my_stdout, my_stderr = my_run_pip(["--version"])
print(f"My pip version: {my_stdout.strip()}")

print("\nMy common pip commands:")
print("  pip install package_name")
print("  pip install package==1.0.0")
print("  pip install package>=1.0.0")
print("  pip install -r requirements.txt")
print("  pip uninstall package_name")
print("  pip list")
print("  pip show package_name")
print("  pip freeze")
print("  pip freeze > requirements.txt")
print("  pip install --upgrade package_name")

my_example_requirements = """# My requirements.txt example
requests==2.28.0
flask>=2.0.0

# Progress: part 2/5
