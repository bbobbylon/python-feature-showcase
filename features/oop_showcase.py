"""
oop_showcase.py
================

Demonstrates: classes, `__init__`, instance methods, inheritance,
`super()`, dunder ("double underscore") methods, and the modern
`@dataclass` shortcut.

Analogy: A class is a BLUEPRINT (like the architectural plans for a
house), and an object (also called an "instance") is an actual HOUSE
built from that blueprint. You can build many houses (objects) from one
blueprint (class), and each one has its own furniture (data / attributes)
even though they share the same floor plan (methods / behavior).
"""

from __future__ import annotations

from dataclasses import dataclass, field


def run_demo() -> None:
    print("\n=== 1. A Basic Class ===")
    _demo_basic_class()

    print("\n=== 2. Inheritance & super() ===")
    _demo_inheritance()

    print("\n=== 3. Dunder Methods (__str__, __eq__, __add__) ===")
    _demo_dunder_methods()

    print("\n=== 4. @dataclass (a modern shortcut) ===")
    _demo_dataclass()


class Animal:
    """
    A basic class. `__init__` is the constructor -- it runs automatically
    when you create a new Animal, and it's where you set up the object's
    starting data ("attributes").

    `self` refers to "this particular instance" -- it's how a method
    reaches back into ITS OWN data. Every instance method takes `self` as
    its first parameter (Python passes it automatically; you don't supply
    it yourself when calling the method).
    """

    def __init__(self, name: str, sound: str) -> None:
        self.name = name  # instance attribute: unique to each Animal object
        self.sound = sound

    def speak(self) -> str:
        """An instance method -- behavior that every Animal shares."""
        return f"{self.name} says {self.sound}!"


def _demo_basic_class() -> None:
    dog = Animal("Rex", "Woof")
    cat = Animal("Whiskers", "Meow")

    print(f"  {dog.speak()}")
    print(f"  {cat.speak()}")
    print("  Same blueprint (Animal), two different objects with their own data.")


class Dog(Animal):
    """
    Inheritance: `Dog` is a MORE SPECIFIC version of `Animal`. It gets
    everything `Animal` has for free, and can add or override behavior.

    Analogy: if `Animal` is "vehicle" blueprints, `Dog` is a "sports car"
    blueprint that inherits the general "has an engine, can drive" parts
    but adds its own specifics (a spoiler, a turbo button).
    """

    def __init__(self, name: str, breed: str) -> None:
        # `super()` gives us access to the PARENT class (Animal) so we can
        # reuse its __init__ instead of duplicating the logic here.
        super().__init__(name, sound="Woof")
        self.breed = breed  # Dog-specific attribute that Animal doesn't have

    def fetch(self) -> str:
        """A method that only Dog has -- Animal doesn't know how to fetch."""
        return f"{self.name} the {self.breed} fetches the ball!"

    def speak(self) -> str:
        """
        Overriding: Dog provides its OWN version of `speak`, which replaces
        (rather than reuses) Animal's version when called on a Dog.
        """
        base_message = super().speak()  # you can still call the parent's version
        return f"{base_message} (a very good dog, in fact)"


def _demo_inheritance() -> None:
    rex = Dog("Rex", "Golden Retriever")
    print(f"  {rex.speak()}")
    print(f"  {rex.fetch()}")
    print(f"  isinstance(rex, Animal) -> {isinstance(rex, Animal)}  (a Dog IS an Animal)")


class Money:
    """
    Dunder ("double underscore") methods let your custom objects hook into
    Python's built-in behavior: printing, equality checks, arithmetic
    operators, and more. This is how, for example, `datetime` objects can
    be subtracted from each other with a plain `-`.
    """

    def __init__(self, dollars: float) -> None:
        self.dollars = dollars

    def __str__(self) -> str:
        """Controls what `print(money_object)` and `str(money_object)` show."""
        return f"${self.dollars:.2f}"

    def __repr__(self) -> str:
        """Controls the 'developer-facing' representation, shown in lists/debuggers."""
        return f"Money({self.dollars!r})"

    def __eq__(self, other: object) -> bool:
        """Controls what `==` does between two Money objects."""
        if not isinstance(other, Money):
            return NotImplemented
        return self.dollars == other.dollars

    def __add__(self, other: "Money") -> "Money":
        """Controls what `+` does between two Money objects."""
        return Money(self.dollars + other.dollars)


def _demo_dunder_methods() -> None:
    wallet = Money(20.50)
    tip = Money(4.50)

    print(f"  str(wallet) via __str__: {wallet}")
    print(f"  repr in a list via __repr__: {[wallet, tip]}")
    print(f"  wallet == Money(20.50) via __eq__: {wallet == Money(20.50)}")
    print(f"  wallet + tip via __add__: {wallet + tip}")


@dataclass
class Point3D:
    """
    @dataclass is a decorator (see functions_and_decorators.py) that
    auto-generates the boilerplate `__init__`, `__repr__`, and `__eq__`
    methods for a class that's mainly a container for data.

    Without @dataclass, you'd have to hand-write:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        def __repr__(self):
            return f"Point3D(x={self.x}, y={self.y}, z={self.z})"
        def __eq__(self, other):
            ...

    @dataclass writes all of that for you based on the type-hinted fields
    below. This is a very "Pythonic" way to reduce repetitive code.
    """

    x: float
    y: float
    z: float = 0.0  # default value, just like a normal function argument
    tags: list[str] = field(default_factory=list)  # safe way to default to a mutable list


def _demo_dataclass() -> None:
    origin = Point3D(0, 0, 0)
    point = Point3D(1, 2, 3, tags=["origin-adjacent"])

    print(f"  origin -> {origin}   (auto-generated __repr__)")
    print(f"  point  -> {point}")
    print(f"  origin == Point3D(0, 0, 0) -> {origin == Point3D(0, 0, 0)}  (auto-generated __eq__)")
