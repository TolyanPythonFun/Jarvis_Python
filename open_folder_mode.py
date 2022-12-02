import os

input_ = input('')

for root, dirs, files, in os.walk('C:\\'):
    if str(root).endswith(input_):
        print(root)
        os.system(f"explorer.exe {root}")

# os.system(r"explorer.exe C:")