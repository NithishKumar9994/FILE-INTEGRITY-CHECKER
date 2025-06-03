# FILE-INTEGRITY-CHECKER

COMPANY: CODTECH IT SOLUTIONS

NAME: NITHISHKUMAR K

INTERN ID: CT04DF1039

DOMAIN: Cyber Security & Ethical Hacking

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION:-

File Integrity Checker

In the world of cybersecurity and system administration, maintaining the integrity of files is a fundamental requirement. Whether it’s a configuration file on a production server, a log file that records critical events, or an executable used in sensitive operations, any unauthorized or unintended change can lead to serious vulnerabilities, security breaches, or data corruption. To address this, a File Integrity Checker is developed as a security tool that monitors and verifies the consistency and trustworthiness of files over time by comparing their hash values.

What is File Integrity Monitoring?
File Integrity Monitoring (FIM) is a process of validating the integrity of operating system and application software files by comparing the current state of the files with a known good baseline. The known good state is usually determined by calculating a cryptographic hash of the file. If the hash changes, it indicates that the file has been altered. This change could be due to legitimate updates or unauthorized access such as malware or hacker activity.

How Hashing Works
A hash function converts an input (in this case, a file’s contents) into a fixed-length string of characters, which appears random. Popular hashing algorithms include:

MD5 – Fast but no longer secure due to collision vulnerabilities.

SHA-1 – Better than MD5 but still deprecated in security contexts.

SHA-256 – Part of the SHA-2 family, widely recommended for modern systems.

Hashing is deterministic, meaning the same file will always produce the same hash. Even the slightest change in a file (like one character) will result in a drastically different hash output, making it ideal for integrity checks.

Purpose and Use Cases
Detect Unauthorized Changes: Alerts administrators to changes made by hackers or malware.

Compliance Requirements: Industries such as finance and healthcare require file integrity monitoring under standards like PCI-DSS and HIPAA.

Forensic Analysis: Helps investigators confirm if files were tampered with.

Backup Validation: Ensures that restored files are identical to the originals.

Working Principle of the File Integrity Checker
The File Integrity Checker operates in two major phases:

Baseline Creation:

The tool calculates and stores the hash value of target files.

This information is typically saved in a secure file (e.g., hashes.json or a database).

This forms the "known good state".

Monitoring and Verification:

At later intervals, the tool recalculates the hash of each file.

The new hash is compared against the stored baseline.

If there’s a mismatch, it means the file has changed.

The tool logs the differences and optionally raises alerts.

Implementing in Python Using hashlib
Python is an excellent choice for building a File Integrity Checker due to its readability and the power of its standard libraries. The hashlib library provides built-in support for various hashing algorithms like MD5, SHA-1, and SHA-256.

A basic version of the script performs the following tasks:

Recursively scan directories and calculate SHA-256 hashes for each file.

Save the hash values with file paths in a JSON file.

Provide options to update the hash database (baseline) or check integrity.

Print/log any differences found during comparison.

Key Features of a Good File Integrity Checker
Support for Multiple Hash Algorithms

Recursive Directory Monitoring

Logging and Reporting

User-Friendly CLI or GUI

Real-time or Scheduled Monitoring

Optional Alert System (Email/Log File/GUI Notification)

Security Best Practices
The hash database should be stored in a secure, write-protected location.

The tool should itself be monitored for changes.

Avoid using outdated algorithms like MD5 and SHA-1.

Combine file metadata (size, permissions) with hash values for better integrity checks.

Conclusion
A File Integrity Checker is an essential tool in any cybersecurity toolkit. It helps ensure that critical files remain untampered and trustworthy. By using Python and libraries like hashlib, such tools can be built efficiently and customized to suit the specific needs of an organization or project. Implementing a file integrity monitoring system is a proactive step towards stronger digital security and compliance.





OUTPUT

![Image](https://github.com/user-attachments/assets/b8f61a8e-2643-4cee-92a5-2b57203c113a)





