# FILE INTEGRITY CHECKER

*COMAPNY*: CODTECH IT SOLUTIONS

*NAME*: MADIPADIGA KOUSHEEL

*INTERN ID*: CT04DL611

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4WEEKS

*MENTOR*: NEELA SANTOSH 

# FILE INTEGRITY CHECKER DESCRPTION
A File Integrity Checker is a cybersecurity tool used to detect unauthorized changes to files by monitoring their content over time. 
It ensures that files (e.g., system files, configuration files, or codebases) remain unchanged unless explicitly updated.
This tool is commonly used in security-sensitive environments to detect tampering, malware injections, or accidental modifications.
When developed using Python for the backend, and HTML/CSS for the frontend interface, within Visual Studio Code, the tool becomes a 
practical and customizable utility suitable for developers, administrators, and security analysts.

# TECHNOLOGIES AND TOOLS USED 
Python: Backend programming to compute file hashes and compare them.
HTML/CSS: Frontend interface to allow users to upload/select files and view integrity results.
Visual Studio Code: Integrated development environment used to develop and manage the project.
Flask (Optional): Lightweight web framework to serve the frontend and connect it with backend Python logic.
hashlib: Python standard library used to generate secure hashes like MD5, SHA-1, or SHA-256.
os / pathlib: For file handling and directory management.
json: To store and compare file hashes over time.

# CORE LOGIC IN PYTHON 
1.Baseline Hash Generation:
The user selects one or more files to monitor.
The tool calculates a cryptographic hash (e.g., SHA-256) for each file using hashlib.
Hashes are stored in a JSON file or database with the file name and path as keys.

2.Integrity Checking:
On subsequent runs, the tool recalculates the current hash of each monitored file.
It compares the new hash to the previously stored hash.
If the hashes differ, the tool flags the file as modified, deleted, or added.

3.Frontend Interaction:
The user interacts via an HTML/CSS interface (e.g., upload files, start scan, view reports).
Flask routes handle the upload, scan, and result display.

# APPLICABILITY
This tool is applicable in:
Web servers and application directories: To detect if any files were tampered with by attackers.
Critical system files: For monitoring OS configurations and security settings.
Compliance auditing: Used in regulated environments like healthcare or finance.
Software development: Ensuring critical files are not unintentionally altered.
Digital forensics: Detect unauthorized changes in digital evidence.

# SUMMARY 
A File Integrity Checker built with Python, HTML, and CSS in Visual Studio Code is a practical tool to detect file tampering and ensure system integrity. 
By using cryptographic hashing, it helps maintain trust in the integrity of sensitive files. While it’s not a full-fledged intrusion detection system, 
it serves as a foundational security component in personal or small business environments and is ideal for educational purposes, internal audits, and basic monitoring tasks

# OUTPUTS
![Image](https://github.com/user-attachments/assets/deb05450-202d-483c-b90e-e9ef266ad30a)

![Image](https://github.com/user-attachments/assets/8ed434bd-1b1c-48ae-addf-ba0e1023d3bb)

![Image](https://github.com/user-attachments/assets/82f891f0-6899-4d16-9bac-f5f17a08d956)

