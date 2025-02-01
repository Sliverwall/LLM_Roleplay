Requires Ollama and pyperclip

Default model used is Mistral 7b parameter model, however this can be adjusted in observer.py

LLM_Roleplay is a set of curated prompts to assit with roleplaying. 

The observer.py script monitors user's clipboard. To interact with the LLM, just copy an input to the clipboard, then it will generate a response back to the clipboard. This allows seemless use while in game.

The agent has set of personas, instructions, and context to choose from. 

To construct a custom agent, initialize using the Agent class then set is persona, instruction, and constraint. Use a temp vector to adjust the creativity along each component.

in configure_agent.py are some preset agents to use. Define the agent used in the observer.py file

# Set persona and instruction to moderate, and constraint to mild


temps = [1, 1, 0]


agent = Agent(persona="scribe",
              instruction="rewrite",
              constraint="length",
              temps=temps)

              
This will set the agent to act as a scribe that can rewrite input int he style of a fanasty context. It will try to keep the length to about 2 sentences.
