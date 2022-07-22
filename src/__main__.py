import src.book
from pathlib import Path

book = src.book.Book(path_to_recipes=Path('./receitas'))
book.build_book_simple()