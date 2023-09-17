from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import os
import shutil

gauth = GoogleAuth()
# Try to load saved client credentials
# Still need verifcation for the first time. Ignore the warning in cmd.

# Uncomment the next line if you have your credential token detail save in a text file of your local machine
gauth.LoadCredentialsFile("/path/to/your/creds.txt") #change the parameter with your path to the text file have credential token
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("/path/to/your/creds.txt") #change the parameter with your path to where you want to save the credential token (basically same as line 12)
drive = GoogleDrive(gauth)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

directory_path = 'path/to/your/folder'  #path of the folder you want to upload
destination_path = 'path/to/where/the/zip/go'  #zip location
archive_name = 'folder'

os.chmod('path/to/your/folder', 0o777)

# Provide the format 'zip' when calling make_archive
shutil.make_archive(
    os.path.join(destination_path, archive_name),
    'zip',  # Specify the archive format
    directory_path
)

os.chmod('/path/to/your/zip/folder.zip', 0o777)

file = drive.CreateFile({'title': 'fileName' + dt_string + '.zip', 'parents': [{'id': ''}]}) #id is the last part of your google drive url 
file.SetContentFile('/path/to/your/zip/folder.zip')
file.Upload()




#The second folder, pretty much the same!
directory_path2 = '/path/to/your/second/folder'  #folder2 path
destination_path2 = '/path/to/where/you/want/to/place/the/zip'  # db zip location
archive_name2 = 'folder2'

os.chmod('/path/to/your/second/folder', 0o777)

# Provide the format 'zip' when calling make_archive
shutil.make_archive(
    os.path.join(destination_path2, archive_name2),
    'zip',  # Specify the archive format
    directory_path2
)

os.chmod('/path/to/your/second/zip/folder/folder2.zip', 0o777)

file2 = drive.CreateFile({'title': 'receipts - ' + dt_string + '.zip', 'parents': [{'id': ''}]})
file2.SetContentFile('/path/to/your/second/zip/folder/folder2.zip')
file2.Upload()
