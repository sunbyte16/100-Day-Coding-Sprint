def process_queries(q, queries):
    stock = {}

    for query in queries:
        if query[0] == '1':
            # Add chocolates
            choc_type = query[1]
            qty = int(query[2])
            stock[choc_type] = stock.get(choc_type, 0) + qty

        else:
            # Sell chocolates
            choc_type = query[1]
            qty = int(query[2])

            available = stock.get(choc_type, 0)
            sold = min(qty, available)

            print(sold)
            stock[choc_type] = available - sold


if __name__ == "__main__":
    q = int(input())
    queries = [input().split() for _ in range(q)]
    process_queries(q, queries)
