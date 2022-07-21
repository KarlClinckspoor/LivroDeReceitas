import src.toml_reader as toml_reader
from pathlib import Path

def test_read_recipe():
    recipe = toml_reader.load_recipe(Path("./test_arroz_japones.toml"))
    print(recipe['cabecalho'])
    print(recipe['ingredientes'][0])
    print(recipe['ingredientes'][1])
    print(recipe['modoDePreparo'])

