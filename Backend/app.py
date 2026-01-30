from flask import Flask, Response, abort
from flask_cors import CORS
import random

import json
from datetime import date

app = Flask(__name__)
CORS(app)

# -----------------------------
# Load Bhagavad Gita database
# -----------------------------
with open("gita_db.json", "r", encoding="utf-8") as f:
    gita = json.load(f)

# -----------------------------
# Helper function for Unicode JSON response
# -----------------------------
def unicode_json(data, status=200):
    return Response(
        json.dumps(data, ensure_ascii=False, indent=2),
        status=status,
        mimetype="application/json"
    )

# -----------------------------
# Home route (sanity check)
# -----------------------------
@app.route("/")
def home():
    return unicode_json({
        "message": "Bhagavad Gita Shlok API is running",
        "total_shloks": len(gita)
    })

# -----------------------------
# Shlok of the Day
# -----------------------------
@app.route("/api/shlok/random")
def shlok_of_the_day():
    index = random.randint(0, len(gita) - 1)
    return unicode_json(gita[index])

# -----------------------------
# Get shlok by chapter & verse
# -----------------------------
@app.route("/api/shlok/<int:chapter>/<int:verse>")
def get_shlok(chapter, verse):
    for shlok in gita:
        if shlok["chapter"] == chapter and shlok["verse"] == verse:
            return unicode_json(shlok)

    return unicode_json(
        {"error": "Shlok not found"},
        status=404
    )

# -----------------------------
# Run the application
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

