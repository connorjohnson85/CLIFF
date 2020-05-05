from services.Speech import textToSpeech as ts, inputTesting, textTesting
import random
import os


def chat(mode, name):
	textTesting(mode, "C.L.I.F.F.: Hello {0}! What is going on?".format(name))
	while True:
		answer = inputTesting(mode, "Connor: ".format(name))
		if "bye" in answer:
			textTesting(mode, "C.L.I.F.F.: goodbye {}".format(name))
			break

