import os


all_files = os.listdir()
print(len(all_files))
count = 0
 
for FILE in all_files:
    print(FILE)
    if FILE.endswith('.txt'):
            print('reading')
            count+=1
            foo = str(FILE)
            with open(foo, 'r') as file :
              filedata = file.read()
            
#             print('\n',filedata)

            # Replace the target string
            filedata = filedata.replace('bla/foo/CDR_Test/cdr/foo', 'bla/foo/CDR/cdr/foo')


            # Write the file out again
            with open(foo, 'w') as file:
              file.write(filedata)
print(count)

