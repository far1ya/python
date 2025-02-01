text="""   this is first line
                this is second line
                    this is third line"""
for line in text.splitlines():
    print(line.lstrip())
