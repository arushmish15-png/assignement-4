try:
  file_handler = open("sample.txt", "rt")
  
  l1 = file_handler.readline()
  l2 = file_handler.readline()
  
  file_handler.close()
  print("Reading file content:")
  print(f"line 1: {l1}")
  print(f"line 2: {l2}")

except FileNotFoundError:
    print("Error: the file'sample.txt' was not found. ")
