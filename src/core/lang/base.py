from dataclasses import dataclass, field
from typing import List, Optional


# Core concept independent of language
@dataclass
class Concept:
    id: int
    pos: str
    concept_vector: Optional[List[float]] = field(default=None)

# Many-to-Many relationship mapping
@dataclass
class ConceptMapping:
    id: int
    concept_id: int
    lexicon_id: int

# Vocabulary for any language
@dataclass
class Lexicon:
    id: int
    lang_code: str
    word: str
    vector_embedding: Optional[List[float]] = field(default=None)

# Usage examples tied to specific context
@dataclass
class Example:
    id: int
    lang_code: str
    concept_mapping_id: int
    sentence: str