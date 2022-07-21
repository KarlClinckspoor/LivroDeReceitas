from __future__ import annotations

import tomli
from pathlib import Path


def load_recipe(path: Path) -> dict:
    with open(path, 'r', encoding='utf8') as fhand:
        recipe = tomli.loads(fhand.read())
    return recipe
