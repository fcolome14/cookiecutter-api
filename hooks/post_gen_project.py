import os
import shutil
import sys
from pathlib import Path

def move_project_contents_to_parent():
    project_dir = Path.cwd()
    project_name = "{{ cookiecutter.project_slug }}"
    subfolder_path = project_dir / project_name

    # Ensure the subfolder exists
    if not subfolder_path.exists() or not subfolder_path.is_dir():
        print(f"Error: Expected subfolder '{project_name}' not found.")
        sys.exit(1)

    print(f"Moving contents from {subfolder_path} to {project_dir}...")

    # Move each file/folder from subfolder to the root
    for item in subfolder_path.iterdir():
        dest = project_dir / item.name
        if dest.exists():
            print(f"Skipping existing item: {dest}")
        else:
            shutil.move(str(item), str(dest))
            print(f"Moved: {item.name}")

    # Remove the now-empty subfolder
    try:
        subfolder_path.rmdir()
        print(f"Removed empty directory: {subfolder_path}")
    except OSError:
        print(f"Could not remove {subfolder_path} — directory not empty")

if __name__ == "__main__":
    move_project_contents_to_parent()
