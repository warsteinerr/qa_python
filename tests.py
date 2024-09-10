from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_three_books(self, books):
        assert len(books.get_books_genre()) == 3

    def test_add_new_book_add_extra_book(self, books):
        books.add_new_book('Смешнулькин')
        assert 'Смешнулькин' in books.get_books_genre()

    def test_set_book_genre(self,books):
        books.set_book_genre('Дюна', 'Фантастика')
        assert books.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, books):
        books.add_new_book('Смешнулькин')
        books.set_book_genre('Смешнулькин', 'Хохотушки')
        assert books.get_book_genre('Смешнулькин') == ''


    @pytest.mark.parametrize('book,book_genre', [['Дюна', 'Фантастика'],['Дом лжи','Детективы'],['Ребекка', 'Детективы']])
    def test_get_book_genre(self, books, book, book_genre):
        books.set_book_genre(book, book_genre)
        assert books.get_book_genre(book) == book_genre

    def test_get_book_genre_non_existent(self, books):
        assert books.get_book_genre('Идиот') is None

    @pytest.mark.parametrize('book_genre, expected_books', [['Детективы', ['Дом лжи', 'Ребекка']], ['Фантастика', ['Дюна']]])
    def test_get_books_with_specific_genre(self, books, book_genre, expected_books):
        assert books.get_books_with_specific_genre(book_genre) == expected_books

    def test_get_books_with_specific_genre_non_existent_genre(self, books):
        assert len(books.get_books_with_specific_genre('Хохотульки')) == 0

    def test_get_books_genre(self, books):
        expected_books_genre = {'Дюна': 'Фантастика', 'Дом лжи': 'Детективы', 'Ребекка': 'Детективы' }
        assert books.get_books_genre() == expected_books_genre

    def test_get_books_genre_empty(self):
        test_books = BooksCollector()
        assert test_books.get_books_genre()  == {}

    def test_get_books_for_children(self, books):
        assert books.get_books_for_children() == ['Дюна']

    def test_get_books_for_children_no_valid_books(self,books):
        books.set_book_genre('Дюна', 'Детективы')
        assert books.get_books_for_children() == []

    def test_add_book_in_favorites(self, books):
        books.add_book_in_favorites('Дюна')
        assert len(books.favorites) == 1

    def test_add_book_in_favorites_non_existent_book(self, books):
        books.add_book_in_favorites('Смешнулькин')
        assert 'Смешнулькин' not in books.favorites

    def test_delete_book_from_favorites(self, books):
        books.add_book_in_favorites('Дюна')
        books.delete_book_from_favorites('Дюна')
        assert len(books.favorites) == 0


    def test_get_list_of_favorites_books_add_two_favorites(self, books):
        books.add_book_in_favorites('Дюна')
        books.add_book_in_favorites('Дом лжи')
        expected_favorites = books.favorites
        assert books.get_list_of_favorites_books() == expected_favorites





