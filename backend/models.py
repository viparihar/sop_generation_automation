from pydantic import BaseModel
from typing import List


class MeetingRequest(BaseModel):
    meeting_id: str


class SOPModel(BaseModel):

    title: str

    objective: str

    scope: str

    roles_and_responsibilities: List[str]

    procedure_steps: List[str]

    risks_and_considerations: List[str]

    follow_up_actions: List[str]