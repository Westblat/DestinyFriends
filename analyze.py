import json

def analyze(file_name):
    f = open(file_name)
    data = json.load(f)
    playerCount = {}

    print("Analyzation started")
    for y in data:

            players_list = y["Response"]["entries"]
            players_in_activity = []
            for player_data in players_list:
                # Removed players who did not complete the raid
                if player_data.get('values').get("completed").get("basic").get("displayValue") == 'No':
                    continue
                try:
                    # Gets the name of the player
                    player = player_data["player"]["destinyUserInfo"]["bungieGlobalDisplayName"]
                    if player == '':
                        # Legacy players who don't have the previous name
                        player = player_data["player"]["destinyUserInfo"]["displayName"]
                    if playerCount.get(player):
                        playerCount[player] = playerCount[player] + 1
                    else:
                        playerCount[player] = 1
                    players_in_activity.append(player)
                except KeyError:
                    # Sometimes the player is just gone, this is that
                    print("ERROR", player_data["player"])
                    pass

    sorted_count = dict(sorted(playerCount.items(), key=lambda item: item[1], reverse=True))
    top_n = 10
    top_sorted_count = list(sorted_count.items())[:top_n]
    print("final player count ", sorted_count)
    print(f'Top {top_n} raid buddies')
    for name, amount in top_sorted_count:
        print(name, amount)
    print("\nUnique raiders", len(sorted_count.keys()))
    more_then_one = {k: v for k, v in sorted_count.items() if v > 1}
    print("\nUnique raiders with more then 1 clear", len(more_then_one.keys()))


if __name__ == "__main__":
    analyze("4611686018467273361.json")
