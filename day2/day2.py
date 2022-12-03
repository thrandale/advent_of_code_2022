import re

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

print("Part 1:", sum([getScore(types[theirs], types[mine]) for theirs, mine in input]))
print("Part 2:", sum([getScore2(types[their], types[mine]) for their, mine in input]))

# solutions, but in single lines
# print("Part 1:", sum([b + (3 if a == b else (6 if b == (a + 1) or b == (a - 2) else 0)) for a, b in [[int(x), int(y)] for x, y in [re.sub("A|X", "1", re.sub("B|Y", "2", re.sub("C|Z", "3", line))).split(" ") for line in open("input.txt").read().splitlines()]]]))
# print("Part 2:", sum([3 * (b - 1) + ((a - 1 if a > 1 else 3) if b == 1 else ((a + 1 if a < 3 else 1) if b == 3 else a)) for a, b in [[int(x), int(y)] for x, y in [re.sub("A|X", "1", re.sub("B|Y", "2", re.sub("C|Z", "3", line))).split(" ") for line in open("input.txt").read().splitlines()]]]))
