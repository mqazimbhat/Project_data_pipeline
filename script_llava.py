import os
import json
import random

# -------- CONFIG --------
video_dir = "./Trimmed_Clips"
output_json = "./LLaVA/llava_video_data.json"
caption_json = "./Captions.json"  # Dictionary: { "clip_filename.mp4": "caption" }
questions = [
    "Please explain what is going on in the video.",
    "Describe the activity shown in the video.",
    "What action is being performed?",
    "What is happening in this clip?",
    "Summarize the video content."
]
# ------------------------

# Load captions
with open(caption_json, "r") as f:
    caption_data = json.load(f)

# Create LLaVA-style list
llava_data = []
for clip_file, caption in caption_data.items():
    clip_path = os.path.join(video_dir, clip_file)
    if not os.path.exists(clip_path):
        continue

    question = random.choice(questions)
    conversation = [
        {
            "from": "human",
            "value": f"<video> {clip_file}\n{question}"
        },
        {
            "from": "gpt",
            "value": caption
        }
    ]
    llava_data.append(conversation)

# Save to JSON
os.makedirs(os.path.dirname(output_json), exist_ok=True)
with open(output_json, "w") as f:
    json.dump(llava_data, f, indent=2)

print(f"✅ LLaVA video-format JSON saved to: {output_json}")