import json
import os

# Input: original YouCookII annotation JSON
input_json = "./youcookii_annotations_trainval.json"
output_json = "./Captions.json"

with open(input_json, "r") as f:
    data = json.load(f)

captions = {}

for video_id, info in data["database"].items():
    if "annotations" not in info:
        continue
    for ann in info["annotations"]:
        clip_id = ann["id"]
        sentence = ann["sentence"]
        clip_name = f"{video_id}_clip_{clip_id}.mp4"
        captions[clip_name] = sentence

with open(output_json, "w") as f:
    json.dump(captions, f, indent=2)

print(f"✅ Captions.json created with {len(captions)} entries")