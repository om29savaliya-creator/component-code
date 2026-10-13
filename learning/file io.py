
def check_for_line(n):
    i=1
    word=n
    line = True

    with open("practice.txt","r") as f:
        while line :    
            line =f.readline()
            if(word in line):
                print("your word found in line ",i)
                return ""
            i += 1
    return -1

print(check_for_line("learning"))