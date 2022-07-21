from src.cleaner import clean_for_latex
from string import Template

class Ingredient:

    # ingredients
    quantity_str = 'qtde'
    unit_str = 'unidade'
    observation_str = 'obs'
    name_str = 'nome'

    latex_template = Template(r"\item $quantity $unit de $name. ($obs)")
    def __init__(self, ingredient: dict[str, str]):
        self.name: str = ingredient.get(self.name_str, '')
        try:
            self.quantity: float = float(ingredient.get(self.quantity_str, ''))
        except ValueError as e:
            print(f"Exception {e}. Quantity added isn't a valid number, replaced with 0")
            self.quantity: float = 0
        self.unit: str = ingredient.get(self.unit_str, '')
        self.observation: str = clean_for_latex(ingredient.get(self.observation_str, ''))

        if self.name == '':
            raise Warning("Ingredient added without name! Will appear blank")
        if self.quantity == 0:
            raise Warning("Ingredient added without or with invalid quantity! Will appear blank")
        if self.unit == '':
            raise Warning("Ingredient added without unit! Will appear blank")

    def to_latex(self, latex_template: Template | None = None) -> str:
        if not latex_template:
            latex_template = self.latex_template
        return latex_template.substitute(quantity = self.quantity, unit = self.unit, name = self.name, obs = self.observation) + '\n'
