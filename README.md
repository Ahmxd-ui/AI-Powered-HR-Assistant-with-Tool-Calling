# 🤖 AI-Powered HR Assistant

An intelligent HR chatbot built with **Python**, **LangChain**, **Google Gemini**, and **Gradio**. This assistant automates common HR tasks by using "tool calling" (function execution) to retrieve employee data, check leave balances, and generate role-specific interview questions.

It features **context awareness**, allowing it to remember employee details across the conversation (e.g., finding an ID from a name and then checking leave balance without re-asking).

## 🚀 Features

* **Intelligent Tool Calling:** Automatically decides when to call a Python function versus answering from general knowledge.
* **Context Memory:** Remembers previous interactions. If you ask about "Alice," it remembers her ID for subsequent questions like "check leave balance."
* **Employee Lookup:** Can find an employee's ID just by their name.
* **Leave Balance Checker:** Instantly retrieves remaining leave days from a mock database.
* **Interview Question Generator:** Creates tailored technical questions for specific roles (e.g., DevOps, Data Scientist).

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **LLM:** Google Gemini 1.5 Flash (via `langchain-google-genai`)
* **Orchestration:** LangChain
* **Interface:** Gradio (Web UI)
* **Environment Management:** Python Dotenv

## 📂 Project Structure

```text
HR_ASSISTANT/
├── src/
│   ├── __pycache__/
│   ├── agent.py          # Contains the System Prompt and tool binding logic
│   ├── app.py            # The Gradio web interface
│   └── tools.py          # Contains the mock DB and the new 'get_employee_id_by_name' function
├── venv/                 # Virtual environment folder
├── .env                  # Stores your GOOGLE_API_KEY
├── .gitignore            # Files to be ignored by Git
├── README.md             # Documentation file
└── requirements.txt      # List of python libraries
```

## ⚡ Installation & Setup
### 1. Clone the Repository
```Bash
git clone <repository-url>
cd hr_assistant
```
### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

#### Windows:
```Bash
python -m venv venv
venv\Scripts\activate
```
#### Mac/Linux:
```Bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```Bash
pip install -r requirements.txt
```
### 4. Configure API Key

Create a .env file in the root directory and add your Google Gemini API key:
```bash
GOOGLE_API_KEY=your_actual_api_key_here
```
Don't have a key? Get one from Google AI Studio.
## 🏃‍♂️ Usage

### Run the Application:
```Bash
python app.py
```
Access the UI: Open your browser and navigate to the local URL provided in the terminal (usually http://127.0.0.1:7860).

#### Try These Queries:

"Who is Alice Johnson?" (Tests name lookup)

"What is her leave balance?" (Tests memory & context)

"Generate interview questions for a DevOps Engineer." (Tests generation tool)

"Details for employee E33445" (Tests direct ID lookup)

## 🐛 Troubleshooting

### Error: 404 NOT_FOUND models/gemini-1.5-flash...

Cause: The generic model alias might not be resolving correctly in your region or library version.

Fix: Open agent.py and ensure the model name is pinned to a specific version:
```Python
model="gemini-1.5-flash-001"
```
### Error: ValueError: too many values to unpack

Cause: A mismatch between Gradio's history format and the unpacking logic.

Fix: Ensure you are using the robust loop in app.py that checks if len(turn) >= 2.

## 🛡️ License

This project is open-source and available under the MIT License.