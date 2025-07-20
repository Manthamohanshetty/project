import mysql.connector

# ✅ Database connection
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Replace with your MySQL username
        password="Mohan@$436", # Replace with your MySQL password
        database="score_boards"
    )

# ✅ Menu
def score_card_menu():
    while True:
        print("""
🏏 Score Card Menu
    1. Add a batsman
    2. Add a bowler
    3. View Batsman's Card
    4. View Bowler's Card
    5. Update Batsman's Score
    6. Update Bowler's Stats
    7. Remove a player
    8. View Highest Score
    9. Exit
        """)
        try:
            choice = int(input("Enter your choice (1-9): "))
            match choice:
                case 1: add_batsman()
                case 2: add_bowler()
                case 3: view_batsmans_card()
                case 4: view_bowlers_card()
                case 5: update_batsmans_card()
                case 6: update_bowlers_card()
                case 7: remove_player()
                case 8: get_highest_score()
                case 9:
                    print("Exiting... 🏁")
                    break
                case _: print("Invalid choice. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

# ✅ Add batsman
def add_batsman():
    conn = connect()
    cursor = conn.cursor()
    player_name = input("Enter batsman's name: ")
    score = int(input("Enter team score: "))
    wickets = int(input("Enter total wickets: "))
    runs = int(input("Enter runs scored: "))
    balls = int(input("Enter balls faced: "))
    fours = int(input("Enter number of fours: "))
    sixes = int(input("Enter number of sixes: "))
    average = round(runs / balls, 2) * 100 if balls != 0 else 0.0

    cursor.execute("""
        INSERT INTO score_entry(score, wickets, player_name, runs, balls, fours, sixes, average)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (score, wickets, player_name, runs, balls, fours, sixes, average))
    conn.commit()
    print(f"✅ Batsman '{player_name}' added successfully.")
    conn.close()

# ✅ Add bowler
def add_bowler():
    conn = connect()
    cursor = conn.cursor()
    player_name = input("Enter batsman's name to link bowler stats: ")
    cursor.execute("SELECT id FROM score_entry WHERE player_name = %s", (player_name,))
    result = cursor.fetchone()

    if result:
        score_entry_id = result[0]
        bowler_name = input("Enter bowler's name: ")
        overs = int(input("Enter overs bowled: "))
        runs_conceded = int(input("Enter runs conceded: "))
        wickets_taken = int(input("Enter wickets taken: "))
        maidens = int(input("Enter maiden overs: "))
        economy = round(runs_conceded / overs, 2) if overs != 0 else 0.0

        cursor.execute("""
            INSERT INTO bowlers(score_entry_id, bowler_name, no_of_overs, no_of_runs, no_of_wickets, no_of_maidens, economy)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (score_entry_id, bowler_name, overs, runs_conceded, wickets_taken, maidens, economy))
        conn.commit()
        print(f"✅ Bowler '{bowler_name}' added successfully.")
    else:
        print("❌ Batsman not found. Add batsman first.")
    conn.close()

# ✅ View batsman's card
def view_batsmans_card():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM score_entry")
    rows = cursor.fetchall()
    print("\n🏏 Batsman's Scorecard:")
    for row in rows:
        print(row)
    conn.close()

# ✅ View bowler's card
def view_bowlers_card():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bowlers")
    rows = cursor.fetchall()
    print("\n🎯 Bowler's Scorecard:")
    for row in rows:
        print(row)
    conn.close()

# ✅ Update batsman's card
def update_batsmans_card():
    conn = connect()
    cursor = conn.cursor()
    player_name = input("Enter batsman's name to update: ")
    cursor.execute("SELECT id FROM score_entry WHERE player_name = %s", (player_name,))
    result = cursor.fetchone()

    if result:
        batsman_id = result[0]
        runs = int(input("Updated runs: "))
        balls = int(input("Updated balls faced: "))
        fours = int(input("Updated fours: "))
        sixes = int(input("Updated sixes: "))
        average = round(runs / balls, 2) if balls != 0 else 0.0

        cursor.execute("""
            UPDATE score_entry
            SET runs = %s, balls = %s, fours = %s, sixes = %s, average = %s
            WHERE id = %s
        """, (runs, balls, fours, sixes, average, batsman_id))
        conn.commit()
        print(f"✅ Batsman's score updated for '{player_name}'.")
    else:
        print("❌ Batsman not found.")
    conn.close()

# ✅ Update bowler's card
def update_bowlers_card():
    conn = connect()
    cursor = conn.cursor()
    bowler_name = input("Enter bowler's name to update: ")
    cursor.execute("SELECT id FROM bowlers WHERE bowler_name = %s", (bowler_name,))
    result = cursor.fetchone()

    if result:
        bowler_id = result[0]
        overs = int(input("Updated overs: "))
        runs = int(input("Updated runs conceded: "))
        wickets = int(input("Updated wickets taken: "))
        maidens = int(input("Updated maiden overs: "))
        economy = round(runs / overs, 2) if overs != 0 else 0.0

        cursor.execute("""
            UPDATE bowlers
            SET no_of_overs = %s, no_of_runs = %s, no_of_wickets = %s, no_of_maidens = %s, economy = %s
            WHERE id = %s
        """, (overs, runs, wickets, maidens, economy, bowler_id))
        conn.commit()
        print(f"✅ Bowler's stats updated for '{bowler_name}'.")
    else:
        print("❌ Bowler not found.")
    conn.close()

# ✅ Remove a player
def remove_player():
    conn = connect()
    cursor = conn.cursor()
    player_name = input("Enter player name to remove: ")
    cursor.execute("SELECT * FROM score_entry WHERE player_name = %s", (player_name,))
    result = cursor.fetchone()

    if result:
        confirm = input(f"Are you sure you want to delete '{player_name}'? (yes/no): ").lower()
        if confirm == 'yes':
            cursor.execute("DELETE FROM score_entry WHERE player_name = %s", (player_name,))
            conn.commit()
            print(f"✅ Player '{player_name}' removed.")
        else:
            print("❎ Deletion cancelled.")
    else:
        print("❌ Player not found.")
    conn.close()

# ✅ View highest score
def get_highest_score():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT player_name, runs FROM score_entry ORDER BY runs DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        print(f"\n🏆 Highest Score: {result[1]} runs by {result[0]}")
    else:
        print("No data found.")
    conn.close()

# ✅ Run the program
if __name__ == "__main__":
    score_card_menu()