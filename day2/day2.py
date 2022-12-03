input = [
    tuple(x for x in line.split(" ")) for line in open("input.txt").read().splitlines()
]

types = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
scores = [0, 3, 6]


def getScore(theirs, mine):
    score = mine
    if theirs == mine:
        return score + scores[1]
    elif mine == (theirs + 1) or mine == (theirs - 2):
        return score + scores[2]
    else:
        return score


def getScore2(theirs, score):
    if score == 1:
        mine = theirs - 1 if theirs > 1 else 3
    elif score == 3:
        mine = theirs + 1 if theirs < 3 else 1
    else:
        mine = theirs
    return mine + scores[score - 1]


print(sum([getScore2(types[their], types[mine]) for their, mine in input]))
