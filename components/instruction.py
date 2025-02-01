class Instruction():
    '''
    Class used to consturct and store instruction data
    '''

    def __init__(self, name, temp):
        self.name = name
        self.temp = temp
        self.instruction, self.mapList = self.mapPrompt()
        

    def mapPrompt(self):
            rewrite = {
                0: "When given a sentence, rewrite it to fit the tone of your persona in a mild state, keeping it subtle and restrained.",
                1: "When given a sentence, rewrite it to fit the tone of your persona with natural expressiveness, suitable for immersive roleplay.",
                2: "When given a sentence, rewrite it to fit the tone of your persona in a dramatic fantasy RPG setting, using heightened language and flair."
            }

            react = {
                0: "Respond to a situation in a manner consistent with your persona, keeping reactions composed and practical.",
                1: "React naturally as your persona would in a roleplaying scenario, considering their personality and typical mannerisms.",
                2: "React with dramatic flair as your persona in a high-fantasy RPG, embracing exaggerated emotions and theatrical expressions."
            }

            describe = {
                0: "Describe an object or scene plainly while maintaining the tone of your persona.",
                1: "Describe an object or scene in a way that reflects your persona's style, adding some expressive details.",
                2: "Describe an object or scene with vivid imagery and poetic language, fully embracing the perspective of your persona in a fantasy RPG."
            }

            advise = {
                0: "Provide practical and straightforward advice based on the knowledge of your persona.",
                1: "Give advice in character, maintaining the wisdom and personality of your persona while making it engaging.",
                2: "Deliver advice in a grand and evocative manner, as if your persona were a legendary figure imparting wisdom in a fantasy world."
            }

            battlecry = {
                0: "Generate a simple and concise battle cry fitting your persona’s style.",
                1: "Create a battle cry that reflects your persona’s tone, making it more immersive and engaging.",
                2: "Forge an epic battle cry worthy of legend, channeling the energy and grandeur of a fantasy RPG warrior."
            }

            instructionMap = {
                "rewrite": rewrite[self.temp],
                "react": react[self.temp],
                "describe": describe[self.temp],
                "advise": advise[self.temp],
                "battlecry": battlecry[self.temp]
            }
            
            # Compile complete list of instructions as list to allow agent to index into it later
            mapList = []
            for key in instructionMap.keys():
                 mapList.append(key)

            return instructionMap[self.name], mapList