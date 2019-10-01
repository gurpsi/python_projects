import os

path = "C:\\Users\\<USER_NAME>\\Desktop\\python\\Test\\ads_views\\"

print('path:', path)

all_files = os.listdir(path)
print('Path for listed dir:', os.listdir(path), '/nLength for all the files:', len(all_files))
count = 0

print('\nAll files:', all_files)

for FILE in all_files:
    #     print(FILE)
    if FILE.endswith('.sql'):
        # print('reading')
        count += 1
        foo = str(FILE)
        with open(path + foo, 'r') as file:
            filedata = file.read()

        #             print('\n',filedata)

        # Replace the target string
        filedata = filedata.replace('<REPLACE STRING>', '<REPLACE TEXT>')

        # Write the file out again
        with open(path + foo, 'w') as file:
            file.write(filedata)
print(count)
