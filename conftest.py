import pytest
from main import BooksCollector

@pytest.fixture
def books():
    collector = BooksCollector()
    collector.add_new_book('Дюна')
    collector.add_new_book('Дом лжи')
    collector.add_new_book('Ребекка')
    collector.set_book_genre('Дюна', 'Фантастика')
    collector.set_book_genre('Дом лжи', 'Детективы')
    collector.set_book_genre('Ребекка', 'Детективы')
    return collector