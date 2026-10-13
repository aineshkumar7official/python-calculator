import math  # Standard PEP 8 placement for imports
import re  # Standard PEP 8 placement for imports


def calculate_v2(user_input):
    """
    Evaluates a mathematical expression using the Shunting-yard algorithm.
    This method parses a mathematical expression into two distinct stacks (lists):
    the numbers_tray and the operators_tray. Using a priority dictionary, it evaluates
    operators based on higher precedence as it loops through the expression, executing
    calculations immediately when an operator outranks the next incoming symbol.
    """
    user_input = user_input.replace(" ", "")  # Remove spaces from the input

    # 1. Define PEMDAS Priority Levels
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
        "sqrt": 4,
        "log": 4,
        "sin": 4,
        "cos": 4,
        "tan": 4,
    }

    # 2. Separate numbers and symbols into a clean list from user_input
    parts = re.split(r"([+\-*/()^]|sqrt|log|sin|cos|tan)", user_input)
    #remove any spaces and empty strings from the list
    parts = [part for part in parts if part]

    numbers_tray = []
    operators_tray = []

    # 3. Define the Math Engine Room
    def process_top_operator():
        operator = operators_tray.pop()

        # Word functions only look right, so pop exactly ONE number
        if operator in ["sqrt", "log", "sin", "cos", "tan"]:
            number = numbers_tray.pop()

            if operator == "sqrt":
                if number < 0:
                    #specifes error so that the user knows why the error occurred
                    raise ValueError(
                        "Error: Cannot take the square root of a negative number."
                    )
                result = math.sqrt(number)
            elif operator == "log":
                if number <= 0:
                    #specifes error so that the user knows why the error occurred
                    raise ValueError(
                        "Error: Logarithm is undefined for non-positive numbers."
                    )
                result = math.log10(number)
            # **operation** then convert...
            elif operator == "sin":
                result = math.sin(math.radians(number))
            elif operator == "cos":
                result = math.cos(math.radians(number))
            elif operator == "tan":
                result = math.tan(math.radians(number))

        # Standard symbols look left and right, so pop TWO numbers
        #keeps order of operartions correct by popping the right number first, then the left number
        else:
            right_number = numbers_tray.pop()
            left_number = numbers_tray.pop()

            if operator == "+":
                result = left_number + right_number
            elif operator == "-":
                result = left_number - right_number
            elif operator == "*":
                result = left_number * right_number
            elif operator == "^":
                result = left_number**right_number
            elif operator == "/":
                if right_number == 0:
                    raise ZeroDivisionError(
                        "Error: Division by zero is not allowed."
                    )
                result = left_number / right_number

        numbers_tray.append(result)

    # 4. Loop through the parts from left to right to enforce PEMDAS 
        #try: atttemps to calculate and if error occurs, don't stop run backup program instead
    try:
        #looks at every piece of equation from left to right
        for token in parts:
            #get priority and tells program that a new math zone has started
            if token in priority or token in ["(", ")"]:
                if token == "(":
                    operators_tray.append(token)
                elif token == ")":
                    #calculate everything until end of parenthesses
                    while operators_tray and operators_tray[-1] != "(":
                        process_top_operator()
                    if not operators_tray:
                        return "Error: Mismatched parentheses."
                    operators_tray.pop()  # Remove the opening parenthesis
                # runs if there is no parenthesis
                else:
                    while (
                        operators_tray
                        and operators_tray[-1] != "("
                        and priority[operators_tray[-1]] >= priority[token]
                    ):
                        process_top_operator()
                    operators_tray.append(token)
            else:
                numbers_tray.append(float(token))

        # 5. Clean-up Phase: Run through any remaining operators left over (RESTORED)
        while operators_tray:
            if operators_tray[-1] == "(":
                return "Error: Mismatched parentheses."
            process_top_operator()

    #errors
    #catches division by zero
    except ZeroDivisionError as e:
        return str(e)
    #catches trying to square root a negative number
    except ValueError as e:
        if "Error:" in str(e):
            return str(e)
        return "Error: Invalid character or number detected."
    #if the user inputs an invalid character or number, it will return an error message
    except IndexError:
        return "Error: Invalid equation layout."

    # 6. Return the final answer (RESTORED)
    if numbers_tray:
        return round(numbers_tray[0], 2)
    else:
        return "Error: Invalid equation."



#if statement for code to run only when the script is executed directly, not when imported as a module
if __name__ == "__main__":
    stop_words = ["quit", "exit", "i'm done", "done", "stop"]

    #allows for continuous input from the user until they decide to quit
    while True:
        user_input = input("Enter an equation (or type 'quit' when done): ")

        if user_input.lower() in stop_words:
            print("Thank you for using the calculator!")
            break

        answer = calculate_v2(user_input)
        print(answer)



    


    
