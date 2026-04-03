from dataclasses import dataclass, field
from typing import Optional

from .base import ConceptMapping, Lexicon, Example

LANG_CODE = 'zh-tw'

@dataclass
class ConceptMappingForZHTW(ConceptMapping):
    pass

@dataclass
class LexiconForZHTW(Lexicon):
    lang_code: str = LANG_CODE
    pinyin: Optional[str] = field(default=None)
    zhuyin: Optional[str] = field(default=None)

@dataclass
class ExampleForZHTW(Example):
    lang_code: str = LANG_CODE