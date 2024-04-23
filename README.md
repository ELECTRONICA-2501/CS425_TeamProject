NBA Management System
Overview

This NBA Management System is a comprehensive web application built using Flask, which allows users to manage various entities related to a basketball league. The system handles operations for entities such as players, teams, games, coaches, seasons, records, and junction tables for plays. This README details the system's setup, usage, and capabilities.
Features
1. Database Connection

    Establishes a connection to a MySQL database with given credentials and database specifics.
    Connection handling includes error management to ensure reliable database interactions.

2. CRUD Operations

    Create, Read, Update, and Delete (CRUD) operations for players, teams, games, coaches, and seasons.
    Specialized pages for managing player associations and game records.
    Supports complex interactions like adding and removing players from teams, updating game scores, and managing coach tenures.

3. Flask Routes

    Various endpoints to handle webpage requests, render templates, and execute backend logic based on POST and GET requests.
    Each route is associated with specific functionality, such as adding new data, updating existing data, and deleting.

4. User Interface

    Uses Flask templates to render HTML pages that provide a user-friendly interface to interact with the database.
    Flash messages to provide feedback for database operations like successful inserts or errors.

5. Security and Input Handling

    Uses placeholders and parameterized queries to prevent SQL injection.
    Handles null values appropriately to ensure database integrity.

Setup and Installation
Prerequisites

    Python 3
    Flask
    MySQL Connector for Python
    Access to a MySQL server with appropriate user permissions.

Installation Steps

    Ensure Python and pip are installed.
    Install Flask and MySQL connector using pip:

    pip install Flask mysql-connector-python

    Set up your MySQL database and user credentials.
    Configure the database connection settings in the create_connection function.

Running the Application

    Start the Flask application by executing:

    python app.py

Pages and Their Functionalities
/

    The main index page that provides navigation to various parts of the application.

/players, /teams, /games, /seasons, /coach, /records

    These endpoints allow for managing the respective entities through forms that support adding, updating, and deleting records.
    Render templates display current records and provide forms for submitting changes.

/delete_player/<int:player_id>

    Handles the deletion of players, ensuring that no dependent records prevent the operation.

Advanced Functionalities

    Implements complex SQL queries for analytics, such as calculating average points per game over seasons, identifying top performers, and more through the /advanced_queries endpoint.

Junction Tables and Special Queries

    Manages player-team associations and tracks historical data through junction tables like plays_for.
    Supports queries that require conditional logic and calculations across multiple tables.

Conclusion

This NBA Management System is a robust platform for managing a basketball league's operations with an emphasis on database interactions and user interface design. It demonstrates advanced CRUD operations, complex SQL query handling, and practical use of Flask in a web application environment.
