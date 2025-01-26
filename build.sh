#!/bin/bash

# Find all PA folders (e.g., PA1, PA2, PA3)
pa_folders=$(ls -d PA*/)

# Generate index.html for each PA folder
for pa in $pa_folders; do
    pa=${pa%/}  # Remove trailing slash
    echo "Generating reports for $pa..."
    python3 generate_pa_reports.py --pa $pa
done

# Generate root index.html
echo "Generating root index.html..."
python3 generate_root_index.py
