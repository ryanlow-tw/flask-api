def parse_data(results):
    data = []
    for row in results:
        data.append({
            'id': f'{row.id}',
            'author': f'{row.author}',
            'title': f'{row.title}',
            'image_url': f'{row.image_url}',
            'small_image_url': f'{row.small_image_url}',
            'price': f'{row.price}',
            'isbn': f'{row.isbn}',
            'isbn13': f'{row.isbn13}',
            'original_publication_year': f'{row.original_publication_year}',
            'original_title': f'{row.original_title}',
            'language_code': f'{row.language_code}',
            'average_rating': f'{row.average_rating}'})

    return data
