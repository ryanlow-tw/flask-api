def parse_data(table_results):
    data = []
    for row in table_results:
        data.append(
            {
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
                'average_rating': f'{row.average_rating}'
            }
        )

    return {'results': data}


def parse_query(query_strings, query_builder, database):

    order = query_strings.get("order", "").lower()
    name = query_strings.get("name", "").lower()
    price = query_strings.get("price", None)
    language = query_strings.get("language", "").lower()
    isbn = query_strings.get("isbn", "")
    isbn13 = query_strings.get("isbn13", "")

    if name != "":
        query_builder = query_builder.filter(database.c.author.contains(name))

    if price is not None:
        price = int(price)
        query_builder = query_builder.filter(database.c.price.contains(price))

    if language != "":
        query_builder = query_builder.filter(database.c.language_code.contains(language))

    if isbn != "":
        query_builder = query_builder.filter(database.c.isbn.contains(isbn))

    if isbn13 != "":
        query_builder = query_builder.filter(database.c.isbn13.contains(isbn13))

    if order == "desc":
        query_builder = query_builder.order_by(database.c.price.desc()).all()

    elif order == "asc":
        query_builder = query_builder.order_by(database.c.price).all()

    else:
        query_builder = query_builder.all()

    return query_builder
