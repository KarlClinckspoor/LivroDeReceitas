from __future__ import annotations

import tomli
from pathlib import Path


def load_recipe(path: Path) -> dict:
    with open(path, "r", encoding="utf8") as fhand:
        try:
            recipe = tomli.loads(fhand.read())
        except tomli.TOMLDecodeError as e:
            print(f'Could not read file {path}. Exception {e}')
            raise Exception
    return recipe
