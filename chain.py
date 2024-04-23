from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):


    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: int) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return "Numero no consumido"




class PrimosHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        if self.es_primo(request):
            return f"PrimosHandler: Consumí numero primo{request}"
        else:
            return super().handle(request)
    
    def es_primo(self, n: int) -> bool:
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


class ParesHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        if self.EsPar(request):
            return f"ParesHandler: Consumí numero par {request}"
        else:
            return super().handle(request)
    def EsPar(self, n: int) -> bool:
        return n % 2 == 0


def client_code(handler: Handler) -> None:


    for number in range(1,100):
        print(f"\nClient: Procesando numero {number}")
        result = handler.handle(number)
        print(f"  {result}")

if __name__ == "__main__":
    Pares = ParesHandler()
    Primos = PrimosHandler()

    Primos.set_next(Pares)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Primos > Pares\n")
    client_code(Primos)
    print("\n")