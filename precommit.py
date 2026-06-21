import toml, os

readme = """# School Modpack
Click on [releases](https://github.com/MrurBo/school-modpack/releases), select what platform you are on, and add it to your launcher. All the mods download and update automatically, but you can still add your own  (As long as it's client-sided only.)

# Contributing
Refer to the [Packwiz installation guide](https://packwiz.infra.link/installation/), and use ONLY mods from modrinth by using `packwiz modrinth add [modrinth URL, slug/project ID, or search]`. If removing, use `packwiz refresh` once the file is removed. Changing the `README.md` file requires editing the `precommit.py` file. The modlist gets appended to the end of the README.md.
Before commiting, refer to the next section.

# Before Commiting
Run the precommit script in the project base directory:
```
uv venv
uv sync
uv run precommit.py
```

# Modlist"""

mods = sorted(
    map(lambda p: toml.load("mods/" + p), os.listdir("mods/")),
    key=lambda mod: mod["side"],
)
modslist = "\n"
client = [x for x in mods if x["side"] == "client"]
server = [x for x in mods if x["side"] == "server"]
server = [x for x in mods if x["side"] == "both"]
modslist += "\n## Client-sided\n"
for mod in client:
    modslist += f" * [**{mod['name']}**](https://modrinth.com/project/{mod['update']['modrinth']['mod-id']})\n"
modslist += "\n## Server-sided\n"
for mod in server:
    modslist += f" * [**{mod['name']}**](https://modrinth.com/project/{mod['update']['modrinth']['mod-id']})\n"
modslist += "\n## Both\n"
for mod in server:
    modslist += f" * [**{mod['name']}**](https://modrinth.com/project/{mod['update']['modrinth']['mod-id']})\n"

with open("readme.md", "w", encoding="utf-16") as f:
    f.write(readme + modslist)
