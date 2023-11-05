with open("abc.txt") as f, open("xyz.txt", "w") as f2:
    for line in f:
        line = line.strip()
        if len(line) <= 80:
            f2.write(line + "\n")
        else:
            words = line.split(" ")
            new_line = ""
            for word in words:
                if len(new_line) + len(word) > 80 and new_line:
                    f2.write(new_line + "\n")
                    new_line = ""
                new_line += word + " "       
            f2.write(new_line + "\n")