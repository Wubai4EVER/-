import json
import matplotlib.pyplot as plt

def analyze(filepath):
    data = json.load(open(filepath))
    states = [e["state"] for e in data.get("history", [])]
    counts = {s: states.count(s) for s in set(states)}
    plt.bar(counts.keys(), counts.values())
    plt.title("Emotion Cycle Counts")
    plt.xlabel("Emotion State")
    plt.ylabel("Occurrences")
    plt.show()

if __name__ == "__main__":
    analyze("infra/logs/mental_logs/emotions.json")
