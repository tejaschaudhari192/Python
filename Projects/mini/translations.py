from translate import Translator

to = Translator(to_lang='mr')
line = input("Enter line to translate: ")
linetranslated = to.translate(line)
print("Translated line is: ", linetranslated)