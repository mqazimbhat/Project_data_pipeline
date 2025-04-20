import os
import json
# from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip

# -------- CONFIG --------
video_dir = "./Videos"  # Folder containing your full YouCook2 videos (renamed to video_id.mp4)
output_dir = "./Trimmed_Clips"  # Where to save the trimmed clips
json_path = "./youcookii_annotations_trainval.json"  # Path to your annotation JSON

# ------------------------

# Load JSON annotations
with open(json_path, "r") as f:
    data = json.load(f)

os.makedirs(output_dir, exist_ok=True)

for video_id, video_data in data["database"].items():
    video_file = os.path.join(video_dir, f"{video_id}.mp4")
    if not os.path.exists(video_file):
        print(f"Skipping {video_id} - file not found.")
        continue

    print(f"Processing {video_id}...")
    try:
        video = VideoFileClip(video_file)
        for ann in video_data["annotations"]:
            start, end = ann["segment"]
            clip_id = ann["id"]
            sentence = ann["sentence"]

            output_filename = f"{video_id}_clip_{clip_id}.mp4"
            output_path = os.path.join(output_dir, output_filename)

            # Trim and write clip
            clip = video.subclip(start, end)
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)
        video.close()
    except Exception as e:
        print(f"Error processing {video_id}: {e}")