from src.recipe import Recipe
from src.toml_reader import load_recipe
from pathlib import Path

def test_recipe():
    recipe_dict = load_recipe(Path('./test_arroz_japones.toml'))
    recipe = Recipe(recipe_dict)
    print(recipe.to_latex())
