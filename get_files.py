#To do:
# get the list of blocks in some way
# get the list of entities in some way
# get toki pona translations
# get cartouches for names
import pathlib
minecraft_directory = pathlib.Path(input("\nminecraft directory:\n"))
version = input("version (example: 1.19.4, 1.21.1): ")
assets_directory=(minecraft_directory/"versions"/version/version/"assets"/"minecraft").resolve()
print(list((assets_directory/"textures").iterdir()))
with open(assets_directory) as a:
    pass