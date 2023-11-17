bash
#!/bin/bash
download_folder="/home/lpatrizi/Downloads/"
python_script="/home/lpatrizi/personal_projects/python_scripts/sort_file.py"

while true; do
    inotifywait -e create -r "$download_folder"
    python3 "$python_script"
done
