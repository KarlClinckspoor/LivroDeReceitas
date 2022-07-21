def clean_for_latex(text: str):
    bad_chars = ['_']
    for char in bad_chars:
        text = text.replace(char, fr'\{char}')
    return text