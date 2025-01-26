# generate_pa_reports.py
import os
import argparse
from collections import defaultdict

def generate_pa_index(pa_folder):
    """Generates an index.html for a specific PA folder with MOSS reports."""
    
    # HTML template with dynamic PA number in title and header
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>MOSS Reports - {pa_folder.upper()}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            color: #0056b3;
        }}
        input[type="text"] {{
            width: 100%;
            padding: 10px;
            margin: 20px 0;
            box-sizing: border-box;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #0056b3;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        a {{
            text-decoration: none;
            color: #007BFF;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
    <script>
        function filterTable() {{
            const input = document.getElementById("searchBar").value.toLowerCase();
            const rows = document.querySelectorAll("#reportTable tbody tr");
            rows.forEach(row => {{
                const name = row.querySelector("td:nth-child(2)").textContent.toLowerCase();
                row.style.display = name.includes(input) ? "" : "none";
            }});
        }}
    </script>
</head>
<body>
    <h1>MOSS Reports for {pa_folder.upper()}</h1>
    <p>Search for a student's CruzID:</p>
    <input type="text" id="searchBar" placeholder="Type to search..." onkeyup="filterTable()">
    <table id="reportTable">
        <thead>
            <tr>
                <th>#</th>
                <th>Student CruzID</th>"""

    # File type detection logic
    def extract_file_type(filename):
        for file_type in ["List.c", "Lex.c", "Matrix.c"]:
            if file_type in filename:
                return file_type
        return None

    # First pass: Identify all file types and their counts
    file_types = defaultdict(int)
    valid_student_folders = []

    # Validate PA folder exists
    if not os.path.exists(pa_folder):
        print(f"Error: {pa_folder} directory not found!")
        return

    for student_folder in os.listdir(pa_folder):
        student_path = os.path.join(pa_folder, student_folder)
        if os.path.isdir(student_path):
            valid_student_folders.append(student_folder)
            type_counts = defaultdict(int)
            for item in os.listdir(student_path):
                if item.startswith("Matches for") and item.endswith(".html"):
                    file_type = extract_file_type(item)
                    if file_type:
                        type_counts[file_type] += 1
            for ft, count in type_counts.items():
                file_types[ft] = max(file_types[ft], count)

    # Generate column headers
    columns = []
    for file_type in sorted(file_types.keys()):
        count = file_types[file_type]
        if count == 1:
            columns.append((file_type, 1))
            html_content += f'                <th>{file_type} Report</th>\n'
        else:
            for i in range(1, count + 1):
                columns.append((file_type, i))
                html_content += f'                <th>{file_type} Report {i}</th>\n'

    html_content += """            </tr>
        </thead>
        <tbody>
"""

    # Populate table rows
    serial_no = 1
    for student_folder in sorted(valid_student_folders):
        student_path = os.path.join(pa_folder, student_folder)
        report_links = {col: "N/A" for col in columns}
        
        files = defaultdict(list)
        for item in os.listdir(student_path):
            if item.startswith("Matches for") and item.endswith(".html"):
                file_type = extract_file_type(item)
                if file_type:
                    files[file_type].append(item)
        
        # Sort files for each type
        for ft in files:
            files[ft].sort()
        
        # Assign files to columns
        for ft in files:
            for i, file in enumerate(files[ft], 1):
                col = (ft, i)
                if col in report_links:
                    report_links[col] = f'<a href="./{student_folder}/{file}">View Report</a>'
        
        # Add row to table
        html_content += f"""            <tr>
                <td>{serial_no}</td>
                <td>{student_folder}</td>
"""
        for col in columns:
            html_content += f'                <td>{report_links[col]}</td>\n'
        
        html_content += "            </tr>\n"
        serial_no += 1

    # Close HTML structure
    html_content += """        </tbody>
    </table>
</body>
</html>
"""

    # Write to PA folder's index.html
    output_path = os.path.join(pa_folder, "index.html")
    with open(output_path, "w") as f:
        f.write(html_content)
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate MOSS report index.html for programming assignments',
        epilog='Example: python generate_pa_reports.py --pa PA1'
    )
    parser.add_argument('--pa', required=True, 
                      help='PA folder to process (e.g., PA1, PA2)')
    args = parser.parse_args()
    
    generate_pa_index(args.pa)