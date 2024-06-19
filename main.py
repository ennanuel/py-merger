import os
import shutil
import click
import re

env_path = os.path.join(os.path.dirname(__file__), '.env')
if(os.path.exists(env_path)):
    with open(env_path, 'r') as env_file:
        for line in env_file:
            key, value = line.strip().split("=")
            os.environ[key] = value

def walk_through_dir(): 
    source_dir = os.environ.get("SOURCE_DIR")
    destination_dir = os.environ.get("DESTINATION_DIR")
    forbidden_folders = os.environ.get("FOLDERS_TO_SKIP_REGEX")
    forbidden_files = os.environ.get("FILES_TO_SKIP_REGEX")

    try:
        if not os.path.exists(source_dir): raise Exception("Source folder doesn't exist")
            
        for root, directories, files in os.walk(source_dir):
            if re.search(forbidden_folders, root):
                continue
            else:
                folder_path = re.sub(source_dir, destination_dir, root)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                for filename in files:
                    if re.search(forbidden_files, filename):
                        continue
                    else:
                        file_source = os.path.join(root, filename)
                        file_destination = os.path.join(folder_path, filename)

                        if os.path.exists(file_destination):
                            timestamp_source = os.path.getmtime(file_source)
                            timestamp_destination = os.path.getmtime(file_destination)

                            if timestamp_destination > timestamp_source:
                                continue
                            else:
                                os.remove(file_destination)
                            
                        shutil.copyfile(file_source, file_destination)
                        print(f'{filename} copied!')

        print("Merge Completed!")               
    except Exception as e:
        click.echo(f'Error: {str(e)}')

walk_through_dir()