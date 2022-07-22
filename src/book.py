from src.recipe import Recipe
from pathlib import Path
from string import Template
from src.toml_reader import load_recipe
from functools import cmp_to_key

class Book:
    header = open('header.tex', 'r', encoding='utf8').read()
    recipe_entry_template = Template(r"\include{$recipe}" + '\n')
    structure_template = Template(
        r"$header" + '\n' +
        r"\begin{document}" + '\n' +
        r"$recipes" + '\n' +
        r"$appendix" + '\n' +
        r'\end{document}'
              )
    book_path = Path('book.tex')


    def __init__(self, path_to_recipes: Path | None):
        if not path_to_recipes:
            path_to_recipes = Path('/receitas/')
        self.recipe_paths = path_to_recipes.glob('*toml')
        self.path_to_recipes = path_to_recipes

    def build_book_simple(self):
        recipes: list[Recipe] = []
        recipe_txts: list[str] = []
        latex_files: list[Path] = []

        # Converting recipes to latex
        for file in self.recipe_paths:
            recipe = Recipe(load_recipe(file))
            txt = recipe.to_latex(use_latexindent=True)

            latex_file = file.with_suffix('.tex')
            latex_files.append(latex_file)
            with open(latex_file, 'w', encoding='utf8') as fhand:
                fhand.write(txt)

            recipes.append(recipe)
            recipe_txts.append(txt)

        # Sort recipes
        zipped = list(zip(recipes, recipe_txts, latex_files))

        recipe_type_transf = {'salgado': 0, 'doce': 1} # todo: dehardcode this
        zipped.sort(key = lambda x: (x[0].header.name, recipe_type_transf[x[0].header.type]))

        recipes, recipe_txts, latex_files = zip(*zipped)

        book_content = self.structure_template.substitute(
            header = self.header,
            recipes = ''.join([self.recipe_entry_template.substitute(recipe=str(file.parent) + '/' + file.stem) for file in latex_files]),
            appendix = self.recipe_entry_template.substitute(recipe='apendices'),
        )

        with open(self.book_path, 'w', encoding='utf8') as fhand:
            fhand.write(book_content)



