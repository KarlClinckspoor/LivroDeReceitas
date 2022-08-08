from src.cleaner import clean_for_latex
from string import Template


class PreparationStep:
    description_str = "descr"
    footnote_str = "footnote"

    latex_template = Template(r"\item $description $footnote")

    def __init__(self, preparation: dict):
        self._preparation = preparation
        self.description = clean_for_latex(preparation.get(self.description_str, ""))
        self.footnote = clean_for_latex(preparation.get(self.footnote_str, ""))
        if self.footnote:
            self.footnote = r'\footnote{' + self.footnote + '}'

        if self.description == "":
            raise Warning("Preparation step is missing a description!")

    def to_latex(self, latex_template: Template | None = None):
        if not latex_template:
            latex_template = self.latex_template
        return latex_template.substitute(
            description=self.description, footnote=self.footnote
        )
