from datetime import datetime
from persistence.dreams import save_new_dream
from entities import Dream, DreamDraft, Dreamer, DreamerDraft
from persistence.db import dreams_collection
from dataclasses import asdict

# Using Starlette

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

def save_dream(dream: DreamDraft) -> str:
    dream.dreamer = DreamerDraft(**dream.dreamer)
    print(f"saving dream of {dream.dreamer.name}.")
    new_dream = save_new_dream(dream)
    return new_dream.id

app = Starlette(debug=True)

@app.route('/register-dream', methods=["POST"])
async def register_dream(request):
    data = await request.json()
    print(data['dreamer'])
    obj: DreamDraft = DreamDraft(data['dreamer'], data['dream'], data['date'])
    dream_id = save_dream(obj)
    res = JSONResponse({"id": dream_id})
    return res

