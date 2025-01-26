# generate_root_index.py
import os

# HTML template
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>CSE101 MOSS Reports</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 20px;
            background-color: #f4f4f9;
        }
        h1 { 
            color: #0056b3; 
            border-bottom: 2px solid #0056b3;
            padding-bottom: 10px;
        }
        .pa-list {
            list-style: none;
            padding: 0;
        }
        .pa-list li {
            margin: 15px 0;
        }
        .pa-list a {
            text-decoration: none;
            color: #007BFF;
            font-size: 20px;
            transition: color 0.3s;
        }
        .pa-list a:hover {
            color: #0056b3;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>CSE101 MOSS Reports</h1>
    <ul class="pa-list">
        {pa_links}
    </ul>
</body>
</html>
"""

# Find all PA folders (e.g., PA1, PA2)
pa_folders = sorted([f for f in os.listdir() if f.startswith("PA") and os.path.isdir(f)])

# Generate links for each PA
pa_links = []
for pa in pa_folders:
    if os.path.exists(os.path.join(pa, "index.html")):
        pa_links.append(f'<li><a href="./{pa}/index.html">{pa} Reports</a></li>')

# Insert links into the HTML template
final_html = html_content.replace("{pa_links}", "\n".join(pa_links))

# Write to root index.html
with open("index.html", "w") as f:
    f.write(final_html)

print("Root index.html generated successfully!")