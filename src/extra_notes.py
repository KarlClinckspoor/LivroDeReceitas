from src.cleaner import clean_for_latex
from string import Template

class ExtraNotes:

    description_str = 'descr'
    latex_template = Template(r'\emph{$text}')

    def __init__(self, extra_notes: dict[str, str]):
        self._extra_notes = extra_notes
        self.text = clean_for_latex(extra_notes.get(self.description_str, ""))

    def to_latex(self, latex_template: Template | None = None):
        if not latex_template:
            latex_template = self.latex_template
        return latex_template.substitute(text = self.text)