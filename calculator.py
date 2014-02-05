import arithmetic
# Get input from user
while True:
    input = raw_input("> ")
    # Parse the input into a list
    input_list = input.split(" ")
    # Look for a quit condition and break
    if input_list[0] == "q":
        break
    # Match any conditions to the correct function
    if input_list[0] == "+":
        print arithmetic.add(int(input_list[1]), int(input_list[2]))
    else:
        print "that's not relevant input"
