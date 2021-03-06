from app.services.timers.ITimer import ITimer
from app.services.observers.IObserver import IObserver
from helpers.DateTime import DateTime
from threading import Thread

class IntervalTimer(ITimer):

    def __init__(self, interval: DateTime):
        self._interval = interval
        self._subscribes = []

    def start(self):
        thread = Thread(target=IntervalTimer.startСountdown,
                        args=(self,))
        thread.start()
        # thread.join()

    def startСountdown(self):
        while True:
            initialInterval = DateTime.now()
            while initialInterval < self._interval:
                initialInterval = DateTime.now()

            self._infoSubscribers()
            self._interval.restart()

    def addSubscriber(self, subscriber: IObserver):
        self._subscribes.append(subscriber)

    def _infoSubscribers(self):
        for subscribe in self._subscribes:
            subscribe.checkResources()