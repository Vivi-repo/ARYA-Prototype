from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

from converstaion import ConversationAgent
aria = ConversationAgent()
def preload_memories(agent):
    agent.observe("Vetha said I'm worthy", event_type="bonding", impact=0.8, emotion="soft")
    agent.observe("My bestfriend left me stranded on the road", event_type="betrayal", impact=0.9, emotion="tense")
    agent.observe("I completed my first ever personal coding project", event_type="ambition", impact=0.7, emotion="proud")

 #talking to Aria
user_input = input("You:")
aria_response = aria.respond(user_input)

#her mood aware reply can be seen
print(aria_response)

