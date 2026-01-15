import time


class StarTrek:

    def __init__(self, name, rank, actor, nickname):
        self.name = name
        self.rank = rank
        self.actor = actor
        self.nickname = nickname

    def __str__(self):
        return f"{self.actor} as {self.rank} {self.name}, nickname: {self.nickname}"

    def speak(self, line):
        return f"{self.nickname}: {line}"


janeway = StarTrek("Kathryn Janeway", "Captain", "Kate Mulgrew", "Janeway")
paris = StarTrek("Tom Paris", "Lieutenant", "Robert Duncan McNeil", "Tom")
tuvok = StarTrek("Tuvok", "Lieutenant", "Tim Russ", "Tuvok")
kim = StarTrek("Harry Kim", "Ensign", "Garrett Wang", "Kim")


def say(line, pause=3):
    print(line)
    time.sleep(pause)


say(janeway.speak("Tom, set a course for the Nekrit Expanse. Maximum warp."))
say(paris.speak("Aye, ma'am. Course laid in."))
say("The ship suddenly shakes.")
say(paris.speak("Captain, something just hit us!"))
say(kim.speak("We're getting heat by a Kazon ship, port side!"))
say(tuvok.speak("Shields are holding at 63 percent. Weapons are ready. I recommend a counterattack."))
say(janeway.speak("Hold steady. Target the Kazon ship and return fire, controlled burst."))
say(tuvok.speak("Target locked."))
say(janeway.speak("Do it."))
