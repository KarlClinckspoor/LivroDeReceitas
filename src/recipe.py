from src.header import Header
from src.ingredient import Ingredient
from src.cleaner import clean_for_latex
from src.extra_notes import ExtraNotes
from src.preparation_step import PreparationStep
from string import Template

class Recipe:

    header_str = 'cabecalho'
    ingredient_str = 'ingredientes'
    preparation_str = 'modoDePreparo'
    extra_str = 'NotasExtras'

    latex_template = Template(r"""$header
    {
        \begin{itemize}
        $ingredients
        \end{itemize}
    }
    {
        \begin{enumerate}
        $preparation
        \end{enumerate}
        
        $extras
    }
    """)

    def __init__(self, toml_dict: dict):
        self.header = Header(toml_dict.get(self.header_str))
        self.ingredients = [Ingredient(i) for i in toml_dict.get(self.ingredient_str)]
        self.preparation_steps = [PreparationStep(i) for i in toml_dict.get(self.preparation_str)]
        self.extras = ExtraNotes(toml_dict.get(self.extra_str))


    def to_latex(self, latex_template: Template | None = None):
        if not latex_template:
            latex_template = self.latex_template
        return latex_template.substitute(
            header=self.header.to_latex(),
            ingredients='\n'.join(ingredient.to_latex() for ingredient in self.ingredients),
            preparation='\n'.join(step.to_latex() for step in self.preparation_steps),
            extras=self.extras.to_latex()
            )


