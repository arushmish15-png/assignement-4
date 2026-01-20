input1 = input("enter text to write to the file: ")

with open("output.txt", "wt") as fh:
    fh.write(input1+"\n")
print("data successfully written to output.txt")

input2 = input("enter additional text to append: ")

with open("output.txt", "at") as fh:
    fh.write(input2+"\n")
print("data successfully appended \n ")
print(f"final content of output.txt:")

with open("output.txt", "rt") as fh:
    content = fh.read()
    print(content)
