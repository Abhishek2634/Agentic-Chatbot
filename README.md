# 🤖 LangGraph Agentic AI Chatbot

A powerful, stateful AI application built with **LangGraph** and **Streamlit** that provides multiple AI-powered use cases including basic chatting, web-enhanced conversations, and automated AI news summarization.

## ✨ Features

- **🧠 Basic Chatbot**: Simple conversational AI using Groq's language models
- **🌐 Web-Enhanced Chatbot**: Intelligent chatbot with real-time web search capabilities
- **📰 AI News Summarizer**: Automated fetching and summarization of latest AI news with customizable timeframes
- **🎨 Interactive UI**: Clean, responsive Streamlit interface
- **⚡ Multiple LLM Support**: Groq integration with various model options
- **🔧 Configurable**: Easy configuration management through INI files
- **📊 Stateful Workflows**: Advanced agent behaviors using LangGraph

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Conda or virtual environment
- API Keys:
  - **Groq API Key** (Required for all use cases)
  - **Tavily API Key** (Required for web search and AI news features)

### Installation

1. **Clone the repository**

```bash
    git clone https://github.com/Abhishek2634/Agentic-Chatbot.git
    cd AgenticChatbot
```


2. **Create and activate virtual environment**
```bash
    conda create -n agentic-ai python=3.13
    conda activate agentic-ai

    # using venv
    python -m venv venv
    source venv/bin/activate    # On MacOS
    # On Windows: venv\Scripts\activate
```


3. **Install dependencies**

```bash
    pip install -r requirements.txt
```



### API Keys Setup

#### Get Groq API Key
1. Visit [Groq Console](https://console.groq.com)
2. Sign up/Login and create an API key
3. Enter it in the Streamlit sidebar when running the app

#### Get Tavily API Key (Optional - for web features)
1. Visit [Tavily](https://tavily.com)
2. Sign up and get your API key
3. Enter it in the Streamlit sidebar for web-enhanced features

## 🎯 Usage

### Running the Application

```bash
    streamlit run app.py
```


The app will open in your browser at `http://localhost:8501`

### Use Cases

#### 1. **Basic Chatbot**
- Simple conversational AI
- No additional API keys required beyond Groq
- Perfect for general Q&A and conversations

#### 2. **Chatbot With Web Search**
- Enhanced chatbot with real-time web search
- Requires both Groq and Tavily API keys
- Provides up-to-date information from the web

#### 3. **AI News Summarizer**
- Automated AI news fetching and summarization
- Choose from Daily, Weekly, or Monthly timeframes
- Saves summaries locally in markdown format
- Requires both Groq and Tavily API keys

## 📁 Project Structure
```bash
AgenticChatbot/
├── app.py # Main entry point
├── requirements.txt # Dependencies
├── .gitignore # Git ignore rules
├── AINews/ # Local news storage (gitignored)
│ └── .gitkeep # Keeps directory structure
├── src/
│ └── langgraph_agentic_ai/
│ ├── init.py
│ ├── main.py # Core application logic
│ ├── LLMS/
│ │ ├── init.py
│ │ └── groqllm.py # Groq LLM integration
│ ├── graph/
│ │ ├── init.py
│ │ └── graph_builder.py # LangGraph workflow builder
│ ├── nodes/
│ │ ├── init.py
│ │ ├── basic_chatbot_node.py
│ │ ├── chatbot_with_tool_node.py
│ │ └── ai_news_node.py # AI news processing
│ ├── tools/
│ │ ├── init.py
│ │ └── search_tool.py # Web search tools
│ ├── state/
│ │ ├── init.py
│ │ └── state.py # State management
│ └── ui/
│ ├── init.py
│ ├── uiconfigfile.py # Configuration management
│ ├── uiconfigfile.ini # App configuration
│ └── streamlitui/
| | ├── init.py
| | ├── loadui.py # UI components
| | |── display_result.py # Result display

```


## 🛠️ Dependencies

### Core Dependencies

- **langchain**
- **langgraph**
- **langchain_community**
- **langchain_core**
- **langchain-groq**
- **langchain_openai**
- **faiss-cpu**
- **streamlit**
- **tavily-python**



### Supporting Libraries
- **langchain**: LLM framework for building applications
- **langgraph**: Stateful multi-actor applications with LLMs
- **langchain-groq**: Groq integration for fast inference
- **streamlit**: Web UI framework
- **tavily-python**: Web search API integration
- **faiss-cpu**: Vector similarity search
- **langchain_community**: Community integrations
- **langchain_core**: Core abstractions
- **langchain_openai**: OpenAI integration



### Available Models

- **mixtral-8x7b-32768**: Powerful mixture of experts model
- **llama3-8b-8192**: Fast and efficient Llama 3 model
- **llama3-70b-8192**: Large Llama 3 model for complex tasks
- **gemma2-9b-it**: Google's Gemma 2 instruction-tuned model

## 🌐 Deployment

### Streamlit Community Cloud

1. **Push to GitHub** (ensure AINews folder structure is preserved with .gitkeep)
2. **Deploy on Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set entry point as `app.py`
   - Your app will be available at `https://your-app-name.streamlit.app`


### Quick Links

- 🌐 [Live Demo](agentic-ai-chatbott.streamlit.app/)
- 📚 [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- 🚀 [Streamlit Documentation](https://docs.streamlit.io/)
- 🤖 [Groq API](https://console.groq.com/)
- 🔍 [Tavily Search](https://tavily.com/)


**Built with ❤️ using LangGraph, Streamlit, and modern AI technologies**