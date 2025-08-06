#from dir name.filename import function name
from functions.get_file_content import get_file_content

if __name__ == "__main__":
    result = get_file_content("calculator", "main.py")
    print(f"Result for current directory:\n{result}")

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Result for 'pkg/calculator.py' directory:\n{result}")

    result = get_file_content("calculator", "/bin/cat")
    print(f"Result for '/bin/cat' directory:\n{result}")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for 'pkg/does_not_exist.py' directory:\n{result}")