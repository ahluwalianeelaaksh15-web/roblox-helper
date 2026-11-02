from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Knowledge base for Roblox Helper
RESPONSES = {
    "adopt me": "In Adopt Me!, you can hatch pets, build houses, and trade with friends! Tip: Do daily tasks to earn Bucks faster.",
    "blox fruits": "Blox Fruits is an action game! Tip: Grind quests at your level area and try to get light or buddha fruits early on for easy leveling.",
    "brookhaven": "Brookhaven RP is a roleplay game where you can own houses, drive vehicles, and explore the city with friends.",
    "tower of hell": "Tower of Hell is an obby game with no checkpoints! Tip: Take your time and practice your jump timing.",
    "robux": "To get Robux, buy them from the official Roblox store or earn them by creating Roblox games/clothing. Beware of free Robux scams!",
    "lag": "To fix lag in Roblox: Lower graphics settings in-game (Esc > Settings), close background tabs, or use an Ethernet connection."
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message', '').lower()

    # Simple rule-based search
    response = "I'm not sure about that game yet! Ask me about Adopt Me, Blox Fruits, Brookhaven, Tower of Hell, Robux, or Lag tips."

    for key in RESPONSES:
        if key in user_message:
            response = RESPONSES[key]
            break

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
