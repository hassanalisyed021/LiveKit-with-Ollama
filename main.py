from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
)
from livekit.plugins import deepgram, silero, cartesia, openai
from dotenv import load_dotenv
import logging

load_dotenv()

# Remove tools for pure conversational assistant

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    # Create the agent with general assistant instructions
    agent = Agent(
        instructions="""You are a helpful and friendly voice assistant built by LiveKit. 
        
        You can help with:
        - Answering general questions
        - Having conversations
        - Providing information and explanations
        - Simple calculations
        - Telling the current time
        - Creative tasks like storytelling or jokes
        
        Keep your responses conversational, concise, and natural for voice interaction. 
        Be helpful, polite, and engaging. If you don't know something specific, 
        acknowledge it honestly and offer what help you can.""",
        tools=[],  # No tools - pure conversation
    )
    
    # Create session with Ollama via OpenAI plugin
    session = AgentSession(
        stt=deepgram.STT(model="nova-2", language="en"),
        llm=openai.LLM(
            model="deepseek-r1:1.5b",
            base_url="http://localhost:11434/v1",
            api_key="ollama",
            temperature=0.7,
        ),
        tts=cartesia.TTS(model="sonic-english", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"),
        vad=silero.VAD.load(),
    )

    # Start the session
    await session.start(agent=agent, room=ctx.room)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))