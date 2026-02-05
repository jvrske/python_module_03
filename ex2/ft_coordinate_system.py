import math


def create_tuple(x: int, y: int, z: int) -> tuple:
    return tuple([x, y, z])


def distance(p1, p2) -> int:
    x1, y1, z1, = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x2 - x1)**2 +
        (y2 - y1)**2 +
        (z2 - z1)**2
    )


def parse(posit: str) -> tuple:
    try:
        posit = posit.split(",")
        if len(posit) != 3:
            raise ValueError("Not enough corrdinates")
        x = int(posit[0])
        y = int(posit[1])
        z = int(posit[2])
        print(f"Parsed position: ({x}, {y}, {z})") 
        return create_tuple(x, y, z)
    except ValueError as error:
        print(f"Parsing invalid coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, \
Args: {error.args}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    position = (10, 20, 5)
    position2 = (0, 0, 0)
    print(f"Position created: {position}")

    dist = distance(position, position2)
    print(f"Distance between {position2} and {position} = {dist:.2f}\n")

    print("Parsing coordinates: \"3,4,0\"")
    position3 = parse("3,4,0")
    dist = distance(position3, position2)
    print(f"Distance between {position2} and {position3}: {dist:.1f}\n")

    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    parse("abc,def,ghi")

    print("\nUnpacking demonstration:")
    player = create_tuple(3, 4, 0)
    print(f"Player at x={player[0]}, y={player[1]}, z={player[2]} ")
    print(f"Coordinates: X={player[0]}, Y={player[1]}, Z={player[2]} ")