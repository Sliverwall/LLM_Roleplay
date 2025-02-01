
import ollama
from agent import Agent
# Init ollama client
client = ollama.Client()

# Define model
model = 'mistral'

# Work to build prompt
# Get initial statement from clipboard pyperclip.paste()
copied_text = ["Let us ride to Bruma"]

# Create agent to generate a prompt
personas = ["scribe",
            "pirate",
            "teacher",
            "philosopher",
            "warrior",
            "eso_warrior"]

instructions = ["rewrite",
                "react",
                "describe",
                "advise",
                "battlecry"]

constraints = ["length",
            "formality",
            "archaic_language",
            "violence",
            "mysticism",
            "humor"]

temps = [1, 1, 0]
agent = Agent(persona=personas[0],
              instruction=instructions[2],
              constraint=constraints[0],
              temps=temps)

prompt = agent.constructPrompt(input=copied_text)

# Send query to the model
response = client.generate(model=model, prompt=prompt)

# Save the response from model
model_response = response.response

# Copy response back to the clipboard
print("Response generated...")

print(model_response)


