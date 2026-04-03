from dataclasses import dataclass, field
from typing import Optional

from .base import ConceptMapping, Lexicon, Example

LANG_CODE = 'en'

@dataclass
class ConceptMappingForEN(ConceptMapping):
    pass

@dataclass
class LexiconForEN(Lexicon):
    lang_code: str = LANG_CODE
    pronunciation: Optional[str] = field(default=None)

@dataclass
class ExampleForEN(Example):
    lang_code: str = LANG_CODE