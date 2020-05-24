import os
import unicodedata

test_string = r"""
\receita{Peito de frango com alecrim, sálvia, alho e limão}{
	\begin{itemize}
		\item Filé de peito de frango.
		\item Sal
		\item Pimenta do reino
		\item Ghee (manteiga clarificada)
		\item Alho picado
		\item Sálvia
		\item Alecrim
		\item Limão grande (suco)
		\item Manteiga
	\end{itemize}
}{
	\begin{enumerate}
		\item Temperar os filés de frango com sal e pimenta do reino.
		\item Picar o alho, sálvia e alecrim
		\item Extrair o suco do limão
		\item Fritar ligeiramente no ghee até dourar um pouco. Reservar.
		\item Na mesma frigideira ainda com ghee, fritar o alho picado e acrescentar a
		      sálvia, alecrim bem picados.
		\item Saltear um pouco e acrescentar o suco do limão.
		\item Após aquecer o suco, acrescentar a manteiga.
		\item Após derreter a manteiga, voltar o frango até o molho ficar bem incorporado.
	\end{enumerate}
}
"""

# import pdb; pdb.set_trace()

def find_recipes(string: str) -> list:
    depth = 0
    count = 0
    recipes = []
    recipe = []
    mode = 'seeking'  # seeking recipe, counting
    string_seek = r'\receita'

    for i, char in enumerate(string):
        if mode == 'seeking':
            if string[i:i+len(string_seek)] == string_seek:
                mode = 'counting'
            else:
                continue
        if mode == 'counting':
            if count == 3:
                recipe.append(char)
                recipes.append(''.join(recipe))
                recipe = []  # Resets for next recipe
                mode = 'seeking'  # Seeks next recipe
                count = 0
                continue
            if char == '{':
                depth += 1
            if char == '}':
                depth -= 1
                if depth == 0:
                    count += 1
            recipe.append(char)

    return recipes


def export_recipe(recipe: str) -> None:
    recipe_title = recipe[recipe.find('{')+1:recipe.find('}')]
    # TODO: Are there other things to clean?
    # Remove unwanted characters
    clean_recipe_title = recipe_title.replace('\\checkmark', '').replace('/', '').strip()
    # Capitalize each word
    clean_recipe_title = ''.join(list(map(str.capitalize, clean_recipe_title.split())))
    # Remove accents
    clean_recipe_title = unicodedata.normalize('NFD', clean_recipe_title).encode('ascii', 'ignore').decode('utf-8')
    with open(clean_recipe_title+'.tex', 'w') as fhand:
        fhand.write(recipe)
        print(f'Outputted recipe {clean_recipe_title}')
        add_recipe_file(clean_recipe_title, 'recipes.tex')
        print('Added include string to recipes.tex')


def add_recipe_file(recipe_file_name: str, main_tex_file: str) -> None:
    if os.path.isfile(main_tex_file):
        mode = 'a'
    else:
        mode = 'w'
    includestring = r"\input{" + f"{recipe_file_name}" + "}\n"
    with open(main_tex_file, mode) as fhand:
        fhand.write(includestring)


if __name__ == '__main__':
    fhand = open('ReceitasSalgadas.tex', 'r').read()
    recipes = find_recipes(fhand)
    for recipe in recipes:
        export_recipe(recipe)
