from random import choice
from flask import Flask, redirect

app = Flask(__name__)

words = {
    "1": "Kelly’s eye",
    "2": "One little duck",
    "3": "Cup of tea",
    "4": "Knock at the door",
    "5": "Man alive",
    "6": "Tom Mix",
    "7": "Lucky seven",
    "8": "Garden gate",
    "9": "Doctor’s orders",
    "10": "Boris’ den",
    "11": "Legs eleven",
    "12": "One dozen",
    "13": "Unlucky for some",
    "14": "Valentine’s Day",
    "15": "Young and keen",
    "16": "Sweet 16 and never been kissed",
    "17": "Dancing queen",
    "18": "Coming of age",
    "19": "Goodbye teens",
    "20": "One score",
    "21": "Drunken Bum",
    "22": "Two little ducks",
    "23": "Thee and me",
    "24": "Two dozen",
    "25": "Duck and dive",
    "26": "Pick and mix",
    "27": "Gateway to heaven",
    "28": "In a state/Over weight",
    "29": "Rise and shine",
    "30": "Dirty Gertie",
    "31": "Get up and run",
    "32": "Buckle my shoe",
    "33": "Dirty knee",
    "34": "Ask for more",
    "35": "Jump and jive",
    "36": "Three dozen",
    "37": "More than eleven",
    "38": "Christmas cake",
    "39": "39 steps",
    "40": "Life begins",
    "41": "Time for fun",
    "42": "Winnie the Pooh",
    "43": "Down on your knees",
    "44": "Droopy drawers",
    "45": "Halfway there",
    "46": "Up to tricks",
    "47": "Four and seven",
    "48": "Four dozen",
    "49": "PC",
    "50": "Half a century",
    "51": "Tweak of the thumb",
    "52": "Danny La Rue",
    "53": "Stuck in a tree",
    "54": "Clean the floor",
    "55": "Snakes alive",
    "56": "Shotts Bus",
    "57": "Heinz varieties",
    "58": "Make them wait",
    "59": "Brighton Line",
    "60": "Five dozen",
    "61": "Baker’s bun",
    "62": "Hows the crew",
    "63": "Tickle me 63",
    "64": "Red raw",
    "65": "Old age pension",
    "66": "Clickety click",
    "67": "Stairway to heaven",
    "68": "Saving Grace",
    "69": "Favourite of mine",
    "70": "Three score and ten",
    "71": "Bang on the drum",
    "72": "Six dozen",
    "73": "Queen bee",
    "74": "Hit the floor",
    "75": "Strive and strive",
    "76": "Trombones",
    "77": "Sunset strip",
    "78": "39 more steps",
    "79": "One more time",
    "80": "Eight and blank",
    "81": "Stop and run",
    "82": "Straight on through",
    "83": "Time for tea",
    "84": "Seven dozen",
    "85": "Staying alive",
    "86": "Between the sticks",
    "87": "Torquay in Devon",
    "88": "Two fat ladies",
    "89": "Nearly there",
    "90": "Top of the shop",
}


def init():
    global previous_numbers
    global numbers
    previous_numbers = []
    numbers = list(range(1, 91))


@app.route("/")
def root():
    for _ in range(0, 3):
        try:
            number = choice(numbers)
            previous_numbers.append(str(number))
            numbers.remove(number)
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
                    }}
                    .number {{
                        font-size: 150px;
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
                    <form action="/">
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
        except NameError:
            init()
            continue


@app.route("/reset")
def reset():
    init()
    return redirect("/", code=302)
