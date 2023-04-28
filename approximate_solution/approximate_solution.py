import random
import math


def countOfSentence(sentence, values):
    count = 0
    for c in sentence:
        if truthOfClause(c, values):
            count += 1
    return count


def truthOfClause(c, values):
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

    # Here is where approximation deviates from exact soltuion
    # Exact solution calcs all possible first, but approx uses randomization and hillclimbing
    # Initialize the current best value set to a random boolean assignment of length n
    best_value_set = [random.choice([True, False]) for _ in range(n)]

    # Eval count of satisfied clauses for the curr best value set
    max_3sat = countOfSentence(sentence, best_value_set)

    # Set the temperature to some high initial value
    # Set the cooling factor something less than 1
    temperature = 100.0
    cooling = 0.95

    # Iterate until the temperature falls below .001
    while temperature > 0.001:
        # Select a random neighbor value set by flipping the value of a random variable in the current best value set
        neighbor_value_set = list(best_value_set)

        # The largest speed bottleneck is generating a random int
        # *This is true for small graphs*
        flip_index = random.randint(0, n - 1)
        neighbor_value_set[flip_index] = not neighbor_value_set[flip_index]

        # Eval the count of satisfied clauses for the neighbor value set
        neighbor_count = countOfSentence(sentence, neighbor_value_set)

        # If neighbor val higher, neighbor is now best
        if neighbor_count > max_3sat:
            best_value_set = neighbor_value_set
            max_3sat = neighbor_count

        # else, accept the neighbor set with probability
        else:
            # prob is used to determine whether or not to accept the neighboring value set
            # as the new best value set. As temp decreases prob of accepting decreases
            prob = math.exp((neighbor_count - max_3sat) / temperature)
            if random.random() < prob:
                best_value_set = neighbor_value_set
                max_3sat = neighbor_count
        temperature *= cooling

    print(max_3sat)
    next = 1
    for val in best_value_set:
        print(next, "T" if val else "F")
        next += 1


if __name__ == "__main__":
    main()
