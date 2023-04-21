# import speech_recognition as sr

# def get_voice_input():
#     recognizer = sr.Recognizer()

#     # load the language model
#     language_model = sr.language_model.LanguageModel()
#     language_model.load("en-us.lm.bin")

#     # set up the decoder with the language model and acoustic model
#     decoder_config = sr.Decoder.default_config()
#     decoder_config.set_string('-hmm', 'en-us')
#     decoder_config.set_string('-lm', 'en-us.lm.bin')
#     decoder_config.set_string('-dict', 'cmudict-en-us.dict')
#     decoder_config.set_string('-logfn', '/dev/null')
#     decoder = sr.Decoder(decoder_config)

#     with sr.Microphone() as source:
#         print("Please say something...")
#         audio = recognizer.listen(source)

#         try:
#             text = decoder.recognize_sphinx(audio)
#             print(f"You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             print("Sorry, I couldn't understand what you said.")
#             return None
#         except sr.RequestError:
#             print("Sorry, the service is unavailable. Try again later.")
#             return None

# get_voice_input()