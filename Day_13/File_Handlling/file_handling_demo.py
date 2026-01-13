# Open file once and read everything
with open('demo.txt', 'r') as file:
    content = file.read()
    print(content)

    # Move cursor back to start
    file.seek(0)

    print("Read one line at a time: ")
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

    file.seek(0)

    print("Read all lines into a list: ")
    lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        print(f"line {i}: {line.strip()}")

    
