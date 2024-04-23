from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from string import ascii_uppercase
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: str = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm emitting an ID.")
        self._state = self.generate_id()

        print(f"Subject: ID emitted: {self._state}")
        self.notify()

    def generate_id(self) -> str:
        """
        Generate a random 4-letter ID.
        """
        return ''.join(choice(ascii_uppercase) for _ in range(4))


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    _id: str = "UDTC"

    def update(self, subject: Subject) -> None:
        if subject._state == self._id:
            print(f"ConcreteObserverA: My ID ({self._id}) matches the emitted ID ({subject._state})")


class ConcreteObserverB(Observer):
    _id: str = "CSSO"

    def update(self, subject: Subject) -> None:
        if subject._state == self._id:
            print(f"ConcreteObserverB: My ID ({self._id}) matches the emitted ID ({subject._state})")


class ConcreteObserverC(Observer):
    _id: str = "NDOD"

    def update(self, subject: Subject) -> None:
        if subject._state == self._id:
            print(f"ConcreteObserverC: My ID ({self._id}) matches the emitted ID ({subject._state})")


class ConcreteObserverD(Observer):
    _id: str = "TCQD"

    def update(self, subject: Subject) -> None:
        if subject._state == self._id:
            print(f"ConcreteObserverD: My ID ({self._id}) matches the emitted ID ({subject._state})")


if __name__ == "__main__":

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    for _ in range(8):
        subject.some_business_logic()
