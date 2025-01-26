import os
import shutil
import re
import argparse

def organize_reports(working_dir):
    for file in os.listdir(working_dir):
        if file.endswith(".html") and file.startswith("Matches"):
            # Extract CruzIDs using regex (supports lowercase letters and numbers)
            cruz_ids = re.findall(r'_([a-z0-9]+)_pa\d+', file)
            
            if len(cruz_ids) != 2:
                print(f"Skipping {file} - could not find 2 CruzIDs")
                continue

            cruz_id1, cruz_id2 = cruz_ids

            # Process both students
            for cruz_id in [cruz_id1, cruz_id2]:
                student_folder = os.path.join(working_dir, cruz_id)
                os.makedirs(student_folder, exist_ok=True)

                # Copy HTML file
                src_html = os.path.join(working_dir, file)
                dest_html = os.path.join(student_folder, file)
                shutil.copy(src_html, dest_html)

                # Copy companion folder
                companion_folder = file.replace(".html", "_files")
                src_companion = os.path.join(working_dir, companion_folder)
                if os.path.exists(src_companion):
                    dest_companion = os.path.join(student_folder, companion_folder)
                    if os.path.exists(dest_companion):
                        shutil.rmtree(dest_companion)
                    shutil.copytree(src_companion, dest_companion)

            # Cleanup original files after copying to both students
            os.remove(src_html)
            if os.path.exists(src_companion):
                shutil.rmtree(src_companion)

            print(f"Created reports for {cruz_id1} and {cruz_id2} in {working_dir}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Organize MOSS reports for PA folders.")
    parser.add_argument("-d", type=str, required=True, help="Process a specific PA folder (e.g., PA1).")
    args = parser.parse_args()

    # Get the folder name from the user
    folder_name = args.d

    # Check if the folder exists in the current directory with exact case sensitivity
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        # Verify case sensitivity by comparing the folder name with the actual directory listing
        actual_folders = os.listdir()
        if folder_name not in actual_folders:
            print(f"Folder '{folder_name}' does not exist (case mismatch).")
            # print(f"Folder '{folder_name}' does not exist (case mismatch). Available folders: {', '.join(actual_folders)}")
        else:
            print(f"Processing {folder_name}...")
            organize_reports(folder_name)
    else:
        print(f"Folder '{folder_name}' does not exist in the current directory.")

if __name__ == "__main__":
    main()