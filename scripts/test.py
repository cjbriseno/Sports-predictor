from nba_api.stats.endpoints import playercareerstats, playergamelog

# Pull Lebron James career stats
print("\n--Fetchng Lebron James career stats--")
career = playercareerstats.PlayerCareerStats(player_id='2544')
df = career.get_data_frames()[0]
print(df)

print("\n--Fetching Lebron James 2024-25 Playoffs game log--")
gamelog = playergamelog.PlayerGameLog(player_id='2544', season='2024-25', season_type_all_star='Playoffs')
df = gamelog.get_data_frames()[0]
print(df)

print("\n--test--")
print(df.iloc[3])

df.to_csv("lebron_james_24_playoffs.csv")

print("--Average 5--")
df['PTS_Average5'] = df['PTS'].mean()
print(df['PTS_Average5'])