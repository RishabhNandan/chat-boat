# Simple AI Chatbot
print("Hello! I'm your chatbot. How can I assist you today?")
print("Type 'exit' anytime to end the chat.")

while True:
    user_input = input("You: ").lower()  # Convert input to lowercase for easy matching

    # Exit condition
    if user_input == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Greetings
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")
    
    # Asking about chatbot
    elif "who are you" in user_input or "what are you" in user_input:
        print("Chatbot: I'm a simple chatbot created to assist you with basic queries.")
    
    # Help or assistance
    elif "help" in user_input or "assist" in user_input:
        print("Chatbot: Sure! Let me know what you need help with.")
    
    # Hobbies or interests
    elif "hobby" in user_input or "what do you like" in user_input:
        print("Chatbot: I enjoy chatting with people and helping them out!")
    
    # Default response
    else:
        print("Chatbot: I'm not sure about that. Can you try asking something else?")
