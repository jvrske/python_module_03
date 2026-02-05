import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            scores = []
            total_players = []

            for args in sys.argv[1:]:
                score = int(args)
                scores.append(score)
            print(f"Scores processed: {scores}")

            for player in sys.argv[1:]:
                total_players.append(player)
            print(f"Total players: {len(total_players)}")

            total_score = sum(scores)
            print(f"Total score: {total_score}")

            average_score = total_score / len(total_players)
            print(f"Average score: {average_score}")

            high_score = max(scores)
            print(f"High score: {high_score}")

            lowest_score = min(scores)
            print(f"Low score: {lowest_score}")

            range = high_score - lowest_score
            print(f"Score range: {range}")
        except ValueError:
            print("Invalid input")
