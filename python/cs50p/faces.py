def main():
    text = input("Text: ")
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


