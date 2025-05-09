# GhostFinder - Username Search Tool

**GhostFinder** is a simple command-line tool that allows you to search for usernames across multiple websites. The tool scans a list of predefined websites and checks if the given username is present or not on each of them. It's especially useful for OSINT (Open Source Intelligence) investigations or just for finding whether a specific username is available or taken across various platforms.

### Features:
- **Search Multiple Usernames:** You can search for one or more usernames simultaneously.
- **Cross-Website Search:** It checks usernames across several websites (defined in a JSON schema).
- **Estimated Scan Time:** The tool calculates and provides an estimate of how long the scan will take based on the number of sites.

### Requirements:
- Python 3.x
- `requests` library (for making HTTP requests)
- `art` library (for ASCII art rendering)

You can install the required dependencies with:
```bash
pip install -r requirements.txt
