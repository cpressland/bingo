from random import choice
from flask import Flask, redirect

app = Flask(__name__)

words = {
    "1": "One Direction",
    "2": "Dr Who",
    "3": "Cup of herbal tea",
    "4": "Knock at the door",
    "5": "Johnny's Alive",
    "6": "Little Mix",
    "7": "David Beckham",
    "8": "Golden Gate",
    "9": "Selfie Time",
    "10": "Boris’ den",
    "11": "Stranger Things",
    "12": "Dirty dozen",
    "13": "Unlucky for some",
    "14": "Valentine’s Day",
    "15": "Your claim to fame",
    "16": "Sweet 16",
    "17": "Dancing Queen",
    "18": "Party on Tatooine",
    "19": "Time for Quarantine",
    "20": "Facemasks Aplenty",
    "21": "Vaccines are fun",
    "22": "Scooby Doo and Scrappy too",
    "23": "The Bees Knees",
    "24": "It's Dumbledore",
    "25": "Dobbie Dies",
    "26": "She's had her Weetabix",
    "27": "Bridesmaid Dresses",
    "28": "Over Weight",
    "29": "Rise and Shine",
    "30": "Liz Lemon Rocks",
    "31": "Man Bun",
    "32": "Jimmy Choo",
    "33": "Dirty knees",
    "34": "Murder on the Dance Floor",
    "35": "Jump and Jive",
    "36": "New Tricks",
    "37": "A Hobbits Tale",
    "38": "Magnum P.I.",
    "39": "Love Island Time",
    "40": "Hello Naughty",
    "41": "Time for Fun",
    "42": "Winnie the Pooh",
    "43": "Fish, Chips and Pea's",
    "44": "Scores on the Doors",
    "45": "Halfway there",
    "46": "Up to tricks",
    "47": "Four and seven",
    "48": "Tag a mate",
    "49": "Amazon Prime",
    "50": "Hawaii Five-O",
    "51": "Aliens!",
    "52": "Chicken Vindaloo",
    "53": "Stuck in a tree",
    "54": "Grannys Drawers",
    "55": "Snakes alive",
    "56": "Chill with Netflix",
    "57": "Heinz varieties",
    "58": "Make them wait",
    "59": "Tequila and Lime",
    "60": "Five dozen",
    "61": "Baker's bun",
    "62": "Turn the screw",
    "63": "Oh my god, they killed Kennedy",
    "64": "Will you still love me",
    "65": "Thunderbirds are Go",
    "66": "Jedi Tricks",
    "67": "Retirement Heaven",
    "68": "Cathrine Tate",
    "69": "Moonwalk Time",
    "70": "I'm holding out for a Hero",
    "71": "Fox on the run",
    "72": "Six dozen",
    "73": "Not the Bees!",
    "74": "Recycle More",
    "75": "What a time to be alive",
    "76": "Ripley Saves Hicks",
    "77": "Sunset strip",
    "78": "Haters Gunna Hate",
    "79": "One more time",
    "80": "Imagine!",
    "81": "Girls just wana have fun",
    "82": "Electric Boogaloo",
    "83": "Gluten Free",
    "84": "Ghostbusters",
    "85": "Staying alive",
    "86": "Instagram Pix",
    "87": "Walk like an Egyptian",
    "88": "Will and Kate",
    "89": "Busta Rhyme",
    "90": "Joe Ninety",
}


def init():
    global previous_numbers
    global numbers
    previous_numbers = []
    numbers = list(range(1, 91))


@app.route("/")
def root():
    try:
        previous_numbers
        return redirect("/play", code=302)
    except NameError:
        init()
        return redirect("/play", code=302)


@app.route("/play")
def play():
    try:
        number = previous_numbers[-1]
        return f"""
        <html>
            <style>
                body {{
                    font-family: Helvetica, Arial, Sans-Serif;
                    text-align: center;
                    background-color: black;
                    color: white;

                }}
                pre {{
                    white-space: pre-wrap;
                    font-size: 25px;
                }}
                .number {{
                    font-size: 200px;
                }}
                .phrase {{
                    font-size: 50px;
                }}
                .button {{
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                }}
                .next {{
                    background-color: #4CAF50;
                }}
                .reset {{
                    background-color: #f44336;
                }}
            </style>
            <body>
                <span class="number">{number}</span><br />
                <span class="phrase">{words[str(number)]}</span><br />
                <br />
                <form action="/increment">
                    <input type="submit" class="button next" value="Next Number" />
                </form>
                <p>Previous Numbers:</p>
                <pre>{' '.join(previous_numbers)}</pre>
                <br />
                <br />
                <form action="/reset">
                    <input type="submit"
                    class="button reset"
                    onclick="return confirm('Are you sure?')"
                    value="Reset" />
                </form>
            </body>
        </html>
        """
    except IndexError:
        return redirect("/gameover", code=302)
    except NameError:
        return redirect("/", code=302)


@app.route("/gameover")
def gameover():
    return f"""
        <html>
            <style>
                body {{
                    font-family: Helvetica, Arial, Sans-Serif;
                    text-align: center;
                    background-color: black;
                    color: white;

                }}
                pre {{
                    white-space: pre-wrap;
                    font-size: 50px;
                }}
                .gameover {{
                    font-size: 50px;
                }}
                .button {{
                    background-color: #f44336;
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                }}
            </style>
            <body>
                <span class="gameover">Game over!!!</span><br />

                <form action="/reset">
                    <input type="submit" class="button reset" value="Reset" />
                </form>

                <p>Previous Numbers:</p>
                <pre>{' '.join(previous_numbers)}</pre>
            </body>
        </html>
        """


@app.route("/increment")
def increment():
    try:
        number = choice(numbers)
        previous_numbers.append(str(number))
        numbers.remove(number)
        return redirect("/play", code=302)
    except IndexError:
        return redirect("/gameover", code=302)


@app.route("/reset")
def reset():
    init()
    return redirect("/increment", code=302)
