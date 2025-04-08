from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# --- Create and seed DB if it doesn't exist ---
def init_db():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Create Player table
        cursor.execute("""
            CREATE TABLE Player (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                image TEXT NOT NULL
            )
        """)

        # Create Fixture table
        cursor.execute("""
            CREATE TABLE Fixture (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                team1 TEXT NOT NULL,
                team2 TEXT NOT NULL,
                team1_logo TEXT NOT NULL,
                team2_logo TEXT NOT NULL,
                score TEXT,
                status TEXT NOT NULL,
                competition_name TEXT,
                competition_logo TEXT
            )
        """)

        # Create Event table
        cursor.execute("""
            CREATE TABLE Event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fixture_id INTEGER,
                player TEXT NOT NULL,
                minute INTEGER NOT NULL,
                team TEXT NOT NULL,
                FOREIGN KEY (fixture_id) REFERENCES Fixture(id)
            )
        """)

        # Seed players
        players = [
            ("Gian Piero Gasperini", "Coach", "gasperini.jpg"),
            ("Marco Carnesecchi", "Goalkeeper", "carnesecchi.png"),
            ("Rui Patricio", "Goalkeeper", "patricio.webp"),
            ("Francesco Rossi", "Goalkeeper", "rossi.webp"),
            ("Rafael Toloi", "Defender", "toloi.png"),
            ("Juan Cuadrado", "Defender", "cuadrado.png"),
            ("Davide Zappacosta", "Defender", "zappacosta.webp"),
            ("Berat Djimsiti", "Defender", "djimsiti.webp"),
            ("Sead Kolasinac", "Defender", "kolasinac.webp"),
            ("Raoul Bellanova", "Defender", "bellanova.webp"),
            ("Isak Hien", "Defender", "hien.webp"),
            ("Odilon Kossounou", "Defender", "kossounou.webp"),
            ("Matteo Ruggeri", "Defender", "ruggeri.webp"),
            ("Giorgio Scalvini", "Defender", "scalvini.webp"),
            ("Marten de Roon", "Midfielder", "de_roon.webp"),
            ("Mario Pasalic", "Midfielder", "pasalic.webp"),
            ("Marco Brescianini", "Midfielder", "brescianini.webp"),
            ("Ederson", "Midfielder", "ederson.webp"),
            ("Lazar Samardzic", "Midfielder", "samardzic.webp"),
            ("Ademola Lookman", "Forward", "lookman.webp"),
            ("Gianluca Scamacca", "Forward", "scamacca.webp"),
            ("Charles De Ketelaere", "Forward", "ketelaere.webp"),
            ("Mateo Retegui", "Forward", "retegui.webp")
        ]
        cursor.execute("""
    SELECT name, position, image, full_name, birthday, role, height, nationality, shirt_number, goals, assists, appearances 
    FROM Player
""")
        rows = cursor.fetchall()
        players_data = []
        for row in rows:
            players_data.append({
            "name": row[0],
            "position": row[1],
            "image": row[2],
            "full_name": row[3],
            "birthday": row[4],
            "role": row[5],
            "height": row[6],
            "nationality": row[7],
            "shirt_number": row[8],
            "goals": row[9],
            "assists": row[10],
            "appearances": row[11]
        })

        # Seed fixture
        cursor.execute("""
            INSERT INTO Fixture (date, team1, team2, team1_logo, team2_logo, score, status, competition_name, competition_logo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "Sun, Mar 10",
            "Atalanta",
            "Juventus",
            "atalanta.png",
            "juventus.png",
            "4 - 0",
            "finished",
            "Serie A",
            "serie_a_logo.png"
        ))
        fixture_id = cursor.lastrowid

        # Seed events
        events = [
            ("Lookman", 12, "Atalanta"),
            ("Retegui", 24, "Atalanta"),
            ("Lookman", 55, "Atalanta"),
            ("De Ketelaere", 73, "Atalanta")
        ]
        for player, minute, team in events:
            cursor.execute("INSERT INTO Event (fixture_id, player, minute, team) VALUES (?, ?, ?, ?)",
                           (fixture_id, player, minute, team))

        conn.commit()
        conn.close()
        print("✅ Database created and data seeded!")

# Initialize DB
init_db()

def position_to_emoji(position):
    emojis = {
        "Goalkeeper": "🧤",
        "Defender": "🛡️",
        "Midfielder": "🎯",
        "Forward": "⚡",
        "Coach": "👔"
    }
    return emojis.get(position, "❓")  # Default fallback emoji

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/team_stats")
def team_stats():
    return render_template("team_stats.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/player")
def players():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, position, image FROM Player")  # <-- ADD `id` here
    rows = cursor.fetchall()
    conn.close()

    players_data = [{
        "id": row[0],
        "name": row[1],
        "position": row[2],
        "image": row[3]
    } for row in rows]

    return render_template("players.html", players=players_data, emoji=position_to_emoji)

@app.route("/fixtures")
def fixtures():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Fixture")
    fixture_rows = cursor.fetchall()

    fixtures_data = []

    for fixture in fixture_rows:
        fixture_id = fixture[0]
        fixture_dict = {
            "date": fixture[1],
            "team1": fixture[2],
            "team2": fixture[3],
            "team1_logo": fixture[4],
            "team2_logo": fixture[5],
            "score": fixture[6],
            "status": fixture[7],
            "competition": {
                "name": fixture[8],
                "logo": fixture[9]
            },
            "events": []
        }

        cursor.execute("SELECT player, minute, team FROM Event WHERE fixture_id = ?", (fixture_id,))
        event_rows = cursor.fetchall()

        for event in event_rows:
            fixture_dict["events"].append({
                "player": event[0],
                "minute": event[1],
                "team": event[2]
            })

        fixtures_data.append(fixture_dict)

    conn.close()
    return render_template("fixtures.html", fixtures=fixtures_data)

@app.route("/player/<int:player_id>")
def player_detail(player_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Player WHERE id = ?", (player_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        player = {
            "id": row[0],
            "name": row[1],
            "position": row[2],
            "image": row[3],
            "full_name": row[4],
            "birthday": row[5],
            "role": row[6],
            "height": row[7],
            "nationality": row[8],
            "shirt_number": row[9],
            "goals": row[10],
            "assists": row[11],
            "appearances": row[12],
        }
        return render_template("player_detail.html", player=player)
    else:
        return "Player not found", 404

# --- Run the App ---
if __name__ == "__main__":
    app.run(debug=True)