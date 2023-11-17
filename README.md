# Organize your folder

This small Python class performs the task of organizing a folder. 

Usage for the python script 
```
python script.py [-f FOLDER_PATH] [-i FILE_PATH]") 

```

**Arguments**:
```
   -f, --folder    Set the folder path (default: /default_folder)
   -i, --file      Set the file path 
```

##Example
For example, I've used it in combination with a bash script to organize my downloads folder so that each time I download a new file, it goes into the most suitable subfolder within downloads. This way, I always have everything in order (more or less). 
On Linux, you can use 'inotify-tools' and a simple bash script to monitor your download folder for new files and run your Python script when a new file is detected. 
Here's how you can set it up:
   $sudo apt-get install inotify-tools
Then you need to create a bash script that in my case is watch_downloads.sh and make it executable. Then execute the script.
Now, your script will be executed each time a new file is created in your download folder. Remember to keep the bash script running in the background, as it will continuously monitor for new files and execute your Python script as needed. You can run it at system startup or using tools like 'screen' or 'tmux' to keep it running persistently.
