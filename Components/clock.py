import math
import datetime
import threading
import time

from config import eventForClock, event
from hand_detect import run_until_hand_detected
from utils import debugShow, clearPorts


def startClock(io_ports_for_clock):
    hourNow = datetime.datetime.now().time().hour
    minuteNow = datetime.datetime.now().time().minute
    ioPorts = io_ports_for_clock
    while not eventForClock.isSet():
        if not ioPorts[hourNow % 12].isLightOn():
            ioPorts[hourNow % 12].lightOn()
        if hourNow % 12 != math.floor(minuteNow / 5):
            ioPorts[math.floor(minuteNow / 5)].lightOn()
        if hourNow % 12 != math.floor(minuteNow / 5):
            ioPorts[math.floor(minuteNow / 5)].lightOff()
        minuteNow = datetime.datetime.now().time().minute
        hourNow = datetime.datetime.now().time().hour
