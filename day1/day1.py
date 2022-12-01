print(
    sum(
        sorted(
            [
                sum([int(num) for num in elf.split()])
                for elf in open("day1/input.txt").read().split("\n\n")
            ],
            reverse=True,
        )[:3]
    )
)
