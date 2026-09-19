from openai import OpenAI

client= OpenAI()

print("AI Chatbot")
print("Type 'quit' to exit. \n")

while True:
    user_message =input('you')

    if user_message.lower() == 'quit':
        break
    response = client.responses.create(
        model = "gpt-5.6-luna",
        input = user_message
    )

    print('AI', response.output_text)
    
