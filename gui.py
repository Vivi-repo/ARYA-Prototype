from main import preload_memories
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from converstaion import ConversationAgent
from emotion_detector import detect_user_emotion  #  added for user mood detection

# initializing Aria
aria = ConversationAgent()
preload_memories(aria)

# creating the main window
root = tk.Tk()
root.title("Aria - Your emotionally aware AI friend")
root.configure(bg="#ffd6e8")
root.geometry("500x600")

# creating a label widget to hold Aria's image or avatar
avatar_label = tk.Label(root, bg="#ffd6e8")
avatar_label.pack(pady=10)

# matching emotion to image filename
def get_avatar_path(emotion):
    mood_map = {
        "tense": "avatars/aria_sad.jpg",
        "sad": "avatars/aria_sad.jpg",
        "angry": "avatars/aria_angry.jpg",
        "love": "avatars/aria_loved.jpg",
        "happy": "avatars/aria_happy.jpg",
        "soft": "avatars/aria_happy.jpg",
        "neutral": "avatars/aria_neutral.jpg"
    }
    return mood_map.get(emotion, "avatars/aria_neutral.jpg")

def update_avatar(emotion):
    path = get_avatar_path(emotion)
    try:
        img = Image.open(path).resize((120, 120))
        tk_img = ImageTk.PhotoImage(img)
        avatar_label.config(image=tk_img)
        avatar_label.image = tk_img  # Keep a reference
    except:
        avatar_label.config(text="No image", fg="white")

# chat display
chat_window = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, bg="#f8bbd0", fg="#333333", font=("Helvetica", 11)
)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "Aria wants to talk...\n")
chat_window.config(state=tk.DISABLED)

# input box
entry_box = tk.Entry(root, font=("Helvetica", 11))
entry_box.pack(pady=10, padx=10, fill=tk.X)

# send_message function
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return

    # show user message in chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

    # clear entry box
    entry_box.delete(0, tk.END)

    # detect user emotion (e.g. rude, sweet, sad)
    user_emotions = detect_user_emotion(user_input)

    # get Aria's response
    aria_response = aria.respond(user_input)

    # decide how to update avatar
    if user_emotions:
        update_avatar(user_emotions[0])  # show emotion Aria feels based on user's words
    else:
        update_avatar(aria.bio.get_mood())  # fallback to Aria’s internal mood

    # show Aria's response
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{aria_response}\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

# Send button
send_button = tk.Button(
    root,
    text="Send",
    command=send_message,
    bg="#f48fb1",
    fg="white",
    font=("Helvetica", 10, "bold")
)
send_button.pack(pady=5)

root.mainloop()




    



