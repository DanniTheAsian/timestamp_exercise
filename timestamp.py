"""Docstring der fortæller om modulet"""


# Vi laver en class: TimeStamp

class TimeStamp:
    """Her skal der være en docstring"""
    #===== Constructor ======
    # Når der laves  en connstructor, bruger vi __init__()
    #__init__ bruges til at initialiserer attributter af instancer
    def __init__(
                # Argumenter her
                 self, # der skal være en self her da den refferer til sig selv
                 hours: int = 0,
                 minutes: int = 0,
                 seconds: int = 0 ):

        if not TimeStamp.is_valid(hours, minutes, seconds):
            raise ValueError("Invalid time")

        # Instance attributter
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # ========== Getters & setters =========
    #Get: henter data og skal returnerer (af hvad jeg forstår)
    def getters(self):
        """docstring her"""
        return self.hours, self.minutes, self.seconds
    #Set: tildeler data

    def setters(self, hours, minutes, seconds):
        """docstring her"""
        if not TimeStamp.is_valid(hours, minutes, seconds):
            raise ValueError("Invalid time")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    #SKIP FUNKTIONER
    def skip_second(self):
        """docstring her"""
        self.seconds += 1
        if self.seconds > 59:
            self.seconds = 0
            self.skip_minute()

    def skip_minute(self):
        """docstring her"""
        self.minutes += 1
        if self.minutes > 59:
            self.minutes = 0
            self.skip_hour()

    def skip_hour(self):
        """docstring her"""
        self.hours += 1
        if self.hours > 23:
            self.hours = 0


    # skip another timestamp
    def skip(self, timestamp: "TimeStamp"):
        """docstring her"""
        self.hours += timestamp.hours
        self.minutes += timestamp.minutes
        self.seconds += timestamp.seconds

        # Flyt minutter fra sekunder (formel: nye_minutter = minutter + ⌊sekunder/60⌋)
        self.minutes += self.seconds // 60

        # minutter = minutter mod 60 (Hold de resterende sekunder)
        self.seconds %= 60

        self.hours += self.minutes // 60
        self.minutes %= 60

        #Rest af timer (timer mod 24)
        self.hours %= 24

    def copy(self) -> "TimeStamp":
        """docstring her"""
        return TimeStamp(self.hours, self.minutes, self.seconds)


    #__eq__ er en speciel method, som sammenligner 2 attributer,
    # og returnerer en boolean
    def __eq__(self, other) -> bool:
        if isinstance(other, TimeStamp):
            raise ValueError('blablbla')
        return (self.hours == other.hours
                and self.minutes == other.minutes
                and self.seconds == other.seconds)

    #__lt__er en speciel method. det står for "less than",
    # som checker om værdi a er mindre end b (a < b)
    # Det returner en boolean
    def __lt__(self, other) -> bool:
        if not isinstance(other, TimeStamp):
            return False
        return (self.hours, self.minutes, self.seconds) < \
            (other.hours, other.minutes, other.seconds)

    #__le__ er en speciel method. det står for "less or equal",
    # som checker om værdi a er mindre eller ligemed b (a <= b)
    # Det returner en boolean
    def __le__(self, other) -> bool:
        if not isinstance(other, TimeStamp):
            return False
        return (self.hours, self.minutes, self.seconds) <= \
            (other.hours, other.minutes, other.seconds)

    # en speciel method, som returnerer en string
    def __str__(self) -> str:

        #02d er en format-specifikation i f-strings.
        #0 = udfylder med 0
        #2 = 2 cifre
        #d = decimal
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    # __repr__ er en speciel method som er en "præcis" tekst der repræsenterer ens objekt.abs
    #Bruges primært til debugging
    def __repr__(self) -> str:
        return f'Timestamp: {self.hours}, {self.minutes}, {self.seconds}'

    @staticmethod # en decorator,som er en "basic function som vi kender"
                    #som bare tjekker tal
    def is_valid(hours, minutes, seconds) -> bool:
        """docstring her"""
        return (0 <= hours <= 23) and (0 <= minutes <= 59) and (0 <= seconds <= 59)

if __name__ == '__main__':
    time = TimeStamp(12, 0, 59)
    for i in range(50):
        print(time)
        time.skip_second()
