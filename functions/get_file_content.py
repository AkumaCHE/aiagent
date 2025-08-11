import os
from google.genai import types
from config import MAX_CHARS




def get_file_content(working_directory, file_path):
    #print("get file content function called")
    file_path_abs = os.path.join(working_directory, file_path)
    working_dir_abs = os.path.abspath(working_directory)
    full_file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    #print(f'working directory: {working_dir_abs}')
    #print(f'file path: {file_path_abs}')
    #print(f'full file path: {full_file_path_abs}')

    # If the file_path is outside the working_directory, return a string with an error:
    #.startswith
    if not full_file_path_abs.startswith(working_dir_abs):
        #print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # If the file_path is not a file, again, return an error string:
    if not os.path.isfile(full_file_path_abs):
        #print(f'Error: File not found or is not a regular file: "{file_path}"')
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    try:
        with open(full_file_path_abs, "r") as f:
            size_chars = os.path.getsize(full_file_path_abs)
            file_content_string = f.read(MAX_CHARS)
            
            #print(f'size is:{size_chars}')
            
            if size_chars > MAX_CHARS:
                
                
                #print(f'return file content string > 10000: {file_content_string} [...File "{file_path}" truncated at 10000 characters]')
                return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
            
            #print(f'return file content string < 10000: {file_content_string}')
            return file_content_string
    except Exception as e:
        #print(str(e))
        return f'Error: {str(e)}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns contents of file truncated to {MAX_CHARS} characters, constrained to files in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The location of the file, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)



