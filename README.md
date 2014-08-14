Metanote is a CLI for creating file and folder manifests for tracking simple metadata.
Metanote is written in Python and is only compatible with Python version 3.2 and later.

Usage:
$bash: Python metanote.py --path path\to\folder

Optional flags:
1) --path; used to specify a path to a folder if you want to run metanote somewhere else beside the current directory.
2) --overwrite; add this flag if you want to overwrite any existing metanote JSON file
3) --repair; add this flag if you are having problems reading your metanote JSON file (data corruption or bad editing)