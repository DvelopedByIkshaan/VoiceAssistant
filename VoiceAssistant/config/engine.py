from config import wakeword
from config.__init__ import __init__parser
from config.addons.proccessor import processor
from config.wakeword import WAKE


def wake_word_engiene():
    while True:
        print("Say something!")
        wakecall = input(":")
        if wakecall.count(WAKE) > 0:
            pass
            Exception = processor()
            print("Wake Word Called"), Exception