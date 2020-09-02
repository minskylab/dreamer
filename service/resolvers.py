from datetime import datetime
from persistence.dreams import save_new_dream
from flask import Flask, request, json, jsonify
from entities import Dream, DreamDraft, Dreamer, DreamerDraft
from persistence.db import dreams_collection
from dataclasses import asdict

app = Flask("Dreamer Simple API")


def save_dream(dream: DreamDraft) -> str:
    dream.dreamer = DreamerDraft(**dream.dreamer)
    print(f"saving dream of {dream.dreamer.name}.")
    new_dream = save_new_dream(dream)
    return new_dream.id


@app.route('/register-dream', methods=["POST"])
def hello_world():
    obj: DreamDraft = DreamDraft(**json.loads(request.data))
    dream_id = save_dream(obj)
    res = jsonify({"id": dream_id})
    return res
