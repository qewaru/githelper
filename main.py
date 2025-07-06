import sys

input_txt = sys.stdin.read()
lines = input_txt.splitlines()

untracked_section = False

files_to_add = []

for line in lines:
    line = line.rstrip()

    if line.startswith("Untracked files:"):
        untracked_section = True
        continue

    if untracked_section:
        if line.startswith(r"  (use") or line.startswith("no changes"):
            continue
        elif not line.startswith(""):
            untracked_section = False
        else:
            files_to_add.append(line.strip())
            continue
    
    if line.startswith("\tmodified:   "):
        files_to_add.append( line.split("\tmodified:   ")[1])
    elif line.startswith("\tdeleted:   "):
        files_to_add.append( line.split("\tdeleted:   ")[1])


for path in files_to_add:
    if "[" in path or "]" in path:
        print(f'"{path}"', end=" ")
    else:
        print(path, end=" ")