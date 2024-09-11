Реализованы следующие проверки 
test_add_new_book_add_three_books - проверяем, что все книги добавились
test_add_new_book_add_extra_book - проверяем, что к раннее созданным через фикстуру книгам можно добавить еще
test_set_book_genre - проверяем, что книге корректно присвоился жанр
test_set_book_genre_invalid_genre - проверяем, что, если жанр не из списка жанров, он не присваивается книге
test_get_book_genre - проверяем что книги корректно добавились в словарь и корректно вернулись
test_get_book_genre_non_existent - проверяем вызов жанра книги, по несуществующему ключу в словаре.
test_get_books_with_specific_genre - проверяем корректность филтрации книг по жанрам
test_get_books_with_specific_genre_non_existent_genre - проверяем поведение при вызове список книг по несуществующему жанру
test_get_books_genre - проверяем получение корректного словаря, после добавления в него книг
test_get_books_genre_empty - проверяем вызов словаря, если в него не добавлены книги
test_get_books_for_children - проверяем корректность вызова детских книг из словаря
test_get_books_for_children_no_valid_books - проверяем корректность вызова детских книг, если таковых нет в словаре
test_add_book_in_favorites - проверяем корректность добавления книг в избранное
test_add_book_in_favorites_non_existent_book - проверяем корректность поведения при добавлении в избранное книг, которых нет в словаре
test_delete_book_from_favorites - проверяем корректность удаления книг из избранного
test_get_list_of_favorites_books_add_two_favorites - проверяем корректность вызова списка избранных книг, после добавления их в него
