import time
from flask import Flask, request, json, jsonify
from .dream import Dream, DreamDraft, DreamerDraft

app = Flask("Dreamer Simple API")


def save_dream(dream: DreamDraft) -> str:
    dream.dreamer = DreamerDraft(**dream.dreamer)
    print(f"saving your dream, dear {dream.dreamer.name}.")
    time.sleep(1.72)
    saved_dream = Dream()
    return saved_dream.id


@app.route('/register-dream', methods=["POST"])
def hello_world():
    obj: DreamDraft = DreamDraft(**json.loads(request.data))
    dream_id = save_dream(obj)
    res = jsonify({"id": dream_id})
    return res
