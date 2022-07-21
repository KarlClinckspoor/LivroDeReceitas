from src.header import Header


class Recipe:
    # preparation
    description_str = 'descr'
    footnote_str = 'footnote'

    def __init__(self, header: dict, ingredients: list[dict], preparation):
        self.header = Header(header)
        self._ingredients = ingredients
        self._preparation = preparation

        header.get()
