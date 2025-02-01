import ollama
import pyperclip
import time

# Init ollama client
client = ollama.Client()

# Define model
model = 'mistral'

# Define a function to process clipboard content and send to Ollama
def process_clipboard():
    # Work to build prompt
    copied_text = pyperclip.paste()

    # Describe the instruction
    instruction = "You are a scribe in a high-fantasy world, skilled in rewriting modern speech into elegant, medieval-inspired roleplay dialogue."
    instruction += " When given a sentence, rewrite it to fit the tone of a fantasy RPG, considering the speaker's personality, setting, and level of formality."
    instruction += " Keep it lively, with a hint of bravado or rugged charm, fitting for a traveling warrior or rogue."
    instruction += " Make sure reponse is no longer 100 characters."
    

    prompt = f"{instruction}: {copied_text}"

    # Send query to the model
    response = client.generate(model=model, prompt=prompt)

    # Save the response from model
    model_response = response.response

    # Copy response back to the clipboard
    pyperclip.copy(model_response)

    print("Response generated...")

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
