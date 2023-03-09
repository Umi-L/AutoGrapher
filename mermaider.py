from AutoGrapher.BracketTypes import BracketType
from AutoGrapher.Flowchart import Flowchart


def mermaidify(chart: Flowchart, type="TD"):
    """Convert a flowchart to mermaid code"""

    excluded = []

    # escape all special characters
    mermaided = [line.replace("[", "\[").replace("]", "\]") for line in chart.tokens]

    # replace all " with '
    mermaided = [line.replace('"', "'") for line in mermaided]

    # define each line as a mermaid variable with the index as the name

    for index, line in enumerate(mermaided):

        # if the line is a subgraph, add the subgraph header
        if chart.brackets[index] == BracketType.BEGIN_SUBGRAPH:
            mermaided[index] = f"subgraph {line}"
            excluded.append(index)
            continue
        # if the line is a subgraph end, add the subgraph footer
        elif chart.brackets[index] == BracketType.END_SUBGRAPH:
            mermaided[index] = f"end"
            excluded.append(index)
            continue

        token = f'var{index}{chart.brackets[index].openBracket()}"{line}"{chart.brackets[index].closeBracket()}'
        mermaided[index] = token

    tmpChart = []


    lastValidToken = 0

    # add arrows between each line and append to the flowchart ignoring excluded lines
    for index, line in enumerate(mermaided):
        if index not in excluded:
            if index != 0:
                tmpChart.append(f'var{lastValidToken} --> var{index}')
            lastValidToken = index

    mermaided += tmpChart
    # add indentation to the flowchart
    mermaided = ["    " + line for line in mermaided]

    # add the mermaid header
    mermaided = [f"flowchart {type}"] + mermaided

    return mermaided