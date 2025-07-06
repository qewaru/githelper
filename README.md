# Git commit helper
This project is a small Python utility that will help you add make commits

## Description
Current version supports only output from `git status` and result is a string of changed files. 
You still manually need to interact with `git` commands (e.g. `git status`/`git add (script output)`/etc.).

## Usage
1. Make changes in your current project
2. Run `git status | python3 path/to/script.py` in terminal (you can make an alias for this command)
3. Copy the output string
4. Use the output in the `git add` command.

## Planned features
1. Convert the script to a standalone app (so it could be invoken as a script, not by the path)
2. Change the logic, so all git proceedures will be done by the app
3. Add verification state, so user can remove/add some files manually before the changes
4. Make GUI version of the app
