# MOSS Web Dashboard

A web-based dashboard for viewing MOSS (Measure of Software Similarity) reports for programming assignments (PAs). This project automates the generation of HTML reports and provides a centralized interface for accessing them.
---

### Access the Dashboard

You can access the MOSS Web Dashboard at the following URL:

[**MOSS Web Dashboard**](https://cse101-pa-moss-reports-w25.netlify.app/)


### Login Credentials

- **Username**: `cse101-admin-w25`
- **Password**: `admin@cse101-w25`
---

## Features
- **Dynamic Report Generation**: Automatically generates `index.html` files for each PA folder.
- **Searchable Interface**: Allows searching for student reports by CruzID.
- **Scalable**: Supports multiple PAs (e.g., PA1, PA2, etc.) with minimal configuration.
- **Netlify Integration**: Automatically deploys updates when changes are pushed to GitHub.
---

## Repository Structure
```
moss_web/
├── PA1/ # Reports for Programming Assignment 1
│ ├── student1/ # Student folder (e.g., CruzID)
│ │ └── ... # MOSS report files
│ ├── index.html # Auto-generated dashboard for PA1
├── PA2/ # Reports for Programming Assignment 2
│ ├── student2/ # Student folder
│ │ └── ... # MOSS report files
│ ├── index.html # Auto-generated dashboard for PA2
├── generate_pa_reports.py # Script to generate PA-specific dashboards
├── generate_root_index.py # Script to generate the root dashboard
├── index.html # Root dashboard (links to all PAs)
└── README.md # This file
```

---

## Setup

### Prerequisites
- Python 3.x
- Git
- Netlify account (for deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/SuryaCS719/moss_web.git
   cd moss_web
   ```

2. Add MOSS reports:
   - Place student reports in the appropriate PA folder (e.g., PA1/student1/).
   - Ensure report filenames follow the format: Matches for <filename>.html.

3. Generate dashboards:
   Run the scripts to generate index.html files:
   ```bash
   python3 generate_pa_reports.py --pa PA1
   python3 generate_pa_reports.py --pa PA2
   python3 generate_root_index.py
   ```

4. Deploy to Netlify:
   Push changes to GitHub:
   ```bash
   git add .
   git commit -m "Updated reports"
   git push origin main
   ```
   Netlify will automatically build and deploy the site.

## Usage
- Access the root dashboard at: https://<your-netlify-site>.netlify.app
- Navigate to specific PAs (e.g., PA1, PA2) using the links on the root page.
- Use the search bar to filter reports by student CruzID.

## Scripts

### generate_pa_reports.py
- Generates an index.html file for a specific PA folder.
- Usage:
  ```bash
  python3 generate_pa_reports.py --pa PA1
  ```

### generate_root_index.py
- Generates the root index.html file linking to all PA dashboards.
- Usage:
  ```bash
  python3 generate_root_index.py
  ```

## Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- MOSS for code similarity detection.
- Netlify for hosting and continuous deployment.
