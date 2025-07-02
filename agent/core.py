from fastapi import FastAPI, WebSocket
from .emotion_engine import EmotionEngine
from .self_discovery import generate_new_emotion_tag

app = FastAPI(title="Kuromi Agent")

agent = EmotionEngine()

@app.get("/status")
async def status():
    return {"state": agent.state.name}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    async for msg in ws.iter_text():
        state = agent.react(msg)
        new_tag = generate_new_emotion_tag()
        await ws.send_text(f"State: {state.name}, NewEmotion: {new_tag}")
