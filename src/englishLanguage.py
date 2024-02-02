from timeDay import TimeDay


class EnglishLanguage:
    def congrats(self):
        return "Well said!"

    def salutation(self, timeDay):
        if (timeDay == TimeDay.Morning):
            return "Good morning"
        elif (timeDay == TimeDay.Afternoon):
            return "Good afternoon"
        elif (timeDay == TimeDay.Evening):
            return "Good evening"
        elif (timeDay == TimeDay.Night):
            return "Good night"
        else:
            return "Hello"

    def goodbye(self, timeDay):
        if (timeDay == TimeDay.Morning):
            return "Goodbye"
        elif (timeDay == TimeDay.Afternoon):
            return "Goodbye"
        elif (timeDay == TimeDay.Evening):
            return "Good night"
        elif (timeDay == TimeDay.Night):
            return "Good night"
        else:
            return "Goodbye"