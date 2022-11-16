class TextProcessor:
    def __init__(self):
        self._punktuation = '!@#$%^&*()_+<>?,./'
    def __is_punktuation(self, symbol):
        return symbol in self._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for symbol in text:
            if self.__is_punktuation(symbol):
                continue
            clean_text += symbol
        return clean_text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Your str without puncs is here ---> {}".format(self.__clean_string))
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


data_interface = DataInterface()
test_text = ["Imma . trying. to , delete ! punctuations"]
test = data_interface.process_texts(test_text)
