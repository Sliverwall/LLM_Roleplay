import ollama
import pyperclip
import time
import configure_agent
import components.utils
# Init ollama client
client = ollama.Client()

# Define model
models = ['mistral', 'deepseek-r1:7b']
model = models[1]

# Import agent map
agents = configure_agent.agents

# Default agent
defaultTag = "cs"

# Track the previous clipboard content
previous_clipboard_content = ""

while True:
    # Get current clipboard content
    current_clipboard_content = pyperclip.paste()

    # Check if clipboard content has changed
    if current_clipboard_content != previous_clipboard_content:
        # Log statement to confirm script entered processing mode
        print("Copy event detected...")

        # Work to build prompt
        input_text = pyperclip.paste()

        # extract tag from input_text
        tag, cleanInput = components.utils.extractInputFromTag(input_text=input_text, defaulTag=defaultTag)

        print("Tag used: ", tag)
        # Use tag to hash proper agent
        agent = agents[tag]
        # Process new clipboard content
        agent.processClipboard(
            model=model,
            client=client,
            cleanInput=cleanInput
                          )
        # Update the previous clipboard content
        current_clipboard_content = pyperclip.paste()
        previous_clipboard_content = current_clipboard_content

    # Sleep for a short period to prevent high CPU usage
    time.sleep(1)
