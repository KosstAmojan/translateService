from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)


@app.route('/translate', methods=['POST'])
def translate():
    """
    Receives the translation request via POST.
    """

    # Convert received JSON to dictionary and parse.
    translate_request = request.get_json()
    target = translate_request.get('trgt')
    text = translate_request.get('text')

    # create a translate object, pass the arguments to that object's
    # translate() method

    translator = Translator()
    rsp = translator.translate(text, dest=target)

    rsp_object = {
        'src':rsp.src,
        'dest':rsp.dest,
        'text':rsp.text
    }

    return jsonify(rsp_object)

if __name__ == '__main__':
    import os
    app.run(debug=True, port=int(os.environ.get('PORT', 8080)))
