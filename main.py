import flask
from flask import request, jsonify
import re
import requests as rq
import random

app = flask.Flask(__name__)

def imglink(search):
  a = rq.get(f"https://unsplash.com/s/photos/{search}").text
  regex = r"https://images\S+.=80"
  c = re.findall(regex, a)
  return c[random.randint(0,len(c))]

@app.route("/api/search", methods=["GET"])
def search():
  """Searches for images and returns a list of image links."""
  search_term = request.args.get("q")
  image_link = imglink(search_term)
  return jsonify({"image_link": image_link})

if __name__ == "__main__":
  app.run(debug=True)
  