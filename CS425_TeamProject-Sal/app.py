from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

# def create_connection():
#         connection = mysql.connector.connect(
#             host="localhost",
#             user=input("Enter username: "),
#             password=getpass("Enter password: "),
#             database="nba_DB_2"
#         )
#         return connection


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Zb44696924&", #getpass("Enter password: "), 
            database="nba_DB_2"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

""" Flask Backend """
@app.route('/')
def index():
    return render_template('index.html')
    #return redirect(url_for('manage_teams'))


@app.route('/players', methods=['GET', 'POST'])
def manage_players():
    conn = create_connection()
    if request.method == 'POST':
        # Handling form submission for adding, updating, and deleting players
        if 'add' in request.form:
            name = request.form['name']
            team_id = request.form['team_id']
            position = request.form['position']
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO players (Player_Name, TeamID, Position) VALUES (%s, %s, %s)", (name, team_id, position))
            conn.commit()
            cursor.close()
        elif 'delete' in request.form:
            player_id = request.form['player_id']
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM players WHERE PlayerID = %s", (player_id,))
            conn.commit()
            cursor.close()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT PlayerID, Player_Name, TeamID, Position FROM players")
    players = cursor.fetchall()
    cursor.close()
    return render_template('players.html', players=players)



# @app.route('/teams', methods=['GET', 'POST'])
# def manage_teams():
#     conn = create_connection()
#     if request.method == 'POST':
#         # Handling form submission for adding, updating, and deleting teams
#         if 'add' in request.form:
#             team_name = request.form['team_name']
#             state = request.form['state']
#             city = request.form['city']
#             arena = request.form['arena']
#             cursor = conn.cursor()
#             cursor.execute(
#                 "INSERT INTO teams (Team_Name, State, City, Arena) VALUES (%s, %s, %s, %s)", (team_name, state, city, arena))
#             conn.commit()
#             cursor.close()
#         elif 'delete' in request.form:
#             team_id = request.form['team_id']
#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM teams WHERE TeamID = %s", (team_id,))
#             conn.commit()
#             cursor.close()
#     cursor = conn.cursor()
#     cursor.execute("SELECT TeamID, Team_Name, State, City, Arena FROM teams")
#     teams = cursor.fetchall()
#     cursor.close()
#     return render_template('teams.html', teams=teams)


@app.route('/teams', methods=['GET', 'POST'])
def manage_teams():
    conn = create_connection()
    if request.method == 'POST':
        team_name = request.form.get('team_name')
        state = request.form.get('state')
        city = request.form.get('city')
        arena = request.form.get('arena')
        action = request.form.get('action')
        team_id = request.form.get('team_id')

        with conn.cursor() as cursor:
            if action == 'Add':
                cursor.execute(
                    "INSERT INTO teams (Team_Name, State, City, Arena) VALUES (%s, %s, %s, %s)",
                    (team_name, state, city, arena)
                )
            elif action == 'Update':
                cursor.execute(
                    "UPDATE teams SET Team_Name = %s, State = %s, City = %s, Arena = %s WHERE TeamID = %s",
                    (team_name, state, city, arena, team_id)
                )
            elif action == 'Delete':
                cursor.execute(
                    "DELETE FROM teams WHERE TeamID = %s", (team_id,)
                )
            conn.commit()

        return redirect(url_for('manage_teams'))

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(
            "SELECT TeamID, Team_Name, State, City, Arena FROM teams")
        teams = cursor.fetchall()

    return render_template('teams.html', teams=teams)


@app.route('/seasons', methods=['GET', 'POST'])
def manage_seasons():
    conn = create_connection()
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'Add':
            start_date = request.form.get('start_date')
            end_date = request.form.get('end_date')
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO seasons (Start_Date, End_Date) VALUES (%s, %s)",
                    (start_date, end_date)
                )

        elif action == 'Update':
            season_id = request.form.get('season_id')
            start_date = request.form.get('update_start_date')
            end_date = request.form.get('update_end_date')
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE seasons SET Start_Date = %s, End_Date = %s WHERE SeasonID = %s",
                    (start_date, end_date, season_id)
                )

        elif action == 'Delete':
            season_id = request.form.get('season_id')
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM seasons WHERE SeasonID = %s", (season_id,))

        conn.commit()
        return redirect(url_for('manage_seasons'))

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT SeasonID, Start_Date, End_Date FROM seasons")
        seasons = cursor.fetchall()

    return render_template('seasons.html', seasons=seasons)




@app.route('/games', methods=['GET', 'POST'])
def manage_games():
    conn = create_connection()
    if request.method == 'POST':
        if 'add' in request.form:
            game_date = request.form['game_date']
            team1_id = request.form['team1_id']
            team2_id = request.form['team2_id']
            team1_score = request.form['team1_score']
            team2_score = request.form['team2_score']
            home_team_id = request.form['home_team_id']
            season_id = request.form['season_id']
            cursor = conn.cursor()
            cursor.execute("INSERT INTO games (GameDate, Team1ID, Team2ID, Team1Score, Team2Score, HomeTeamID, SeasonID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (game_date, team1_id, team2_id, team1_score, team2_score, home_team_id, season_id))
            conn.commit()
            cursor.close()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT GameID, GameDate, Team1ID, Team2ID, Team1Score, Team2Score, HomeTeamID, SeasonID FROM games")
    games = cursor.fetchall()
    cursor.close()
    return render_template('games.html', games=games)


@app.route('/delete_player/<int:player_id>', methods=['POST'])
def delete_player(player_id):
    conn = create_connection()
    if not conn:
        flash('Could not establish a database connection.', 'error')
        return redirect(url_for('manage_players'))

    try:
        with conn.cursor() as cursor:
            # Check for dependent records in 'plays_for' table
            cursor.execute(
                "SELECT * FROM plays_for WHERE PlayerID = %s", (player_id,))
            dependent_records = cursor.fetchone()
            if dependent_records:
                flash(
                    'Cannot delete player with existing team associations. Remove dependencies first.', 'error')
            else:
                cursor.execute(
                    "DELETE FROM players WHERE PlayerID = %s", (player_id,))
                conn.commit()
                flash('Player deleted successfully.', 'success')
    except Error as e:
        conn.rollback()
        flash(f"Failed to delete player: {e}", 'error')
    finally:
        conn.close()

    return redirect(url_for('manage_players'))


@app.route('/coach', methods=['GET', 'POST'])
def manage_coach():
    conn = create_connection()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Add':
            coach_name = request.form.get('coach_name')
            years_exp = request.form.get('years_exp')
            championships_won = request.form.get('championships_won')
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO coach (Coach_Name, YearsExp, ChampionshipsWon) VALUES (%s, %s, %s)",
                    (coach_name, years_exp, championships_won)
                )
                conn.commit()
        elif action == 'Update':
            coach_id = request.form.get('coach_id')
            coach_name = request.form.get('update_coach_name')
            years_exp = request.form.get('update_years_exp')
            championships_won = request.form.get('update_championships_won')
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE coach SET Coach_Name = %s, YearsExp = %s, ChampionshipsWon = %s WHERE CoachID = %s",
                    (coach_name, years_exp, championships_won, coach_id)
                )
                conn.commit()
        elif action == 'Delete':
            coach_id = request.form.get('coach_id')
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM coach WHERE CoachID = %s", (coach_id,))
                conn.commit()

        return redirect(url_for('manage_coach'))

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(
            "SELECT CoachID, Coach_Name, YearsExp, ChampionshipsWon FROM coach")
        coach = cursor.fetchall()

    return render_template('coach.html', coach=coach)


@app.route('/records', methods=['GET', 'POST'])
def manage_records():
    conn = create_connection()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Add':
            player_id = request.form.get('player_id')
            game_id = request.form.get('game_id')
            points = request.form.get('points')
            rebounds = request.form.get('rebounds')
            assists = request.form.get('assists')
            blocks = request.form.get('blocks')
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO records (PlayerID, GameID, Points, Rebounds, Assists, Blocks) VALUES (%s, %s, %s, %s, %s, %s)",
                    (player_id, game_id, points, rebounds, assists, blocks)
                )
                conn.commit()
        elif action == 'Update':
            record_id = request.form.get('record_id')
            points = request.form.get('update_points')
            rebounds = request.form.get('update_rebounds')
            assists = request.form.get('update_assists')
            blocks = request.form.get('update_blocks')
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE records SET Points = %s, Rebounds = %s, Assists = %s, Blocks = %s WHERE RecordID = %s",
                    (points, rebounds, assists, blocks, record_id)
                )
                conn.commit()
        elif action == 'Delete':
            record_id = request.form.get('record_id')
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM records WHERE RecordID = %s", (record_id,))
                conn.commit()

        return redirect(url_for('manage_records'))

    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(
            "SELECT RecordID, PlayerID, GameID, Points, Rebounds, Assists, Blocks FROM records")
        records = cursor.fetchall()

    return render_template('records.html', records=records)

"""Junction Tables"""
# @app.route('/plays_for', methods=['GET', 'POST'])
# def manage_plays_for():
#     conn = create_connection()
#     if not conn:
#         return render_template('error.html')  # Handle the error appropriately

#     if request.method == 'POST':
#         player_id = request.form.get('player_id')
#         team_id = request.form.get('team_id')
#         start_date = request.form.get('start_date') or None
#         end_date = request.form.get('end_date') or None
#         action = request.form.get('action')

#         try:
#             with conn.cursor() as cursor:
#                 if action == 'Add':
#                     cursor.execute(
#                         "INSERT INTO plays_for (PlayerID, TeamID, Start_Date, End_Date) VALUES (%s, %s, %s, %s)",
#                         (player_id, team_id, start_date, end_date)
#                     )
#                 elif action == 'Update':
#                     cursor.execute(
#                         "UPDATE plays_for SET Start_Date = %s, End_Date = %s WHERE PlayerID = %s AND TeamID = %s",
#                         (start_date, end_date, player_id, team_id)
#                     )
#                 elif action == 'Delete':
#                     cursor.execute(
#                         "DELETE FROM plays_for WHERE PlayerID = %s AND TeamID = %s",
#                         (player_id, team_id)
#                     )
#                 conn.commit()
#         except Error as e:
#             flash(f"Database error: {e}", "error")
#             conn.rollback()

#         return redirect(url_for('manage_plays_for'))

#     with conn.cursor(dictionary=True) as cursor:
#         cursor.execute("SELECT * FROM plays_for")
#         plays_for = cursor.fetchall()

#     return render_template('plays_for.html', plays_for=plays_for)



if __name__ == '__main__':
    app.run(debug=True)


""" CRUD (Create, Read, Update, Delete) functionalities """

""" Player """
def add_player():
    """Adds a new player to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    name = input("Enter player's name: ")
    team_id = input("Enter player's team ID: ")
    position = input("Enter player's position: ")
    query = "INSERT INTO players (Player_Name, TeamID, Position) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, team_id, position))
    conn.commit()
    print("Player added successfully.")
    cursor.close()
    conn.close()


def read_players():
    """Displays all players from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT PlayerID, Player_Name, TeamID, Position FROM players"
    cursor.execute(query)
    for (player_id, name, team_id, position) in cursor:
        print(
            f"ID: {player_id}, Name: {name}, Team ID: {team_id}, Position: {position}")
    cursor.close()
    conn.close()


def update_player():
    """Updates a player's details in the database."""
    conn = create_connection()
    cursor = conn.cursor()
    player_id = input("Enter player's ID to update: ")
    new_name = input("Enter new name: ")
    new_team_id = input("Enter new team ID: ")
    new_position = input("Enter new position: ")
    query = "UPDATE players SET Player_Name = %s, TeamID = %s, Position = %s WHERE PlayerID = %s"
    cursor.execute(query, (new_name, new_team_id, new_position, player_id))
    conn.commit()
    print("Player updated successfully.")
    cursor.close()
    conn.close()


def delete_player():
    """Deletes a player from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    player_id = input("Enter player's ID to delete: ")
    query = "DELETE FROM players WHERE PlayerID = %s"
    cursor.execute(query, (player_id,))
    conn.commit()
    print("Player deleted successfully.")
    cursor.close()
    conn.close()


# # Example usage
# create_player(('Michael', 'SG', 198, 'Duke University', 1))
# read_players()
# update_player(6, 'John Updated Doe')
# delete_player(6)
# read_players()

""" Team """
# Function to add a new team


def add_team():
    conn = create_connection()
    cursor = conn.cursor()
    team_name = input("Enter team's name: ")
    state = input("Enter team's state: ")
    city = input("Enter team's city: ")
    arena = input("Enter team's arena: ")
    query = "INSERT INTO teams (Team_Name, State, City, Arena) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (team_name, state, city, arena))
    conn.commit()
    print("Team added successfully.")
    cursor.close()
    conn.close()

# Function to list all teams
def list_teams():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT TeamID, Team_Name, State, City, Arena FROM teams"
    cursor.execute(query)
    for team in cursor.fetchall():
        print(team)
    cursor.close()
    conn.close()


""" Season """
# Function to add a new season
def add_season():
    conn = create_connection()
    cursor = conn.cursor()
    start_date = input("Enter the season's start date (YYYY-MM-DD): ")
    end_date = input("Enter the season's end date (YYYY-MM-DD): ")
    query = "INSERT INTO seasons (Start_Date, End_Date) VALUES (%s, %s)"
    cursor.execute(query, (start_date, end_date))
    conn.commit()
    print("Season added successfully.")
    cursor.close()
    conn.close()

# Function to list all seasons
def list_seasons():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT SeasonID, Start_Date, End_Date FROM seasons"
    cursor.execute(query)
    for season in cursor.fetchall():
        print(season)
    cursor.close()
    conn.close()


""" Game """
# Function to add a new game
def add_game():
    conn = create_connection()
    cursor = conn.cursor()
    game_date = input("Enter the game date (YYYY-MM-DD): ")
    team1_id = input("Enter the first team's ID: ")
    team2_id = input("Enter the second team's ID: ")
    team1_score = input("Enter the first team's score: ")
    team2_score = input("Enter the second team's score: ")
    home_team_id = input("Enter the home team's ID: ")
    season_id = input("Enter the season's ID: ")
    query = """
    INSERT INTO games (GameDate, SeasonID, Team1ID, Team2ID, Team1Score, Team2Score, HomeTeamID) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (game_date, season_id, team1_id,
                   team2_id, team1_score, team2_score, home_team_id))
    conn.commit()
    print("Game added successfully.")
    cursor.close()
    conn.close()

# Function to list all games
def list_games():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT GameID, GameDate, SeasonID, Team1ID, Team2ID, Team1Score, Team2Score, HomeTeamID FROM games"
    cursor.execute(query)
    for game in cursor.fetchall():
        print(game)
    cursor.close()
    conn.close()


"""Test cases"""

def execute_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()

# Function for each test case
def list_all_teams_and_arenas():
    print("1. List all teams and their arenas:")
    execute_query(
        """
        SELECT Team_Name, Arena 
        FROM teams;
        """)


def find_coaches_with_more_than_5_years_experience():
    print("\n2. Find coaches with more than 5 years of experience:")
    execute_query("SELECT Coach_Name, YearsExp FROM coach WHERE YearsExp > 5;")


def display_players_team_and_position():
    print("\n3. Display players, their team, and position:")
    execute_query("""
    SELECT p.Player_Name, t.Team_Name, p.Position 
    FROM players p JOIN teams t ON p.TeamID = t.TeamID;
    """)


def seasons_with_game_counts():
    print("\n4. Seasons with their respective games count:")
    execute_query("""
    SELECT s.Start_Date, s.End_Date, COUNT(g.GameID) AS Games_Count 
    FROM seasons s LEFT JOIN games g ON s.SeasonID = g.SeasonID 
    GROUP BY s.SeasonID;
    """)


def top_scoring_player_in_each_game():
    print("\n5. Top scoring player in each game:")
    execute_query("""
    SELECT r.GameID, r.PlayerID, r.Points AS Highest_Points
    FROM records r
    INNER JOIN (
        SELECT GameID, MAX(Points) AS MaxPoints
        FROM records
        GROUP BY GameID
    ) AS max_scores ON r.GameID = max_scores.GameID AND r.Points = max_scores.MaxPoints;
    """)


def list_all_time_stars():
    print("\n6. List all players who have been an all-time star in any season:")
    execute_query("""
    SELECT DISTINCT p.Player_Name 
    FROM players p 
    JOIN allTimeStars a ON p.PlayerID = a.PlayerID;
    """)


def coaches_tenure_at_each_team():
    print("\n7. Coaches with their tenure period at each team:")
    execute_query("""
    SELECT c.Coach_Name, t.Team_Name, co.Start_Date, co.End_Date 
    FROM coaches co 
    JOIN coach c ON co.CoachID = c.CoachID 
    JOIN teams t ON co.TeamID = t.TeamID;
    """)


def average_points_per_game_for_each_player():
    print("\n8. Average points per game for each player:")
    execute_query("""
    SELECT PlayerID, AVG(Points) AS Avg_Points 
    FROM records 
    GROUP BY PlayerID;
    """)


def games_where_home_team_won():
    print("\n9. Games where the home team won:")
    execute_query("""
    SELECT GameID, HomeTeamID 
    FROM games 
    WHERE (HomeTeamID = Team1ID AND Team1Score > Team2Score) 
    OR (HomeTeamID = Team2ID AND Team2Score > Team1Score);
    """)


def players_who_played_for_multiple_teams():
    print("\n10. Players who have played for multiple teams:")
    execute_query("""
    SELECT PlayerID, COUNT(DISTINCT TeamID) AS Teams_Played 
    FROM plays_for 
    GROUP BY PlayerID 
    HAVING Teams_Played > 1;
    """)


def all_time_stars_for_latest_season():
    print("\n11. All-Time Stars for the latest season:")
    execute_query("""
    SELECT a.StarID, p.Player_Name, c.Coach_Name, s.Start_Date, s.End_Date 
    FROM allTimeStars a 
    LEFT JOIN players p ON a.PlayerID = p.PlayerID 
    LEFT JOIN coach c ON a.CoachID = c.CoachID 
    JOIN seasons s ON a.SeasonID = s.SeasonID 
    ORDER BY s.Start_Date DESC LIMIT 1;
    """)


def top_5_highest_scoring_games():
    print("\n12. Top 5 highest scoring games:")
    execute_query("""
    SELECT GameID, (Team1Score + Team2Score) AS TotalScore 
    FROM games 
    ORDER BY TotalScore DESC LIMIT 5;
    """)


def seasonal_ranking_of_teams_based_on_wins():
    print("\n13. Seasonal ranking of teams based on wins:")
    execute_query("""
    SELECT SeasonID, Team, COUNT(*) AS Wins
    FROM (
        SELECT SeasonID, Team1ID AS Team 
        FROM games 
        WHERE Team1Score > Team2Score
        UNION ALL
        SELECT SeasonID, Team2ID 
        FROM games 
        WHERE Team2Score > Team1Score
    ) AS WinsPerTeam
    GROUP BY SeasonID, Team;
    """)


def player_performance_improvement_over_seasons():
    print("\n14. Player performances improvement over seasons:")
    execute_query("""
    WITH SeasonScores AS (
      SELECT r.PlayerID, s.SeasonID, AVG(r.Points) AS AvgPoints 
      FROM records r JOIN games g ON r.GameID = g.GameID JOIN seasons s ON g.SeasonID = s.SeasonID 
      GROUP BY r.PlayerID, s.SeasonID
    )
    SELECT PlayerID, SeasonID, AvgPoints, LAG(AvgPoints) OVER (PARTITION BY PlayerID ORDER BY SeasonID) AS PrevSeasonAvgPoints 
    FROM SeasonScores;
    """)


def top_rebound_players_by_season():
    print("\n15. Top rebound players by season:")
    execute_query("""
    SELECT s.SeasonID, r.PlayerID, SUM(r.Rebounds) AS TotalRebounds, 
    DENSE_RANK() OVER (PARTITION BY s.SeasonID ORDER BY SUM(r.Rebounds) DESC) AS top_rebounder 
    FROM records r 
    JOIN games g ON r.GameID = g.GameID 
    JOIN seasons s ON g.SeasonID = s.SeasonID 
    GROUP BY s.SeasonID, r.PlayerID;
    """)


# if __name__ == "__main__":
#     list_all_teams_and_arenas()
#     find_coaches_with_more_than_5_years_experience()
#     display_players_team_and_position()
#     seasons_with_game_counts()
#     top_scoring_player_in_each_game()
#     list_all_time_stars()
#     coaches_tenure_at_each_team()
#     average_points_per_game_for_each_player()
#     games_where_home_team_won()
#     players_who_played_for_multiple_teams()
#     all_time_stars_for_latest_season()
#     top_5_highest_scoring_games()
#     seasonal_ranking_of_teams_based_on_wins()
#     player_performance_improvement_over_seasons()
#     top_rebound_players_by_season()

""" user-interface """


# def manage_players():
#     while True:
#         print("\nPlayer Management")
#         print("1. Add Player")
#         print("2. List Players")
#         print("3. Update Player")
#         print("4. Delete Player")
#         print("5. Go Back")
#         choice = input("Select an option: ")

#         if choice == "1":
#             add_player()
#         elif choice == "2":
#             read_players()
#         elif choice == "3":
#             update_player()
#         elif choice == "4":
#             delete_player()
#         elif choice == "5":
#             return
#         else:
#             print("Invalid choice. Please try again.")


# def manage_teams():
#     while True:
#         print("\nTeam Management")
#         print("1. Add Team")
#         print("2. List Teams")
#         print("3. Update Team")
#         print("4. Delete Team")
#         print("5. Go Back")
#         choice = input("Select an option: ")

#         if choice == "1":
#             add_team()
#         elif choice == "2":
#             list_teams()
#         # Implement update_team() and delete_team() functions similar to players
#         elif choice == "5":
#             return
#         else:
#             print("Invalid choice. Please try again.")


# def manage_seasons():
#     while True:
#         print("\nSeason Management")
#         print("1. Add Season")
#         print("2. List Seasons")
#         print("3. Update Season")
#         print("4. Delete Season")
#         print("5. Go Back")
#         choice = input("Select an option: ")

#         if choice == "1":
#             add_season()
#         elif choice == "2":
#             list_seasons()
#         # Implement update_season() and delete_season() functions similar to players
#         elif choice == "5":
#             return
#         else:
#             print("Invalid choice. Please try again.")


# def manage_games():
#     while True:
#         print("\nGame Management")
#         print("1. Add Game")
#         print("2. List Games")
#         print("3. Update Game")
#         print("4. Delete Game")
#         print("5. Go Back")
#         choice = input("Select an option: ")

#         if choice == "1":
#             add_game()
#         elif choice == "2":
#             list_games()
#         # Implement update_game() and delete_game() functions similar to players
#         elif choice == "5":
#             return
#         else:
#             print("Invalid choice. Please try again.")


# def main():
#     while True:
#         print("\nNBA Database Management")
#         print("1. Manage Players")
#         print("2. Manage Teams")
#         print("3. Manage Seasons")
#         print("4. Manage Games")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             manage_players()
#         elif choice == "2":
#             manage_teams()
#         elif choice == "3":
#             manage_seasons()
#         elif choice == "4":
#             manage_games()
#         elif choice == "5":
#             print("Exiting the NBA Database Management System.")
#             break
#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()
