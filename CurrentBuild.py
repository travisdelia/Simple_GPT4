import sys
import os
import openai
from openai import OpenAI
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
import ctypes
from pathlib import Path




client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

# Initialize an empty list of messages
# Initialize conversation
conversation = [
        {'role': 'system', 'content': 'You are a helpful devoted assistant, who does whatever is asked of them.'}
    ]

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Create the window
root = tk.Tk(className='GPT4 Chat')
#set window size
root.geometry("1020x1800+0+0")
#set window color
root.configure(bg='gray12')



# Create the chat window
chat_window = tk.LabelFrame(root, bg="gray12", fg="white", font=('Arial','11','bold'), pady=0, padx=0,)
chat_window.pack(fill=tk.BOTH, expand=True)
#bag= PhotoImage(file="chatbacker.png")
chat = Label(chat_window, text='', pady=15, padx=85, bg="gray12", fg="white", font=('Arial','11','bold'), )
chat.pack(fill=tk.BOTH, expand=True)
chatty= tk.Text(chat, bg="gray17", highlightbackground="gray12", highlightthickness=15, bd=0, fg="white",font=('Arial','11','bold'), padx=25, pady=15,wrap="word", height=50, width=100)
#chatty.tag_configure("tag-left", justify='left')
#chatty.tag_configure("tag-right", justify='right')
#chatty.tag_add("tag-left", 1.0, "end")
#chatty.tag_add("tag-right", 1.0, "end")
chatty.pack(fill=tk.Y, expand=1)


# Create the input field
input_field = tk.Entry(chat_window, width=45, bg="gray17",  fg="white",font=('Arial','11','bold'))
input_field.pack(side='bottom', pady=0, padx=30, fill=tk.X, expand=True)
#define the transform output function


chatty.tag_configure("tag-left", justify='left')
chatty.tag_configure("tag-right", justify='right')



def insert_User(output):
    chatty.tag_configure("tag-right", justify='right')
    chatty.insert(tk.END, output.replace('\\n', '\n'), 'tag-right' )
    chatty.tag_add("tag-right", "end-2l", "end-1c")

def insert_Bot(output):
    def add_char():
        try:
            chatty.insert(tk.END, next(content_gen),'tag-left')
            chatty.tag_add("tag-left", "end-2l", "end-1c")
            chatty.see("end")
            chatty.after(50, add_char)
        except StopIteration:
            return

    chatty.tag_configure("tag-left", justify='left')
    content_gen = iter(output.replace('\\n', '\n'))
    add_char()

def ctrlEvent(event):
    if event.state == 4 and event.keysym == 'c':
        content = input_field.selection_get()
        root.clipboard_clear()
        root.clipboard_append(content)
        return "break"
    elif event.state == 4 and event.keysym == 'v':
        input_field.insert('end', root.selection_get(selection='CLIPBOARD'))
        return "break"
    else:
        return "break"

# Main loop
def main_loop():
  # Prompt the user for a prompt
  prompt = input_field.get()
  mymessage = (datetime.now().strftime("%H:%M") + "\n" + prompt + "\n")
  insert_User(mymessage)
  # Exit the program if the user enters "exit"
  if prompt.lower() == "exit":
    sys.exit()
  # Append the prompt to the list of messages
  conversation.append({'role': 'user', 'content': prompt})
  # Generate a response to the prompt
  response = OpenAI().chat.completions.create(
      model='gpt-4',  # Use GPT-4 model
      messages=conversation
        )
  # Print the response
  assistant_reply = response.choices[0].message.content
  botmessage = (datetime.now().strftime("%H:%M") + "\n" + assistant_reply + "\n")


  conversation.append({'role': 'assistant', 'content': assistant_reply})
  insert_Bot(botmessage)

  input_field.delete(0, 'end')


input_field.bind("<Return>", lambda event: main_loop())

# Start the window
root.mainloop()

