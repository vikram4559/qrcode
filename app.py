import os
from flask import Flask, redirect

app = Flask(__name__)

# This is the destination URL — change this later to your website
current_url = "https://maps.google.com/?q=Your+Restaurant+Location"

@app.route("/")
def dynamic_redirect():
    return redirect(current_url, code=302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's provided PORT
    app.run(host="0.0.0.0", port=port)
