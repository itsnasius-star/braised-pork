from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import sys


def extract_video_id(url_or_id: str) -> str:
    """Extract YouTube video ID from a URL or return the raw ID."""
    if "youtube.com" in url_or_id:
        parsed_url = urlparse(url_or_id)
        return parse_qs(parsed_url.query).get("v", [None])[0]
    if "youtu.be" in url_or_id:
        return urlparse(url_or_id).path.strip("/")
    return url_or_id


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript text from YouTube."""
    api = YouTubeTranscriptApi()
    fetched_transcript = api.fetch(video_id)
    lines = [snippet.text for snippet in fetched_transcript]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/fetch_youtube_transcript.py <youtube_url_or_id> <output_file>")
        sys.exit(1)

    video_url_or_id = sys.argv[1]
    output_file = Path(sys.argv[2])
    video_id = extract_video_id(video_url_or_id)

    if not video_id:
        print("Could not extract video ID.")
        sys.exit(1)

    transcript_text = fetch_transcript(video_id)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(transcript_text, encoding="utf-8")

    print(f"Transcript saved to {output_file}")


if __name__ == "__main__":
    main()