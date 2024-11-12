disk_size_bytes = 1.44 * 1024 * 1024

book_size_bytes = 100 * 50 * 25 * 4

num_books = disk_size_bytes // book_size_bytes

print(f"Количество книг, помещающихся на дискету: {num_books}")