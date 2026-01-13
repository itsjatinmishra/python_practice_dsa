import os;

# Specify the directory you want to list
directory_path = "/";
# List all files and directories
contents = os.listdir(directory_path);

#Print each file and directory
for item in contents:
    print(item);