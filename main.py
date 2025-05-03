import ollama

def main():
    messages = []
    while True:
        query = input("You: ")
        messages.append({'role': 'user', 'content': query})

        if query.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Goodbye! 👋")
            break

        response = ollama.chat(
            model='deepseek-r1:1.5b',
            messages=messages
        )
        assistant_response = response['message']['content']
        print(f"Assistant: {assistant_response}")

        
        messages.append({'role': 'assistant', 'content': assistant_response})


if __name__ == "__main__":
    main()