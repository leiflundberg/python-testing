import glob 

if glob.glob("*.txt"):
    print("Filetype exists")
else: 
    print("Filetype DOENS'T exist")