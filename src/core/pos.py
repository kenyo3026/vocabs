from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PartOfSpeechDatum:
    code: str
    en_name: str
    zh_name: str
    is_content_word: bool = True

@dataclass(frozen=True)
class PartOfSpeechForEN:
    NOUN      = PartOfSpeechDatum(code="n.", en_name="Noun", zh_name="名詞")
    VERB      = PartOfSpeechDatum(code="v.", en_name="Verb", zh_name="動詞")
    ADJECTIVE = PartOfSpeechDatum(code="adj.", en_name="Adjective", zh_name="形容詞")
    ADVERB    = PartOfSpeechDatum(code="adv.", en_name="Adverb", zh_name="副詞")
    PHRASE    = PartOfSpeechDatum(code="phr.", en_name="Phrase", zh_name="片語")

    PRONOUN      = PartOfSpeechDatum(code="pron.", en_name="Pronoun", zh_name="代名詞", is_content_word=False)
    PREPOSITION  = PartOfSpeechDatum(code="prep.", en_name="Preposition", zh_name="介係詞", is_content_word=False)
    CONJUNCTION  = PartOfSpeechDatum(code="conj.", en_name="Conjunction", zh_name="連接詞", is_content_word=False)
    DETERMINER   = PartOfSpeechDatum(code="det.", en_name="Determiner", zh_name="限定詞", is_content_word=False)
    INTERJECTION = PartOfSpeechDatum(code="intj.", en_name="Interjection", zh_name="感嘆詞", is_content_word=False)
    PREFIX       = PartOfSpeechDatum(code="pref.", en_name="Prefix", zh_name="字首", is_content_word=False)
    SUFFIX       = PartOfSpeechDatum(code="suff.", en_name="Suffix", zh_name="字尾", is_content_word=False)

    @classmethod
    def get_by_code(cls, code: str) -> Optional[PartOfSpeechDatum]:
        for _, value in vars(cls).items():
            if isinstance(value, PartOfSpeechDatum) and value.code == code:
                return value
        return None

    @classmethod
    def all_codes(cls) -> list[str]:
        return [
            value.code for key, value in vars(cls).items()
            if isinstance(value, PartOfSpeechDatum)
        ]