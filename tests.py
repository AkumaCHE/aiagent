#from dir name.filename import function name
from functions.write_file import write_file

if __name__ == "__main__":
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result for write file lorem.txt file:\n{result}")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result for write file 'pkg/morelorem.txt' file:\n{result}")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result for write file '/tmp/temp.txt' file:\n{result}")

