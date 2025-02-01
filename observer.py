import ollama
import pyperclip
import time
import configure_agent

# Init ollama client
client = ollama.Client()

# Define model
model = 'mistral'

# Define agent
agent = configure_agent.consiseScribe

# Define a function to process clipboard content and send to Ollama
def process_clipboard():
    # Work to build prompt
    input_text = pyperclip.paste()

    # Generate prompt from agent
    prompt = agent.constructPrompt(input=input_text)

    # Send query to the model
    response = client.generate(model=model, prompt=prompt)

    # Save the response from model
    model_response = response.response

    # Copy response back to the clipboard
    pyperclip.copy(model_response)

    print("Response generated...")
    print(model_response)

# Track the previous clipboard content
previous_clipboard_content = ""

while True:
    # Get current clipboard content
    current_clipboard_content = pyperclip.paste()

    # Check if clipboard content has changed
    if current_clipboard_content != previous_clipboard_content:
        print("Copy event detected...")
        # Process new clipboard content
        process_clipboard()
        # Update the previous clipboard content
        current_clipboard_content = pyperclip.paste()
        previous_clipboard_content = current_clipboard_content

    # Sleep for a short period to prevent high CPU usage
    time.sleep(1)
