CREATE DATABASE nba_DB_2;
USE nba_DB_2;

-- Create the foundational tables first
CREATE TABLE teams(
    TeamID int AUTO_INCREMENT PRIMARY KEY,
    Team_Name varchar(255),
    State varchar(255),
    City varchar(255),
    Arena varchar(255)
);


CREATE TABLE coach(
    CoachID INT AUTO_INCREMENT PRIMARY KEY,
    Coach_Name varchar(255),
    YearsExp int,
    ChampionshipsWon int
    -- Removed Start_Date and End_Date, will track tenure in coaches table
);

-- Table that has a foreign key dependency on teams
CREATE TABLE players(
    PlayerID int AUTO_INCREMENT PRIMARY KEY,
    Player_Name varchar(255),
    Position varchar(255),
    Height int,
    College varchar(255),
    TeamID int,
    FOREIGN KEY(TeamID) REFERENCES teams(TeamID) on update cascade on delete cascade
);

CREATE TABLE seasons(
    SeasonID int AUTO_INCREMENT PRIMARY KEY,
    Start_Date date,
    End_Date date
);


CREATE TABLE games(
    GameID int AUTO_INCREMENT PRIMARY KEY,
    GameDate date,
    SeasonID int,
    Team1ID int,
    Team2ID int,
    Team1Score int, -- Score for the first team
    Team2Score int, -- Score for the second team
    HomeTeamID int, -- Indicates which team was the home team
    FOREIGN KEY(Team1ID) REFERENCES teams(TeamID) on update cascade on delete cascade,
    FOREIGN KEY(Team2ID) REFERENCES teams(TeamID) on update cascade on delete cascade,
    FOREIGN KEY(SeasonID) REFERENCES seasons(SeasonID) on update cascade on delete cascade,
    FOREIGN KEY(HomeTeamID) REFERENCES teams(TeamID) on update cascade on delete cascade
);


CREATE TABLE allTimeStars (
    StarID INT AUTO_INCREMENT PRIMARY KEY,
    PlayerID INT,
    CoachID INT,
    SeasonID INT,
    FOREIGN KEY (PlayerID) REFERENCES players (PlayerID) on update cascade on delete cascade,
    FOREIGN KEY (CoachID) REFERENCES coach (CoachID) on update cascade on delete cascade,
    FOREIGN KEY (SeasonID) REFERENCES seasons (SeasonID) on update cascade on delete cascade,
    UNIQUE (PlayerID , SeasonID),
    UNIQUE (CoachID , SeasonID)
);


CREATE TABLE records (
    RecordID int AUTO_INCREMENT PRIMARY KEY,
    PlayerID int,
    GameID int,
    Points int,
    Rebounds int,
    Assists int,
    Blocks int,
    FOREIGN KEY (PlayerID) REFERENCES players(PlayerID) on update cascade on delete cascade,
    FOREIGN KEY (GameID) REFERENCES games(GameID) on update cascade on delete cascade
);

-- ----------------------------------------------juction tables---------------------------

-- junction table
CREATE TABLE coaches (
    TeamID int,
    CoachID int,
    Start_Date date,
    End_Date date,
    PRIMARY KEY (TeamID, CoachID),
    FOREIGN KEY (TeamID) REFERENCES teams(TeamID) on update cascade on delete cascade,
    FOREIGN KEY (CoachID) REFERENCES coach(CoachID) on update cascade on delete cascade
);


-- junction table
CREATE TABLE plays_for (
    PlayerID int,
    TeamID int,
    Start_Date date,
    End_Date date,
    PRIMARY KEY (PlayerID, TeamID),
    FOREIGN KEY (PlayerID) REFERENCES players(PlayerID) on update cascade on delete cascade,
    FOREIGN KEY (TeamID) REFERENCES teams(TeamID) on update cascade on delete cascade
);


-- -----------------------------------------sample data---------------------------------------

INSERT INTO teams (Team_Name, State, City, Arena) VALUES
('Los Angeles Lakers', 'California', 'Los Angeles', 'Staples Center'),
('Golden State Warriors', 'California', 'San Francisco', 'Chase Center'),
('Chicago Bulls', 'Illinois', 'Chicago', 'United Center'),
('Boston Celtics', 'Massachusetts', 'Boston', 'TD Garden'),
('Miami Heat', 'Florida', 'Miami', 'AmericanAirlines Arena');

INSERT INTO coach (Coach_Name, YearsExp, ChampionshipsWon) VALUES
('Frank Vogel', 8, 1),
('Steve Kerr', 7, 3),
('Billy Donovan', 5, 0),
('Brad Stevens', 6, 0),
('Erik Spoelstra', 12, 2);

INSERT INTO players (Player_Name, Position, Height, College, TeamID) VALUES
('LeBron James', 'SF', 206, 'St. Vincent-St. Mary HS', 1),
('Stephen Curry', 'PG', 191, 'Davidson', 2),
('Zach LaVine', 'SG', 196, 'UCLA', 3),
('Jayson Tatum', 'SF', 203, 'Duke', 4),
('Jimmy Butler', 'SF', 201, 'Marquette', 5);

INSERT INTO seasons (Start_Date, End_Date) VALUES
('2019-10-22', '2020-10-11'),
('2020-12-22', '2021-07-20'),
('2021-10-19', '2022-06-30'),
('2022-10-18', '2023-06-15'),
('2023-10-17', '2024-06-10');

INSERT INTO games (GameDate, SeasonID, Team1ID, Team2ID, Team1Score, Team2Score, HomeTeamID) VALUES
('2020-12-25', 2, 1, 2, 138, 115, 1),
('2021-01-30', 2, 3, 4, 123, 104, 3),
('2021-02-14', 2, 5, 1, 98, 110, 5),
('2022-03-11', 3, 2, 3, 113, 107, 2),
('2022-04-07', 3, 4, 5, 105, 99, 4);

INSERT INTO allTimeStars (PlayerID, CoachID, SeasonID) VALUES
(1, NULL, 1),
(NULL, 2, 2),
(3, NULL, 3),
(NULL, 4, 4),
(5, NULL, 5);

INSERT INTO records (PlayerID, GameID, Points, Rebounds, Assists, Blocks) VALUES
(1, 1, 22, 9, 8, 2),
(2, 1, 30, 5, 12, 0),
(3, 2, 25, 4, 6, 1),
(4, 2, 28, 7, 4, 1),
(5, 3, 32, 6, 5, 2);

INSERT INTO coaches (TeamID, CoachID, Start_Date, End_Date) VALUES
(1, 1, '2019-08-01', NULL),
(2, 2, '2014-05-14', NULL),
(3, 3, '2020-09-22', NULL),
(4, 4, '2013-07-03', NULL),
(5, 5, '2008-04-28', NULL);

INSERT INTO plays_for (PlayerID, TeamID, Start_Date, End_Date) VALUES
(1, 1, '2018-07-01', NULL),
(2, 2, '2009-07-07', NULL),
(3, 3, '2014-08-05', NULL),
(4, 4, '2017-06-22', NULL),
(5, 5, '2011-12-08', NULL);


-- -----------------------------------------test cases---------------------------------------

-- 1. List all teams and their arenas
SELECT Team_Name, Arena 
FROM teams;

-- 2. Find coaches with more than 5 years of experience
SELECT Coach_Name, YearsExp 
FROM coach 
WHERE YearsExp > 5;

-- 3. Display players, their team, and position
SELECT p.Player_Name, t.Team_Name, p.Position 
FROM players p JOIN teams t ON p.TeamID = t.TeamID;

-- 4. Seasons with their respective games count
SELECT s.Start_Date, s.End_Date, COUNT(g.GameID) AS Games_Count 
FROM seasons s LEFT JOIN games g ON s.SeasonID = g.SeasonID 
GROUP BY s.SeasonID;
-- A LEFT JOIN includes all rows from the left table (seasons in this case), 
-- and matches rows from the right table (games). 
-- If there is no match, the result set will still include the row from the left table
-- but with NULL values for columns from the right table.

-- 5. Top scoring player in each game
-- SELECT GameID, PlayerID, MAX(Points) AS Highest_Points 
-- FROM records 
-- GROUP BY GameID;
SELECT r.GameID, r.PlayerID, r.Points AS Highest_Points
FROM records r
INNER JOIN (
    SELECT GameID, MAX(Points) AS MaxPoints
    FROM records
    GROUP BY GameID
) AS max_scores ON r.GameID = max_scores.GameID AND r.Points = max_scores.MaxPoints;


-- 6. List all players who have been an all-time star in any season
SELECT DISTINCT p.Player_Name 
FROM players p 
	JOIN allTimeStars a ON p.PlayerID = a.PlayerID;

-- 7. Coaches with their tenure period at each team
SELECT c.Coach_Name, t.Team_Name, co.Start_Date, co.End_Date 
FROM coaches co 
	JOIN coach c ON co.CoachID = c.CoachID 
	JOIN teams t ON co.TeamID = t.TeamID;

-- 8. Average points per game for each player
SELECT PlayerID, AVG(Points) AS Avg_Points 
FROM records 
GROUP BY PlayerID;

-- 9. Games where the home team won
SELECT GameID, HomeTeamID 
FROM games 
WHERE (HomeTeamID = Team1ID AND Team1Score > Team2Score) 
	OR (HomeTeamID = Team2ID AND Team2Score > Team1Score);

-- 10. Players who have played for multiple teams
SELECT PlayerID, COUNT(DISTINCT TeamID) AS Teams_Played 
FROM plays_for 
GROUP BY PlayerID 
HAVING Teams_Played > 1;

-- 11. All-Time Stars for the latest season
SELECT a.StarID, p.Player_Name, c.Coach_Name, s.Start_Date, s.End_Date 
FROM allTimeStars a 
	LEFT JOIN players p ON a.PlayerID = p.PlayerID 
    LEFT JOIN coach c ON a.CoachID = c.CoachID 
    JOIN seasons s ON a.SeasonID = s.SeasonID 
ORDER BY s.Start_Date DESC LIMIT 1;

-- 12. Top 5 highest scoring games
SELECT GameID, (Team1Score + Team2Score) AS TotalScore 
FROM games 
ORDER BY TotalScore DESC LIMIT 5;

-- 13. Seasonal ranking of teams based on wins
SELECT SeasonID, Team, COUNT(*) AS Wins
FROM (
    (SELECT SeasonID, Team1ID AS Team 
    FROM games 
    WHERE Team1Score > Team2Score)
    UNION ALL
    (SELECT SeasonID, Team2ID 
    FROM games 
    WHERE Team2Score > Team1Score)
) AS WinsPerTeam
GROUP BY SeasonID, Team;




-- 14. Player performances improvement over seasons
WITH SeasonScores AS (
  SELECT r.PlayerID, s.SeasonID, AVG(r.Points) AS AvgPoints 
  FROM records r JOIN games g ON r.GameID = g.GameID JOIN seasons s ON g.SeasonID = s.SeasonID 
  GROUP BY r.PlayerID, s.SeasonID
)
SELECT PlayerID, SeasonID, AvgPoints, LAG(AvgPoints) OVER (PARTITION BY PlayerID ORDER BY SeasonID) AS PrevSeasonAvgPoints 
FROM SeasonScores;

-- 15. Top rebound players by season
SELECT s.SeasonID, r.PlayerID, SUM(r.Rebounds) AS TotalRebounds, 
	DENSE_RANK() OVER (PARTITION BY s.SeasonID ORDER BY SUM(r.Rebounds) DESC) AS top_rebounder 
FROM records r 
	JOIN games g ON r.GameID = g.GameID 
    JOIN seasons s ON g.SeasonID = s.SeasonID 
GROUP BY s.SeasonID, r.PlayerID;
