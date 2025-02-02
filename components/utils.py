import re
# Util function to extract input and tag from original input
def extractInputFromTag(input_text: str, defaulTag: str):
    startTag = "<"
    endTag = ">"
    input_list = list(input_text)
    if startTag not in input_list  and endTag not in input_list:
        tag = defaulTag
        cleanInput = input_text
    else:
        tag = ""
        cleanInput = ""
        collectTag = False
        collectInput = False
        for char in input_text:
            if collectInput:
                cleanInput += char
            if char == endTag:
                collectTag = False
                collectInput = True
            if collectTag:
                tag += char

            if char == startTag:
                collectTag = True
    return tag, cleanInput

def remove_think_tags(text):
    """Removes content wrapped in <think></think> tags from a given string."""
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
