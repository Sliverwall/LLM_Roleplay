
'''
Module used to configure and save preset agents
'''
from components.agent import Agent

# Possible component options
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


# Define preset agents below
consiseScribe = Agent(
    persona="scribe",
    instruction='rewrite',
    constraint="length",
    temps=[1,1,0]
    )

consiseESOWarrior = Agent(
    persona="eso_warrior",
    instruction='rewrite',
    constraint="length",
    temps=[1,1,0]
    )

wiseTeacher = Agent(
    persona="teacher",
    instruction='advise',
    constraint="length",
    temps=[1,1,0]
    )

# Construct map to extract pre-configed agents from tags
agents = {
    "cs": consiseScribe,
    "cw": consiseESOWarrior,
    "wt": wiseTeacher
}