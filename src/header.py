class Header:
    # header
    name_str = "nome"
    approve_K_str = 'karlAprova'
    approve_KK_str = 'karenAprova'
    label_str = 'label'
    photo_str = 'foto' # todo: move picture to another part?
    type_str = 'tipo'
    tags_str = 'tags'
    tested_str = 'testado'

    latex_template = r"\receitaemoji[{tested}{approveK}{approveKK}]\{{name}{label}\}"

    def __init__(self, header: dict):
        self._header = header
        self.name = header.get(self.name_str, '')
        self.label = header.get(self.label_str, "") # todo: make label if not provided
        self.photo_path = header.get(self.photo_str, "")
        self.type = header.get(self.type_str, "")
        self.tags = header.get(self.tags_str, tuple())
        self.tested = header.get(self.tested_str, "")
        self.approveK = header.get(self.approve_K_str, "")
        self.approve_KK = header.get(self.approve_KK_str, "")

    def to_latex(self, latex_template: str | None = None):
        if not latex_template:
            latex_template = self.latex_template
        latex_template.format(tested = self.tested, approveK = self.approveK, approveKK = self.approve_KK, name=self.name, label=self.label)