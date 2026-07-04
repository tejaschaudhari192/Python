from flask import Flask, request, jsonify
from flask_cors import CORS
from translate import Translator

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST', 'GET'])
def translate_text():
    try:
        if request.method == 'POST':
            data = request.get_json()

            if 'text' not in data or 'language' not in data:
                return jsonify({'error': 'Invalid request. Please provide both text and language parameters.'}), 400

            text = data['text']
            language = data['language']
        elif request.method == 'GET':
            text = request.args.get('text')
            language = request.args.get('language')

            if text is None or language is None:
                return jsonify({'error': 'Invalid request. Please provide both text and language parameters.'}), 400
        else:
            return jsonify({'error': 'Method not allowed.'}), 405

        translator = Translator(to_lang=language)
        translated_text = translator.translate(text)

        return jsonify({'translated_text': translated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '_main_':
    app.run(debug=True)