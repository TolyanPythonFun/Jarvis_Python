import glob
import os

files = glob.glob('C:\**\*.py', recursive=True)
for file in enumerate(files, start=1):
    #if 'Malwarebytes' in str(file).split('\\')[-1]:
    #    print(file)
    print(file)


