# Laptop-virtual-assistance
This project is a desktop voice assistant.
It uses speech recognition, text-to-speech, and a modern web-based GUI built with Eel. The assistant runs two processes: one for GUI and interaction, and another for hotword detection.

🚀 Features

Modern GUI using Eel (Python + HTML/JS)

Multitasking with multiprocessing: one for the assistant, one for hotword

Speech-to-text (listen and respond)

Text-to-speech responses

Command execution module

Hotword detection module

Automatically opens in Microsoft Edge app mode

🗂 Project Structure

. ├── run.py # Main entry point with multiprocessing \n ├── main.py # Starts the Eel web app \n ├── sooha.db # Database (usage assumed in engine module) \n ├── engine/ \n │ ├── features.py # Speech features (hotword, speak, etc.) \n │ └── command.py # Custom command logic \n ├── www/ │ └── index.html # Web UI for the assistant \n Note: Actual contents of engine/ and www/ folders are assumed based on usage.

🔧 Requirements Install dependencies: pip install eel pyttsx3 SpeechRecognition Also ensure you have: Microsoft Edge (optional; used to open GUI in app mode) Microphone (for voice input)

🧠 How it Works run.py launches two separate processes:

One runs the GUI and assistant (main.py)
Another listens for hotword using microphone input
When the assistant starts, it opens index.html in a browser app window. Voice commands are processed, and the assistant responds using TTS.

🏁 How to Run python run.py This starts both assistant and hotword listener. GUI will automatically open in Microsoft Edge. Use your voice to interact!

⚠ Notes The assistant expects certain directories (engine/, www/) and files (index.html, database, etc.). You can change browser or port in main.py.

📌 To-Do Ideas

Add chatbot integration (e.g., ChatGPT API)

Add system-level controls (volume, brightness)

Add music or app launching

Enhance GUI with animations

🧑‍💻 Author Dhruvi Solnaki BTech IT | PPSU College
