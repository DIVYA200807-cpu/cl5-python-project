from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Instrument:", self.name)

    @abstractmethod
    def play_sound(self):
        pass



class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar")

    def play_sound(self):
        print("Sound: Strum Strum")



class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano")

    def play_sound(self):
        print("Sound: Ting Ting")



class Drum(Instrument):
    def __init__(self):
        super().__init__("Drum")

    def play_sound(self):
        print("Sound: Boom Boom")



guitar = Guitar()
piano = Piano()
drum = Drum()


guitar.show_name()
guitar.play_sound()

print()

piano.show_name()
piano.play_sound()

print()

drum.show_name()
drum.play_sound()