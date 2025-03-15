# ChainLite - AI-Powered Chatbot Framework

ChainLite is a comprehensive Python framework designed to simplify the development and deployment of AI-powered chatbot applications. Built on top of Chainlit and supporting Google's Gemini models, ChainLite provides developers with a robust toolkit for creating intelligent conversational interfaces with minimal setup and configuration.

## Overview

ChainLite bridges the gap between complex AI model integration and practical chatbot development. It offers a structured approach to building conversational AI applications while maintaining flexibility for customization. The framework is particularly well-suited for:

- Educational chatbots
- Customer support systems
- Personal AI assistants
- Knowledge base query systems
- Code assistance tools

## Key Features

### Core Functionality

- **Chainlit Integration**: Out-of-the-box support for Chainlit's web interface, enabling rapid deployment of chat UIs
- **Gemini Model Support**: Native integration with Google's Gemini models through OpenAI-compatible API endpoints
- **Context Management**: Automatic chat history tracking and context preservation for coherent conversations
- **Streaming Responses**: Real-time token streaming for natural conversation flow
- **Error Handling**: Comprehensive error handling and logging for production environments

### Development Features

- **Agent Configuration**: Simple setup of AI agents with customizable instructions and behaviors
- **Environment Management**: Easy configuration through .env files for API keys and model settings
- **Session Management**: Built-in session handling for multi-user support
- **Modular Architecture**: Clean separation of concerns for easy extension and customization
- **Lightweight Design**: Minimal dependencies and efficient resource utilization

## Getting Started

### Prerequisites

Before using ChainLite, ensure your system meets these requirements:

- Python 3.8 or higher
- Google Gemini API key
- Basic understanding of Python and chatbot development
- Node.js (for Chainlit frontend)

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install ChainLite:
   ```bash
   pip install chainlite
   ```

3. Set up your environment variables:
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   echo "MODEL_NAME=gemini-1.5-flash" >> .env
   ```

### Basic Usage

1. Create a new chatbot script:
   ```python
   from chainlite import Chatbot

   chatbot = Chatbot(
       name="AI Assistant",
       instructions="You are a helpful assistant",
       model="gemini-1.5-flash"
   )

   if __name__ == "__main__":
       chatbot.run()
   ```

2. Start the chatbot:
   ```bash
   chainlit run chatbot.py
   ```

## Advanced Features

### Custom Agent Configuration

ChainLite allows for detailed agent customization:
