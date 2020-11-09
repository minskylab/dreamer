from loguru import logger
from dataclasses import asdict
from datetime import datetime
from persistence.db import cases_collection
from uuid import uuid4
from entities import Case
from processing.headband_process import headband_verify
from processing.house_process import house_verify
from processing.name_process import name_verify


def processcase(Case_a) -> Case:
    Case_a['headband_photo']=headband_verify(Case_a['headband_photo'])
    Case_a['house_photo']=house_verify(Case_a['house_photo'])
    Case_a['client_name']=name_verify(Case_a['client_name'])

    return Case_a
