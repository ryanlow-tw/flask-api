def parse_books_query_strings(collections, query_strings):
    mongo_query = {}

    selected_rows = {'_id': 0}

    order_mapping = {"desc": -1,
                     "asc": 1}

    numeric_mapping = {
        "average_rating": float,
        "original_publication_year": int,
        "price": int
    }

    for key, value in query_strings.items():
        if key != "order" and key not in numeric_mapping:
            mongo_query[key] = {'$regex': value, '$options': 'i'}

    for key in numeric_mapping:
        if key in query_strings:
            function = numeric_mapping[key]
            mongo_query[key] = function(query_strings[key])

    if "order" in query_strings:
        order = order_mapping[query_strings["order"]]
        results = collections.find(mongo_query, selected_rows).sort("price", order)
    else:
        results = collections.find(mongo_query, selected_rows)

    return results
