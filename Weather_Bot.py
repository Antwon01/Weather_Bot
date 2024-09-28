import requests
import tkinter as tk
from tkinter import font

API_KEY = 'ae172e26efce0a6809c2fae33ebd286b'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get('cod') == 200:
        weather = f"Weather in {data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}."
    else:
        weather = "Sorry, I couldn't find that city."
    return weather

def send_message(event=None):
    city = entry_field.get()
    if city.lower() == 'exit':
        app.quit()
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + city + '\n', 'user')
        weather = get_weather(city)
        chat_window.insert(tk.END, "Chatbot: " + weather + '\n\n', 'bot')
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        entry_field.delete(0, tk.END)

app = tk.Tk()
app.title("Weather Chatbot")

#Colors
background_color = "#C9C9C9"  
bot_color = "#0080ff"         
user_color = "#00b300"        
entry_bg_color = "#ffffff"    
button_color = "#333333"      
button_text_color = "#ffffff" 
app.configure(bg=background_color)

# Configure the grid to expand with window resizing
app.grid_rowconfigure(1, weight=1) 
app.grid_columnconfigure(0, weight=1)

# Fonts
instruction_font = font.Font(family='Helvetica', size=12, weight='bold')
chat_font = font.Font(family='Helvetica', size=12)
entry_font = font.Font(family='Helvetica', size=12)
button_font = font.Font(family='Helvetica', size=12, weight='bold')

# Instruction
instruction_label = tk.Label(
    app, text="Enter city name (e.g., 'London' or 'New York'):",
    bg=background_color, fg="#000000", font=instruction_font
)
instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Chat window (Text widget)
chat_window = tk.Text(
    app, bd=1, bg="#ffffff", fg="#000000", font=chat_font, state=tk.DISABLED
)
chat_window.grid(row=1, column=0, columnspan=2, padx=10, sticky="nsew")

# Tag configurations for text coloring
chat_window.tag_config('user', foreground=user_color)
chat_window.tag_config('bot', foreground=bot_color)

# Scrollbar for the chat window
scrollbar = tk.Scrollbar(app, command=chat_window.yview)
chat_window['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=1, column=2, sticky='ns')

# Initial message in chat window
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Chatbot: Please enter a city name to get the current weather.\n\n", 'bot')
chat_window.config(state=tk.DISABLED)

# Entry field for user input
entry_field = tk.Entry(
    app, bd=1, bg=entry_bg_color, fg="#000000", font=entry_font
)
entry_field.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
entry_field.bind("<Return>", send_message)
entry_field.focus_set()

# Send button
send_button = tk.Button(
    app, text="Send", command=send_message,
    bg=button_color, fg=button_text_color, font=button_font
)
send_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

app.mainloop()