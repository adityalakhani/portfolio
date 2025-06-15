
title: Automate the boring stuffdesc: Organize screenshots with python and a dash of AIdate_posted: February 25, 2025tags: [python, automation]slug: automate-the-boring-stuff
Automate the Boring Stuff
Tired of organizing screenshots manually? Let's automate it with Python and a sprinkle of AI!
Step 1: Organize Files
Use Python's os module to scan a directory and move screenshots to folders based on their creation date.
import os
import shutil
from datetime import datetime

def organize_screenshots(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg')):
            filepath = os.path.join(directory, filename)
            creation_time = os.path.getctime(filepath)
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m')
            dest_folder = os.path.join(directory, date_folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_folder, filename))

organize_screenshots("/path/to/screenshots")

Step 2: Add AI for Tagging
Use an AI model (e.g., via OpenAI API) to generate tags for each screenshot based on its content.
import openai

def tag_screenshot(image_path):
    # Placeholder for AI-based image tagging
    response = openai.Image.create(
        prompt=f"Describe the content of this image: {image_path}",
        n=1
    )
    tags = response['data'][0]['text'].split(',')
    return [tag.strip() for tag in tags]

Automate your workflow and save time!
