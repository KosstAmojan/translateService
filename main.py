from flask import Flask, request
import json
from googletrans import Translator

app = Flask(__name__)


@app.route('/translate', methods=['POST'])
def translate():
    """
    Receives the translation request via POST.
    """

    # Convert received JSON to dictionary and parse.
    translate_request = json.loads(request.get_json())
    target = translate_request.get('trgt')
    text = translate_request.get('text')

    # create a translate object, pass the arguments to that object's
    # translate() method

    translator = Translator()
    rsp = translator.translate(text, dest=target)

    return rsp.text


if __name__ == '__main__':
    import os
    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))
