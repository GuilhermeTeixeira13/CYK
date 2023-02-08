def read_rules(num_rules):
    rules_mtx = []
    for i in range(num_rules):
        line = list(str(input()).split(" "))
        line.remove("->")
        rules_mtx.append([line[0], ''.join(line[1::])])
    return rules_mtx


def create_triangular_mtx(size):
    return [[[] for _ in range(i+1)] for i in range(size)]


def fill_cell(mtx, mtx_size, l, c, production_result, rules):
    for rule in rules:
        if production_result in rule[1] and rule[0] not in mtx[invert_lines(mtx_size, l)][c]:
            mtx[invert_lines(mtx_size, l)][c].append(rule[0])


def invert_lines(size, line):
    return size - line - 1


def extract_k_length_substrings(s, k):
    return [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == k]


def cartesian_product(l1, l2):
    return [i+str(j) for i in l1 for j in l2]


def extract_substring_combos(s):
    return [[s[:i], s[i:]] for i in range(1, len(s))]


def search_for_str_generators(mtx, mtx_size, s, w):
    return mtx[mtx_size-(len(s)-1)-1][extract_k_length_substrings(w, len(s)).index(s)]


def print_output(mtx, word):
    print("YES") if "S" in mtx[0][0] else print("NO")
    for l in range(len(word)):
        for cell in mtx[l]:
            if cell:
                for w in sorted(cell):
                    print(w+"\t\t", end="") if w == sorted(cell)[-1] else print(w, end=" ")
            else:
                print("\t\t", end="")
        print()
    print("\t\t".join(list(word)))
    print()


def solve(w, rules):
    mtx = create_triangular_mtx(len(w))
    n = len(w)

    for c in range(0, n):
        fill_cell(mtx, n, 0, c, w[c], rules)

    for l in range(n-2, -1, -1):
        interspersed_substrings = extract_k_length_substrings(w, invert_lines(n, l-1))
        for pos, word in enumerate(interspersed_substrings):
            substring_combos = extract_substring_combos(word)
            for combo in substring_combos:
                x = search_for_str_generators(mtx, n, combo[0], w)
                y = search_for_str_generators(mtx, n, combo[1], w)
                cart_prod_xy = cartesian_product(x, y)
                for element in cart_prod_xy:
                    fill_cell(mtx, n, invert_lines(n, l), pos, element, rules)

    print_output(mtx, w)


word_to_recognize = str(input())
m = int(input())
r = read_rules(m)
solve(word_to_recognize, r)

