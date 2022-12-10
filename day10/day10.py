with open("input.txt") as file:
    X = 1
    cycles = 0
    remainingCycles = 0
    sprite = 0

    part1 = 0

    rows = 6
    pixels = 40
    charSize = 2
    CRT = [["  " for _ in range(pixels)] for _ in range(rows)]
    for line in file:
        cmd = line.split()[0]
        V = 0
        if cmd == "noop":
            remainingCycles += 1
        elif cmd == "addx":
            remainingCycles += 2
            V = int(line.split()[1])

        while remainingCycles > 0:
            row = cycles // pixels
            pixel = cycles % pixels

            if pixel in range(sprite - 1, sprite + 2):
                CRT[row][pixel] = "##"

            if pixel == 20:
                part1 += cycles * X

            cycles += 1
            remainingCycles -= 1

        X += V
        sprite = X

    print("Part 1:", part1, end="\n\n")

    print("Part 2:")
    left = "|| "
    right = "||"
    border = "=" * (pixels * 2 + len(left) + len(right))
    print(border)
    for row in CRT:
        print("|| " + "".join(row) + "||")
    print(border)
