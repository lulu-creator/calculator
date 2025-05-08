import re

def evaluate(expression):
    # Remove whitespace
    expression = expression.replace(" ", "")
    # Use regex to split the expression into tokens (numbers and operators)
    tokens = re.findall(r'(\d+|[+\-*/])', expression)
    if not tokens:
        return "Invalid expression"
    
    # Convert tokens to a list of numbers and operators
    values = []
    operators = []
    for token in tokens:
        if token.isdigit():
            values.append(float(token))
        else:
            operators.append(token)
    
    # Evaluate the expression
    if len(values) != len(operators) + 1:
        return "Invalid expression"
    
    result = values[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += values[i + 1]
        elif operators[i] == '-':
            result -= values[i + 1]
        elif operators[i] == '*':
            result *= values[i + 1]
        elif operators[i] == '/':
            if values[i + 1] == 0:
                return "Division by zero"
            result /= values[i + 1]
        else:
            return "Invalid operator"
    
    return result

def main():
    print("Welcome to the Command-Line Calculator!")
    print("Enter an expression (e.g., 2 + 3 * 4) or 'exit' to quit.")
    
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = evaluate(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main() 