import os

# 1. Create & Write
f = open("file.txt", "w")
f.write("File Handling Example\n")
f.close()

# 2. Read
f = open("file.txt", "r")
print(f.read())
f.close()

# 3. Append
f = open("file.txt", "a")
f.write("Appending new data\n")
f.close()

# 4. Read Line by Line
f = open("file.txt", "r")
for line in f:
    print(line)
f.close()

# 5. Update / Modify
f = open("file.txt", "r")
data = f.read()
f.close()

data = data.replace("Example", "Demo")

f = open("file.txt", "w")
f.write(data)
f.close()

# 6. Rename File
os.rename("file.txt", "new_file.txt")

# 7. Check File Exists
if os.path.exists("new_file.txt"):
    print("File exists")

# 8. Delete File
os.remove("new_file.txt")
