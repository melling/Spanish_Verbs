# from enum import Enum
# from typing import Dict, List, Tuple

from VerbTense import VerbTense
# import VerbRule
from PresentTenseRules import PresentTenseRules
from VerbConjugationRule import VerbConjugationRule
# import VerbConjugation

# import string
# from VerbLoader import load_all_verb_rules
import VerbLoader

# fname = "verbs.csv"

# names: List[str] = ["Guido", "Jukka", "Ivan"]
# version: Tuple[int, int, int] = (3, 7, 1)
# options: Dict[str, bool] = {"centered": False, "capitalize": True}


def print_conj(verb_rule: VerbConjugationRule, verb_tense: VerbTense):
  print("v={} T={}".format(verb_rule.infinitive, verb_tense))


if __name__ == "__main__":
  print("Starting present_conj.py")

  verbs = VerbLoader.load_all_verb_rules("verbs.csv")
  vt = PresentTenseRules()
  for rule in verbs:
    # print("rule 1 must be ar verbs")
    # print_conj(rule, 1)
    vt.show_present_tense(rule)
# print(rule.infinitive)

# PresentTenseRules.present_regular_ar("hablar")
# print(verbs)
"""
hablar = present_regular_ar("hablar")
print("{}".format(hablar))
vrule = VerbConjugationRule("hablar", 1, 0, 0)
vrule2 = VerbConjugationRule("comer", 1, 0, 0)
#vrule.getPresentConj()

v1 = VerbConjugation("hablar", VerbTense.present, "hablo", "hablo", "hablo", "hablo", "hablo", "hablo")
# print(v1)	
"""

