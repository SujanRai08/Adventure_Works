# handle errors gracefulluy and ensures the pipeline doesn't crash 
# common errors - valuerror, typerror,KeyError 
# handle expected error during the data processing 
try:
    result = int('abc')
except ValueError as e:
    print(f'error:{e}')
finally:
    print('processing completing')
# usages - validate data during etl jobs or api requests: 

# file handling - efficently file reading/writing is crucial for data engineering 
with open('data.txt','w') as file:
    file.write('id,name\n1,alice\n2,bob\n')

with open('data.txt','r') as file:
    for line in file:
        print(line.strip())
        

# managing large files 
# use generators for handle large files 
def read_large_file(file_name):
    with open(file_name,'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('large_data.txt'):
    print(line)
    