from markdown import markdown 
from os import listdir, path

def read(fp: str) -> str:
    f = open(fp, "r")
    all = f.read()
    f.close()
    return all

def write(fp: str, all: str):
    f = open(fp, "w")
    f.write(all)
    f.close()

index = read("templates/index.html")
entry = read("templates/entry.html")
entries = ""

for net in listdir("nets"):
    if not net.endswith(".md"):
        continue
    fp = path.join("nets", net)
    entries += entry.replace("[net]", markdown(read(fp)))

write("index.html", index.replace("[entries]", entries))
