def remove_left_recursion(grammar):
    non_terminals = list(grammar.keys())
    new_grammar = {}

    for A in non_terminals:
        productions = grammar[A]
        non_A_productions = [prod for prod in productions if prod[0] != A]
        A_productions = [prod[1:] for prod in productions if prod[0] == A]

        if A_productions:
            A_prime = A + "'"
            new_grammar[A] = [prod + A_prime for prod in non_A_productions]
            new_grammar[A_prime] = [prod + A_prime for prod in A_productions] + ["ε"]
        else:
            new_grammar[A] = productions

    return new_grammar


# Example left-recursive grammar
left_recursive_grammar = {"A": ["Aα", "β"], "B": ["Bβ", "γ"]}

# Remove left recursion
new_grammar = remove_left_recursion(left_recursive_grammar)

# Print the modified grammar without left recursion
for non_terminal, productions in new_grammar.items():
    print(f"{non_terminal} -> {' | '.join(productions)}")
