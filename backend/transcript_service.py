import json
from pathlib import Path


class TranscriptService:

    def get_transcript(self, meeting_id: str):
        BASE_DIR = Path(__file__).resolve().parent
        meetings_file = BASE_DIR / "data" / "meetings.json"

        with open(
            meetings_file,
            "r",
            encoding="utf-8"
        ) as file:

            meetings = json.load(file)

        meeting = meetings.get(meeting_id)

        if not meeting:
            return None

        transcript_path = (
            BASE_DIR
            / "data"
            / "transcripts"
            / meeting["file"]
        )

        return transcript_path.read_text(
            encoding="utf-8"
        )