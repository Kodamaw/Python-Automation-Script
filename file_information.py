with open("file_locations.txt") as f:
    folders = f.readlines()
    

if len(folders) < 6:
    with open("file_locations.txt", "w") as f:
        f.writelines(['\n','\n','\n','\n','\n','\n'])
        folders = ['\n','\n','\n','\n','\n','\n']
   
        
folder_locations = {
    "SourceFolder":folders[0].rstrip("\n"),
    "AudioFolder":folders[1].rstrip("\n"),
    "VideoFolder":folders[2].rstrip("\n"),
    "ImageFolder":folders[3].rstrip("\n"),
    "DocumentFolder":folders[4].rstrip("\n"),
    "MiscFolder":folders[5].rstrip("\n")
}


file_extensions = {
"audio":[".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"], # List of audio file extensions

"video":[".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", 
               ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".m2ts"], # List of video file extensions

"document":[".pdf", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".doc", ".docx", ".zip"], # List of document file extensions

"image":[".jpg", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw",
             ".cr2", ".nrw", ".k25",".bmp", ".dib", ".heif", ".heic", ".indd", ".ind", ".indt",
             ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".jfif",
             ".gif", ".jif", ".jfi", ".jpe"] # List of image file extensions
}