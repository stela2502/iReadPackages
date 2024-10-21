#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Check for required non-Python executables
REQUIRED_EXECUTABLES=("samtools" "bedops")

for exe in "${REQUIRED_EXECUTABLES[@]}"; do
    if ! command -v $exe &> /dev/null; then
        echo "$exe is not installed. Please install it."
        exit 1
    fi
done

# Copy executables to /usr/local/bin
echo "Copying scripts to /usr/local/bin..."

SCRIPTS=$(find iReadPackage/ -maxdepth 1)
for script in "${SCRIPTS[@]}"; do
    cp "$script" "/usr/local/bin/$(basename "$script")"  # Copy to /usr/local/bin
    chmod +x "/usr/local/bin/$(basename "$script")"  # Make it executable
done

echo "Installation complete! You can now run the scripts from anywhere."

