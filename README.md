# LangChain + Ollama + Streamlit Demo

This is a demo app using [LangChain](https://www.langchain.com/) and [Ollama](https://ollama.com/) with a Streamlit frontend.

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
4. Set up your .env file
    ```bash
    LANGCHAIN_API_KEY=your-langchain-api-key
    LANGCHAIN_PROJECT=your-langchain-project-name
5. Run the app
    ```bash
    streamlit run app.py

```markdown
## 💬 Sample Usage
**Question:** What is LangChain?

**Response:** LangChain is a framework for developing applications powered by language models...
