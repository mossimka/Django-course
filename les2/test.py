from typing import (
  Callable,
  NoReturn, 
  TypeVar, 
  Union, 
  Optional, 
  Any, 
  List, 
  Tuple, 
  Dict, 
  Set, 
  Sequence, 
  Iterable, 
  TypedDict,
  NamedTuple,
)

users_cnt_or_some_str: int | str = 42
another_var: Union[int, str] = "Hello"

some_str_ot_not: str | None = None #bad shit
some_str_ot_not = "Now it's a string"
another_var2: Union[str, None] = None #bad shit
some_str_ot_not2 = "Another string"
  
some_str_ot_not2: Optional[str] = None  #valid
any_var: Any = None #valid

marks_list: List[int] = [1, 2, 3] #valid
marks_tuple_invalid: Tuple[int] = (1, 2, 3) # invalid
marks_tuple: Tuple[int, ...] = (1, 2, 3,) # valid

marks_tuple: Tuple[int, ...] = (
  1,
  2,
  3,
)  # valid (multiline)

name_age_dict: Dict[str, int] = {
  "Alice": 30,
  "Bob": 25,
} # valid

unique_names_set: Set[str] = {"Alice", "Bob", "Charlie"} # valid old, new set


def greet(names: Sequence[str]) -> None:
  """
  Print a greeting for each name in the list.

  :params  names (Sequence[str]): A sequence of names to greet
  :return:  None
  """
  for name in names:
    print(f"Hello, {name}!")

def greet(names: Sequence[str]) -> None:
    name: str
    for name in names:
        print(f"Hello, {name}!")


a: Iterable[str] = iter(["Alice", "Bob", "Charlie"])
next(a)
next(a)
next(a)
# next(a)  # This would raise StopIteration

class Person:
  """Example person class with type annotations."""

  def __getattribute__(self, name) -> Any:
    pass


greet_func: Callable[[Sequence[str]], None] = greet


def block_user(request: Any) -> Any:
  """Block a user based on the request."""
  user_id: str = request.get("user_id", -1)
  user_ids: list[int | str | bool] = ["Temirbolat", 123, False, None, 456, "Alice", True]
  user = [user for user in user_ids if user == user_id][0]
  print("Blocked user:", user)
  return None


T = TypeVar('T')
T = TypeVar('T', bound=Model)  # inherits from Model

def print_values(values: List[T]) -> None:
  for value in values:
    print(value)


class MovieDict(TypedDict):
  """
  A dictionary representing a movie with its name and release year.
  """

  name: str
  year: int
  


movies: list[MovieDict] = [
  {"name": "Inception", "year": 2010}, 
  {"name": "The Matrix", "year": 1999}, 
  {"name": "Interstellar", "year": 2014},
  {"name": "The Godfather", "year": 1972},
]

class FindMovieResult(NamedTuple):
  """
  A named tuple representing the result of finding a movie.
  """
  movie: Optional[MovieDict]
  """current movie"""
  another_movie: Optional[MovieDict]
  """next movie"""
  found: bool
  """is found in movies"""


def find_movies_by_name(movies: List[MovieDict], name: str) -> FindMovieResult:
  """
  Find a movie by name in a list of movie dictionaries.

  :param movies: List of movie dictionaries.
  :param name: Name of the movie to find.
  :return: A tuple containing the movie dictionary if found, otherwise None, and a boolean indicating success.
  """
  for movie in movies:
    if movie.get("name") == name:
      return FindMovieResult(
        movie=movie, 
        another_movie=movie,
        found=True)
  return FindMovieResult(None, None, False)

result = find_movies_by_name(movies, "Inception").movie




def raise_exception() -> NoReturn:
  """Function that always raises an exception.(100%)"""
  raise Exception("This function always raises an exception")

def raise_exception(val: int) -> NoReturn: #invalid -> None
  """Function that always raises an exception.(100%)"""
  if val > 10:
    raise Exception("This function always raises an exception")