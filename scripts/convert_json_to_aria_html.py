import json

# Load JSON data from file
with open('dilber_comics_transcript.json', 'r') as f:
    data = json.load(f)

# Start the HTML content
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dilbert Comic Transcripts - Accessible</title>
</head>
<body>

    <header role="banner">
        <h1>Dilbert Comic Transcripts</h1>
        <p>Accessible text transcripts of *Dilbert* comics from 1989 to 2023</p>
    </header>

    <main role="main">
'''

# Generate HTML sections for each comic entry
for date, info in data.items():
    # Generate transcript paragraphs
    transcript_paragraphs = ''.join(f'<p>{line}</p>' for line in info['transcript'].split('\n') if line.strip())
    
    # Add a section for each comic
    html_content += f'''
        <section aria-labelledby="comic-{date}">
            <h2 id="comic-{date}">Comic Date</h2>
            <time datetime="{date}">{date}</time>
            <p><a href="{info['originalimageurl']}">View Original Image on Archive.org</a></p>
            <div role="document" aria-labelledby="comic-{date}-transcript">
                <h3 id="comic-{date}-transcript">Transcript</h3>
                {transcript_paragraphs}
            </div>
        </section>
    '''

# Close the HTML structure
html_content += '''
    </main>
</body>
</html>
'''

# Write to an HTML file
with open('dilbert_transcripts.html', 'w') as f:
    f.write(html_content)

print("HTML file generated as 'dilbert_transcripts.html'")