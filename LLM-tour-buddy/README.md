# LLM Tour Buddy

This project is an AI chatbot that provides tourist information about Turkey. It has two different versions that can run via a Streamlit interface and a terminal. The project was developed using LangChain and Ollama.

## Features

- **Interactive Chat Interface:** Provides a user-friendly web interface using Streamlit.
- **Terminal Support:** Can also be run via the command line.
- **Turkey-Focused Information:** Provides information about Turkey's history, tourist attractions, local cuisine, and travel tips.
- **Conversation Memory:** Remembers the chat history to produce more consistent answers.

## Setup

> **Note:** These instructions assume that you have already cloned the `LLM-Practices` repository and you are inside the `LLM-tour-buddy` directory in your terminal.

1.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # for macOS/Linux
    # venv\Scripts\activate  # for Windows
    ```

2.  **Install Required Libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Ollama:**
    This project uses Ollama, a local language model (LLM) runner. If you don't have Ollama installed on your system, download and install it from the [official website](https://ollama.com/).

4.  **Download the Language Model:**
    The project uses the `llama3.2:3b` model. You can download the model with the following command:
    ```bash
    ollama pull llama3.2:3b
    ```

## Usage

### Streamlit Interface

To start the web-based interface, run the following command:

```bash
streamlit run streamlit_tourist_bot.py
```

### Terminal Application

To run the chatbot via the terminal:

```bash
python tourist_bot_terminal.py
```

You can type `quit` to exit the application.

## Project Structure

-   `streamlit_tourist_bot.py`: The main file containing the Streamlit interface.
-   `tourist_bot_terminal.py`: The terminal-based chatbot.
-   `requirements.txt`: The file listing the project's dependencies.
-   `README.md`: This file. 