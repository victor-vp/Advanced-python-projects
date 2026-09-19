# Advanced-python-projects
AI Integration
AI Chatbot

A simple command-line chatbot built in Python using the OpenAI API. Type a message, get a response, and keep the conversation going until you type quit.

How it works

The script runs a loop that:

Takes a line of input from the user
Sends it to the OpenAI API
Prints the model's response
Repeats until the user types quit
Requirements
Python 3.8+
The openai Python package
An OpenAI API key
Setup
bash
pip install openai

Set your API key as an environment variable (don't hardcode it in the script):

Windows (PowerShell):

powershell
setx OPENAI_API_KEY "your_key_here"

Mac/Linux:

bash
export OPENAI_API_KEY="your_key_here"
Usage
bash
python ai_chatbot.py

Example session:

AI Chatbot
Type 'quit' to exit.

you: what's the capital of France?
AI: The capital of France is Paris.
you: quit
Notes

Built during a hands-on workshop on Generative AI tools and prompt engineering, covering how to structure API calls to a language model and manage a basic conversation loop.

Author

Vishal Prasad — Electrical and Computer Engineering, College of Engineering Trivandrum
