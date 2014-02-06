import arithmetic
# Get input from user
while True:
    input = raw_input("> ")
# Parse the input into a list
    input_list = input.split(" ")
# Look for a quit condition and break
    operator = input_list[0]
    if operator == "q":
        break
# Match any conditions to the correct function
    if operator == "+":
        print arithmetic.add(int(input_list[1]), int(input_list[2]))

    elif operator == "-":
        print arithmetic.subtract(int(input_list[1]), int(input_list[2]))

    elif operator == "*":
        print arithmetic.multiply(int(input_list[1]), int(input_list[2]))

    elif operator == "/":
        print arithmetic.divide(float(input_list[1]), float(input_list[2]))

    elif operator == "square":
        print arithmetic.square(float(input_list[1]))

    elif operator == "cube":
        print arithmetic.cube(float(input_list[1]))

    elif operator == "pow":
        print arithmetic.power(float(input_list[1]))

    elif operator == "mod":
        print arithmetic.mod(float(input_list[1], input_list[2]))

    else: 
        print "that's not relevant input"
