import os
current_dir = os.getcwd()

save_dir = "saved_file"

path = os.path.join(current_dir,save_dir)
os.makedirs(path)

