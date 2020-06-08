import os
import sys
import time
from bs4 import BeautifulSoup as bs
from urllib import request
from typing import List


def readFile(name: str) -> List[str]:
    fre = open(name, "r")
    content = [x[1:-1].replace("\\n", "\n")
               for x in fre.read()[1:-1].split(", ")]
    fre.close()
    return content


def test(id: int, out: str) -> None:
    os.system("./a.out < cin.txt > cout.txt")

    USR = open("cout.txt", "r").read().strip()
    OUT = out.strip()

    if (USR == OUT):
        print(f"\n\033[92mTest Case #{id+1}: AC (Accepted)\033[0m")
        print(USR + "\n")
    else:
        print(f"\n\033[91mTest Case #{id+1}: WA (Wrong Answer)\033[0m")
        print(USR + "\n\n" + OUT + "\n")


def testAll(src: str) -> None:
    print(f"> g++ {src}")
    os.system(f"g++ {src}")

    print("\n> Running Tests")

    IN = readFile("in.txt")
    OUT = readFile("out.txt")
    CASES = len(IN)

    for i in range(CASES):
        CIN = open("cin.txt", "w")
        CIN.write(IN[i])
        CIN.close()

        test(i, OUT[i])


def set(problemId: str) -> None:
    pId = problemId
    problem = f"https://codeforces.com/problemset/problem/{pId[:-1]}/{pId[-1]}"
    with request.urlopen(problem) as response:
        content = response.read()
    soup = bs(content, features="html.parser")

    IN = []
    OUT = []
    NAME = str(soup.findAll("div", {"class": "title"})[0])[
        22:-6].replace(" ", "\ ") + ".cpp"

    for case in soup.findAll("div", {"class": "input"}):
        txt = str(case.findAll("pre")[0])[5:-6].replace("<br/>", "\n")
        IN.append(txt)

    for case in soup.findAll("div", {"class": "output"}):
        txt = str(case.findAll("pre")[0])[5:-6].replace("<br/>", "\n")
        OUT.append(txt)

    fin = open("in.txt", "w").write(str(IN))
    fout = open("out.txt", "w").write(str(OUT))


if __name__ == "__main__":
    if sys.argv[1] == "s":
        set(sys.argv[2])

    elif sys.argv[1] == "g":
        commands = [
            "git add .", f'git commit -m "{" ".join(sys.argv[2:])}"', "git push", "clear"]

        for cmd in commands:
            print(f"> {cmd}")
            os.system(cmd)
            time.sleep(0.5)

    else:
        src = (" ".join(sys.argv[1:])).replace(" ", "\ ")
        testAll(src)
