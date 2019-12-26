class Foo:
    def __init__(self):
        self.a = False
        self.b = False
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.a = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.a:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.b = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.b:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()