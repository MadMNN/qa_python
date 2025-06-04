from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_too_long_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('X' * 41)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_genre_sets_correctly(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_set_book_genre_invalid_genre_does_nothing(self):
        collector = BooksCollector()
        collector.add_new_book('Неизвестная')
        collector.set_book_genre('Неизвестная', 'Поэзия')
        assert collector.get_book_genre('Неизвестная') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_for_children_excludes_age_restricted(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Король Лев']

    def test_add_book_in_favorites_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_add_book_in_favorites_ignores_if_not_in_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        assert collector.get_books_genre() == {'451 градус по Фаренгейту': ''}
