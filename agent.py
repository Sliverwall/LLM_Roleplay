
from components.persona import Persona
from components.instruction import Instruction
from components.constraint import Constraint
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
