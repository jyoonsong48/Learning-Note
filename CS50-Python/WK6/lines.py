import sys

if len(sys.argv) == 1:
    print("Too few commend-line arguments")
    sys.exit(1)
if len(sys.argv) == 3:
    print("Too many commend-line arguments")
    sys.exit(1)

is_docstring = False
docstring_type = None
docstring_d = '"""'
docstring_s = "'''"

while sys.argv[1].endswith(".py"):
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    else:
        lines = file.readlines()
        count_lines = []
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            """
            if is_docstring:
                if line.endswith(docstring_type):
                    is_docstring = False
                    docstring_type = None
                continue
            if (line.startswith(docstring_d) and line.endswith(docstring_d) and len(line) > 3) or \
            (line.startswith(docstring_s) and line.endswith(docstring_s) and len(line) > 3):
                continue
            if line.startswith(docstring_d):
                is_docstring = True
                docstring_type = docstring_d
                continue
            if line.startswith(docstring_s):
                is_docstring = True
                docstring_type = docstring_s
                continue
            """
            count_lines.append(i)
        print(len(count_lines))
        break

else:
    print("Not a python file")
    sys.exit(1)

