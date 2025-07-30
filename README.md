# LiveKit Voice Assistant

A conversational voice assistant built with LiveKit that uses local Ollama models for natural language processing, Deepgram for speech-to-text, and Cartesia for text-to-speech.

## Features

- Real-time voice conversations
- Local LLM processing with Ollama (Llama 3.2 1B model)
- High-quality speech recognition via Deepgram
- Natural-sounding voice synthesis with Cartesia
- Voice activity detection
- Pure conversational assistant (no external tools/functions)

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.8 or higher
- A LiveKit Cloud account (or self-hosted LiveKit server)
- API keys for required services

**Note:** This project assumes you have Ollama already downloaded and running on your system for the local LLM processing.

## Installation

### 1. Clone or Create the Project

Create a new directory for your project and save the main code as `main.py`.

### 2. Create Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

```bash
# Create virtual environment
python -m venv voice_assistant_env

# Activate virtual environment
# On Windows:
voice_assistant_env\Scripts\activate

# On macOS/Linux:
source voice_assistant_env/bin/activate
```

### 3. Install Python Dependencies

The `requirements.txt` file is already available in the repository. Simply install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file in your project root with the following variables:

```env
# LiveKit Configuration
LIVEKIT_URL=wss://your-livekit-project.livekit.cloud
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret

# Deepgram API Key (for Speech-to-Text)
DEEPGRAM_API_KEY=your-deepgram-api-key

# Cartesia API Key (for Text-to-Speech)
CARTESIA_API_KEY=your-cartesia-api-key
```

### 5. Get Required API Keys

#### LiveKit:
1. Visit [LiveKit Cloud](https://cloud.livekit.io)
2. Sign up for a free account
3. Create a new project
4. Copy your project URL, API key, and API secret from the project settings

#### Deepgram:
1. Visit [Deepgram](https://console.deepgram.com)
2. Sign up for a free account (includes $200 in free credits)
3. Navigate to the API Keys section in your dashboard
4. Create a new API key and copy it

#### Cartesia:
1. Visit [Cartesia](https://play.cartesia.ai)
2. Sign up for an account
3. Go to your account settings or API section
4. Generate an API key and copy it

## Configuration Changes Required

Before running the project, you need to make the following changes to ensure Ollama is properly configured:

### Ollama Setup (Prerequisite)
Ensure you have:
1. **Ollama installed** on your system
2. **Ollama server running**: Execute `ollama serve` in your terminal
3. **Llama 3.2 1B model downloaded**: Run `ollama pull llama3.2:1b`

### Verify Ollama Installation
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# List installed models
ollama list
# Should show llama3.2:1b in the list
```

## Running the Project

### 1. Activate Virtual Environment
```bash
# On Windows:
voice_assistant_env\Scripts\activate

# On macOS/Linux:
source voice_assistant_env/bin/activate
```

### 2. Ensure Ollama is Running
```bash
# Start Ollama server (if not already running)
ollama serve
```

### 3. Verify Ollama Model
```bash
ollama list
# Should show llama3.2:1b in the list
```

### 4. Run the LiveKit Agent
```bash
python main.py dev
```

The agent will start and connect to your LiveKit room.

### 5. Test the Voice Assistant

You can test the assistant using:

#### Option A: LiveKit Playground
1. Go to your LiveKit Cloud dashboard
2. Navigate to the Playground
3. Join a room and start talking

#### Option B: Custom Client Application
Create a simple client application or use LiveKit's example clients to connect to the room.

#### Option C: LiveKit CLI (for testing)
```bash
# Install LiveKit CLI
npm install -g livekit-cli

# Join a room for testing
livekit-cli join-room --url wss://your-project.livekit.cloud --api-key your-key --api-secret your-secret --room test-room --identity test-user
```

## Project Structure

```
your-project/
├── main.py              # Main agent code
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── voice_assistant_env/ # Virtual environment folder
```

## Configuration Options

### Modify the LLM Model
To use a different Ollama model, change the model parameter:
```python
llm=openai.LLM(
    model="llama3.2:3b",  # or any other Ollama model
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    temperature=0.7,
)
```

### Adjust Voice Settings
Change the Cartesia voice by modifying the voice ID:
```python
tts=cartesia.TTS(
    model="sonic-english", 
    voice="your-preferred-voice-id"
)
```

### Modify STT Language
Change the Deepgram language setting:
```python
stt=deepgram.STT(model="nova-2", language="es")  # for Spanish
```

## Troubleshooting

### Common Issues:

1. **Ollama connection errors**
   - Ensure Ollama is running: `ollama serve`
   - Check if the model is installed: `ollama list`
   - Verify the base URL is correct: `http://localhost:11434/v1`

2. **API key errors**
   - Double-check all API keys in your `.env` file
   - Ensure the `.env` file is in the same directory as `main.py`

3. **LiveKit connection issues**
   - Verify your LiveKit URL, API key, and secret
   - Check if your LiveKit project is active

4. **Audio issues**
   - Ensure your microphone is working and permitted
   - Check browser audio permissions

### Debug Mode
Run with debug logging:
```bash
LIVEKIT_LOG_LEVEL=debug python main.py dev
```

## Customization

### Adding Custom Instructions
Modify the agent instructions in `main.py`:
```python
agent = Agent(
    instructions="""Your custom instructions here...""",
    tools=[],
)
```

### Adding Tools/Functions
To add functionality, import and add tools to the agent:
```python
from livekit.agents import function_tool

@function_tool
async def get_weather(location: str):
    # Your weather function implementation
    pass

agent = Agent(
    instructions="...",
    tools=[get_weather],
)
```

## Performance Tips

- Use smaller models (like llama3.2:1b) for faster responses
- Adjust temperature (0.1-1.0) to control response creativity
- Consider using quantized models for better performance on limited hardware

## Support

For issues specific to:
- **LiveKit**: Check [LiveKit Documentation](https://docs.livekit.io)
- **Ollama**: Visit [Ollama GitHub](https://github.com/ollama/ollama)
- **Deepgram**: See [Deepgram Docs](https://developers.deepgram.com)
- **Cartesia**: Visit [Cartesia Documentation](https://docs.cartesia.ai)

## License

This project is open source. Please check individual service terms for API usage.
