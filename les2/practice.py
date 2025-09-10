from typing import (
    Union,
    Callable,
    NoReturn,
    TypeVar,
    Optional,
    Any,
    Sequence,
    Iterable,
    TypedDict,
    NamedTuple,
)


# Example of a list with mixed types (not great practice, but valid typing)
user_ids: list[int | str] = [42, "1234a", 7, "1245a"]


class User:
    """Class for representing a user."""

    id: int | str
    name: str
    age: Optional[int]
    is_admin: bool
    gender: Any
    friends: list["User"]
    parents: tuple["User", ...]

    def __init__(
        self,
        id: Union[int, str] = 42,
        name: str = "John Doe",
        age: Optional[int] = None,
        is_admin: bool = False,
        gender: Any = "Not specified",
    ) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.is_admin = is_admin
        self.gender = gender
        self.friends: list[User] = []
        self.parents: tuple[User, ...] = ()

    def get_is_admin(self) -> bool:
        """Return True if the user is an admin, False otherwise."""
        return self.is_admin


# Example instance
user_a: User = User(0, "Alice", 30, True, "Female")
checker: Callable[[], bool] = user_a.get_is_admin


# Phone book example
phone_book: dict[str, str] = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
}

skus: set[str] = {"SKU123", "SKU456", "SKU789"}


class Order:
    """Example class with a sequence of foods."""

    foods: Sequence[str] = ["pizza", "sushi", "burger"]


def handle_404(exc: Any) -> NoReturn:
    """Custom handler that always raises an exception (like a 404)."""
    raise Exception("404 Not Found: " + str(exc))


# Generics example with User subclasses
T = TypeVar("T", bound=User)
users: list[T] = []
for user in users:
    print(f"User Name: {user.name} - is Admin: {user.is_admin}")


# Iterable / Iterator example 
urls: Iterable[str] = iter(
    [
        "https://www.linkedin.com/feed/?trk=404_page",
        "https://www.google.com/",
        "https://www.github.com/",
    ]
)
print(next(urls))


class Pizza(TypedDict):
    """Pizza details."""

    size: str
    toppings: list[str]

#use named tuple
# When you want lightweight data containers (immutable records).
# When the object doesn’t need behavior (methods), only data.
# When you want both tuple unpacking and attribute access.

class CheesesPercentage(NamedTuple):
    """Cheese percentage details."""

    cheese: str
    percentage: float


class Pizza4Cheese(Pizza):
    """Pizza with 4 cheese details."""

    cheese_types: list[CheesesPercentage]

# Use Sequence when:
# You want to accept any ordered container, not just list.
# You don’t plan to mutate it (because Sequence only guarantees read operations).


def first_item(items: Sequence[int]) -> int:
    return items[0]

print(first_item([1, 2, 3]))     # list works
print(first_item((10, 20, 30)))  # tuple works
print(first_item(range(5)))      # range works

