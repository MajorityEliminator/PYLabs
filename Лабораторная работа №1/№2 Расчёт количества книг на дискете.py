# TODO Найдите количество книг, которое можно разместить на дискете

total_memory = 1.44*pow(1024, 2)
bytes_per_symbol = 4
symbols_per_line = 25
lines_per_page = 50
pages_per_book = 100

total_books = total_memory//(bytes_per_symbol*symbols_per_line*lines_per_page*pages_per_book)

print("Количество книг, помещающихся на дискету:", int(total_books))
