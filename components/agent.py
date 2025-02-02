
from components.persona import Persona
from components.instruction import Instruction
from components.constraint import Constraint
from components.utils import remove_think_tags
import pyperclip
class Agent():
    '''
    Class used to store, configure, and mix various pre-made prompts to interact with local LLMS
    '''
    def __init__(self, persona: str, instruction: str, constraint: str, temps=[1,1,1]):
        # Instruction list to help build the persona
        self.persona = persona
        self.instruction = instruction
        self.constraint = constraint
        self.temps = temps

    def constructPersona(self):
        # Initialize Persona
        personaObj = Persona(name=self.persona,temp=self.temps[0])

        # Give context to persona by telling the LLM to act like it
        personaContext = "Your persona is a"

        # Join the context with the persona prompt to create the persona instruction
        personaInstruction = f"{personaContext} {personaObj.prompt}"

        # Return the persona instruction to use in final output
        return personaInstruction
    def constructInstruction(self):
        # Initialize Instruction obj
        instructionObj = Instruction(self.instruction, temp=self.temps[1])

        # Return the action instruction to use in final output
        return instructionObj.instruction
    def constructConstraint(self):
        # Initialize constraint obj
        constraintObj = Constraint(self.constraint, temp=self.temps[2])

        # Return the action instruction to use in final output
        return constraintObj.constraint


    # Method to create a list of maps of all possible settings for each of the agent's components.
    def constructMapList(self):
        personaObj = Persona(name=self.persona,temp=self.temps[0])
        instructionObj = Instruction(self.instruction, temp=self.temps[1])
        constraintObj = Constraint(self.constraint, temp=self.temps[2])

        personaMap = personaObj.mapList
        instructionMap = instructionObj.mapList
        constraintMap  = constraintObj.mapList

        maps = [personaMap, instructionMap, constraintMap]
        return maps

    # Method to take agent elements to made a taliored prompt
    def constructPrompt(self, input: str):
        persona = self.constructPersona()
        instruction = self.constructInstruction()
        constraint = self.constructConstraint()

        prompt = f"{persona} {instruction} {constraint}: {input}"
        return prompt
    # Define a function to process clipboard content and send to Ollama
    def processClipboard(self, client, model, cleanInput):
        # Generate prompt from agent
        prompt = self.constructPrompt(input=cleanInput)

        # Send query to the model
        response = client.generate(model=model, prompt=prompt)

        # Save the response from model
        model_response = response.response

        # If using COT model, remove think tags
        if model == 'deepseek-r1:7b':
            model_response = remove_think_tags(model_response)
        # Copy response back to the clipboard
        pyperclip.copy(model_response)

        print("Response generated...")
        print(model_response)