from flask import Flask, jsonify, abort, request
import json

ARGUMENT_COUNT = 2

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    return [quote for quote in quotes if quote["id"] == qid]


@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify({"quotes": quotes}), 200


@app.route("/api/quotes/<int:qid>", methods=["GET"])
def get_quote(qid):
    quote = _get_quote(qid)
    if quote == []:
        abort(404)
    return jsonify({"quotes": quote}), 200


@app.route("/api/quotes", methods=["POST"])
def create_quote():

    if request.json == {}:
        abort(400)
    elif len(request.json) < ARGUMENT_COUNT:
        abort(400)

    for quote in quotes:
        if (
            quote["quote"] == request.json["quote"]
            and quote["movie"] == request.json["movie"]
        ):
            abort(400)

    new_quote = {
        "id": quotes[-1]["id"] + 1,
        "quote": request.json["quote"],
        "movie": request.json["movie"],
    }
    quotes.append(new_quote)
    return jsonify({"quote": new_quote}), 201


@app.route("/api/quotes/<int:qid>", methods=["PUT"])
def update_quote(qid):
    if len(request.json) == 0:
        abort(400)

    for quote in quotes:
        if quote["id"] == qid:
            quote["quote"] = request.json["quote"]
            quote["movie"] = request.json["movie"]
            return jsonify({"quote": quote}), 200
    abort(404)


@app.route("/api/quotes/<int:qid>", methods=["DELETE"])
def delete_quote(qid):
    found = False
    for quote in quotes:
        if quote["id"] == qid:
            found = True
    if not found:
        abort(404)

    for index, quote in enumerate(quotes):
        if quote["id"] == qid:
            quotes.pop(index)
            return jsonify({"quotes": quotes}), 204
