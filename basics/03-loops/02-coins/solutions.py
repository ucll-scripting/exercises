def coins(one, two, five, goal):
    for x in range(0, one+1):
        for y in range(0, two+1):
            for z in range(0, five+1):
                if x + 2 * y + 5 * z == goal:
                    return True

    return False