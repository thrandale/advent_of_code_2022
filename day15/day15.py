# The line to check for Part 1
targetLine = 2_000_000
# The bounds for Part 2
maxRange = 4_000_000


def mDist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


with open("input.txt") as file:
    sensors = []
    beaconsOnLine = set()
    part1 = 0
    part2 = 0

    # a values are '/' lines, b values are '\' lines
    # using the formula y = x + a or y = -x + b
    aValues = set()
    bValues = set()

    # Get the sensors that can see the target line
    for line in file:
        sensor, beacon = line.split(": ")
        sX, sY = [int(x.split("=")[1]) for x in sensor.split(", ")]
        bX, bY = [int(x.split("=")[1]) for x in beacon.split(", ")]
        sRange = mDist((sX, sY), (bX, bY))
        sensors.append((sX, sY, sRange))

        # Check if the beacon is on the target line
        if bY == targetLine:
            beaconsOnLine.add(bX)

        # add the a and b values for the line, a values are '/' lines, b values are '\' lines
        aValues.add(sY - sX + sRange + 1)
        aValues.add(sY - sX - sRange - 1)
        bValues.add(sX + sY + sRange + 1)
        bValues.add(sX + sY - sRange - 1)

    """ Part 1 """
    seenRanges = []
    seen = set()

    # Find the range of points each sensor can see
    for sensor in sensors:
        distFromTarget = abs(targetLine - sensor[1])

        # Check if the sensor can see the target line
        if sensor[2] < distFromTarget:
            continue

        # get the points that the sensor can see
        newRange = sensor[2] - distFromTarget
        seenRanges.append((sensor[0] - newRange, sensor[0] + newRange))

    # Merge overlapping ranges
    seenRanges = sorted(seenRanges, key=lambda x: x[0])
    ranges = []
    for r in ranges:
        if not ranges or ranges[-1][1] < r[0]:
            ranges.append(r)
        else:
            ranges[-1] = (min(ranges[-1][0], r[0]), max(ranges[-1][1], r[1]))

    # Add all the points in the ranges to the set of seen points
    for start, end in seenRanges:
        seen.update(range(start, end + 1))

    # Remove any beacons that are on the line
    for point in beaconsOnLine:
        seen.discard(point)

    """ Part 2 """
    # Find a point where two of the lines intersect, and can't be seen by any sensors
    for a in aValues:
        for b in bValues:
            intersection = ((b - a) // 2, (a + b) // 2)
            # Make sure the point is in range
            if all(0 < c < maxRange for c in intersection):
                # Check if it can be seen by any sensors
                if all(
                    mDist(intersection, (sensor[0], sensor[1])) > sensor[2]
                    for sensor in sensors
                ):
                    part2 = intersection[0] * 4_000_000 + intersection[1]

    print("Part 1:", len(seen))
    print("Part 2:", part2)
