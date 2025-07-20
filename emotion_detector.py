# emotion_detector.py

emotion_keywords = {
    "happy": ["happy", "joyful", "excited", "grateful", "blessed", "content", "cheerful", "thrilled", "great"],
    "sad": ["sad", "down", "depressed", "blue", "unhappy", "crying", "low", "miserable"],
    "tired": ["tired", "exhausted", "sleepy", "drained", "fatigued", "worn out", "burnt out", "lethargic"],
    "angry": ["angry", "mad", "furious", "irritated", "annoyed", "pissed", "frustrated"],
    "anxious": ["anxious", "worried", "nervous", "stressed", "scared", "afraid", "panicked"],
    "lonely": ["lonely", "alone", "isolated", "ignored", "left out", "abandoned", "unloved"],
    "confident": ["confident", "proud", "strong", "capable", "empowered", "determined"],
    "bored": ["bored", "meh", "dull", "nothing to do", "uninspired", "disinterested"],
    "in love": ["in love", "crushing", "infatuated", "smitten", "heart-eyes", "in love with someone"]
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


def generate_emotion_response(user_input):
    detected_emotions = []

    for emotion, keywords in emotion_keywords.items():
        for word in keywords:
            if word in user_input.lower():
                detected_emotions.append(emotion)
                break

    detected_emotions = list(set(detected_emotions))

    if not detected_emotions:
        return "Thanks for sharing. Want to talk more about it?", []

    response_sentences = [responses[emotion] for emotion in detected_emotions]

    if len(response_sentences) == 1:
        joined_response = response_sentences[0]
    elif len(response_sentences) == 2:
        joined_response = " and ".join(response_sentences)
    else:
        joined_response = ", but ".join(response_sentences[:-1]) + ", and " + response_sentences[-1]

    return joined_response, detected_emotions


def load_user_memory():
    import os
    import json
    memory_file = "memory.json"
    if not os.path.exists(memory_file):
        with open(memory_file, "w") as f:
            json.dump({}, f)

    with open(memory_file, "r") as f:
        return json.load(f)
