import os 
import shutil
import sys
import os

def print_usage():
        print("Usage: python script.py [-f FOLDER_PATH] [-i FILE_PATH]")
        print("Description: The program organize your file in the target folder according to its type \n if you don't specify the filepath, the program organize the whole folder")
        print("Arguments:")
        print("  -f, --folder    Set the folder path (default: /home/lpatrizi/Downloads)")
        print("  -i, --file      Set the file path ")

def main():
        # Default values
        folder_path = "/home/lpatrizi/Downloads/"
        file_path = ""

        # Parse command line arguments
        for i in range(1, len(sys.argv), 2):
                arg = sys.argv[i]
                if arg == "-f" or arg == "--folder":
                    folder_path = sys.argv[i + 1]
                elif arg == "-i" or arg == "--file":
                    file_path = sys.argv[i + 1]
                elif arg in {"-h", "--help"}:
                    print_usage()
                    sys.exit(0)
                else:
                    print(f"Error: Unknown option {arg}")
                    print_usage()
                    sys.exit(1)

        # Validate folder path
        if not os.path.isdir(folder_path):
                print("Error: The provided folder path is not valid.")
                sys.exit(1)

        # Validate file path
        if file_path != "":
                if not os.path.isfile(file_path):
                        print("Error: The provided file path is not valid.")
                        sys.exit(1)

        print(f"Folder Path: {folder_path}")
        print(f"File Path: {file_path}")

        return folder_path, file_path



class Organizer:
        def __init__(self, folder):
                self.folder = folder

                self.file_types = {
                        "pdf":  "PDFs",
                        "png":  "Images",
                        "jpg":  "Images",
                        "jpeg": "Images",
                        "txt":  "TextFiles",
                        "docx": "Doc",
                        "zip":  "Archives",
                        "epub": "Ebooks",
                        "mobi": "Ebooks",
                        "xlsx": "Tables",
                        "pptx": "Presentation",
                        "mp4":  "Video",
                        "mp3":  "Music",
                        "MOV":  "Video",
                        "gif":  "Gif"
                        
                        # Add more file types and corresponding folders as needed
                }

        def sort_folder(self):

                for filename in os.listdir(self.folder):
                        file_path = os.path.join(self.folder, filename)

                        # Check if it's a file and not a directory
                        if os.path.isfile(file_path):
                                self.sort(filename, file_path)

        def sort_new_file(self, filename):
                file_path = os.path.join(self.folder, filename)

                # Check if it's a file and not a directory
                if os.path.isfile(file_path):
                        self.sort(filename, file_path)


        def sort(self, filename, file_path):
                        # Extract the file extension
                        _, file_extension = os.path.splitext(filename.lower())

                        # Determine the destination folder based on the file extension
                        destination_folder = self.file_types.get(file_extension[1:], "Other")

                        # Create the destination folder if it doesn't exist
                        destination_path = os.path.join(self.folder, destination_folder)
                        os.makedirs(destination_path, exist_ok=True)

                        # Move the file to the destination folder
                        shutil.move(file_path, destination_path)
                        # print(f"Moved {filename} to {destination_folder}")



if __name__ == '__main__':

        folder_path, file_path = main()
        sorter = Organizer(folder_path)
        if file_path != "":
                sorter.sort_new_file(file_path)
        else:
                sorter.sort_folder()
