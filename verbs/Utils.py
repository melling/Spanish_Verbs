
# https://stackoverflow.com/questions/2556108/rreplace-how-to-replace-the-last-occurrence-of-an-expression-in-a-string


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


if __name__ == "__main__":
    print("Starting Utils...")
    verb = "preferir"
    v1 = rreplace(verb, "e", "ie", 1)
    print(v1)
