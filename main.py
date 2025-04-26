import ollama

def main():
    query = input("How can i help you 🤓: ")
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[
            {'role': 'user', 'content': query}
        ]
    )
    print(response['message']['content'])

if __name__ == "__main__":
    main()
