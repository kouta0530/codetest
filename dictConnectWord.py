import itertools


def filter(list):
    dict = {}

    for i in list:
        if i not in dict:
            dict[i] = {}
        else:
            list.remove(i)

    return list


def main():
    lines = ["fajf"]
    text = [c for c in lines[0]]
    wordDict = [c for c in text]
    hash = {}
    li = []
    for i in range(1, len(text)+1):
        li += list(itertools.combinations(text, r=i))

    test = filter(li)
    print(len(test))


main()
