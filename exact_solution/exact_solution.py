from itertools import product as p


def countOfSentence(sentence, values):
    count = 0
    for c in sentence:
        if truthOfClause(c, values):
            count += 1
    return count


def truthOfClause(c, values):  # helper
    for b, let in c:
        if b == values[let - 1]:
            return True
    return False


# @profile
def main():
    n, m = tuple([int(x) for x in input().split(" ")])
    sentence = []
    for c in range(m):
        clause = []
        for x in [int(x) for x in input().split(" ")]:
            if x < 0:
                clause.append((False, -x))
            else:
                clause.append((True, x))
        sentence.append(clause)
    all_possible = list(p([True, False], repeat=n))  # it may be faster to not do this as a list
    clause_counts = [countOfSentence(sentence, values) for values in all_possible]
    max_3sat = max(clause_counts)
    best_value_set = all_possible[clause_counts.index(max_3sat)]
    print(max_3sat)
    next = 1
    for val in best_value_set:
        print(next, "T" if val else "F")
        next += 1


if __name__ == "__main__":
    main()
