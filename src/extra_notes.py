from src.cleaner import clean_for_latex
from string import Template


class ExtraNotes:

    description_str = "descr"
    latex_template = Template(
        r"$photo" r"\begin{itshape}" "\n" r"$text" "\n" r"\end{itshape}"
    )
    photo_template = Template(r"\fotoreceita{0.7\textwidth}{$path$}")

    def __init__(self, extra_notes: dict[str, str] | None, photo_path: str = ""):
        if extra_notes:
            self._extra_notes = extra_notes
            self.text = clean_for_latex(extra_notes.get(self.description_str, ""))
            if photo_path:
                self.photo = self.photo_template.substitute(path=photo_path)
            else:
                self.photo = ""
        else:
            self.text, self.photo = "", ""

    def to_latex(self, latex_template: Template | None = None):
        if not latex_template:
            latex_template = self.latex_template
        return latex_template.substitute(photo=self.photo, text=self.text)
