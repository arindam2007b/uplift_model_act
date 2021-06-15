import os


dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",      #do not require the os.path.join as we are creating only a single directory
    "saved_models",
    "src"
]

#creating the above mentioned directories from the dirs list
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"), "w") as f:   #creating an empty .gitkeep file inside all the directories
        pass



files = [
    "dvc.yaml",
    ".gitignore",
    "parameters.yaml",
    os.path.join("src","__init__.py"),
]

#creating the files
for file_ in files:
    with open(file_,"w") as f:
        pass