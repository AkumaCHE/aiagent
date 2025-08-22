import os
from google import genai
from dotenv import load_dotenv
import sys
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions
from functions.get_files_info import schema_get_files_info
from call_function import call_function


def generate_content(client, messages):
    #print("generate content function accessed")
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )


    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    return response, prompt_tokens, response_tokens



def main():
    #print("Hello from aiagent!")
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Enter query to chatbot")
    parser.add_argument("--verbose", action="store_true", help="increase output text")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=args.prompt)]),
]
    iteration_count = 0
    while iteration_count <20:
        iteration_count += 1
        try:
            response, prompt_tokens, response_tokens = generate_content(client, messages)
        except Exception as e:
            print(f"Error: {e}")
            break
        
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if args.verbose:
            print(f"User prompt: {args.prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")  

        if not response.function_calls:
            print("Final Response:")
            print(response.text) 
            break


        function_responses = []  # Create a list to collect the results

        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, args.verbose)

            if not function_call_result.parts[0].function_response.response:
                raise Exception("Fatal Error")
            

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")


            # Add this result to our collection
            function_responses.append(function_call_result.parts[0])

        # After the loop, add all function results to messages
        messages.append(types.Content(role="user", parts=function_responses))



if __name__ == "__main__":
    main()

