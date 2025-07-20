from memory_engine import MemoryEngine
from biostate import BioState
from emotion_detector import generate_emotion_response, load_user_memory
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ConversationAgent:
    def __init__(self, name="Aria"):
        self.name = name
        self.memory = MemoryEngine()
        self.bio = BioState()

    def observe(self, event, event_type="neutral", impact=0.5, emotion="neutral"):
        self.memory.store(event, impact=impact, emotion=emotion)
        self.bio.update_on_event(event_type)

    def respond(self, prompt):
        # Load memory.json-based keyword memory
        user_memory = load_user_memory()

        # Generate emotional keyword-based reply (from emotion_detector)
        keyword_response, emotions = generate_emotion_response(prompt)

        # Get internal mood and past memories
        mood = self.bio.get_mood()
        memories = self.memory.recall(mood)
        memory_summary = ". ".join([m["event"] for m in memories]) if memories else "no strong memories"

        # Construct prompt for Groq's LLM
        gpt_prompt = f"""
        You are Aria, an emotionally-aware AGI.
        Your current mood is: {mood}.
        You have the following recent memories: {memory_summary}.
        The user just said: "{prompt}"
        Here's how you felt about it: {keyword_response}
        Now respond naturally and emotionally. Speak like a human, not a robot.
        """

        # Get response from Groq LLM
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": gpt_prompt}],
            temperature=0.8
        )

        gpt_reply = response.choices[0].message.content.strip()
        return f"{self.name} ({mood}): {gpt_reply}"
