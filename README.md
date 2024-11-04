# Dilbert Comic Transcripts (1989-2023)

This repository contains accessible text transcripts of *Dilbert* comics spanning from 1989 to 2023. The comics were discontinued in 2023, and the official website was taken down. This project aims to preserve the text from each comic's "speech bubbles", making it accessible for fans, researchers, and anyone who relies on screen readers for text content.

## Project Structure

- **dilbert_comics_transcripts.json**: The original JSON file containing comic metadata and transcripts.
- **dilbert_comics_transcripts_aria.html**: An HTML file including the JSON data with a quick full-text search function and date selector designed to be accessible with screen readers using ARIA tags.
- **scripts**: Python script used to generate a one-page HTML file from the JSON data.

## Accessibility

This project is optimized for accessibility:
- **ARIA Roles**: ARIA roles and landmarks are added to provide context to each comic transcript, ensuring smooth navigation for screen readers.
- **Time Tags**: Each comic’s date is marked using the `<time>` tag, making it clear when each comic was originally published.
- **Original Image Links**: Links to the original images are included for reference through Archive.org, as the website hosting the comics is no longer available.

## Sample JSON Structure

The JSON structure used in this project is as follows:
```json
{
    "YYYY-MM-DD": {
        "image": "comic_image.gif",
        "originalimageurl": "https://archive.org/...",
        "title": "",
        "transcript": "Comic transcript text"
    }
}
