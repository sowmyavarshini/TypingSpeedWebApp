from flask import Flask, render_template, request, jsonify
import random
from dotenv import load_dotenv
import os

load_dotenv()
Secret_key = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", Secret_key)


passages = [
"The sun dipped below the horizon, casting long shadows across the tranquil meadow. Birds were returning to their nests, their songs gradually fading into the evening silence.Amidst the bustling city, a lone street musician played his guitar with passion. His melodies echoed through the busy streets, captivating the hearts of those who paused to listen.",
"In the heart of the dense forest, a small stream meandered peacefully. Its crystal-clear waters glistened as they flowed over smooth pebbles, creating a soothing melody of nature. As the rain began to fall, people hurriedly opened their umbrellas and rushed for cover. The city streets transformed into a shimmering dance of umbrellas in the rain.",
"The old bookstore at the corner of the street held a treasure trove of stories. Dusty shelves were lined with books that had witnessed the passage of time and held the wisdom of generations. High up in the mountains, the air was crisp and the view breathtaking. Snow-capped peaks stretched as far as the eye could see, reminding us of the grandeur of nature.",
"In the bustling market, vendors shouted their prices and shoppers haggled for the best deals. The aroma of street food filled the air, tempting passersby with its irresistible allure. A gentle breeze rustled the leaves of the ancient oak tree, carrying with it the promise of a new season. The cycle of life continued, as it had for countless years before.",
"This is a sample text for your typing speed test web app. You can use it to evaluate your typing speed and accuracy. The goal is to type the given text as accurately and quickly as possible. Remember to pay attention to punctuation and spaces. Good luck! The waves crashed against the shore, a rhythmic dance that had been ongoing since the dawn of time. The ocean held mysteries untold, its depths a canvas of hidden wonders. The old bookstore at the corner of the street held a treasure trove of stories. Dusty shelves were lined with books that had witnessed the passage of time and held the wisdom of generations. High up in the mountains, the air was crisp and the view breathtaking."

]


@app.route('/')
def index():
    passage = random.choice(passages)
    return render_template('index.html', passage=passage)


def calculate_wpm(text, start_time, passage):
    typed_words = text.split()
    passage_words = passage.split()

    correctly_typed_words = 0

    for typed_word, passage_word in zip(typed_words, passage_words):
        if typed_word == passage_word:
            correctly_typed_words += 1
    wpm = correctly_typed_words
    return wpm


@app.route('/calculate_wpm', methods=['POST'])
def calculate_wpm_endpoint():
    data = request.json
    text = data.get('text', '')
    passage = data.get('passage', '')
    wpm = calculate_wpm(text, passage)

    return jsonify({'wpm': int(wpm)})


if __name__ == '__main__':
    app.run(debug=False)
