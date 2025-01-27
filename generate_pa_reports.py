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
        "FindComponents.c": ["components", "findcomponents"],  # Multiple keywords for flexibility
        "Graph.c": ["graph"],
    },
    "PA4": {
        "Matrix.c": ["matrix"],
        "Sparse.c": ["sparse"],
        "List.c": ["list"],
    }
    # Add more PAs as needed
}



def generate_student_index(student_folder, pa_folder, reports):
    """Generate individual student index page with all their matches"""
    student_path = os.path.join(pa_folder, student_folder)
    os.makedirs(student_path, exist_ok=True)
    
    # Sort reports for better readability
    reports = sorted(reports, key=lambda x: os.path.basename(x))
    
    # Modern student page template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{student_folder} - {pa_folder.upper()} Reports</title>
    <style>
        :root {{
            --primary: #2c3e50;       /* Dark Blue */
            --secondary: #3498db;     /* Bright Blue */
            --accent: #e74c3c;        /* Red */
            --light: #ecf0f1;         /* Light Gray */
            --dark: #2c3e50;          /* Dark Blue */
            --success: #2ecc71;       /* Green */
            --warning: #f1c40f;       /* Yellow */
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

        .header h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}

        .back-link {{
            color: var(--light);
            text-decoration: none;
            font-size: 0.9rem;
            display: inline-block;
            margin-top: 1rem;
        }}

        .back-link:hover {{
            text-decoration: underline;
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
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            margin-bottom: 1.5rem;
        }}

        .report-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }}

        .report-item h3 {{
            font-size: 1.25rem;
            margin-bottom: 1rem;
            color: var(--primary);
        }}

        .report-link {{
            display: inline-block;
            padding: 0.5rem 1rem;
            background: var(--secondary);
            color: white !important;
            border-radius: 20px;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            text-decoration: none !important;
        }}

        .report-link:hover {{
            background: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        @media (max-width: 768px) {{
            .header {{
                padding: 1.5rem;
            }}

            .report-item {{
                padding: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 {student_folder}'s {pa_folder.upper()} Reports</h1>
            <a href="../index.html" class="back-link">← Back to {pa_folder.upper()} Overview</a>
        </div>

        <ul class="report-list">
            {"".join([
                f'''<li class="report-item">
                    <h3>Report {i + 1}: {os.path.basename(report).split("_")[-1].split(".")[0]}.c</h3>
                    <a class="report-link" href="{os.path.basename(report)}">View Full Report</a>
                </li>'''
                for i, report in enumerate(reports)
            ])}
        </ul>
    </div>
</body>
</html>"""

    # Write to student's index.html
    output_path = os.path.join(student_path, "index.html")
    with open(output_path, "w") as f:
        f.write(html_content)
    print(f"Generated student index for {student_folder} at {output_path}")

def generate_pa_index(pa_folder):
    """Generates a modern index.html for PA folders with enhanced UI/UX"""
    
    # Dynamically get file types for this PA
    file_types = PA_FILE_TYPES.get(pa_folder.upper(), {})
    
    # HTML template with dynamic content
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
            box-shadow: 0 0 8px rgba(52,152,219,0.3);
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
            border: 2px solid var(--primary);
        }}

        th, td {{
            padding: 1rem;
            text-align: left;
            border-bottom: 2px solid var(--primary);
            border-right: 1px solid #ddd;
        }}

        th {{
            background: var(--primary);
            color: white;
            position: sticky;
            top: 0;
            white-space: nowrap;
            border-right: 1px solid rgba(255,255,255,0.1);
        }}

        th:last-child, td:last-child {{
            border-right: none;
        }}

        tr:hover {{
            background: #f8f9fa;
        }}

        .report-link {{
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: var(--secondary);
            color: white !important;
            border-radius: 20px;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            text-decoration: none !important;
            margin: 2px;
        }}

        .report-link:hover {{
            background: var(--primary);
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .na {{
            color: #95a5a6;
            font-style: italic;
        }}

        .no-results {{
            text-align: center;
            padding: 2rem;
            color: #95a5a6;
            display: none;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 0.5rem;
            }}
            
            .header {{
                padding: 1.5rem;
                margin-bottom: 1rem;
            }}
            
            th, td {{
                padding: 0.8rem;
            }}
        }}
    </style>
    <script>
        function filterTable() {{
            const input = document.getElementById("searchBar").value.toLowerCase();
            const rows = document.querySelectorAll("#reportTable tbody tr");
            let visibleCount = 0;
            
            rows.forEach(row => {{
                const name = row.querySelector("td:nth-child(2)").textContent.toLowerCase();
                const isVisible = name.includes(input);
                row.style.display = isVisible ? "" : "none";
                if(isVisible) visibleCount++;
            }});
            
            document.getElementById("noResults").style.display = visibleCount ? "none" : "block";
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

    # First pass: Identify all file types and their counts
    active_report_types = set()
    valid_student_folders = []

    if not os.path.exists(pa_folder):
        print(f"Error: {pa_folder} directory not found!")
        return

    for student_folder in os.listdir(pa_folder):
        student_path = os.path.join(pa_folder, student_folder)
        if os.path.isdir(student_path):
            print(f"Processing student: {student_folder}")
            valid_student_folders.append(student_folder)
            for item in os.listdir(student_path):
                if item.startswith("Matches for") and item.endswith(".html"):
                    print(f"Found report: {item}")
                    file_type = extract_file_type(item)
                    if file_type:
                        active_report_types.add(file_type)

    # Generate column headers
    columns = sorted(active_report_types)
    for file_type in columns:
        html_content += f'                <th>{file_type}</th>\n'

    html_content += """                    </tr>
                </thead>
                <tbody>"""

    # Populate table rows
    serial_no = 1
    for student_folder in sorted(valid_student_folders, key=lambda x: x.lower()):
        student_path = os.path.join(pa_folder, student_folder)
        report_links = {ft: [] for ft in columns}
        
        # Collect reports
        for item in os.listdir(student_path):
            if item.startswith("Matches for") and item.endswith(".html"):
                file_type = extract_file_type(item)
                if file_type in columns:
                    report_path = os.path.join(student_folder, item).replace(' ', '%20')
                    report_links[file_type].append(f'<a class="report-link" href="{report_path}">View</a>')
        
        # Add row to table
        html_content += f"""                    <tr>
                        <td>{serial_no}</td>
                        <td><a href="{student_folder}/index.html">{student_folder}</a></td>"""
        
        for ft in columns:
            links = report_links[ft]
            if links:
                html_content += f'<td>{", ".join(links[:3])}</td>'
            else:
                html_content += '<td class="na">-</td>'
        
        html_content += "                    </tr>\n"
        serial_no += 1

    # Close HTML structure
    html_content += f"""                </tbody>
            </table>
            <div id="noResults" class="no-results">
                🕵️ No matching students found
            </div>
        </div>
    </div>
</body>
</html>"""

    # Write to PA folder's index.html
    output_path = os.path.join(pa_folder, "index.html")
    with open(output_path, "w") as f:
        f.write(html_content)
    print(f"Successfully generated modern report index at {output_path}")

    # Generate individual student index pages
    for student_folder in valid_student_folders:
        student_path = os.path.join(pa_folder, student_folder)
        student_reports = [
            os.path.join(student_path, item) 
            for item in os.listdir(student_path) 
            if item.startswith("Matches for") and item.endswith(".html")
        ]
        
        # Generate individual student index
        generate_student_index(student_folder, pa_folder, student_reports)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate modern MOSS report index for programming assignments'
    )
    parser.add_argument('--pa', help='PA folder to process (e.g., PA1, PA2)')
    parser.add_argument('--all', action='store_true', help='Process all PA directories')
    args = parser.parse_args()
    
    if args.all:
        # Process all PA folders with file type configs
        for folder in os.listdir():
            if os.path.isdir(folder) and folder.upper().startswith("PA"):
                generate_pa_index(folder)
    elif args.pa:
        # Process single PA folder
        generate_pa_index(args.pa)
    else:
        print("Error: Please specify either --pa or --all")