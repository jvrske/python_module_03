def rare_achiev(alice: set, bob: set, charlie: set, all_achiev: set):
    rare = set()
    for achievement in all_achiev:
        count = 0

        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1

        if count == 1:
            rare.add(achievement)
    print(f"Rare achievements (1 player): {rare}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon",
               "perfectionist"}

    print(f"Player alice achievements: {alice}")
    print(f"Player alice achievements: {bob}")
    print(f"Player alice achievements: {charlie}")

    print("\n=== Achievement analytics ===")
    all_achiev = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achiev}")
    print(f"Total unique achievements: {len(all_achiev)}")

    common_achiev = alice.intersection(bob).intersection(charlie)
    print(f"\nCommon to all players: {common_achiev}")
    rare_achiev(alice, bob, charlie, all_achiev)

    equal = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {equal}")

    unique = alice.difference(bob)
    print(f"Alice unique: {unique}")
    unique_bob = bob.difference(alice)
    print(f"Bob unique: {unique_bob}")
