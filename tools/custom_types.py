from collections import defaultdict
from typing import Any, TypeAlias, TypedDict
from nltk import DependencyGraph


class ConlluDbRow(TypedDict):
    text: str
    tree: DependencyGraph


Node: TypeAlias = tuple[Any, dict[str, defaultdict[Any, list] | None]] | None
