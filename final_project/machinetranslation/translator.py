"""
TRANSLATION PROGRAM
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import ApiException

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

try:
    language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)


language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)




def english_to_french(english_text):
    """Change to french"""
    french_text = language_translator.translate(text = english_text, model_id='en-fr').get_result
    return french_text

def french_to_english(french_text):
    """Change to english"""
    english_text = language_translator.translate(text = french_text, model_id='fr-en').get_result
    return english_text
