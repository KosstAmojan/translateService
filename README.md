# translateService 
#
# Make call to translateService by sending a post request to port on which service is running. Send request in the format of a json like this:
#
# {'trgt' : "es",
#  'text' : "text to translate" }
# 
# where trgt is the key for the target language value, which should be a two-character code as specified here: 
# https://developers.google.com/admin-sdk/directory/v1/languages and 'text' is the key for the text string to be translated.
#
# See usage example in translate_payload.py. 
#
# 1. Make sure the following python modules are installed via `pip install <module>`: flask, request, requests, json, googletrans.
# 2. For reference, I am running python 3.9.11.
# 3. Assuming python3 is installed to your path as `python`, begin running service via `python main.py`.
