from src.header import Header
from src.ingredient import Ingredient
from src.cleaner import clean_for_latex, run_latexindent
from src.extra_notes import ExtraNotes
from src.preparation_step import PreparationStep
from string import Template


class Recipe:

    header_str = "cabecalho"
    ingredient_str = "ingredientes"
    preparation_str = "modoDePreparo"
    extra_str = "NotasExtras"

    latex_template = Template(
        r"""$header
    {
        \begin{itemize}
        $ingredients
        \end{itemize}
    }
    {
        \begin{enumerate}
        $preparation
        \end{enumerate}
        
        \vspace{1em}
        
        $extras
    }
    """
    )

    def __init__(self, toml_dict: dict):
        self.header = Header(toml_dict.get(self.header_str))
        self.ingredients = [Ingredient(i) for i in toml_dict.get(self.ingredient_str)]
        self.preparation_steps = [
            PreparationStep(i) for i in toml_dict.get(self.preparation_str)
        ]
        self.extras = ExtraNotes(toml_dict.get(self.extra_str), photo_path=self.header.photo_path)

    def to_latex(
        self, latex_template: Template | None = None, use_latexindent: bool = True
    ):
        if not latex_template:
            latex_template = self.latex_template
        text = latex_template.substitute(
            header=self.header.to_latex(),
            ingredients="\n".join(
                ingredient.to_latex() for ingredient in self.ingredients
            ),
            preparation="\n".join(step.to_latex() for step in self.preparation_steps),
            extras=self.extras.to_latex(),
        )
        if use_latexindent:
            text = run_latexindent(text)
        return text
