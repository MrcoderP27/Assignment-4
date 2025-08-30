try:
    file = open("Sample.txt","r")
    lines = file.readlines()
    print("Reading file content:")
    for line in lines:
        print(line.rstrip())
except FileNotFoundError:
    print("Error : The file 'sample.txt' not found.")
except Exception as e:
    print(f"Unexcepted error: {e}")