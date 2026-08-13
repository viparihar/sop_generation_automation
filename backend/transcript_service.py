import json
from pathlib import Path


class TranscriptService:

    def get_transcript(self, meeting_id: str):

        with open(
            "data/meetings.json",
            "r",
            encoding="utf-8"
        ) as file:

            meetings = json.load(file)

        meeting = meetings.get(meeting_id)

        if not meeting:
            return None

        transcript_path = (
            Path("data/transcripts")
            / meeting["file"]
        )

        return transcript_path.read_text(
            encoding="utf-8"
        )