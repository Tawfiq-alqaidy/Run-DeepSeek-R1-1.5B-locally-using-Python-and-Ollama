DeepSeek-R1:1.5B Local Chat with Python & Ollama
This project demonstrates how to run the DeepSeek-R1:1.5B language model locally using Python and the Ollama framework.

✨ Features
Run the DeepSeek-R1:1.5B model locally without internet dependency.

Simple Python script to send prompts and receive responses.

Lightweight setup using a virtual environment.

📋 Requirements
Python 3.8 or higher

Ollama installed and running

DeepSeek-R1:1.5B model pulled via Ollama

⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/deepseek-local-chat.git
cd deepseek-local-chat
2. Create and activate a virtual environment
On Windows:
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Pull the DeepSeek-R1:1.5B model
bash
Copy
Edit
ollama pull deepseek-r1:1.5b
5. Run the script
bash
Copy
Edit
python main.py
The script will prompt the model with a predefined message and display the response.

🛠 Notes
Ensure that Ollama is properly installed and running before executing the script.

You can modify the main.py file to change the prompt or enhance interaction logic.

