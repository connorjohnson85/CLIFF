import googletrans

translator = googletrans.Translator()

result = translator.translate('mita sin a teet')
print(result.text)
print(result)

source = result.src



def Translate(text):
	return translator.translate(text)

