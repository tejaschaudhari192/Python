
cmd_disc = {
    "git init": "initialize empty git repo in directory",
    "ls": "display directory",
    "git status":"you know",
    "git add -A":"unstage to stage",
    "git commit -a -m <messege> ":"commit changes",
    "git push origin <branch> ":"push to hub",

    
}

for cmd in cmd_disc:
    print(cmd)
    print(cmd_disc[cmd])
