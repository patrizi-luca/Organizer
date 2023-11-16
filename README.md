CREATE AN AUTOMATED SCRIPT EVERY TIME YOU DOWNLOAD A FILE 

To create an automated script that runs every time you download a file, you'll need to set up a "watcher" or "listener" for your downloads folder and execute your script when a new file is detected. Here are the general steps to achieve this:

1. *Choose a Script*: Create the Python script that you want to run when a new file is downloaded. This script should contain the actions you want to perform on the downloaded file.

2. *Determine the Download Folder*: Identify the folder where your downloads are saved. This folder's location may vary depending on your operating system and web browser.

3. *File System Monitoring*: You'll need a way to monitor this folder for changes. You can use Python libraries like `watchdog` for this purpose. Install it if you have…
On Linux, you can use `inotify-tools` and a simple bash script to monitor your download folder for new files and run your Python script when a new file is detected. Here's how you can set it up:

1. *Install `inotify-tools`*:

   bash
   sudo apt-get install inotify-tools
   

   This command installs the `inotify-tools` package, which provides tools for monitoring file system events.

2. *Create a Bash Script*:

   Create a bash script (e.g., `watch_downloads.sh`) that uses `inotifywait` to monitor your download folder:

   bash
   #!/bin/bash
   download_folder="/path/to/your/download/folder"
   python_script="/path/to/your_script.py"

   while true; do
       inotifywait -e create -r "$download_folder"
       python3 "$python_script"
   done
   

   Make sure to replace `/path/to/your/download/folder` with the actual path to your download folder and `/path/to/your_script.py` with the path to your Python script.

3. *Make the Script Executable*:

   Make the script executable using the following command:

   bash
   chmod +x watch_downloads.sh
   

4. *Run the Bash Script*:

   Execute the bash script to start monitoring your download folder:

   bash
   ./watch_downloads.sh
   

Now, your script will be executed each time a new file is created in your download folder. Remember to keep the bash script running in the background, as it will continuously monitor for new files and execute your Python script as needed. You can run it at system startup or using tools like `screen` or `tmux` to keep it running persistently.
