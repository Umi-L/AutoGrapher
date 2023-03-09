import sys
import pyperclip

from AutoGrapher.BracketTypes import BracketType
from AutoGrapher.Flowchart import Flowchart
from mermaider import mermaidify
from parser import parse_line

flowchart = Flowchart([])

# check len of sys.argv
if len(sys.argv) != 2:
    print("Usage: python main.py <scriptname>")
    sys.exit(1)

# first arg is the name of the script to flowchart
script = sys.argv[1]

# open the script
with open(script, "r") as f:
    # read the script
    script = f.read()

# split the script into lines
lines = script.splitlines()

# parse each line
for line in lines:
    parse_line(line, flowchart)

# add start element to beginning of flowchart
flowchart.addToken("start", BracketType.CIRCLE, 0)
flowchart.addToken("end", BracketType.CIRCLE)


# convert the flowchart to a mermaid flowchart
mermaided = mermaidify(flowchart)

# print the flowchart
for line in mermaided:
    print(line)

# create an input to copy the flowchart to the clipboard
input("Press enter to copy the flowchart to the clipboard")

# copy the flowchart to the clipboard
pyperclip.copy("\n".join(mermaided))

# exit the program
sys.exit(0)
