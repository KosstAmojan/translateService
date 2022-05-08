# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# must install virtual python environment and appropriate libraries:
# https://pypi.org/project/google-cloud-translate/ (will need to run pip
# commands as myenv/pip/bin)

# set environment variables (may want to change this in your .profile so you
# don't have to set the environment variables each time you run the script)
# for GOOGLE_APPLICATION_CREDENTIALS

# if you have an M1 mac, you need to set these environment variables:
# GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
# GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
# run the following: pip install firebase-admin
#

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
