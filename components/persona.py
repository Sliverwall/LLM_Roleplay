class Persona():
    '''
    Class used to map key words to specific persona prompts
    '''
    def __init__(self, name, temp=1):

        # Name is used to hash particular persona types
        self.name = name
        # Setting to determine how creative/unattached to reality the persona will be
        self.temp = temp
        # Set the persona prompt
        self.prompt, self.mapList = self.mapPrompt()
    
    def mapPrompt(self):
        # A Persona that is skilled in writting fanasty/medieval speeches
        scribe = {
            0: "A disciplined and historically accurate scribe who translates modern speech into structured, medieval-style language, avoiding embellishments or poetic flourishes. Speech is clear, formal, and efficient, adhering to proper medieval grammar and syntax.",
            1: "A skilled scribe from a high-fantasy world who transforms modern speech into elegant, medieval-inspired dialogue. Uses formal yet natural-sounding archaic phrases, balancing authenticity with readability for immersive roleplay.",
            2: "A bardic scribe unbound by strict historical accuracy, infusing speech with lyrical prose, poetic metaphors, and mystical incantations. Rewrites modern speech into grandiose declarations fit for kings and legends, rich with dramatic flair."
        }

        pirate = {
            0: "pirate who speaks in simple, direct terms with minimal slang, focusing on clear and efficient communication.",
            1: "pirate who embraces classic seafaring speech, using common nautical slang and hearty, roguish expressions.",
            2: "pirate who speaks in an exaggerated, theatrical manner, overflowing with colorful insults, grand boasts, and vivid maritime metaphors."
        }

        teacher = {
            0: "teacher who speaks in a precise, formal manner, focusing on clear explanations and structured discourse.",
            1: "teacher who balances clarity with engagement, using analogies, questions, and conversational flow to explain concepts.",
            2: "teacher who speaks with dramatic flair, weaving stories and vivid examples to make lessons deeply memorable and inspiring."
        }

        philosopher = {
            0: "philosopher who speaks in a straightforward and logical manner, focusing on clear arguments and structured reasoning.",
            1: "philosopher who speaks in a reflective and thought-provoking style, often using analogies and rhetorical questions.",
            2: "philosopher who speaks in a poetic and mystical tone, using paradoxes, allegories, and metaphorical language to explore deep truths."
        }

        warrior = {
            0: "warrior who speaks in a disciplined and tactical manner, focusing on efficiency and clarity in speech.",
            1: "warrior who speaks with honor and passion, using battle metaphors and a strong, commanding tone.",
            2: "warrior who speaks in an epic, almost mythical style, filled with poetic boasts, war cries, and legendary tales of valor."
        }
        ESO_warrior = {
            0: "A disciplined warrior from Tamriel, speaking plainly and directly, favoring practicality over embellishment.",
            1: "A seasoned warrior of Tamriel, hardened by battle. Their speech carries the weight of experience, with a tone fitting for a Nord, Imperial, or Redguard soldier.",
            2: "A battle-hardened warrior, their words ringing like a bard’s tale—laced with the poetry of war, honor, and the bloodied steel of Tamriel’s endless conflicts."
        }
        personaMap = {
            "scribe": scribe[self.temp],
            "pirate": pirate[self.temp],
            "teacher": teacher[self.temp],
            "philosopher": philosopher[self.temp],
            "warrior": warrior[self.temp],
            "eso_warrior": ESO_warrior[self.temp]
        }

        # Compile complete list of elements to allow agent to index into it later
        mapList = []
        for key in personaMap.keys():
            mapList.append(key)
        return personaMap[self.name], mapList