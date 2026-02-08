if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    players = ["alice", "bob", "charlie", "diana"]

    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
    }

    achievements = [
        ("alice", "first_kill"),
        ("alice", "boss_slayer"),
        ("bob", "first_kill"),
        ("charlie", "level_10"),
    ]

    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north"
    }
    high_scorers = [name for name in scores if scores[name] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubled = [scores[name] * 2 for name in scores]
    print(f"Scores doubled: {doubled}")
    active = [name for name in players if name in scores]
    print(f"Active players: {active}")

    print("\n=== Dict Comprehensions Examples ===")
    print(f"Player scores: {scores}")
    score_categories = {
        "high": 3,
        "medium": 2,
        "low": 1
    }
    print(f"Score categories: {score_categories}")
    achievement_counts = {player: 0 for player in players}
    for player, ach in achievements:
        achievement_counts[player] += 1
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_player = {player for player in players}
    print(f"Unique players: {unique_player}")
    unique_achievements = {ach for player, ach in achievements}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {regions[name] for name in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    int_scores = [value for value in scores.values()]
    print(f"Average score: {sum(int_scores) / len(int_scores)}")
    top_player = max(scores, key=scores.get)
    top_score = scores[top_player]
    top_achievements = len([a for a in achievements if a[0] == top_player])
    print(f"Top performer: {top_player} ({top_score} points, {top_achievements} achievements)")
