import random
import pyperclip
import re


def urlInit():  # gets URLs from file
    with open("LINKS.txt", "r", encoding="utf8", errors="ignore") as file:
        lines = file.readlines()
        urls = []

        for line in lines:
            urls.extend(re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", line))

        return urls, lines


urls, lines = urlInit()

print(f"There are {len(urls)} links present")
print("Click ENTER for a random link selection; type 1 to remove links labeled as offline; type 0 then ENTER to exit program")

inputVal = input()

while inputVal != "0":
    if inputVal != "1":  # selects a random link
        link = random.choice(urls)
        pyperclip.copy(link)
        print(link)
    else:
        newText = ""

        for indLine in lines:  # removes offile links if requested
            if "offline" not in indLine:
                newText = newText + indLine

        with open("LINKS.txt", "w", encoding="utf8", errors="ignore") as file:
            file.write(newText)

        urls, lines = urlInit()
        print(f"LINKS file repaired.  There are now {len(urls)} links present")

    inputVal = input()