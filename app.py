
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    intent = req.get("fulfillmentInfo", {}).get("tag", "")

    if intent == "loan_enquiry":
        return jsonify({
            "fulfillment_response": {
                "messages": [{"text": {"text": ["How much loan do you need and for how many years?"]}}]
            }
        })
    else:
        return jsonify({
            "fulfillment_response": {
                "messages": [{"text": {"text": ["I didn't understand. Can you rephrase?"]}}]
            }
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
