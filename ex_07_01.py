fname = input("Enter file name: ")
fh = open(fname)

for lines in fh:
    lines=lines.rstrip()
    lines=lines.upper()
    print(lines)