from flask import Flask, render_template, request
app = Flask(__name__)
# Temporary storage (in-memory)
users = []
@app.route("/")
def index():
    return render_template("form.html", users=users)
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    place = request.form["place"]
    state = request.form["state"]
    pincode = request.form["pincode"]

    users.append({
        "name": name,
        "age": age,
        "place": place,
        "state": state,
        "pincode": pincode
    })

    return render_template("result.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
