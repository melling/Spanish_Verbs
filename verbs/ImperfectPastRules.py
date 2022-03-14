from VerbConjugationRule import VerbConjugationRule
import Utils


class ImperfectPastRules:
    regular_ar_suffixes = ["aba", "abas", "aba", "ábamos", "abais", "aban"]
    imperfecto_er_ir_suffixes = ["ía", "ías", "ía", "íamos", "íais", "ían"]
    preterite_er_ir_suffixes = ["ía", "ías", "ía", "íamos", "íais", "ían"]

    verb_rule_msg = {
        "regular": "ImperfectPast Regular",
        "e->ie": "ImperfectPast Rule #2: e->ie, except nos/vos",
        "i->y": "ImperfectPast Rule #3: i->y, except nos/vos",
        "c->z(yo)": "ImperfectPast Rule #4: c->z(yo)",
        "g->j(yo)": "ImperfectPast Rule #5: g->j(yo)",
    }

    @staticmethod
    def conjugate(infinitive: str, suffixes: [str]):
        root = infinitive[:-2]
        conjugation = [root + suffix for suffix in suffixes]
        return conjugation

    def regular_ar(self, infinitive: str):
        conjugation = self.conjugate(infinitive, ImperfectPastRules.regular_ar_suffixes)
        return conjugation

    def regular_er(self, infinitive: str):
        conjugation = self.conjugate(
            infinitive, ImperfectPastRules.preterite_er_ir_suffixes
        )
        return conjugation

    def regular_ir(self, infinitive: str):
        conjugation = self.conjugate(
            infinitive, ImperfectPastRules.preterite_er_ir_suffixes
        )

        return conjugation

    def get_regular_conjugation(self, infinitive):

        if infinitive.endswith("ar"):
            conjugation = self.regular_ar(infinitive)

        elif infinitive.endswith("er"):
            conjugation = self.regular_er(infinitive)

        elif infinitive.endswith("ir"):
            conjugation = self.regular_ir(infinitive)

        else:
            print("unknown")
        return conjugation

    def show_regular(self, verb_rule: VerbConjugationRule):

        if verb_rule.infinitive.endswith("ar"):
            conjugation = self.regular_ar(verb_rule.infinitive)
            rule = "Regular -ar"

        elif verb_rule.infinitive.endswith("er"):
            conjugation = self.regular_er(verb_rule.infinitive)
            rule = "Regular -er"

        elif verb_rule.infinitive.endswith("ir"):
            conjugation = self.regular_ir(verb_rule.infinitive)
            rule = "Regular -ir"

        else:
            conjugation = []
            rule = "unknown"
            print("unknown")

        print(rule)
        print(conjugation)

    def __init__(self):
        print("starting PreteriteTenseRules...")


if __name__ == "__main__":
    print("Starting")
    vt = ImperfectPastRules()
    regular_verbs = ["hablar", "vivir", "comer"]
    for verb in regular_verbs:
        conj = vt.get_regular_conjugation(verb)
        print(conj)
    # vt.get_present_regular_conjugate("vivir")
