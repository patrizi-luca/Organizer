bash
#!/bin/bash
download_folder="/my_download_folder/"
python_script="/my_script_folder/sort_file.py"

while true; do
    inotifywait -e create -r "$download_folder"
    python3 "$python_script"
done
