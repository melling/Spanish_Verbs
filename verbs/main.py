from PresentTenseRules import PresentTenseRules
from PreteriteTenseRules import PreteriteTenseRules
from ImperfectPastRules import ImperfectPastRules
from ConditionalTense import ConditionalTense
from FutureTense import FutureTense

pronouns = ["yo", "tú", "usted", "nosotros", "vosotros", "ustedes"]

# if __name__ == "__main__":
# print("Starting Main.py")
present_tense = PresentTenseRules()
preterite_tense = PreteriteTenseRules()
imperfect_past_tense = ImperfectPastRules()
conditional_tense = ConditionalTense()
future_tense = FutureTense()

regular_verbs = ["hablar", "vivir", "comer"]
# regular_verbs = ["hablar"]
# regular_verbs = ["vivir"]

for verb in regular_verbs:

    present_conj = present_tense.get_regular_conjugation(verb)
    # print("=== Present ===")
    # print(present_conj)

    preterite_conj = preterite_tense.get_regular_conjugation(verb)
    # print("=== Preterite ===")
    # print(preterite_conj)

    imperfect_past_conj = imperfect_past_tense.get_regular_conjugation(verb)
    # print("=== Imperfect Past ===")
    # print(imperfect_past_conj)

    conditional_conj = conditional_tense.get_regular_conjugation(verb)
    future_conj = future_tense.get_regular_conjugation(verb)
    verb_str = verb.center(40, " ")
    print(f"{verb_str}")
    print(f"Pronoun  Present, Preterite, Imperfect Past, Conditional, Future, ")
    for i in range(6):
        #        print(pronouns[i], ",", present_conj[i], ",", preterite_conj[i], ",",
        #              imperfect_past_conj[i], ",", conditional_conj[i], ",",
        #              future_conj[i])
        print(f"{pronouns[i]:9},{present_conj[i]}")
