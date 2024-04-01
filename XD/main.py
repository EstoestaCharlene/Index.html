from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("styles.csv")
x = data.drop(columns=["styles"])
y = data["styles"]
model = DecisionTreeClassifier()
model.fit(x.values ,y)


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():
    fade = 0
    barber = 0
    mohawk = 0
    undercut = 0

    if request.method == "POST":
        Ffade = request.form["fade"]
        Bbarber = request.form["barber"]
        Mmohawk = request.form["mohawk"]
        Uundercut = request.form["undercut"]

        fade = Ffade
        barber = Bbarber
        mohawk = Mmohawk
        undercut = Uundercut

    predicted_value = model.predict([[fade, barber, mohawk, undercut]])

    return render_template("index.html" ,firstname=predicted_value[0])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
