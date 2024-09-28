Weather Chatbot
A simple, interactive GUI-based Weather Chatbot application built using Python's Tkinter library. The chatbot allows users to enter a city name and receives the current weather information for that city using the OpenWeatherMap API.

Table of Contents
Features
Prerequisites
Installation
Usage
Customization
Troubleshooting
License
Acknowledgments
Features
Interactive GUI Interface: User-friendly interface with dynamic resizing and responsive design.
Real-time Weather Data: Fetches current weather information for any city using the OpenWeatherMap API.
Visual Enhancements: Colored messages to distinguish between user input and chatbot responses.
Easy Exit: Type exit or close the window to exit the application gracefully.
Customizable Appearance: Modify colors, fonts, and styles to suit your preferences.
Prerequisites
Python 3.x installed on your system.
OpenWeatherMap API Key: Obtain a free API key by signing up at OpenWeatherMap.
Required Python Libraries:
requests
tkinter (comes pre-installed with most Python distributions)
tkinter.font (part of the Tkinter library)
Installation
Clone or Download the Repository

Since this is a code snippet, you can copy the code into a file named weather_chatbot.py.

Install Required Packages

Open a terminal or command prompt and install the requests library if you haven't already:

bash
Copy code
pip install requests
Set Up Your API Key

Open the weather_chatbot.py file in a text editor.

Replace the placeholder API key with your actual OpenWeatherMap API key:

python
Copy code
API_KEY = 'your_actual_api_key_here'
Usage
Run the Application

In the terminal or command prompt, navigate to the directory containing weather_chatbot.py and run:

bash
Copy code
python weather_chatbot.py
Interact with the Chatbot

Enter City Name: Type the name of the city (e.g., "London", "New York") into the entry field.
Send Message: Press "Enter" or click the "Send" button.
Receive Weather Info: The chatbot will display the current weather information for the specified city.
Exit the Application

Type exit into the entry field and press "Enter".
Or simply close the application window.
Customization
Changing Colors and Fonts
You can customize the appearance of the chatbot by modifying the following variables in the script:

python
Copy code
# Theme colors
background_color = "#f0f0f0"  # Background color of the app
bot_color = "#0080ff"         # Color of chatbot messages
user_color = "#00b300"        # Color of user messages
entry_bg_color = "#ffffff"    # Background color of the entry field
button_color = "#333333"      # Background color of the send button
button_text_color = "#ffffff" # Text color of the send button

# Fonts
instruction_font = font.Font(family='Helvetica', size=12, weight='bold')
chat_font = font.Font(family='Helvetica', size=12)
entry_font = font.Font(family='Helvetica', size=12)
button_font = font.Font(family='Helvetica', size=12, weight='bold')
Adding Features
Display Additional Weather Details: Modify the get_weather function to include humidity, wind speed, etc.
Error Handling: Improve the error messages to provide more detailed feedback.
Language Support: Implement multilingual support for the chatbot interface.
Troubleshooting
ModuleNotFoundError: No module named 'requests'
Solution: Install the requests library using:

bash
Copy code
pip install requests
Invalid API Key or API Errors
Problem: Receiving errors related to the API key or API response.
Solution:
Ensure your API key is correct and active.
Check your internet connection.
Verify that the API endpoint is correct.
GUI Not Displaying Properly
Problem: The application window is not rendering correctly.
Solution:
Ensure you are running Python 3.x.
Confirm that Tkinter is installed (tkinter is included with most Python installations).
Update your Python installation if necessary.
License
This project is provided under the MIT License.

Acknowledgments
OpenWeatherMap: For providing the free weather API.
Python Documentation: For the comprehensive guides on Tkinter and other libraries.
Code Snippet
For reference, here is the complete code of the Weather Chatbot application:

python
Copy code
import requests
import tkinter as tk
from tkinter import font

API_KEY = 'your_actual_api_key_here'  # Replace with your actual API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    # Construct the URL with the city and API key
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

# Set the overall theme colors
background_color = "#f0f0f0"  # Light grey background
bot_color = "#0080ff"         # Blue color for bot messages
user_color = "#00b300"        # Green color for user messages
entry_bg_color = "#ffffff"    # White background for entry field
button_color = "#333333"      # Dark grey color for button
button_text_color = "#ffffff" # White text for button

app.configure(bg=background_color)

# Configure the grid to expand with window resizing
app.grid_rowconfigure(1, weight=1)  # Make the second row expandable
app.grid_columnconfigure(0, weight=1)  # Make the first column expandable

# Fonts
instruction_font = font.Font(family='Helvetica', size=12, weight='bold')
chat_font = font.Font(family='Helvetica', size=12)
entry_font = font.Font(family='Helvetica', size=12)
button_font = font.Font(family='Helvetica', size=12, weight='bold')

# Add instruction label
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
entry_field.focus_set()  # Auto-focus on entry field

# Send button
send_button = tk.Button(
    app, text="Send", command=send_message,
    bg=button_color, fg=button_text_color, font=button_font
)
send_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

app.mainloop()
