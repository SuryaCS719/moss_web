# 🚀 Quick Reference Guide

A cheat sheet for working with the MOSS Web Dashboard.

---

## 📋 Common Commands

### Organizing Reports
```bash
# Organize reports for a specific PA
python3 org_reports.py -d PA1
python3 org_reports.py -d PA2
# ... etc.
```

### Generating Dashboard Pages
```bash
# Generate dashboard for one PA
python3 generate_pa_reports.py --pa PA1

# Generate dashboards for ALL PAs
python3 generate_pa_reports.py --all
```

### Creating Homepage
```bash
# Generate the main index.html
python3 generate_root_index.py
```

### Checking Repeat Offenders
```bash
# Find students flagged multiple times
python3 check_duplicate_usernames.py
```

### Complete Workflow (New PA)
```bash
# 1. Organize the reports
python3 org_reports.py -d PA5

# 2. Generate the PA dashboard
python3 generate_pa_reports.py --pa PA5

# 3. Update the root index
python3 generate_root_index.py

# 4. Check for repeat offenders
python3 check_duplicate_usernames.py

# 5. Deploy to web
git add .
git commit -m "Added PA5 reports"
git push origin main
```

---

## 🗂️ File Structure Quick Reference

```
moss_web/
├── index.html                    ← Homepage (view at root URL)
├── PA1/
│   ├── index.html               ← PA1 overview (/PA1/)
│   └── student_name/
│       ├── index.html           ← Student's reports list
│       └── match_report.html    ← Actual MOSS comparison
├── PA2/ ... PA8/                ← Same structure
├── generate_pa_reports.py       ← Creates PA dashboards
├── generate_root_index.py       ← Creates homepage
├── org_reports.py               ← Organizes reports
├── check_duplicate_usernames.py ← Finds repeat offenders
└── flaggedStudentsPresent.txt   ← Tracking list
```

---

## 🌐 URLs Quick Reference

### Live Website
```
Main: https://cse101-pa-moss-reports-w25.netlify.app/
PA1:  https://cse101-pa-moss-reports-w25.netlify.app/PA1/
PA2:  https://cse101-pa-moss-reports-w25.netlify.app/PA2/
...
```

### Google Sheets
- Each PA has its own tracking sheet
- Links available on the main dashboard
- Format: `https://docs.google.com/spreadsheets/d/[ID]/edit`

---

## 🔧 Git Commands Quick Reference

### Deploying Updates
```bash
# Check what changed
git status

# Stage all changes
git add .

# Commit with message
git commit -m "Your message here"

# Push to GitHub (triggers auto-deploy)
git push origin main
```

### Viewing History
```bash
# See recent commits
git log --oneline -10

# See what changed in last commit
git show
```

### Undoing Changes
```bash
# Undo changes to a file (before commit)
git checkout -- filename.html

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️
git reset --hard HEAD~1
```

---

## 🎨 Color Reference

### PA Button Colors (HEX)
```
PA1: #1a73e8 (Google Blue)
PA2: #34a853 (Google Green)
PA3: #fbbc05 (Google Yellow)
PA4: #ea4335 (Google Red)
PA5: #9c27b0 (Purple)
PA6: #ff9800 (Orange)
PA7: #009688 (Teal)
PA8: #673ab7 (Deep Purple)
```

### Theme Colors
```
Primary:   #2c3e50 (Dark Blue Gray)
Secondary: #3498db (Bright Blue)
Accent:    #e74c3c (Red)
Light:     #ecf0f1 (Light Gray)
```

---

## 📊 PA File Types Configuration

Found in `generate_pa_reports.py` → `PA_FILE_TYPES` dictionary:

```python
PA1: List.c, Lex.c
PA2: List.c, FindPath.c, Graph.c
PA3: FindComponents.c, Graph.c
PA4: Matrix.c, Sparse.c, List.c
PA5: Shuffle.cpp, List.cpp
PA6: Arithmetic.cpp, BigInteger.cpp
PA7: Dictionary.cpp, Order.cpp
PA8: WordFrequency.cpp, Dictionary.cpp
```

---

## 🐛 Troubleshooting

### Script Errors

**Error: "Folder does not exist"**
```bash
# Solution: Check folder name (case-sensitive!)
ls  # List folders to see exact names
python3 org_reports.py -d PA1  # Use exact name
```

**Error: "No module named..."**
```bash
# Solution: Check Python version
python3 --version  # Should be 3.x

# If using wrong Python:
python --version   # Try without the '3'
```

**Error: "Permission denied"**
```bash
# Solution: Make script executable
chmod +x org_reports.py
python3 org_reports.py -d PA1
```

### Website Issues

**Search bar not working**
- Check browser console for JavaScript errors (F12)
- Ensure `filterTable()` function exists in HTML

**Broken links**
- Check that folder names match link hrefs
- Verify files exist at expected paths
- Check for typos in filenames

**Styling issues**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check CSS is properly embedded in HTML
- Verify no syntax errors in style tags

### Git Issues

**"git push" rejected**
```bash
# Solution: Pull first, then push
git pull origin main
git push origin main
```

**Merge conflicts**
```bash
# Solution: Resolve conflicts manually
git status          # See conflicted files
# Edit files to resolve conflicts
git add .
git commit -m "Resolved merge conflicts"
git push origin main
```

---

## 📝 Common File Patterns

### MOSS Report Filename Format
```
Matches for _winter25_student1_pa#_filename.ext and _winter25_student2_pa#_filename.ext.html

Example:
Matches for _winter25_alice_pa1_List.c and _winter25_bob_pa1_List.c.html

Parts:
- winter25: Term
- student1/student2: CruzIDs
- pa#: Assignment number (pa1, pa2, etc.)
- filename.ext: Source file (List.c, Graph.cpp, etc.)
```

### Companion Folder Format
```
Same as report filename but replace .html with _files/

Example:
Matches for _winter25_alice_pa1_List.c and _winter25_bob_pa1_List.c_files/

Contains:
- match#-0.html (left side code)
- match#-1.html (right side code)
- match#-top.html (header/stats)
- tm_*.gif (visualization images)
```

---

## 🎯 Best Practices

### Before Running Scripts
```bash
✅ Check current directory (pwd)
✅ Verify folder exists (ls)
✅ Backup flaggedStudentsPresent.txt
✅ Test with one PA first
```

### When Organizing Reports
```bash
✅ Run org_reports.py first
✅ Then run generate_pa_reports.py
✅ Update root index if needed
✅ Check output before deploying
```

### Before Deploying
```bash
✅ Test locally (open index.html in browser)
✅ Check all links work
✅ Search functionality works
✅ Mobile responsive (resize browser)
✅ No broken images
```

### Committing to Git
```bash
✅ Use descriptive commit messages
✅ Test before pushing
✅ Push during low-traffic times
✅ Check Netlify deploy logs
```

---

## 📞 Getting Help

### In This Repository
- [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md) - Comprehensive explanation
- [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md) - Visual diagrams
- [README.md](README.md) - Technical documentation

### External Resources
- [Python Documentation](https://docs.python.org/3/)
- [HTML/CSS/JS Guide](https://developer.mozilla.org/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Netlify Docs](https://docs.netlify.com/)

### Common Questions

**Q: How do I add a new PA?**
```bash
# 1. Create the PA folder
mkdir PA9

# 2. Add MOSS reports to it
# (copy your reports into PA9/)

# 3. Run the workflow
python3 org_reports.py -d PA9
python3 generate_pa_reports.py --pa PA9

# 4. Update generate_root_index.py to add PA9 button
# (edit the HTML to include PA9)

# 5. Regenerate homepage
python3 generate_root_index.py

# 6. Deploy
git add .
git commit -m "Added PA9"
git push origin main
```

**Q: How do I update student list?**
```bash
# Edit flaggedStudentsPresent.txt
# Add/remove student CruzIDs
# No need to regenerate anything unless you want updated stats
```

**Q: How do I change colors?**
```bash
# Edit generate_root_index.py or generate_pa_reports.py
# Find the CSS section
# Change hex color codes
# Regenerate HTML files
python3 generate_root_index.py
python3 generate_pa_reports.py --all
```

---

## ⚡ Performance Tips

### For Large Courses (200+ students)
- Run scripts during off-hours
- Process one PA at a time
- Use `--pa` flag instead of `--all`
- Consider compressing GIF files

### For Faster Deploys
- Use `.gitignore` for unnecessary files
- Commit related changes together
- Use meaningful commit messages
- Wait for Netlify build to complete

### For Better User Experience
- Keep reports organized
- Update regularly
- Test on multiple browsers
- Ensure mobile compatibility

---

## 🔐 Security Notes

### What NOT to Commit
```bash
❌ Student personal information
❌ Credentials or API keys
❌ .env files
❌ Large binary files (>10MB)
```

### What to Keep Private
- Student grade information
- Personal contact details
- Internal course communications
- Detailed plagiarism decisions

### Public vs Private
- This dashboard: Shows similarity reports only
- Google Sheets: Can contain sensitive details (keep private!)
- GitHub repo: Can be public if no sensitive info

---

## 📊 Usage Analytics

### Typical Timeline
```
Week 1:  PA1 due → MOSS analysis
Week 2:  Organize & deploy PA1 reports
Week 3:  PA2 due → MOSS analysis
Week 4:  Organize & deploy PA2 reports
...
Week 10: Final review of all PAs
```

### Peak Usage Times
- Right after assignment deadlines
- Before grading meetings
- During office hours
- Finals week (review all PAs)

---

## 🎓 Learning Path

### Beginner → Intermediate
1. ✅ Read BEGINNER_GUIDE.md
2. ✅ Explore live website
3. ✅ Run scripts locally
4. ✅ Make small HTML changes
5. ✅ Deploy a test change

### Intermediate → Advanced
6. ✅ Modify Python scripts
7. ✅ Add new features
8. ✅ Customize styling
9. ✅ Automate with shell scripts
10. ✅ Contribute improvements

---

## 💡 Quick Tips

- **Tab completion**: Type `python3 gen` then press Tab to autocomplete
- **History**: Press ↑ to cycle through previous commands
- **Copy path**: Right-click folder → Copy path
- **Find files**: Use `find . -name "*.html"` to locate files
- **Count reports**: Use `ls PA1/*/index.html | wc -l` to count students

---

## 🎉 Success Checklist

When Everything is Working:
- [ ] Homepage loads with all 8 PA buttons
- [ ] Each PA page shows student table
- [ ] Search bar filters correctly
- [ ] Student links work
- [ ] MOSS reports display properly
- [ ] Google Sheets links work
- [ ] Mobile view looks good
- [ ] No console errors (F12)
- [ ] Netlify deploys successfully
- [ ] Git history is clean

---

**🔖 Bookmark this page for quick reference!**

*Last Updated: 2025-11-15*
