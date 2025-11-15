# 🔄 MOSS Web Dashboard Workflow Diagram

This document provides visual representations of how the MOSS Web Dashboard works.

---

## 📊 Complete System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    CSE101 STUDENT SUBMISSIONS                   │
│  👨‍💻 100+ students submit code files (List.c, Graph.c, etc.)     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│                    MOSS ANALYSIS (External)                     │
│  🔍 Stanford's MOSS tool compares all submissions                │
│  📊 Identifies code similarities and generates reports          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│                    RAW MOSS REPORTS OUTPUT                      │
│  📄 Matches for _winter25_alice_pa1_List.c and                  │
│      _winter25_bob_pa1_List.c.html                              │
│  📄 Matches for _winter25_alice_pa1_List.c and                  │
│      _winter25_charlie_pa1_List.c.html                          │
│  📄 ... (dozens more files)                                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│              📂 STEP 1: org_reports.py                          │
│  🎯 Organizes messy reports into student folders                │
│                                                                  │
│  BEFORE:                          AFTER:                        │
│  PA1/                             PA1/                          │
│  ├── report1.html                 ├── alice/                    │
│  ├── report2.html        →        │   ├── report1.html          │
│  └── report3.html                 │   └── report2.html          │
│                                   ├── bob/                      │
│                                   │   ├── report1.html          │
│                                   │   └── report3.html          │
│                                   └── charlie/                  │
│                                       └── report2.html          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│         📊 STEP 2: generate_pa_reports.py                       │
│  🎯 Creates overview tables and student index pages             │
│                                                                  │
│  CREATES:                                                        │
│  ├── PA1/index.html ← Table of all students                     │
│  ├── PA1/alice/index.html ← Alice's reports list                │
│  ├── PA1/bob/index.html ← Bob's reports list                    │
│  └── PA1/charlie/index.html ← Charlie's reports list            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│         🏠 STEP 3: generate_root_index.py                       │
│  🎯 Creates the main homepage with links to all PAs             │
│                                                                  │
│  CREATES:                                                        │
│  └── index.html ← Main dashboard with PA1-PA8 buttons           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│         🔍 STEP 4: check_duplicate_usernames.py (Optional)      │
│  🎯 Finds students flagged multiple times                       │
│                                                                  │
│  OUTPUT:                                                         │
│  Students appearing 2+ times:                                   │
│  - alice: 3 times (PA1, PA3, PA5)                               │
│  - bob: 2 times (PA1, PA2)                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│              🚀 STEP 5: Git + Netlify Deployment                │
│  🎯 Publishes website to the internet                           │
│                                                                  │
│  PROCESS:                                                        │
│  1. git add . ─────→ Stages all files                           │
│  2. git commit ────→ Saves snapshot                             │
│  3. git push ──────→ Uploads to GitHub                          │
│  4. Netlify ───────→ Auto-builds website                        │
│  5. LIVE! 🎉 ─────→ https://cse101-pa-moss-reports-w25...      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ File Organization Structure

```
moss_web/ (Root Directory)
│
├── 📄 index.html ───────────────→ Main homepage with PA buttons
├── 📄 README.md ────────────────→ Technical documentation
├── 📄 BEGINNER_GUIDE.md ────────→ High school friendly guide
├── 📄 flaggedStudentsPresent.txt → List of flagged students
│
├── 🐍 generate_pa_reports.py ───→ Creates PA overview pages
├── 🐍 generate_root_index.py ───→ Creates homepage
├── 🐍 org_reports.py ───────────→ Organizes reports by student
├── 🐍 check_duplicate_usernames.py → Finds repeat offenders
│
├── 🖼️ faviconM.png ─────────────→ Website icon
├── 🖼️ faviconM.ico ─────────────→ Website icon (IE/Edge)
├── 🖼️ faviconM.jpg ─────────────→ Website icon (backup)
│
├── 📁 PA1/ ─────────────────────→ Programming Assignment 1
│   ├── 📄 index.html ───────────→ PA1 overview table
│   ├── 📁 alice/
│   │   ├── 📄 index.html ───────→ Alice's reports list
│   │   ├── 📄 match_report_1.html → MOSS comparison
│   │   └── 📁 match_report_1_files/ → Images/visualizations
│   ├── 📁 bob/
│   │   └── ... (same structure)
│   └── 📁 charlie/
│       └── ... (same structure)
│
├── 📁 PA2/ ─────────────────────→ Programming Assignment 2
│   └── ... (same structure as PA1)
│
├── 📁 PA3/ through PA8/ ────────→ Other assignments
│   └── ... (same structure)
│
└── 📁 .git/ ────────────────────→ Version control history
```

---

## 🌐 Website Navigation Flow

```
                    🏠 HOMEPAGE (index.html)
                    cse101-pa-moss-reports-w25.netlify.app
                              |
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ↓                     ↓                     ↓
    [PA1 Button]          [PA2 Button]         [PA8 Button]
    (Blue)                (Green)              (Deep Purple)
        │                     │                     │
        ↓                     ↓                     ↓
   📊 PA1/index.html     PA2/index.html        PA8/index.html
   ┌────────────────────────────────────────────────────────┐
   │  #  │ Student  │ Lex.c │ List.c │  ← Searchable Table │
   │  1  │ alice    │   2   │   1    │                      │
   │  2  │ bob      │   1   │   3    │  🔍 [Search Bar]     │
   └────────────────────────────────────────────────────────┘
        │
        │ (Click student name)
        ↓
   📄 PA1/alice/index.html
   ┌─────────────────────────────────────────────┐
   │  Alice's PA1 Reports                        │
   │  ─────────────────────────────────          │
   │  Report 1: Lex.c  [View Full Report] ←──┐   │
   │  Report 2: List.c [View Full Report]    │   │
   └─────────────────────────────────────────┘   │
                                                 │
        (Click "View Full Report")               │
                 ↓                               │
   📄 Matches for _winter25_alice_pa1_Lex.c     │
      and _winter25_bob_pa1_Lex.c.html ←────────┘
   ┌──────────────────────────────────────────────┐
   │  ┌─────────────┬─────────────┐               │
   │  │ Alice's Code│  Bob's Code │ ← Side by Side│
   │  ├─────────────┼─────────────┤               │
   │  │ while(...) {│ while(...) {│ ← Highlighted │
   │  │   count++;  │   count++;  │   Matching    │
   │  │ }           │ }           │   Sections    │
   │  └─────────────┴─────────────┘               │
   │  Similarity: 87% ← Percentage                │
   └──────────────────────────────────────────────┘
```

---

## ⚙️ Script Execution Flow

### org_reports.py

```
START
  │
  ↓
Read command: python3 org_reports.py -d PA1
  │
  ↓
Get PA folder name: "PA1"
  │
  ↓
List all files in PA1/
  │
  ↓
For each file matching "Matches*.html":
  │
  ├─→ Extract student names using regex
  │   Example: "Matches for _winter25_alice_pa1_List.c 
  │            and _winter25_bob_pa1_List.c.html"
  │   Extracts: ["alice", "bob"]
  │
  ├─→ Create folders (if not exists):
  │   - PA1/alice/
  │   - PA1/bob/
  │
  ├─→ Copy file to both folders:
  │   - PA1/alice/Matches_for_...html
  │   - PA1/bob/Matches_for_...html
  │
  ├─→ Find companion folder: "Matches_for_..._files/"
  │
  ├─→ Copy companion folder to both:
  │   - PA1/alice/Matches_for_..._files/
  │   - PA1/bob/Matches_for_..._files/
  │
  └─→ Delete original files
  │
  ↓
DONE: Reports organized by student
```

---

### generate_pa_reports.py

```
START
  │
  ↓
Read command: python3 generate_pa_reports.py --pa PA1
  │
  ↓
Look up PA1 file types in PA_FILE_TYPES dictionary
  │
  ├─→ List.c files: ["list"]
  └─→ Lex.c files: ["lex"]
  │
  ↓
Scan PA1/ for student folders
  │
  ├─→ Found: alice/, bob/, charlie/
  │
  ↓
For each student folder:
  │
  ├─→ Count reports for each file type
  │   alice: List.c (2 reports), Lex.c (1 report)
  │   bob: List.c (1 report), Lex.c (3 reports)
  │
  ├─→ Create student's index.html
  │   Lists all their reports with links
  │
  ↓
Create PA1/index.html with:
  │
  ├─→ HTML table with all students
  ├─→ Search bar JavaScript
  ├─→ Modern CSS styling
  │
  ↓
DONE: PA1 dashboard created
```

---

### generate_root_index.py

```
START
  │
  ↓
Define HTML template as a string
  │
  ├─→ Header with title
  ├─→ 8 PA buttons with unique colors:
  │   - PA1: Blue gradient
  │   - PA2: Green gradient
  │   - PA3: Yellow gradient
  │   - PA4: Red gradient
  │   - PA5: Purple gradient
  │   - PA6: Orange gradient
  │   - PA7: Teal gradient
  │   - PA8: Deep purple gradient
  ├─→ Google Sheets links for each PA
  └─→ Footer with credits
  │
  ↓
Write HTML string to index.html
  │
  ↓
DONE: Homepage created
```

---

### check_duplicate_usernames.py

```
START
  │
  ↓
Open flaggedStudentsPresent.txt
  │
  ↓
Read all lines
  │
  ├─→ Skip lines starting with #
  ├─→ Skip empty lines
  │
  ↓
Count occurrences of each username
  │
  ├─→ alice: 3
  ├─→ bob: 2
  ├─→ charlie: 1
  │
  ↓
Filter: Keep only usernames appearing 2+ times
  │
  ├─→ alice: 3 times
  └─→ bob: 2 times
  │
  ↓
Print results
  │
  ↓
DONE: Repeat offenders identified
```

---

## 🎨 Color Scheme Reference

```
Main Dashboard PA Buttons:

PA1: Blue       ████ #1a73e8 → #4285f4 (Google Blue)
PA2: Green      ████ #34a853 → #0f9d58 (Google Green)
PA3: Yellow     ████ #fbbc05 → #f9ab00 (Google Yellow)
PA4: Red        ████ #ea4335 → #d93025 (Google Red)
PA5: Purple     ████ #9c27b0 → #7b1fa2 (Material Purple)
PA6: Orange     ████ #ff9800 → #f57c00 (Material Orange)
PA7: Teal       ████ #009688 → #00695c (Material Teal)
PA8: Deep Purple ████ #673ab7 → #512da8 (Material Deep Purple)

PA Overview Tables:

Primary:   ████ #2c3e50 (Dark Blue Gray)
Secondary: ████ #3498db (Bright Blue)
Accent:    ████ #e74c3c (Red)
Light:     ████ #ecf0f1 (Light Gray)
```

---

## 📊 Data Flow Diagram

```
┌─────────────┐
│   INPUTS    │
└──────┬──────┘
       │
       ├──→ MOSS Report Files (.html)
       ├──→ Companion Files Folders (_files/)
       ├──→ flaggedStudentsPresent.txt
       └──→ PA_FILE_TYPES Configuration
       │
       ↓
┌──────────────────┐
│  PYTHON SCRIPTS  │
├──────────────────┤
│ org_reports.py   │───→ File Organization
│ generate_pa_     │───→ Page Generation
│   reports.py     │
│ generate_root_   │───→ Homepage Creation
│   index.py       │
│ check_duplicate_ │───→ Analysis
│   usernames.py   │
└────────┬─────────┘
         │
         ↓
┌────────────────┐
│    OUTPUTS     │
├────────────────┤
│ • index.html   │───→ Homepage
│ • PA*/index.   │───→ PA Overviews
│   html         │
│ • PA*/student/ │───→ Student Pages
│   index.html   │
│ • Console      │───→ Analysis Results
│   Reports      │
└────────┬───────┘
         │
         ↓
┌─────────────────┐
│  DEPLOYMENT     │
├─────────────────┤
│ Git → GitHub    │───→ Version Control
│ GitHub → Netlify│───→ Auto-Deploy
│ Netlify → Web   │───→ Live Website
└─────────────────┘
```

---

## 🔄 User Interaction Flow

```
Teaching Assistant Workflow:

1. ACCESS DASHBOARD
   Browser → https://cse101-pa-moss-reports-w25.netlify.app/
   
2. SELECT ASSIGNMENT
   Click → [PA3 Button]
   
3. SEARCH FOR STUDENT (Optional)
   Type → "alice" in search bar
   Table → Filters to show only Alice
   
4. VIEW STUDENT REPORTS
   Click → "alice" (student name link)
   New Page → Shows all Alice's PA3 reports
   
5. REVIEW SPECIFIC MATCH
   Click → [View Full Report] button
   MOSS Report Opens → Side-by-side comparison
   
6. ANALYZE SIMILARITY
   Review → Highlighted matching code sections
   Check → Similarity percentage
   Decide → Is this plagiarism or coincidence?
   
7. CHECK GOOGLE SHEETS (Optional)
   Click → "View PA3 Google Sheet" link
   Spreadsheet Opens → Detailed tracking notes
   
8. IDENTIFY PATTERNS (Optional)
   Run → python3 check_duplicate_usernames.py
   See → Students appearing in multiple PAs
   
9. REPORT FINDINGS
   Document → Cases requiring attention
   Meet → With instructor to discuss
```

---

## 🧩 Component Relationships

```
                    MOSS Web Dashboard
                           │
        ┏━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┓
        ↓                                      ↓
   GENERATION LAYER                      PRESENTATION LAYER
        │                                      │
   ┌────┴────┐                          ┌─────┴─────┐
   │ Python  │                          │   HTML    │
   │ Scripts │                          │   Files   │
   └────┬────┘                          └─────┬─────┘
        │                                     │
   ┌────┼────┐                          ┌─────┼─────┐
   ↓    ↓    ↓                          ↓     ↓     ↓
  org  gen   gen                     index  PA*/  Student
 _rep  _pa   _root                    .html  index index
 orts  _rep  _index                          .html .html
 .py   orts  .py
       .py

   DATA LAYER ←──────────┬──────────→ DEPLOYMENT LAYER
        │                                    │
   ┌────┴────┐                          ┌────┴────┐
   │ Files & │                          │ Git +   │
   │ Configs │                          │ Netlify │
   └────┬────┘                          └────┬────┘
        │                                    │
   ┌────┼────┐                               ↓
   ↓    ↓    ↓                         Live Website
  MOSS flag  PA_                       (Internet)
  reps ged   FILE_
  .html Stud TYPES
       .txt  dict
```

---

## 📈 Typical Usage Statistics

```
Average CSE101 Course:
├── Students: ~100-150
├── Assignments: 8 (PA1-PA8)
├── Total Submissions: ~800-1200
├── Flagged Reports: ~50-100 per PA
├── Students Flagged: ~10-20 per PA
└── Repeat Offenders: ~3-5 across multiple PAs

Dashboard Statistics:
├── Total HTML Files: ~500-800
├── Total GIF Images: ~300-600
├── Website Size: ~50-100 MB
├── Page Load Time: <2 seconds
└── Search Response: Instant (<100ms)
```

---

## 🎯 Success Criteria

```
✅ WELL-ORGANIZED
   • Reports sorted by student
   • Easy to navigate
   • Clear naming conventions

✅ FAST & EFFICIENT
   • Search works instantly
   • Pages load quickly
   • Mobile-responsive

✅ COMPREHENSIVE
   • All reports accessible
   • Google Sheets integration
   • Duplicate tracking

✅ USER-FRIENDLY
   • Clear visual hierarchy
   • Color-coded navigation
   • Intuitive interface

✅ MAINTAINABLE
   • Automated generation
   • Version controlled
   • Well-documented
```

---

**For more detailed explanations, see [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)**
