# 🦙 LangChain + Ollama + Streamlit Demo

This is a simple end-to-end demo that integrates **LangChain**, **Ollama**, and **Streamlit** to create a local chatbot interface powered by the **LLaMA 3.2** model.


## 🚀 Features

- Prompt chaining using **LangChain**
- Local LLM support via **Ollama**
- Clean interactive interface with **Streamlit**
- Environment variable management via `.env`

## 📦 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- Python 3.9+
  

## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/mohitmittal1988/LangChain-Ollama-Demo.git
   cd langchain-ollama-demo
2. Create a virtual environment (optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the dependencies
    ```bash
    pip install -r requirement.txt
4.  Download the LLaMA 3.2 model using Ollama
   You need to have Ollama installed on your machine.
   ```bash
     ollama run llama3

5. Set up your .env file
    ```bash
    LANGCHAIN_API_KEY=your-langchain-api-key
    LANGCHAIN_PROJECT=your-langchain-project-name
6. Run the app
    ```bash
    streamlit run app.py

```markdown
 💬 Sample Usage
Question: What is LangChain?

Response: LangChain is a framework for developing applications powered by language models...
