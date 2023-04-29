from exact_solution import max3SATdec
def threeSAT(sentence, num_of_var):
    return max3SATdec(sentence, num_of_var, len(sentence))

def main():
    sentence = [
        [(True, 1), (True, 2), (True, 3)],
        [(True, 1), (True, 2), (False, 3)],
        [(True, 1), (False, 2), (True, 3)],
        [(True, 1), (False, 2), (False, 3)],
        [(False, 1), (True, 2), (True, 3)],
        [(False, 1), (True, 2), (False, 3)],
        [(False, 1), (False, 2), (True, 3)],
        [(False, 1), (False, 2), (False, 3)],
        [(False, 1), (False, 2), (False, 3)],
        [(False, 1), (False, 2), (False, 3)],
    ]
    print(threeSAT(sentence, 3))

if __name__ == "__main__":
    main()
