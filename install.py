import os
import shutil
import subprocess
import sys

# Function to install Python dependencies
def install_requirements():
    if os.path.exists('requirements.txt'):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

# Function to copy scripts to /usr/local/bin and make them executable
def install_scripts():
    source_dir = 'iReadPackage'
    destination_dir = '/usr/local/bin'

    # Ensure destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Search for all Python files in the iReadPackage directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            full_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(destination_dir, os.path.basename(file))
            print(f"Copying {full_file_path} to {dest_file_path}")
            shutil.copy2(full_file_path, dest_file_path)
            os.chmod(dest_file_path, 0o755)  # Make the script executable

# Main installation routine
def main():
    print("Installing requirements...")
    install_requirements()

    print("Installing scripts...")
    install_scripts()

    print("Installation complete!")

if __name__ == '__main__':
    main()
