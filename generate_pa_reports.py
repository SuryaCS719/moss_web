#!/usr/bin/env python3
import os
import argparse

# Centralized PA file type configurations
PA_FILE_TYPES = {
    "PA1": {
        "List.c": ["list"],
        "Lex.c": ["lex"],
    },
    "PA2": {
        "List.c": ["list"],
        "FindPath.c": ["findpath"],
        "Graph.c": ["graph"],
    },
    "PA3": {
        "FindComponents.c": ["components", "findcomponents"],
        "Graph.c": ["graph"],
    },
    "PA4": {
        "Matrix.c": ["matrix"],
        "Sparse.c": ["sparse"],
        "List.c": ["list"],
    },
    "PA5": {
        "Shuffle.cpp": ["shuffle"],
        "List.cpp": ["list"],
    },
    "PA6": {
        "Arithmetic.cpp": ["arithmetic"],
        "BigInteger.cpp": ["biginteger"],
    },
    "PA7": {
        "Dictionary.cpp": ["dictionary"],
        "Order.cpp": ["order"],
    },
    "PA8": {
        "WordFrequency.cpp": ["wordfrequency"],
        "Dictionary.cpp": ["dictionary"],
        # "Order.cpp": ["order"],
    }
}

def generate_student_index(student_folder, pa_folder, reports):
    """Generate individual student index page with all their matches"""
    student_path = os.path.join(pa_folder, student_folder)
    os.makedirs(student_path, exist_ok=True)
    
    reports = sorted(reports, key=lambda x: os.path.basename(x))
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{student_folder} - {pa_folder.upper()} Reports</title>
    <style>
        :root {{
            --primary: #2c3e50;
            --secondary: #3498db;
            --accent: #e74c3c;
            --light: #ecf0f1;
            --dark: #2c3e50;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--light);
            color: var(--dark);
            line-height: 1.6;
            padding: 1rem;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            background: var(--primary);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .back-link {{
            color: var(--light);
            text-decoration: none;
            font-size: 0.9rem;
            display: inline-block;
            margin-top: 1rem;
        }}

        .report-list {{
            list-style: none;
            padding: 0;
            margin-top: 2rem;
        }}

        .report-item {{
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }}

        .report-link {{
            display: inline-block;
            padding: 0.5rem 1rem;
            background: var(--secondary);
            color: white !important;
            border-radius: 20px;
            text-decoration: none !important;
            transition: background 0.3s ease;
        }}

        .report-link:hover {{
            background: var(--accent);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 {student_folder}'s {pa_folder.upper()} Reports</h1>
            <a href="../index.html" class="back-link">← Back to {pa_folder.upper()} Overview</a>
        </div>

        <div class="report-list">
            {"".join([
                f'''<div class="report-item">
                    <h3>Report {i + 1}: {os.path.basename(report).split("_")[-1].split(".")[0]}.c</h3>
                    <a class="report-link" href="{os.path.basename(report)}">View Full Report</a>
                </div>'''
                for i, report in enumerate(reports)
            ])}
        </div>
    </div>
</body>
</html>"""

    output_path = os.path.join(student_path, "index.html")
    with open(output_path, "w") as f:
        f.write(html_content)

def generate_pa_index(pa_folder):
    file_types = PA_FILE_TYPES.get(pa_folder.upper(), {})
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MOSS Reports - {pa_folder.upper()}</title>
    <style>
        :root {{
            --primary: #2c3e50;
            --secondary: #3498db;
            --accent: #e74c3c;
            --light: #ecf0f1;
            --dark: #2c3e50;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--light);
            color: var(--dark);
            line-height: 1.6;
            padding: 1rem;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            background: var(--primary);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .search-container {{
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }}

        .search-box {{
            width: 100%;
            padding: 0.8rem 1.2rem;
            border: 2px solid var(--secondary);
            border-radius: 25px;
            font-size: 1rem;
            transition: all 0.3s ease;
        }}

        .search-box:focus {{
            outline: none;
            border-color: var(--primary);
        }}

        .table-wrapper {{
            overflow-x: auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            min-width: 800px;
        }}

        th, td {{
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}

        th {{
            background: var(--primary);
            color: white;
            font-weight: 600;
        }}

        td {{
            background: white;
        }}

        tr:hover td {{
            background: #f8f9fa;
        }}

        .report-count {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: var(--secondary);
            color: white;
            border-radius: 12px;
            font-size: 0.875rem;
            transition: background 0.3s ease;
        }}

        .report-count:hover {{
            background: var(--accent);
        }}

        .no-reports {{
            color: #a0aec0;
            font-style: italic;
        }}

        .student-link {{
            color: var(--secondary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }}

        .student-link:hover {{
            color: var(--accent);
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
    <div class="container">
        <div class="header">
            <h1>📊 {pa_folder.upper()} MOSS Reports</h1>
        </div>

        <div class="search-container">
            <input type="text" 
                   id="searchBar" 
                   class="search-box"
                   placeholder="Search by CruzID..."
                   onkeyup="filterTable()"
                   aria-label="Search student reports">
        </div>

        <div class="table-wrapper">
            <table id="reportTable">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Student CruzID</th>"""

    def extract_file_type(filename):
        for ft, keywords in file_types.items():
            if any(kw in filename.lower() for kw in keywords):
                return ft
        return None

    active_report_types = set()
    valid_student_folders = []

    if not os.path.exists(pa_folder):
        print(f"Error: {pa_folder} directory not found!")
        return

    for student_folder in os.listdir(pa_folder):
        student_path = os.path.join(pa_folder, student_folder)
        if os.path.isdir(student_path):
            valid_student_folders.append(student_folder)
            for item in os.listdir(student_path):
                if item.startswith("Matches for") and item.endswith(".html"):
                    file_type = extract_file_type(item)
                    if file_type:
                        active_report_types.add(file_type)

    columns = sorted(active_report_types)
    for file_type in columns:
        html_content += f'                <th>{file_type} Matches</th>\n'

    html_content += """                    </tr>
                </thead>
                <tbody>"""

    serial_no = 1
    for student_folder in sorted(valid_student_folders, key=lambda x: x.lower()):
        student_path = os.path.join(pa_folder, student_folder)
        report_counts = {ft: 0 for ft in columns}
        
        for item in os.listdir(student_path):
            if item.startswith("Matches for") and item.endswith(".html"):
                file_type = extract_file_type(item)
                if file_type in columns:
                    report_counts[file_type] += 1
        
        html_content += f"""                    <tr>
                        <td>{serial_no}</td>
                        <td><a href="{student_folder}/index.html" class="student-link">{student_folder}</a></td>"""
        
        for ft in columns:
            count = report_counts[ft]
            if count > 0:
                html_content += f'<td><a href="{student_folder}/index.html" class="report-count">{count}</a></td>'
            else:
                html_content += '<td><span class="no-reports">-</span></td>'
        
        html_content += "                    </tr>\n"
        serial_no += 1

    html_content += """                </tbody>
            </table>
        </div>
    </div>
</body>
</html>"""

    output_path = os.path.join(pa_folder, "index.html")
    with open(output_path, "w") as f:
        f.write(html_content)

    for student_folder in valid_student_folders:
        student_path = os.path.join(pa_folder, student_folder)
        student_reports = [
            os.path.join(student_path, item) 
            for item in os.listdir(student_path) 
            if item.startswith("Matches for") and item.endswith(".html")
        ]
        generate_student_index(student_folder, pa_folder, student_reports)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate modern MOSS report index for programming assignments'
    )
    parser.add_argument('--pa', help='PA folder to process (e.g., PA1, PA2)')
    parser.add_argument('--all', action='store_true', help='Process all PA directories')
    args = parser.parse_args()
    
    if args.all:
        for folder in os.listdir():
            if os.path.isdir(folder) and folder.upper().startswith("PA"):
                generate_pa_index(folder)
    elif args.pa:
        generate_pa_index(args.pa)
    else:
        print("Error: Please specify either --pa or --all")