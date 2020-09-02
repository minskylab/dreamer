from datetime import datetime
from flask import Flask, request, json, jsonify
from .dream import Dream, DreamDraft, Dreamer, DreamerDraft
from persistence.db import dreams_collection


app = Flask("Dreamer Simple API")


def save_dream(dream: DreamDraft) -> str:
    dream.dreamer = DreamerDraft(**dream.dreamer)
    print(f"saving dream of {dream.dreamer.name}.")

    now = str(datetime.now())
    dreamer = Dreamer(name=dream.dreamer.name, age=dream.dreamer.age)
    new_dream = Dream(date=now, dreamer=dreamer)
    dreams_collection.insert(new_dream)

    saved_dream = Dream()
    return saved_dream.id


@app.route('/register-dream', methods=["POST"])
def hello_world():
    obj: DreamDraft = DreamDraft(**json.loads(request.data))
    dream_id = save_dream(obj)
    res = jsonify({"id": dream_id})
    return res
