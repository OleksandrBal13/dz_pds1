class TextProcessor(object):
    def __init__(self, text):
        self.text = text
    def get_clean_string(self):
        puncs = ",", ".", "!", "?"
        for i in range(len(puncs)):
            self.text = self.text.replace(puncs[i],"")
        return self.text
    def is_punktiantion(self):
        if self.text.find("s") == True:
            return True





shon = TextProcessor("s.............dsadadasdas")
print(shon.get_clean_string())
print(shon.is_punktiantion())


##