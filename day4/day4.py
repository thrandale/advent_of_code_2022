input = open("input.txt").read().splitlines()

part1 = 0
part2 = 0
for line in input:
    ranges = [
        [int(x), int(y)] for x, y in [range.split("-") for range in line.split(",")]
    ]
    part1 += (ranges[0][0] - ranges[1][0]) * (ranges[0][1] - ranges[1][1]) <= 0
    part2 += (ranges[0][0] <= ranges[1][1]) and (ranges[0][1] >= ranges[1][0])

print("Part 1:", part1)
print("Part 2:", part2)
