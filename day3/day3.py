input = open("input.txt").read().splitlines()

lowerOffset = 96
upperOffset = 64 - 26

halves = [(line[len(line) // 2 :], line[: len(line) // 2]) for line in input]
shared = ["".join((set(a) & set(b))) for a, b in halves]
part1 = sum([ord(x) - (lowerOffset if x.islower() else upperOffset) for x in shared])

rucksacks = [input[i : i + 3] for i in range(0, len(input), 3)]
shared = ["".join((set(a) & set(b) & set(c))) for a, b, c in rucksacks]
part2 = sum([ord(x) - (lowerOffset if x.islower() else upperOffset) for x in shared])

print("Part 1:", part1)
print("Part 2:", part2)

# solutions, but in single lines
# print("Part 1:", sum([ord(x) - (96 if x.islower() else (64 - 26)) for x in ["".join(set(a) & set(b)) for a, b, in [(line[len(line) // 2 :], line[: len(line) // 2]) for line in input]]]))
# print("Part 2:", sum([ord(x) - (96 if x.islower() else (64 - 26)) for x in ["".join(set(a) & set(b) & set(c)) for a, b, c in [input[i : i + 3] for i in range(0, len(input), 3)]]]))
