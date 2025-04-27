<h1 align="center">DeepSeek-R1:1.5B Local Chat 🚀</h1>

<p align="center">
  <em>Run the DeepSeek-R1:1.5B language model locally using Python and Ollama.</em>
</p>

---

## ✨ Features

- ⚡ Run the **DeepSeek-R1:1.5B** model completely offline.
- 🛠️ Simple Python script to interact with the model.
- 📦 Lightweight setup using a virtual environment.

---

## 📋 Requirements

- 🐍 **Python** 3.8 or higher
- 🧠 **Ollama** installed and running
- 📥 **DeepSeek-R1:1.5B** model pulled via Ollama

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/deepseek-local-chat.git
cd deepseek-local-chat

2. Create and Activate a Virtual Environment
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
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Pull the DeepSeek-R1:1.5B Model
bash
Copy
Edit
ollama pull deepseek-r1:1.5b
5. Run the Script
bash
Copy
Edit
python main.py
The script will send a predefined prompt to the model and display the response.

🛠 Notes
Make sure Ollama is running before you execute the script.

Feel free to customize main.py to change prompts or enhance functionality!

📄 License
This project is licensed under the MIT License.

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,100:22D3EE&height=120&section=footer" /> </p> <p align="center"> <b>Happy Chatting with DeepSeek! 🎉</b> </p> ```
