import math  # Standard PEP 8 placement for imports


def calculate(user_input):
    user_input = user_input.replace(" ", "")  # Remove spaces from the input

    # Addition function
    if "+" in user_input: 
        parts = user_input.split("+") 
        total = float(parts[0])  # Start with the first number, not 0
        for piece in parts[1:]:  # Loop over everything EXCEPT the first piece
            total += float(piece)  
        return round(total, 2)  # Round the result to 2 decimal places

    # Subtraction function
    elif "-" in user_input:  
        parts = user_input.split("-") 
        total = float(parts[0])  # Start with the first number, not 0
        for piece in parts[1:]:  # Loop over everything EXCEPT the first piece
            total -= float(piece) 
        return round(total, 2) 

    # Multiplication function
    elif "*" in user_input: 
        parts = user_input.split("*")  
        total = float(parts[0]) 
        for piece in parts[1:]: 
            total *= float(piece) 
        return round(total, 2) 

    # Division functions
    elif "/" in user_input: 
        parts = user_input.split("/")  
        total = float(parts[0]) 
        for piece in parts[1:]: 
            if float(piece) == 0: 
                return "Error: Division by zero is not allowed." 
            total /= float(piece) 
        return round(total, 2) 

    # Exponentiation function
    elif "^" in user_input: 
        parts = user_input.split("^") 
        total = float(parts[0]) 
        for piece in parts[1:]: 
            total **= float(piece) 
        return round(total, 2) 

    # Modulus function
    elif "%" in user_input: 
        parts = user_input.split("%") 
        total = float(parts[0]) 
        for piece in parts[1:]: 
            total %= float(piece) 
        return round(total, 2) 

    # Square root function
    elif "sqrt" in user_input: 
        parts = user_input.split("sqrt")  
        total = float(parts[1]) 
        if total < 0:  
            return (
                "Error: Cannot calculate the square root of a negative number."  
            )
        return round(total**0.5, 2) 

    # Logarithm function
    elif "log" in user_input: 
        parts = user_input.split("log")  
        total = float(parts[1]) 
        if total <= 0:  
            return "Error: Cannot calculate the logarithm of a non-positive number."  
        return round(math.log10(total), 2) 
    else:
        return "Error: Invalid input. Please enter a valid equation." 


if __name__ == "__main__":  
    stop_words = ["quit", "exit", "i'm done", "done", "stop"] 

    while True: 
        user_input = input(
            "Enter an equation (or type 'quit' when done): "
        ) 

        if user_input.lower() in stop_words: 
            print("Thank you for using the calculator!")  
            break 

        answer = calculate(user_input) 
        print(answer) 

    


    
