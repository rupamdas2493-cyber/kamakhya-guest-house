from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    phone = request.form.get("phone")
    room = request.form.get("room")
    date = request.form.get("date")

    # Save booking
    with open("bookings.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, room, date, datetime.now()])

    # WhatsApp message
    message = f"New Booking:%0AName: {name}%0APhone: {phone}%0ARoom: {room}%0ADate: {date}"

    return redirect(f"https://wa.me/917896860210?text={message}")

if __name__ == "__main__":
    app.run(debug=True)
