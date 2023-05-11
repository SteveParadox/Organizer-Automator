import random
from operator import itemgetter
from flask import Flask, render_template


app = Flask(__name__)

TEAMS = ["Team A", "Team B", "Team C", "Team D", "Team E",
         "Team F", "Team G", "Team H", "Team I",
         "Team J", "Team K", "Team L", "Team M", "Team N", "Team O", "Team P", "Team Q",
         "Team R", "Team S", "Team T"]

league_table = {team: {"Played": 0, "Won": 0, "Drawn": 0, "Lost": 0, "GF": 0, "GA": 0, "Points": 0} for team in TEAMS}


def calculate_goal_diff(team):
    return team["GF"] - team["GA"]


def simulate_game(home_team, away_team):
    home_goals = random.randint(0, 5)
    away_goals = random.randint(0, 5)
    print(f"{home_team} {home_goals} - {away_goals} {away_team}")
    return home_goals, away_goals


def update_table(home_team, away_team, home_goals, away_goals):
    league_table[home_team]["Played"] += 1
    league_table[away_team]["Played"] += 1
    league_table[home_team]["GF"] += home_goals
    league_table[away_team]["GF"] += away_goals
    league_table[home_team]["GA"] += away_goals
    league_table[away_team]["GA"] += home_goals
    league_table[home_team]["GD"] = calculate_goal_diff(league_table[home_team])
    league_table[away_team]["GD"] = calculate_goal_diff(league_table[away_team])
    if home_goals > away_goals:
        league_table[home_team]["Won"] += 1
        league_table[home_team]["Points"] += 3
        league_table[away_team]["Lost"] += 1
    elif home_goals < away_goals:
        league_table[away_team]["Won"] += 1
        league_table[away_team]["Points"] += 3
        league_table[home_team]["Lost"] += 1
    else:
        league_table[home_team]["Drawn"] += 1
        league_table[away_team]["Drawn"] += 1
        league_table[home_team]["Points"] += 1
        league_table[away_team]["Points"] += 1


def play_game_week(game_week):
    for i in range(len(TEAMS)):
        for j in range(len(TEAMS)):
            if i < j:
                home_team = TEAMS[i]
                away_team = TEAMS[j]

                home_goals, away_goals = simulate_game(home_team, away_team)
                update_table(home_team, away_team, home_goals, away_goals)

    table = sorted(league_table.items(), key=lambda x: (-x[1]['Points'], -x[1]['GD']))
    return table


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/league-table")
def get_league_table():
    table = play_game_week(2)
    league_table_sorted = sorted(table, key=lambda x: (-x[1]['Points'], -x[1]['GD']))
    #print(league_table_sorted)
    return render_template("league_table.html", league_table=league_table_sorted)


@app.route("/game-week/<int:game_week>")
def get_game_week(game_week):
    if game_week < 1 or game_week > len(TEAMS) - 1:
        return "Invalid game week"

    start_team_index = (game_week - 1) * 2
    end_team_index = start_team_index + 2

    game_week_teams = TEAMS[start_team_index:end_team_index]
    game_week_fixture = []

    for i in range(len(game_week_teams)):
        for j in range(len(game_week_teams)):
            if i < j:
                home_team = game_week_teams[i]
                away_team = game_week_teams[j]
                game_week_fixture.append((home_team, away_team))

    table = play_game_week(game_week)
    return render_template("game_week.html", game_week=game_week, game_week_fixture=game_week_fixture, league_table=table)


if __name__ == "__main__":
    app.run(debug=True)