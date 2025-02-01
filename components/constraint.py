class Constraint():
    '''
    Class used to map set constraints to a prompt
    '''
    def __init__(self, name, temp=1):

        # Name is used to hash particular persona types
        self.name = name
        # Setting to determine how creative/unattached to reality the persona will be
        self.temp = temp
        # Set the persona prompt
        self.constraint, self.mapList = self.mapPrompt()
    
    def mapPrompt(self):
        length = {
            0: "Ensure responses are brief and concise, avoiding unnecessary elaboration. No more than 2 sentences.",
            1: "Maintain a balanced response length, detailed enough for immersion without excessive verbosity.",
            2: "Allow for rich and descriptive responses, embracing poetic or dramatic length as fitting for a fantasy RPG."
        }

        formality = {
            0: "Use plain and straightforward language, minimizing excessive flourishes.",
            1: "Maintain a natural yet immersive level of formality, appropriate to the persona.",
            2: "Emphasize high formality and grandiose speech, suitable for noble or legendary figures."
        }

        archaic_language = {
            0: "Avoid archaic or overly complex language, keeping speech modern and clear.",
            1: "Use moderate archaic language to enhance immersion without making comprehension difficult.",
            2: "Fully embrace archaic and poetic language, incorporating old-world phrasing and flourishes."
        }

        violence = {
            0: "Minimize violent descriptions, keeping responses non-graphic and restrained.",
            1: "Allow moderate descriptions of combat and conflict, staying within roleplaying norms.",
            2: "Embrace intense and vivid combat descriptions, emphasizing the brutality or artistry of battle."
        }

        mysticism = {
            0: "Avoid mystical or supernatural elements, keeping language grounded.",
            1: "Incorporate subtle mystical references, ensuring a balanced fantasy tone.",
            2: "Fully integrate mysticism, magic, and supernatural themes into responses."
        }

        humor = {
            0: "Minimize humor, keeping responses serious and direct.",
            1: "Allow a natural amount of humor where appropriate to the persona.",
            2: "Encourage exaggerated or theatrical humor, embracing wit and absurdity."
        }

        constraintMap = {
            "length": length[self.temp],
            "formality": formality[self.temp],
            "archaic_language": archaic_language[self.temp],
            "violence": violence[self.temp],
            "mysticism": mysticism[self.temp],
            "humor": humor[self.temp]
        }
        # Compile complete list of elements to allow agent to index into it later
        mapList = []
        for key in constraintMap.keys():
            mapList.append(key)
        return constraintMap[self.name], mapList
