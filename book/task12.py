def create_file(filepath, data):
    with open(filepath, 'w') as file:
        file.write(data)


book_data = """
126, D, AA, 1000
456, B, BB, 2000
789, C, CC, 3000
"""

create_file('Book.txt', book_data)