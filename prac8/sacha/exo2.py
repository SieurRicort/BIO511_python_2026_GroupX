#!usr/bin/python3

def seed_and_extend(query=None, target=None, k=None, max_mismatches=None):
    """Return candidate placements supported by an exact seed."""
    hits = set()
    

    for query_start in range(len(query) - k + 1):
        seed = query[query_start:query_start + k]
        target_start = target.find(seed)

        while target_start != -1:
            placement_start = target_start - query_start
            placement_end = placement_start + len(query)

            if placement_start >= 0 and placement_end <= len(target):
                target_window = target[placement_start:placement_end]
                mismatches = sum(
                    query_base != target_base
                    for query_base, target_base in zip(query, target_window)
                )

                if mismatches <= max_mismatches:
                    hits.add((placement_start, target_window, mismatches))

            target_start = target.find(seed, target_start + 1)

    return hits


database = {
    "gene_A": "GGGATGACCATGATTACGCCAAGCTTT",
    "gene_B": "TTTCCCGGGAAATTTCCCGGG"
}

query = "ATGACCATGATT"

for name, sequence in database.items():
    for hit in seed_and_extend(query=query, target=sequence, k=4, max_mismatches=1):
        print(name, hit)

# 2.1
# gene_A (3, 'ATGACCATGATT', 0) index = 3 so 4th letter

# 2.2
# gene_A (3, 'ATGACCATGATT', 0)
# query = 'ATGACCATGACT' + mistmatch = 1 -> gene_A (3, 'ATGACCATGATT', 1)
# C at index = 10 was a T in first query.

# 2.3

