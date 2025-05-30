from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    tag = req.get("fulfillmentInfo", {}).get("tag", "")

    if tag == "getLoanOffer":
        # Replace with your real logic or Excel-driven output
        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                "Based on your profile, you’re eligible for ₹5,00,000 at 11.5% interest over 5 years."
                            ]
                        }
                    }
                ]
            }
        })

    return jsonify({
        "fulfillment_response": {
            "messages": [
                {"text": {"text": ["Sorry, I didn’t understand."]}}
            ]
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
