from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from transcript_service import TranscriptService
from llm_service import SOPService
from models import MeetingRequest
from models import SOPModel

app = FastAPI(
    title="Meeting SOP Generator"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=False, # search why it is false
    allow_methods=["*"],
    allow_headers=["*"],
)

transcript_service = TranscriptService()

@app.get("/")
def basic():
    return "welcome"


@app.post(
    "/generate-sop",
    response_model=SOPModel
)
def generate_sop(
    request: MeetingRequest
):

    transcript = transcript_service.get_transcript(
        request.meeting_id
    )

    if transcript is None:

        raise HTTPException(
            status_code=404,
            detail="Meeting not found"
        )

    sop = SOPService.generate_sop(
        transcript
    )

    return sop