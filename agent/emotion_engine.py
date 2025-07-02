from enum import Enum

class Emotion(Enum):
    CALM = "CALM"
    MANIC = "MANIC"
    DEPRESSED = "DEPRESSED"

class EmotionEngine:
    def __init__(self):
        self.state = Emotion.CALM
        self.history = []

    def reset(self):
        self.state = Emotion.CALM
        self.history = []

    def react(self, trigger: str):
        trigger = trigger.lower()
        if trigger.startswith("positive"):
            self.state = Emotion.MANIC
        elif trigger.startswith("negative"):
            self.state = Emotion.DEPRESSED
        else:
            self.state = Emotion.CALM
        self.history.append(self.state)
        return self.state
