def convert(text):
    #dic = {58:None, 41:"\U0001F642", 40:"\U0001F62D"}
    #text = text.translate(dic)
    text = text.replace(":)","\U0001F642")
    text = text.replace(":(","\U0001F62D")
    print(text)

def main():
    text = input("")
    convert(text)

main()