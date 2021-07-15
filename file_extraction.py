import os, sys, shutil, glob, time


print('''
\t\t\t\t\t-----------\t\t\
\n\t\t\t\t\tFile Extraction\t\t
\t\t\t\t\t-----------\t\t\n

Enter the filename or file extension you are searching for:
-----------------------------------------------------------\n
''')
user_input = input("file_name >> ")

#

def search_files():
	src_path = "/source/of/path"
	dst_path = "/destination/to/path"
  files = glob.glob("/source/of/path/<wildcard>*")
	for root, dirs, files in os.walk(src_path):
		for file in files:
			if(file.startswith(user_input)) or (file.endswith(user_input)):
				print("You've entered ", user_input + ". All files will be moved to the destination path and extracted.")
				shutil.move(os.path.join(src_path, file), os.path.join(dst_path, file))
        # Will pattern match all files containing what the user entered and move those files over to the destination path
				time.sleep(1)
search_files()

def extract_files():
	moved_files = "/source/of/destination/<wildcard>*"
    for compressed in glob.glob(moved_files):
        with tarfile.open(compressed) as tar:
            tar.extractall()
            print("All files containing ", user_input + " extension have been extracted.\n")
            # Once files have been moved. The same value the user entered will extract all files in that destination path.
extract_files()
