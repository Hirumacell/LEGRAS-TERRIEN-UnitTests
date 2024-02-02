from timeDay import TimeDay


class FrenchLanguage:
    def congrats(self):
        return "Bien dit!"

    def salutation(self, timeDay):
        if (timeDay == TimeDay.Morning):
            return "Bonjour"
        elif (timeDay == TimeDay.Afternoon):
            return "Bonjour"
        elif (timeDay == TimeDay.Evening):
            return "Bonsoir"
        elif (timeDay == TimeDay.Night):
            return "Bonsoir"
        else:
            return "Bonjour"

    def goodbye(self, timeDay):
        if (timeDay == TimeDay.Morning):
            return "Bonne journée"
        elif (timeDay == TimeDay.Afternoon):
            return "Bon après-midi"
        elif (timeDay == TimeDay.Evening):
            return "Bonne soirée"
        elif (timeDay == TimeDay.Night):
            return "Bonne nuit"
        else:
            return "Au revoir"