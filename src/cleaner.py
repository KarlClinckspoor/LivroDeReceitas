from subprocess import run
import os

def clean_for_latex(text: str):
    bad_chars = ["_"]
    for char in bad_chars:
        text = text.replace(char, fr"\{char}")
    return text


def run_latexindent(text: str):
    temp_filename = "temp.tex"
    with open(temp_filename, "w", encoding="utf8") as fhand:
        fhand.write(text)
    command = ["latexindent", "--overwrite", "--silent", temp_filename]
    proc = run(command)
    cleaned = open(temp_filename, "r", encoding="utf8").read()
    os.remove(temp_filename)
    os.remove(temp_filename[:-4] + '.bak0')
    return cleaned
