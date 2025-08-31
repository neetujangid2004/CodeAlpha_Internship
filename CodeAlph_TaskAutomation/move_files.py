# Move all .jpg files from one folder to another

import os
import shutil

source_folder = "/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlph_TaskAutomation/source_folder"    
destination_folder = "/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlph_TaskAutomation/destination_folder"

os.makedirs(destination_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        shutil.move(os.path.join(source_folder, file_name), os.path.join(destination_folder, file_name))
        print(f"Moved: {file_name}")

print("All .jpg files moved successfully!")