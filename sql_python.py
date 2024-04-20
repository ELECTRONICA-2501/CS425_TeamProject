from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector



# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#         database="nba_DB_2",
#     ) as connection:
#         # Now the SELECT query is inside the with block
#         # Reading Records Using the SELECT Statement
#         select_player_query = "SELECT * FROM players LIMIT 5"
#         with connection.cursor() as cursor:
#             cursor.execute(select_player_query)
#             result = cursor.fetchall()
#             for row in result:
#                 print(row)
#             print('\n') 
            
#         # Find coaches with more than 5 years of experience
#         coach_more_5years = """SELECT Coach_Name, YearsExp 
#                                 FROM coach 
#                                 WHERE YearsExp > 5;"""
#         with connection.cursor() as cursor:
#             cursor.execute(coach_more_5years)
#             for coach in cursor.fetchall():
#                 print(coach)
# except Error as e:
#     print(e)


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user= input("Enter username: "),
        password=  getpass("Enter password: "),
        database="nba_DB_2"
    )
    return connection

# def create_connection():
#     """Create a database connection"""
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user=input("Enter username: "),
#             password=getpass("Enter password: "),
#             database="nba_DB_2",
#         )
#         return connection
#     except mysql.connector.Error as e:
#         print(f"Error connecting to MySQL Platform: {e}")
#         return None

""" CRUD (Create, Read, Update, Delete) functionalities """

""" Player """
# def create_player(player):
#     """Create a new player in the players table"""
#     connection = create_connection()
#     cursor = connection.cursor()
#     query = """
#     INSERT INTO players (Player_Name, Position, Height, College, TeamID) VALUES (%s, %s, %s, %s, %s);
#     """
#     cursor.execute(query, player)
#     connection.commit()
#     print("Player created successfully")
#     cursor.close()
#     connection.close()

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


# def read_players():
#     """Query all rows in the players table"""
#     connection = create_connection()
#     cursor = connection.cursor()
#     query = "SELECT * FROM players;"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     cursor.close()
#     connection.close()

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


# def update_player(player_id, player_name):
#     """Update a player's name based on the player's id"""
#     connection = create_connection()
#     cursor = connection.cursor()
#     query = """UPDATE players
#                SET Player_Name = %s
#                WHERE PlayerID = %s"""
#     cursor.execute(query, (player_name, player_id))
#     connection.commit()
#     print("Player updated successfully")
#     cursor.close()
#     connection.close()

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


# def delete_player(player_id):
#     """Delete a player by player id"""
#     connection = create_connection()
#     cursor = connection.cursor()
#     query = """
#     DELETE 
#     FROM players 
#     WHERE PlayerID = %s
#     """
#     cursor.execute(query, (player_id,))
#     connection.commit()
#     print("Player deleted successfully")
#     cursor.close()
#     connection.close()

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
def manage_players():
    while True:
        print("\nPlayer Management")
        print("1. Add Player")
        print("2. List Players")
        print("3. Update Player")
        print("4. Delete Player")
        print("5. Go Back")
        choice = input("Select an option: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            read_players()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")


def manage_teams():
    while True:
        print("\nTeam Management")
        print("1. Add Team")
        print("2. List Teams")
        print("3. Update Team")
        print("4. Delete Team")
        print("5. Go Back")
        choice = input("Select an option: ")

        if choice == "1":
            add_team()
        elif choice == "2":
            list_teams()
        # Implement update_team() and delete_team() functions similar to players
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")


def manage_seasons():
    while True:
        print("\nSeason Management")
        print("1. Add Season")
        print("2. List Seasons")
        print("3. Update Season")
        print("4. Delete Season")
        print("5. Go Back")
        choice = input("Select an option: ")

        if choice == "1":
            add_season()
        elif choice == "2":
            list_seasons()
        # Implement update_season() and delete_season() functions similar to players
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")


def manage_games():
    while True:
        print("\nGame Management")
        print("1. Add Game")
        print("2. List Games")
        print("3. Update Game")
        print("4. Delete Game")
        print("5. Go Back")
        choice = input("Select an option: ")

        if choice == "1":
            add_game()
        elif choice == "2":
            list_games()
        # Implement update_game() and delete_game() functions similar to players
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\nNBA Database Management")
        print("1. Manage Players")
        print("2. Manage Teams")
        print("3. Manage Seasons")
        print("4. Manage Games")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_players()
        elif choice == "2":
            manage_teams()
        elif choice == "3":
            manage_seasons()
        elif choice == "4":
            manage_games()
        elif choice == "5":
            print("Exiting the NBA Database Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
