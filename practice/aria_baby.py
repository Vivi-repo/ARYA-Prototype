import os
import json
#check if file exists
if not os.path.exists("memory.json"):
    #if file doesn't exist, create a new file called memory.json, and overwrite it with new content, temporarily store memory.json as file varaiale, so that we can use it in the follwing block of code
    with open("memory.json", "w") as file:
        #store an empty dictionary in the json file
       memory = {}
       json.dump(memory, file)
#load the contents of updated memory.json file and use it
with open("memory.json","r") as file:
    memory = json.load(file)

emotion_keywords = {
    "happy" : ["happy", "joyful", "excited", "grateful", "blessed", "content", "cheerful", "thrilled","great"],
    "sad" : ["sad", "down", "depressed", "blue", "unhappy", "crying", "low", "miserable"],
    "tired" : ["tired", "exhausted", "sleepy", "drained", "fatigued", "worn out", "burnt out", "lethargic"],
    "angry" : ["angry", "mad", "furious", "irritated", "annoyed", "pissed", "frustrated"],
    "anxious" : ["anxious", "worried", "nervous", "stressed", "scared", "afraid", "panicked"],
    "lonely" : ["lonely", "alone", "isolated", "ignored", "left out", "abandoned", "unloved"],
    "confident" : ["confident", "proud", "strong", "capable", "empowered", "determined"],
    "bored" : ["bored", "meh", "dull","nothing to do", "uninspired", "disinterested"],
    "in love" : ["in love", "crushing", "infatuated", "smitten", "heart-eyes", "in love with someone"]
                  }

responses = {
    "happy": "Yay! I'm so glad you're feeling happy!",
    "sad": "Aw, I'm sorry you're feeling sad. Want to talk about it?",
    "tired": "You should definitely take a break and rest. You deserve it.",
    "angry": "Take a deep breath, love. I'm here if you want to vent.",
    "anxious": "It's okay to feel anxious sometimes. I'm here with you.",
    "lonely": "You're not alone. I'm here with you now.",
    "confident": "Yes queen/king/royalty! Go slay, I'm so proud of you!",
    "bored": "Let's find something fun to do together!",
    "in love": "Ooooh tell me everything! I'm so excited for you!!"
}

lowercased_keywords = {
    emotion.lower() : [word.lower() for word in keywords]
    for emotion, keywords in emotion_keywords.items()
    }

print("Hello, I'm Aria, your personal AI assistant")
if "name" in memory:
    print("Welcome back " + memory["name"] )
    if "mood" in memory:
        print("Last time you said you were feeling " + ", ".join(memory["mood"]) + ". How are you feeling today?")
else:
    name = input("What is your name?")
    memory["name"] = name
    print("Nice to meet you " + name)
    print("How are you feeling today?")

mood_input = input("You: ").lower()

detected_emotion = []

for emotion, keywords in emotion_keywords.items():
    for word in keywords:
        if word in mood_input:
            detected_emotion.append(emotion)
            break
detected_emotion = list(set(detected_emotion))

memory["mood"] = detected_emotion

if detected_emotion:
    response_sentences = [responses[emotion] for emotion in detected_emotion]
    if len(response_sentences) == 1:
        joined_response = response_sentences[0]
    elif len(response_sentences) == 2:
        joined_response = ", and ".join(response_sentences)
    else:
        joined_response = ", but " .join(response_sentences[:-1]) + ", and " + (response_sentences[-1])
    print("Aria: " + joined_response)
else:
    print("Thanks for sharing that with me. Would you like to talk about it?")

with open("memory.json", "w") as file:
    json.dump(memory, file)
        