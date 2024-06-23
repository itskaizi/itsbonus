import csv
import os

def read_nba_standings(file_name):
    eastern_teams_home_lt_away = []
    eastern_point_diff_total = 0
    western_point_diff_total = 0
    eastern_count = 0
    western_count = 0

    print(f"Trying to open file: {file_name}")

    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳過標題行

        for row in reader:
            if len(row) < 9:
                continue  # 跳過欄位數量不足的行

            conference = row[0]
            team = row[1]
            home_record = row[7]
            away_record = row[8]
            points_for = float(row[5])
            points_against = float(row[6])

            # 東區主場勝率低於客場勝率
            if conference == 'Eastern' and calculate_win_rate(home_record) < calculate_win_rate(away_record):
                eastern_teams_home_lt_away.append(team)

            # 計算東區和西區球隊的總得分減失分
            if conference == 'Eastern':
                eastern_point_diff_total += points_for - points_against
                eastern_count += 1
            elif conference == 'Western':
                western_point_diff_total += points_for - points_against
                western_count += 1

    eastern_avg_point_diff = eastern_point_diff_total / eastern_count if eastern_count != 0 else 0
    western_avg_point_diff = western_point_diff_total / western_count if western_count != 0 else 0

    return eastern_teams_home_lt_away, eastern_avg_point_diff, western_avg_point_diff

def calculate_win_rate(record):
    wins, losses = map(int, record.split('-'))
    total_games = wins + losses
    return wins / total_games

# 替換為你的CSV檔案的實際路徑
file_name = '/Users/chihkai/Desktop/workspace/nba_standings.csv'  # 假設檔案位於此路徑

print(f"Current working directory: {os.getcwd()}")

eastern_teams_home_lt_away, eastern_avg_point_diff, western_avg_point_diff = read_nba_standings(file_name)

print("(1) Teams from the Eastern Conference with a win-loss percentage greater than 0.5:")
for team in eastern_teams_home_lt_away:
    print(team)

if eastern_avg_point_diff > western_avg_point_diff:
    print("\n(2)Teams from the Western Conference with a lower win rate at home games compared to away games:")
    print(eastern_avg_point_diff)
else:
    print("\n(3) Average difference between points scored and points allowed for teams in the Eastern Conference with a win-loss percentage greater than 0.5:")
    print(western_avg_point_diff)
