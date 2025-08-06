import os

working_directory = "/calculator"

def get_files_info(working_directory, directory="."):
    #print(f"function called: get_files_info")
    #join 2 paths together
    full_path = os.path.join(working_directory, directory)
    working_dir_abs = os.path.abspath(working_directory)
    full_path_abs = os.path.abspath(os.path.join(working_directory, directory))

    #print("DEBUG working_directory:", working_directory)
    #print("DEBUG directory:", directory)
    #print("DEBUG full_path:", full_path)
    #print("DEBUG working_dir_abs:", working_dir_abs)
    #print("DEBUG full_path_abs:", full_path_abs)

    if not full_path_abs.startswith(working_dir_abs):
    # return an error about being outside permitted directory
        #print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path_abs):
    # If the directory argument is not a directory, again, return an error string
        #print(f'Error: "{directory}" is not a directory')
        return f'Error: "{directory}" is not a directory'
    
    #Build and return a string representing the contents of the directory. It should use this format

    #for item in dir_contents:
        #print(f"what item is it: {item}")
        #print(f"full path including directory item: {full_path_abs}/{item}")
        #size = os.path.getsize(f"{full_path_abs}/{item}")
        #print(f"size: {size}")
        #is_dir = os.path.isdir(f"{full_path_abs}/{item}")
        #print(f"is it a directory: {is_dir}")
        #print(f"{item}: file_size={size} bytes, is_dir={is_dir}")

#Build and return a string representing the contents of the directory. It should use this format
    try:
        dir_contents = os.listdir(full_path_abs)
        #print(f"directory contents: {dir_contents}")
        results = []
        for item in dir_contents:
            item_path = os.path.join(full_path_abs, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            results.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        #print(results)
        return "\n".join(results)
    except Exception as e:
        #print(str(e))
        return f'Error: {str(e)}'


    


#get_files_info("calculator", "main.py")      # should return an error about not being a directory
#get_files_info("calculator", "/bin")         # should return an error about being outside permitted directory
#get_files_info("calculator", ".")            # should return the contents of 'calculator'
