import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir_path = os.path.abspath(working_directory)
    full_file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    #print(f'absolute working path: {abs_working_dir_path}')
    #print(f'absolute full file path: {full_file_path_abs}')


    #If the file_path is outside the working directory, return a string with an error:
    if not full_file_path_abs.startswith(abs_working_dir_path):
        #print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
   
    #If the file_path doesn't exist, return an error string:
    if not os.path.exists(full_file_path_abs):
        #print(f'Error: File "{file_path}" not found.')
        return f'Error: File "{file_path}" not found.'
    
    if not full_file_path_abs.endswith('.py'):
        #print(f'Error: "{file_path}" is not a Python file.')
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command_list = ['python', full_file_path_abs]

        subprocess_result = subprocess.run(command_list + args,timeout=30, capture_output=True, check=True, cwd=abs_working_dir_path)

        exit_code = subprocess_result.returncode
        stdout = subprocess_result.stdout.decode('utf_8')
        stderr = subprocess_result.stderr.decode('utf_8')

        if not stdout and not stderr:
            return "No output produced."

        if exit_code != 0:
            return f"STDOUT: {stdout}\n STDERR: {stderr}\n Process exited with code {exit_code}"

        return f"STDOUT: {stdout}\n STDERR: {stderr}"
    
    except subprocess.CalledProcessError as e:
        exit_code = e.returncode
        stdout = e.stdout.decode('utf_8')
        stderr = e.stderr.decode('utf_8')

        if not stdout and not stderr:
            return "No output produced."
        
        if exit_code != 0:
            return f"STDOUT: {stdout}\n STDERR: {stderr}\n Process exited with code {exit_code}"

        return f"STDOUT: {stdout}\n STDERR: {stderr}"

    except Exception as e:
        return f'Error: executing Python file: {e}'
    

#run_python_file("calculator", "main.py")
#run_python_file("calculator", "main.py")
#run_python_file("calculator", "main.py", ["3 + 5"])
