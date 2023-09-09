def compute_first(productions, non_terminal, first_sets):
    if non_terminal in first_sets:
        return first_sets[non_terminal]

    first_set = set()
    for production in productions[non_terminal]:
        symbol = production[0]

        if symbol.isupper():
            first_set.update(compute_first(productions, symbol, first_sets))
        else:
            first_set.add(symbol)

    first_sets[non_terminal] = first_set
    return first_set


def compute_follow(productions, non_terminal, follow_sets, start_symbol):
    if non_terminal in follow_sets:
        return follow_sets[non_terminal]

    follow_set = set()
    if non_terminal == start_symbol:
        follow_set.add("$")

    for nt, prods in productions.items():
        for prod in prods:
            if non_terminal in prod:
                index = prod.index(non_terminal)
                if index + 1 < len(prod):
                    next_symbol = prod[index + 1]
                    if next_symbol.isupper():
                        follow_set.update(
                            compute_first(productions, next_symbol, follow_sets)
                        )
                    else:
                        follow_set.add(next_symbol)
                elif index + 1 == len(prod):
                    if nt != non_terminal:
                        follow_set.update(
                            compute_follow(productions, nt, follow_sets, start_symbol)
                        )

    follow_sets[non_terminal] = follow_set
    return follow_set


# Example grammar
grammar = {"S": ["AB", "BC"], "A": ["aA", "b"], "B": ["bB", "c"], "C": ["cC", "a"]}

start_symbol = "S"

first_sets = {}
follow_sets = {}

# Calculate FIRST sets
for non_terminal in grammar.keys():
    compute_first(grammar, non_terminal, first_sets)

# Calculate FOLLOW sets
for non_terminal in grammar.keys():
    compute_follow(grammar, non_terminal, follow_sets, start_symbol)

# Print FIRST sets
print("FIRST Sets:")
for non_terminal, first_set in first_sets.items():
    print(f"FIRST({non_terminal}) = {first_set}")

# Print FOLLOW sets
print("\nFOLLOW Sets:")
for non_terminal, follow_set in follow_sets.items():
    print(f"FOLLOW({non_terminal}) = {follow_set}")
