"""\
Github action workflow is kicked in to convert .md files to .rst files using m2r
"""

import os
from m2r import parse_from_file
from m2r import save_to_file

# Get the list of all files and directories
path = "."

for x in os.listdir():
	if x.endswith(".md"):
		# Parse markdown files with extension .md and convert to .rst
		#print(x)
		output = parse_from_file(x)
		save_to_file(x, output)