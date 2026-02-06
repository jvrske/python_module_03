import time


def event_generator(game_events: int) -> None:
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(game_events):
        player = players[i % len(players)]
        event = events[i % len(events)]
        yield f"{player} {event}"


def fibonacci(qnt: int):
    n1 = 0
    n2 = 1
    result = 0
    for i in range(qnt):
        yield result
        n1 = n2
        n2 = result
        result = n1 + n2


def is_prime(n: int):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime(qnt: int):
    nbr = 0
    c = 0
    while c < qnt:
        if is_prime(nbr):
            yield nbr
            c += 1
        nbr += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    game_events = 1000
    print(f"Processing {game_events} game events\n")
    i = 1
    total_events = 0
    treasure_events = 0
    level_up_events = 0
    high_level_players = 0
    start_time = time.time()

    for event in event_generator(game_events):
        print(f"Event {i}: {event}")

        total_events += 1

        if "found treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1

        level = (i % 15)
        if level >= 10:
            high_level_players += 1
        i += 1

    end_time = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")
    print(f"Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib = ""
    ctrl = 1
    for f in fibonacci(10):
        fib += f"{f}"
        if ctrl < 10:
            fib += ", "
            ctrl += 1
    print(f"Fibonacci sequence (first 10): {fib}",)
    prm = ""
    ctrl = 1
    for p in prime(5):
        prm += f"{p}"
        if ctrl < 5:
            prm += ", "
            ctrl += 1
    print(f"Prime numbers (first 5): {prm}")
