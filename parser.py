from AutoGrapher.BracketTypes import BracketType

functionStartIndent = 0

def parse_line(line, flowchart):

    # detecting indentation level
    indent = 0
    for char in line:
        if char == " ":
            indent += 1

    if indent < functionStartIndent:
        functionStartIndent = 0
        flowchart.addToken(line[3:], BracketType.FUNCTION_END)

    # if the line is empty, skip it
    if line == "":
        return

    # if first chars are #<! it's a flowchart subgraph comment
    elif line[0:3] == "#<!":
        flowchart.addToken(line[3:], BracketType.BEGIN_SUBGRAPH)
        return

    # if first chars are #!> it's a flowchart subgraph comment
    elif line[0:3] == "#!>":
        flowchart.addToken(line[3:], BracketType.END_SUBGRAPH)
        return

    # first char is #! it's a flowchart comment
    elif line[0:2] == "#!":
        flowchart.addToken(line[2:], BracketType.HEXAGON)
        return

    # if first char is only a # it's a comment
    elif line[0] == "#":
        return

    # if it contains an input statement it's an input
    elif "input" in line:

        # get the input
        input = line.split("input(")[1].split(")")[0]

        # if directly setting a variable to the input
        if "=" in line:
            # get the variable
            variable = line.split("=")[0]
            # add the variable assignment to the flowchart
            flowchart.addToken("input " + input, BracketType.TRAPEZOID)
            flowchart.addToken("Get " + input + " and set " + variable + " to it", BracketType.PARALLELOGRAM)
        else:
            flowchart.addToken("input " + input, BracketType.TRAPEZOID)

        return

    # if it contains an if statement it's a decision. Parse this into a human readable format
    elif "if" in line:
        # get the condition
        condition = line.split("if ")[1].split(":")[0]

        # add the decision to the flowchart
        flowchart.addToken("decision " + condition, BracketType.RHOMBUS)

        return

    # if its a variable assignment it's a variable assignment
    elif "=" in line:
        # get the variable
        variable = line.split("=")[0]

        # get the assignment of the variable
        assignment = line.split("=")[1].split("#")[0]

        # add the variable assignment to the flowchart
        flowchart.addToken("variable " + variable + " = " + assignment, BracketType.SQUARE)
        return

    # if it contains a print statement it's an output
    elif "print" in line:
        # get the output
        output = line.split("print(")[1].split(")")[0]
        # add the output to the flowchart
        flowchart.addToken("output " + output, BracketType.STADIUM)
        return

    # if it contains a return statement it's a return
    elif "return" in line:
        # get the return
        ret = line.split("return ")[1]
        # add the return to the flowchart
        flowchart.addToken("return " + ret)
        return

    # if it contains a while statement it's a loop
    elif "while" in line:
        # get the condition
        condition = line.split("while ")[1].split(":")[0]
        # add the loop to the flowchart
        flowchart.addToken("loop " + condition)
        return

    # for loop
    elif "for" in line:
        # get the condition
        condition = line.split("for ")[1].split(":")[0]
        # add the loop to the flowchart
        flowchart.addToken("loop " + condition)
        return

    # function
    elif "def" in line:
        # get the function name
        name = line.split("def ")[1].split("(")[0]

        flowchart.registerFunction(name)

        functionStartIndent = indent

        # add the function to the flowchart
        flowchart.addToken("function " + name)
        return

    # break
    elif "break" in line:
        # add the break to the flowchart
        flowchart.addToken("break")
        return

    # detect function call
    for function in flowchart.functions:
        if function + "(" in line:
            # get the function name
            name = function

            # get the arguments
            arguments = line.split(name + "(")[1].split(")")[0]

            # add the function call to the flowchart
            flowchart.addToken("function call " + name + "(" + arguments + ")")
            return
