from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import googletrans

app = Flask(__name__)
CORS(app)

# when website open with this end point this home function will be called
@app.route('/')
def home():
    return render_template('translate.html')


@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    target_language = request.json['target_language']

    translator = googletrans.Translator()
    translated_text = translator.translate(text, dest=target_language).text

    return jsonify({'translated_text': translated_text})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
