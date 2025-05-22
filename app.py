from flask import Flask, redirect

app = Flask(__name__)

current_url = "https://maps.app.goo.gl/YQSjk16vpEp7knNZ8?g_st=com.google.maps.preview.copy"

@app.route("/")
def dynamic_redirect():
    return redirect(current_url, code=302)
