import os

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
resources_dir = os.path.join(root_dir, 'resources')
images_dir = os.path.join(resources_dir, 'images')
