from loguru import logger
from dataclasses import asdict
from datetime import datetime
from persistence.db import dreams_collection
from uuid import uuid4
from entities import Dream, DreamDraft, Dreamer


def save_new_dream(draft: DreamDraft) -> Dream:
    dream_id = str(uuid4())
    now = str(datetime.now())

    dreamer = Dreamer(id=draft.dreamer.id,
                      name=draft.dreamer.name,
                      age=draft.dreamer.age)

    new_dream = Dream(id=dream_id,
                      date=draft.date,
                      dream=draft.dream,
                      dreamer=dreamer,
                      registered_at=now)

    logger.info(f"saving new dream of {dreamer.name}")

    try:
        dreams_collection.insert(asdict(new_dream), sync=True)
    except BaseException as e:
        logger.error(f"error at save the dream {dream_id}")
        e.with_traceback()

    return new_dream
