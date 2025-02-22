# why? - handling the large datasets efficiently without work loading everthing into memory.memoryview

# streaming large file processing
def read_large_file(file_path):
    with open(file_path,"r") as file:
        for line in file:
            yield line.strip()

for line in read_large_file("large_datasets.csv"):
    print(line) 