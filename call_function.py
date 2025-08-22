from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file
from google.genai import types 
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from functions.simple_calculator import simple_calculator, schema_simple_calculator


function_map = {
    'get_file_content': get_file_content,
    'get_files_info': get_files_info,
    'run_python_file': run_python_file,
    'write_file': write_file,
    'simple_calculator': simple_calculator
}

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file, 
        schema_write_file,
        schema_simple_calculator,
    ]
)


def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
 
    if verbose == False:
        print(f" - Calling function: {function_call_part.name}")


    if function_call_part.name not in function_map.keys():
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name, 
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    
    # Convert args to a regular dict
    args = dict(function_call_part.args)
    
    # Only add working_directory to functions that need it
    if function_call_part.name != "simple_calculator":
        args["working_directory"] = "./calculator"
    
    result = function_map[function_call_part.name](**args) 
    

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )        
