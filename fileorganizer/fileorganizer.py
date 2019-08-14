# The File Organizer
# Created By Oliwier Gesla 2019

import os
from pathlib import Path
import sys

DIRECTORIES = {

    #Code
    "/Code": [".c", ".cs", ".h", ".p", ".r", ".sh"],
    "/Code/HTML": [".html5", ".html", ".htm", ".xhtml"],
    "/Code/CSS": [".css", ".scss"],
    "/Code/Python": [".py", ".pyd", ".pyw", ".pyx", ".rpy"],
    "/Code/Javascript": [".js"],
    "/Code/Ruby": [".rb", ".rbw"],
    "/Code/Visual Basic": [".vb", ".vbg", ".vbp", ".vbproj", ".vbx",".vbz"],

    #Images
    "/Images/": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd", ".tif"],
    "/Images/RAW": [".3fr", ".ari", ".arw", ".bay", ".crw", ".cr2", ".cr3", ".cap",
                ".dcs", ".dcr", ".dng", ".drf", ".eip", ".erf", ".fff",
                ".gpr", ".iiq", ".k25", ".kdc", ".mdc", ".mef", ".mos", ".mrw",
                ".nef", ".nrw", ".obm", ".orf", ".pef", ".ptx", ".pxn",
                ".r3d", ".raf", ".raw", ".rwl", ".rw2", ".rwz",
                ".sr2", ".srf", ".srw", ".x3f"],

    #Videos
    "/Videos/": [".avi", ".flv", ".f4v", ".f4p", ".f4a", ".f4b", ".mp4", ".wmv", ".mov",
                ".mpg", ".mp2", ".mp4", ".mpeg", ".mpe", ".mpv", ".m4p", ".m4v",
                ".MTS", ".M2TS", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg",
                ".TS", ".wmv" ".3gp"],

    #Documents
    "/Documents/": [".oxps", ".epub", ".pages", ".fdf", ".ods",
                ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                ".rvg", ".rtf", ".rtfd", ".wpd", ".xml"],
    "/Documents/Word Documents": [".doc" ".dot", ".wbk", ".docx", ".docm",
                ".dotx", ".dotm", ".docb"],
    "/Documents/Excel Documents": [".xls", ".xlt", ".xlm", ".xlsx", ".xlsm", ".xltx",
                ".xltm", ".xlsb", ".xla", ".xlam", ".xll", ".xlw"],
    "/Documents/PowerPoint Documents": [".pptx", ".ppt", ".pptm", ".potx", ".potm", ".ppam",
                ".ppsx", ".ppsm", ".sldx", ".sldm"],
    "/Documents/PDF Documents": [".pdf"],

    #Graphics
    "/Graphics/Photoshop": [".psd", ".psb"],
    "/Graphics/Illustrator": [".ai"],

    #Archives
    "/Archives/": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],

    #Audio
    "/Audio/": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    #Text
    "/Text/": [".txt"],

    #Executables
    "/Executables/": [".exe"],

    #Fonts
    "/Fonts/": [".fnt", ".fon", ".otf", ".ttf"]

}

exclude_directories = ["$RECYCLE.BIN"]

# Map file formats

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

# Settings

picked_directory = sys.argv[1]
overwrite_existing_directories = sys.argv[2]
capitalize_first_letter = sys.argv[3]
create_subdirectories = sys.argv[4]

# Main Functions

def organizer(directory): #Primary Organizer

    os.chdir(directory)
    index = ''

    for dirpath, dirnames, filenames in os.walk(directory):

        #Exclude Certain Directories
        dirnames[:] = [d for d in dirnames if d not in exclude_directories]

        #Overwrite Existing Directories Setting
        if overwrite_existing_directories == 'false':
            del(dirnames[:])

        for filename in filenames:

            file_path = Path(dirpath, filename)
            file_format = file_path.suffix.lower()

            if file_format in FILE_FORMATS:
                directory_path = FILE_FORMATS[file_format]

                if create_subdirectories == 'false' and str(Path(directory_path).parent) != "\\":
                    directory_path = str(Path(directory_path).parent)

                directory_path = Path(directory+directory_path)
                directory_path.mkdir(parents=True, exist_ok=True)

                try:
                    file_path.rename(directory_path.joinpath(filename))
                except FileExistsError:
                    if index:
                        index = '('+str(int(index[1:-1])+1)+')' # Append 1 to number in brackets
                    else:
                        index = '(1)'
                    pass
            else:
                directory_path = Path(directory, "Misc")
                directory_path.mkdir(exist_ok=True)
                try:
                    file_path.rename(directory_path.joinpath(filename))
                except FileExistsError:
                    if index:
                        index = '('+str(int(index[1:-1])+1)+')' # Append 1 to number in brackets
                    else:
                        index = '(1)'
                    pass


        # Remove Empty Directories
        try:
            os.rmdir(dirpath)
        except:
            pass

organizer(picked_directory)
