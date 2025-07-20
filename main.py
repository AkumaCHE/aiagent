import os
from google import genai
from dotenv import load_dotenv
import sys
from google.genai import types
import argparse

def generate_content(client, messages):
    print("generate content accessed")
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages,
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
    
    response, prompt_tokens, response_tokens = generate_content(client, messages)

    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")  

    print(response.text) 


if __name__ == "__main__":
    main()

