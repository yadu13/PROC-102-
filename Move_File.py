import os 
import shutil
from_dir=r'C:\Users\ChitraDeviHaridasan\Project-102'
to_dir=r'C:\Document_Files'
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension=='':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+ 'Document_Files'
        path3=to_dir+'/'+ 'Document_Files'+'/'+file_name
#Check if directory/Folder path Exists before Moving
#Else Make a NEW Folder/Directory then Move
if os.path.exists(path2):
    print('moving'+file_name+'.......')

#Move from Path1-->Path3
    shutil.move(path1,path3)
else:
    os.makedirs(path2)
    print('moving'+file_name+'.......')
    shutil.move(path1,path3)

    import os 
import shutil
from_dir=r'C:\Users\ChitraDeviHaridasan\Project-102'
to_dir=r'C:\Document_Files'
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension=='':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+ 'Document_Files'
        path3=to_dir+'/'+ 'Document_Files'+'/'+file_name
        if os.path.exists(path2):
            print('moving'+file_name+'..')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving'+file_name+'..')
            shutil.move(path1,path3)

