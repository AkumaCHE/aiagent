import os
from google.genai import types

def write_file(working_directory, file_path, content):
    #print(f'write_file func called')
    #print(f'input working dir = {working_directory}')
    abs_working_dir_path = os.path.abspath(working_directory)
    #print(f'absolute working path: {abs_working_dir_path}')
    full_file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_file_path_abs.startswith(abs_working_dir_path):
        #print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    new_directory_path = os.path.dirname(full_file_path_abs)
    if not os.path.exists(new_directory_path):
        
        print(f"directory_path is: {new_directory_path}")
        try:
            os.makedirs(new_directory_path, exist_ok=True)
            
        
        except Exception as e:
            print(str(e))
            return f'Error: {str(e)}'
        

    with open(full_file_path_abs, "w") as f:
        f.write(content)

    #print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes content to a file, constrained to files in the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The location of the file, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is to be written to the file",
            ),
        },
        required=["file_path", "content"],
    ),

)

