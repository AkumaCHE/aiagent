from google.genai import types

def simple_calculator(expression):
    """Safely evaluate simple math expressions"""
    try:
        # Only allow safe math operations
        allowed_chars = set('0123456789+-*/().')
        if not all(c in allowed_chars or c.isspace() for c in expression):
            return "Error: Only basic math operations allowed"
        
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error calculating: {e}"

schema_simple_calculator = types.FunctionDeclaration(
    name="simple_calculator",
    description="Performs basic math calculations like addition, subtraction, multiplication, division",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "expression": types.Schema(
                type=types.Type.STRING,
                description="The math expression to calculate, like '15 * 23 + 7'",
            ),
        },
        required=["expression"],
    ),
)