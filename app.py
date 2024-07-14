from cs50 import SQL
from flask import Flask, render_template, request

app=Flask(__name__)

db = SQL("sqlite:///songs.db")

error = "Invalid choice!"

@app.route("/")
def index():

    """Home Page"""
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():

    """Search Page"""
    if request.method == "GET":
        return render_template("search.html")

    count = 0

    d = request.form.get("danceability")
    if d == None:
        danceability = db.execute("select track_name from songs")
        count += 1

    elif d == "low":
        danceability = db.execute("select track_name from songs where danceability <= ?", 0.25)

    elif d == "average":
        danceability = db.execute("select track_name from songs where danceability >= ? and danceability <= ?", 0.25, 0.5)
    elif d == "high":
        danceability = db.execute("select track_name from songs where danceability >= ? and danceability <= ?", 0.5, 0.75)

    elif d == "very_high":
        danceability = db.execute("select track_name from songs where danceability >= ?", 0.75)

    else:
        return render_template("search.html", error = error)


    e = request.form.get("energy")
    if e == None:
        energy = db.execute("select track_name from songs")
        count += 1

    elif e == "low":
        energy = db.execute("select track_name from songs where energy <= ?", 0.3)

    elif e == "average":
        energy = db.execute("select track_name from songs where energy >= ? and energy <= ?", 0.3, 0.55)

    elif e == "high":
        energy = db.execute("select track_name from songs where energy >= ? and energy <= ?", 0.55, 0.75)

    elif e == "very_high":
        energy = db.execute("select track_name from songs where energy >= ?", 0.75)

    else:
        return render_template("search.html", error = error)


    t = request.form.get("tempo")
    if t == None:
        tempo = db.execute("select track_name from songs")
        count += 1

    elif t == "low":
        tempo = db.execute("select track_name from songs where tempo <= ?", 80)

    elif t == "average":
        tempo = db.execute("select track_name from songs where tempo >= ? and tempo <= ?", 80, 120)

    elif t == "high":
        tempo = db.execute("select track_name from songs where tempo >= ? and tempo <= ?", 120, 160)

    elif t == "very_high":
        tempo = db.execute("select track_name from songs where tempo >= ?", 160)

    else:
        return render_template("search.html", error = error)

    # 1st input
    ar = request.form.get("artists")
    if not ar:
        artists = db.execute("select track_name from songs")
        count += 1

    if ar:
        artists = db.execute("select track_name from songs where artists like ?", "%" + ar + "%")


    l = request.form.get("loudness")
    if l == None:
        loudness = db.execute("select track_name from songs")
        count += 1

    elif l == "low":
        loudness = db.execute("select track_name from songs where loudness <= ?", -10)

    elif l == "average":
        loudness = db.execute("select track_name from songs where loudness >= ? and loudness <= ?", -10, -5)

    elif l == "high":
        loudness = db.execute("select track_name from songs where loudness >= ? and loudness <= ?", -5, 0)

    elif l == "very_high":
        loudness = db.execute("select track_name from songs where loudness >= ?", 0)

    else:
        return render_template("search.html", error = error)

    # 2nd input
    g = request.form.get("selected_option")

    genre_data = db.execute("select distinct(track_genre) as track_genre from songs")

    if not g:
        genre = db.execute("select track_name from songs")
        count += 1

    else:
        for item in range(len(genre_data)):
            if genre_data[item]["track_genre"] == g:
                genre = db.execute("select track_name from songs where track_genre = ?", g)
                break
        else:
            return render_template("search.html", error = error)


    a = request.form.get("acousticness")
    if a == None:
        acousticness = db.execute("select track_name from songs")
        count += 1

    elif a == "low":
        acousticness = db.execute("select track_name from songs where acousticness <= ?", 0.4)

    elif a == "average":
        acousticness = db.execute("select track_name from songs where acousticness >= ? and acousticness <= ?", 0.4, 0.6)

    elif a == "high":
        acousticness = db.execute("select track_name from songs where acousticness >= ? and acousticness <= ?", 0.6, 0.8)

    elif a == "very_high":
        acousticness = db.execute("select track_name from songs where acousticness >= ?", 0.8)

    else:
        return render_template("search.html", error = error)


    li = request.form.get("liveness")
    if li == None:
        liveness = db.execute("select track_name from songs")
        count += 1

    elif li == "low":
        liveness = db.execute("select track_name from songs where liveness <= ?", 0.01)

    elif li == "average":
        liveness = db.execute("select track_name from songs where liveness >= ? and liveness <= ?", 0.01, 0.1)

    elif li == "high":
        liveness = db.execute("select track_name from songs where liveness >= ? and liveness <= ?",0.1, 0.3)

    elif li == "very_high":
        liveness = db.execute("select track_name from songs where liveness >= ?", 0.3)

    else:
        return render_template("search.html", error = error)


    v = request.form.get("valence")
    if v == None:
        valence = db.execute("select track_name from songs")
        count += 1

    elif v == "low":
        valence = db.execute("select track_name from songs where valence <= ?", 0.3)

    elif v == "average":
        valence = db.execute("select track_name from songs where valence >= ? and valence <= ?", 0.3, 0.5)

    elif v == "high":
        valence = db.execute("select track_name from songs where valence >= ? and valence <= ?", 0.5, 0.7)

    elif v == "very_high":
        valence = db.execute("select track_name from songs where valence >= ?", 0.7)

    else:
        return render_template("search.html", error = error)


    if count > 5:
        return render_template("search.html", error = "Provide at least 4 preferences!")

    y1 = []
    for i in range(len(danceability)):
        y1.append(danceability[i]["track_name"])

    y2 = []
    for i in range(len(energy)):
        y2.append(energy[i]["track_name"])

    y3 = []
    for i in range(len(tempo)):
        y3.append(tempo[i]["track_name"])

    y4 = []
    for i in range(len(loudness)):
        y4.append(loudness[i]["track_name"])

    y5 = []
    for i in range(len(acousticness)):
        y5.append(acousticness[i]["track_name"])

    y6 = []
    for i in range(len(liveness)):
        y6.append(liveness[i]["track_name"])

    y7 = []
    for i in range(len(valence)):
        y7.append(valence[i]["track_name"])

    y8 = []
    for i in range(len(genre)):
        y8.append(genre[i]["track_name"])

    y9 = []
    for i in range(len(artists)):
        y9.append(artists[i]["track_name"])

    tracks = set(y1) & set(y2) & set(y3) & set(y4) & set(y5) & set(y6) & set(y7) & set(y8) & set(y9)

    tracks = list(tracks)

    tracks = tracks[:50]

    return render_template("search_results.html", tracks = tracks)

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")

    status = "Form Submitted"
    return render_template("contact.html", status = status)

@app.route("/about")
def about():
    return render_template("about.html")
