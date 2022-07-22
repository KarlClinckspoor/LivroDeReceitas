from string import Template
from src.cleaner import clean_for_latex


class Header:
    name_str = "nome"
    approve_K_str = "karlAprova"
    approve_KK_str = "karenAprova"
    label_str = "label"
    photo_str = "foto"
    type_str = "tipo"
    tags_str = "tags"
    tested_str = "testado"

    latex_template = Template(
        r"\receitaemoji[$tested $approveK $approveKK]{$name \label{$label}}"
    )

    def __init__(self, header: dict):
        self._header = header
        self.name = header.get(self.name_str, "")
        self.label = header.get(self.label_str, "")  # todo: make label if not provided
        self.photo_path = header.get(self.photo_str, "")
        self.type = header.get(self.type_str, "")
        self.tags = header.get(self.tags_str, tuple())
        self.tested = r"\testado" if header.get(self.tested_str, "") else ""
        self.approveK = r"\karlAprova" if header.get(self.approve_K_str, "") else ""
        self.approve_KK = r"\karenAprova" if header.get(self.approve_KK_str, "") else ""

    def to_latex(self, latex_template: Template | None = None):
        if not latex_template:
            latex_template = self.latex_template
        return latex_template.substitute(
            tested=self.tested,
            approveK=self.approveK,
            approveKK=self.approve_KK,
            name=self.name,
            label=self.label,
        )
