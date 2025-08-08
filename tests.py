#from dir name.filename import function name
from functions.run_python import run_python_file

if __name__ == "__main__":
    result = run_python_file("calculator", "main.py")
    print(f"Result for run file main.py file:\n{result}")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Result for run file 'main.py' and args file:\n{result}")

    result = run_python_file("calculator", "tests.py")
    print(f"Result for run file 'tests.py' file:\n{result}")

    result = run_python_file("calculator", "../main.py")
    print(f"Result for run file '../main.py' file:\n{result}")

    result = run_python_file("calculator", "nonexistent.py")
    print(f"Result for run file 'nonexistent.py' file:\n{result}")