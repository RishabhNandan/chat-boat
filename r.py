print("Hello! I'm your chatbot. How can I assist you today?")
print("Type 'exit' anytime to end the chat.")

while True:
    user_input = input("You: ").lower() 
    if user_input == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")
    elif "who are you" in user_input or "what are you" in user_input:
        print("Chatbot: I'm a simple chatbot created to assist you with basic queries.")
    elif "help" in user_input or "assist" in user_input:
        print("Chatbot: Sure! Let me know what you need help with.")
    elif "hobby" in user_input or "what do you like" in user_input:
        print("Chatbot: I enjoy chatting with people and helping them out!")
    else:
        print("Chatbot: I'm not sure about that. Can you try asking something else?")
