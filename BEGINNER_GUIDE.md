# 🎓 Beginner's Guide to the MOSS Web Dashboard

**Welcome!** This guide will help you understand this project from start to finish, even if you're new to programming.

---

## 📚 Table of Contents
1. [What Is This Project?](#what-is-this-project)
2. [Why Does It Exist?](#why-does-it-exist)
3. [Key Concepts Explained](#key-concepts-explained)
4. [How It Works (The Big Picture)](#how-it-works-the-big-picture)
5. [Understanding the Files](#understanding-the-files)
6. [The Complete Workflow](#the-complete-workflow)
7. [How to Use the Dashboard](#how-to-use-the-dashboard)
8. [Technical Terms Glossary](#technical-terms-glossary)

---

## 🤔 What Is This Project?

Imagine you're a teacher with 100 students who all submitted coding homework. You want to check if any students copied each other's code. Checking manually would take forever! This project creates a **website that makes it easy to see which students might have copied from each other**.

### Real-World Analogy
Think of it like a "plagiarism detector" for essays, but for computer code. Just like how teachers use tools to check if students copied essays from the internet, programming instructors use MOSS (the tool behind this project) to check if students copied code from each other.

---

## 🎯 Why Does It Exist?

### The Problem
In a college computer science class called CSE101 at UC Santa Cruz:
- Students complete 8 programming assignments (PA1 through PA8)
- Each student writes code in C or C++ programming languages
- Sometimes students copy code from each other (this is called "academic dishonesty" or "plagiarism")
- Instructors need to catch this to be fair to students who do their own work

### The Solution
This project creates a **visual dashboard** (a website) where teaching assistants can:
- See which students have similar code
- Click on student names to view detailed reports
- Search for specific students quickly
- Keep track of repeat offenders across multiple assignments

---

## 💡 Key Concepts Explained

### What is MOSS?
**MOSS** stands for "Measure Of Software Similarity"
- It's a tool created by Stanford University
- You give it a bunch of code files from different students
- It compares all of them and finds similarities
- It generates HTML reports showing which parts of code are similar

**Important**: This project doesn't RUN MOSS. It takes the reports MOSS already created and makes them easier to view and navigate.

### What is a Dashboard?
A **dashboard** is like a control panel or home screen that shows you important information at a glance.

Examples you might know:
- Netflix homepage (shows all available shows)
- Instagram profile (shows all your posts)
- Car dashboard (shows speed, fuel, temperature)

This dashboard shows all the plagiarism reports organized neatly.

### What are HTML, CSS, and JavaScript?
These are the three languages used to build websites:

- **HTML** = Structure (like the skeleton of a house)
  - Creates headings, paragraphs, links, tables
  
- **CSS** = Style (like paint, furniture, decorations)
  - Makes things colorful, positions elements, adds animations
  
- **JavaScript** = Behavior (like electricity that powers lights and appliances)
  - Makes the search bar work, filters tables, responds to clicks

### What is Python?
**Python** is a programming language (different from HTML/CSS/JavaScript) that:
- Can read and write files
- Can process text and data
- Is great for automation (doing repetitive tasks)

In this project, Python scripts **generate** the HTML files automatically.

---

## 🔄 How It Works (The Big Picture)

Here's the complete journey from start to finish:

### Step 1: Students Submit Code
- 100+ students write code for an assignment (e.g., PA1)
- Each student submits files like `List.c` and `Lex.c`
- These files contain their programming work

### Step 2: MOSS Analysis (Outside This Project)
- The instructor runs MOSS software
- MOSS compares all students' code against each other
- MOSS creates HTML report files showing similarities
- Example report name: `Matches for _winter25_john_pa1_List.c and _winter25_mary_pa1_List.c.html`

### Step 3: Organize Reports (This Project Starts Here!)
Using `org_reports.py`:
- The script reads all the messy report files
- It creates a folder for each student
- It copies relevant reports into each student's folder
- Now reports are organized by student name!

### Step 4: Generate Dashboard Pages
Using `generate_pa_reports.py`:
- Creates an `index.html` file for each assignment (PA1, PA2, etc.)
- This page shows a table of all students and how many matches they have
- Also creates an `index.html` for each student showing their specific reports

### Step 5: Create Main Homepage
Using `generate_root_index.py`:
- Creates the main `index.html` at the root
- This is the first page you see
- Has big colorful buttons to access each assignment

### Step 6: Deploy to the Internet
- All files are uploaded to **GitHub** (a website that stores code)
- **Netlify** (a hosting service) automatically creates a live website
- Now anyone with the link can view the dashboard!

### Visual Flow Diagram
```
Students → Homework Code → MOSS Analysis → Raw Reports
                                               ↓
                                    org_reports.py (organize)
                                               ↓
                                    generate_pa_reports.py (create tables)
                                               ↓
                                    generate_root_index.py (create homepage)
                                               ↓
                                    Git + Netlify (publish online)
                                               ↓
                                    Live Website! 🎉
```

---

## 📁 Understanding the Files

Let's explore what each file does in simple terms:

### 🏠 Main Files (In the Root Folder)

#### 1. `index.html` (The Homepage)
**What it is**: The first page you see when you visit the website.

**What it contains**:
- Title: "CSE101: MOSS Reports | Winter 25"
- 8 colorful buttons (one for each assignment)
- Each button links to that assignment's reports
- Links to Google Sheets for detailed tracking

**Analogy**: Like a building's lobby with signs pointing to different floors.

---

#### 2. `README.md` (The Official Documentation)
**What it is**: Instructions for people who work on this project.

**What it contains**:
- Overview of what the project does
- How to set it up
- How to run the Python scripts
- Links to the live website

**File format**: Markdown (.md) - a simple way to write formatted text.

**Analogy**: Like an instruction manual that comes with IKEA furniture.

---

#### 3. `generate_pa_reports.py` (The Dashboard Builder)
**What it is**: A Python script that creates the assignment overview pages.

**What it does**:
1. Looks in a PA folder (like PA1/)
2. Finds all student folders
3. Counts how many report files each student has
4. Creates a nice HTML table showing this information
5. Creates individual index pages for each student

**Key Features**:
- Knows which files to look for in each assignment (stored in `PA_FILE_TYPES` dictionary)
- Sorts students alphabetically
- Adds a search bar so you can find students quickly

**How to run it**:
```bash
python3 generate_pa_reports.py --pa PA1
```

**Analogy**: Like a librarian who organizes books and creates a catalog.

---

#### 4. `generate_root_index.py` (The Homepage Builder)
**What it is**: A Python script that creates the main homepage.

**What it does**:
1. Creates one big HTML file
2. Adds 8 colorful buttons (PA1-PA8)
3. Each button has a unique color gradient
4. Adds links to Google Sheets
5. Saves it as `index.html`

**The HTML is embedded**: The entire website code is written inside this Python file as a long string!

**How to run it**:
```bash
python3 generate_root_index.py
```

**Analogy**: Like designing a poster that directs people to different events.

---

#### 5. `org_reports.py` (The Organizer)
**What it is**: A Python script that sorts report files into student folders.

**The Problem It Solves**: 
When MOSS generates reports, they come as individual files like:
- `Matches for _winter25_alice_pa1_List.c and _winter25_bob_pa1_List.c.html`

This file needs to be in BOTH Alice's and Bob's folders!

**What it does**:
1. Reads the filename
2. Extracts both student names using **regex** (pattern matching)
3. Creates folders for alice and bob if they don't exist
4. Copies the report file to both folders
5. Also copies the matching `_files` folder (contains images)
6. Deletes the original to keep things clean

**How to run it**:
```bash
python3 org_reports.py -d PA1
```

**Analogy**: Like a mail sorter at the post office putting letters into the right mailboxes.

---

#### 6. `check_duplicate_usernames.py` (The Repeat Finder)
**What it is**: A Python script that finds students who appear multiple times.

**Why it's useful**: If a student is flagged in PA1, PA2, PA3, and PA4, they might be a serial cheater. This script helps identify patterns.

**What it does**:
1. Reads `flaggedStudentsPresent.txt`
2. Counts how many times each name appears
3. Shows students who appear 2+ times
4. Ignores lines that start with `#` (comments)

**How to run it**:
```bash
python3 check_duplicate_usernames.py
```

**Example Output**:
```
Usernames that appear 2 or more times:
aaychen - 3 times
ssriva16 - 3 times
```

**Analogy**: Like a store security system that tracks repeat shoplifters.

---

#### 7. `flaggedStudentsPresent.txt` (The Tracking List)
**What it is**: A text file listing all flagged students, organized by assignment.

**Format**:
```
# PA-1
student1
student2
#student3  ← The # means this is a comment or note

# PA-2
student4
student5
```

**Why use it**: Keeps a record of who was flagged for potential plagiarism in each assignment.

---

#### 8. Favicon Files (`faviconM.png`, `.ico`, `.jpg`)
**What they are**: The small icon that appears in your browser tab.

**Why three formats**: Different browsers prefer different formats, so having all three ensures it works everywhere!

---

### 📂 PA Folders (PA1, PA2, PA3, PA4, PA5, PA6, PA7, PA8)

Each PA folder has the same structure:

#### Structure Example (PA1):
```
PA1/
├── index.html          ← Overview table for this assignment
├── amunoz45/           ← Student folder
│   ├── index.html      ← This student's reports list
│   ├── Match_report.html  ← Actual MOSS comparison
│   └── Match_report_files/  ← Images and visualizations
├── apdas/
│   ├── index.html
│   ├── Match_report.html
│   └── Match_report_files/
└── ... (more students)
```

#### PA Index Page (`PA1/index.html`)
Shows a table like this:

| # | Student CruzID | Lex.c Matches | List.c Matches |
|---|----------------|---------------|----------------|
| 1 | amunoz45       | 1             | -              |
| 2 | apdas          | 1             | 1              |
| 3 | asee1          | 2             | 4              |

- Click on a student name to see their detailed reports
- Use the search bar to find specific students
- Numbers show how many matches were found for each file type

#### Student Index Page (`PA1/amunoz45/index.html`)
Shows all reports for one student:
- Report 1: Lex.c [View Full Report]
- Report 2: List.c [View Full Report]

#### MOSS Report Files
These are the actual plagiarism reports showing:
- **Side-by-side code comparison** (two columns)
- **Highlighted sections** that match between students
- **Percentage similarity** scores
- **Color-coded matching blocks**

---

## 🔧 The Complete Workflow

Here's how to use this project from scratch:

### Prerequisites (What You Need)
1. **Python 3** installed on your computer
2. **A code editor** (like VS Code or Notepad++)
3. **MOSS reports** (HTML files from running MOSS)
4. **Git** (for version control)
5. **Netlify account** (for hosting the website)

---

### Step-by-Step Process

#### Phase 1: Organize Raw Reports

**Scenario**: You just ran MOSS and have 50 HTML files in your PA1 folder.

```bash
# Navigate to the project folder
cd /path/to/moss_web

# Organize reports into student folders
python3 org_reports.py -d PA1
```

**What happens**: 
- Script creates folders for each student
- Copies reports to the appropriate folders
- Your PA1 folder now has organized subdirectories!

---

#### Phase 2: Generate Dashboard Pages

```bash
# Generate the PA1 overview page
python3 generate_pa_reports.py --pa PA1

# Or generate for all PAs at once
python3 generate_pa_reports.py --all
```

**What happens**:
- Creates `PA1/index.html` with a searchable table
- Creates `index.html` in each student folder
- Now you can navigate the reports easily!

---

#### Phase 3: Create Main Homepage

```bash
# Generate the root index page
python3 generate_root_index.py
```

**What happens**:
- Creates the main `index.html` file at the root
- This page has buttons to access all 8 PAs

---

#### Phase 4: Check for Repeat Offenders

```bash
# Find students flagged multiple times
python3 check_duplicate_usernames.py
```

**What happens**:
- Reads `flaggedStudentsPresent.txt`
- Shows which students appear in multiple assignments
- Helps identify patterns of academic dishonesty

---

#### Phase 5: Deploy to the Web

```bash
# Add all files to git
git add .

# Commit with a descriptive message
git commit -m "Added PA1 reports"

# Push to GitHub
git push origin main
```

**What happens**:
- Files upload to GitHub
- Netlify automatically detects the change
- Website rebuilds and deploys
- New reports are now live online!

---

## 🖥️ How to Use the Dashboard

### For Teaching Assistants

#### 1. Access the Website
Visit: https://cse101-pa-moss-reports-w25.netlify.app/

#### 2. Choose an Assignment
Click on one of the colorful buttons (PA1, PA2, etc.)

#### 3. Browse or Search
- **Scroll** through the table to see all students
- **Search** by typing a CruzID in the search bar
- **Look at numbers** to see how many matches each student has

#### 4. Investigate a Student
Click on a student's name (e.g., "amunoz45")
- See all their reports for that assignment
- Click "View Full Report" to see the actual code comparison

#### 5. Review the Comparison
- **Left side**: One student's code
- **Right side**: Another student's code
- **Highlighted sections**: Parts that match
- **Percentage**: How similar they are

#### 6. Check Google Sheets (Optional)
- Click "View PA# Google Sheet" under each assignment button
- See detailed notes and tracking information

---

### For Instructors

#### Making Decisions
The reports help you:
1. **Identify potential plagiarism** - High similarity might indicate copying
2. **See patterns** - Students who appear multiple times
3. **Review evidence** - See exactly which lines match
4. **Be fair** - Make informed decisions based on data

#### Important Notes
- High similarity doesn't always mean cheating (students might use similar approaches)
- Review each case individually
- Consider context (were students allowed to work together?)

---

## 📖 Technical Terms Glossary

### Programming Terms

**CruzID**: The unique username each UC Santa Cruz student has (like "jsmith" for John Smith)

**Repository (Repo)**: A folder that stores all project files and tracks changes over time

**Git**: Software that tracks changes to files (like "undo history" for your entire project)

**GitHub**: A website where people store their Git repositories online

**Netlify**: A service that takes your HTML files and makes them into a live website

**Deployment**: The process of making your website available on the internet

**Command Line / Terminal**: A text-based way to control your computer (like typing commands instead of clicking)

**Script**: A program file that automates tasks (runs multiple commands for you)

**Argument**: Extra information you give to a script (like `--pa PA1` tells the script which PA to process)

---

### Web Development Terms

**HTML (HyperText Markup Language)**: The structure of web pages
- Example: `<h1>Title</h1>` creates a heading

**CSS (Cascading Style Sheets)**: The styling of web pages
- Example: `color: blue;` makes text blue

**JavaScript**: Makes web pages interactive
- Example: The search bar that filters as you type

**Index File**: The main page of a folder (usually `index.html`)
- When you visit `website.com/PA1/`, it automatically shows `PA1/index.html`

**Link/Hyperlink**: Clickable text that takes you to another page

**Button**: A clickable element (in this project, the colored PA buttons)

**Table**: Organized data in rows and columns (like a spreadsheet)

**Search Bar**: A text input where you type to filter results

---

### MOSS-Specific Terms

**MOSS (Measure Of Software Similarity)**: The plagiarism detection tool used by instructors

**Match**: When two students' code has similar or identical sections

**Similarity Percentage**: How much of the code is the same (90% = very similar, 10% = barely similar)

**Report File**: The HTML file showing the comparison between two students

**Companion Files Folder**: The `_files` folder containing images and sub-pages for a report

**Flagged Student**: A student whose code matched someone else's (might or might not be cheating)

---

### File System Terms

**Path**: The location of a file (like an address)
- Example: `/workspace/PA1/amunoz45/index.html`

**Root Directory**: The main folder (represented by `/` at the start)

**Subdirectory**: A folder inside another folder
- PA1 is a subdirectory of the root
- amunoz45 is a subdirectory of PA1

**Extension**: The letters after the dot in a filename
- `.html` = HTML file
- `.py` = Python file
- `.txt` = Text file
- `.gif` = Image file

**Absolute Path**: Full path from the root (e.g., `/workspace/PA1/index.html`)

**Relative Path**: Path from your current location (e.g., if you're in PA1, just `index.html`)

---

## 🎓 Learning Opportunities

### Skills You Can Learn From This Project

1. **Python Programming**:
   - Reading and writing files
   - String manipulation
   - Working with dictionaries and lists
   - Using regular expressions (regex)
   - Command-line arguments

2. **Web Development**:
   - HTML structure
   - CSS styling
   - JavaScript interactivity
   - Responsive design
   - Navigation systems

3. **Version Control**:
   - Using Git
   - Committing changes
   - Pushing to GitHub
   - Collaboration workflows

4. **Automation**:
   - Writing scripts to save time
   - Processing multiple files at once
   - Generating content programmatically

5. **Web Hosting**:
   - Deploying websites
   - Continuous integration/deployment
   - Using Netlify

---

## 🚀 Try It Yourself!

### Beginner Exercises

1. **Explore the Live Website**:
   - Visit the dashboard
   - Click through different PAs
   - Use the search function
   - Look at a MOSS report

2. **Read the Code**:
   - Open `generate_root_index.py`
   - Find where the colors are defined
   - Try to understand the HTML structure

3. **Make a Simple Change**:
   - Change the title in `index.html`
   - Edit a color in the CSS
   - Add your name to the footer

4. **Run a Script**:
   - Install Python 3
   - Try running `python3 check_duplicate_usernames.py`
   - See what output you get

---

## 📚 Additional Resources

### Learn HTML/CSS/JavaScript
- [MDN Web Docs](https://developer.mozilla.org/) - Comprehensive tutorials
- [W3Schools](https://www.w3schools.com/) - Simple, interactive lessons
- [freeCodeCamp](https://www.freecodecamp.org/) - Free courses

### Learn Python
- [Python.org Tutorial](https://docs.python.org/3/tutorial/) - Official guide
- [Codecademy Python](https://www.codecademy.com/learn/learn-python-3) - Interactive lessons
- [Automate the Boring Stuff](https://automatetheboringstuff.com/) - Practical Python

### Learn Git & GitHub
- [GitHub Learning Lab](https://lab.github.com/) - Interactive tutorials
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) - Official docs

---

## ❓ Frequently Asked Questions

### Q: Do I need to know programming to understand this?
**A**: This guide explains everything from scratch! But knowing basic HTML and Python will help.

### Q: Can I use this for my own school project?
**A**: Yes! You can adapt this for any situation where you need to organize and display reports.

### Q: What if I break something?
**A**: That's okay! Git tracks all changes, so you can always undo mistakes. Plus, the original code is backed up on GitHub.

### Q: How long does it take to learn this?
**A**: Reading this guide: 30-60 minutes. Understanding by exploring: a few hours. Building something similar: weeks of learning!

### Q: Is plagiarism detection 100% accurate?
**A**: No! MOSS finds similarities, but humans must decide if it's actually cheating. Similar code might just mean students learned the same concepts.

---

## 🎉 Conclusion

Congratulations on making it through this guide! You now understand:
- What the MOSS Web Dashboard does
- How all the pieces fit together
- What each file does
- How the workflow operates
- The technical concepts involved

### Next Steps
1. Explore the live website
2. Read through the actual code files
3. Try making small changes
4. Experiment with the Python scripts
5. Build your own version for a different purpose!

### Remember
Every expert was once a beginner. Take your time, ask questions, and experiment. The best way to learn is by doing!

---

**Made with ❤️ for high school students interested in computer science**

*Have questions? Open an issue on GitHub or ask your instructor!*
