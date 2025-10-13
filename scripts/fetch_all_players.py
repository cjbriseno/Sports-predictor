"""
This script fetches all NBA players using NBA_API, converts to dataframe, and saves to CSV.
It includes active and inactive players.
"""
from nba_api.stats.static import players
import pandas as pd
import os

# get_players returns a list of dictionaries, each representing a player.
all_nba_players = players.get_players()
print("\nNumber of players fetched: {}".format(len(all_nba_players)))
print(all_nba_players[:10])

print("\nConverting to dataframe...")
df_all_nba_players = pd.DataFrame(all_nba_players)
print(df_all_nba_players.head())

print("\nSaving to csv...")
save_path = "../data/raw/players/all_nba_players.csv"
df_all_nba_players.to_csv(save_path, index = False)
print(f"✅ Saved to: {os.path.abspath(save_path)}")
