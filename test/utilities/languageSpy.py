from utilities.languageStub import LanguageStub


class LanguageSpy(LanguageStub):
    __congratulationsConsulted = False

    def congralutationsConsulted(self):
        return self.__congratulationsConsulted

    def congrats(self):
        self.__congratulationsConsulted = True

    def salutation(self):
        self.__congratulationsConsulted = True

    def goodbye(self):
        self.__congratulationsConsulted = True
