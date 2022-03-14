from VerbConjugationRule import VerbConjugationRule
import Utils


class PreteriteTenseRules:
    preterite_ar_suffixes = ["é", "aste", "ó", "amos", "asteis", "aron"]
    preterite_er_ir_suffixes = ["í", "iste", "ió", "imos", "isteis", "ieron"]
    # preterite_ir_suffixes = ["o", "es", "e", "imos", "ís", "en"]

    verb_rule_msg = {
        "regular": "Preterite Regular",
        "e->ie": "Present Rule #2: e->ie, except nos/vos",
        "i->y": "Present Rule #3: i->y, except nos/vos",
        "c->z(yo)": "Present Rule #4: c->z(yo)",
        "g->j(yo)": "Present Rule #5: g->j(yo)",

    }

    @staticmethod
    def conjugate(infinitive: str, suffixes: [str]):
        root = infinitive[:-2]
        conj = [root + suffix for suffix in suffixes]
        return conj

    def regular_ar(self, infinitive: str):
        conj = self.conjugate(infinitive, PreteriteTenseRules.preterite_ar_suffixes)
        return conj

    def regular_er(self, infinitive: str):
        conj = self.conjugate(infinitive, PreteriteTenseRules.preterite_er_ir_suffixes)
        return conj

    def regular_ir(self, infinitive: str):
        conj = self.conjugate(infinitive, PreteriteTenseRules.preterite_er_ir_suffixes)

        return conj

    def get_regular_conjugation(self, infinitive):

        if infinitive.endswith("ar"):
            conj = self.regular_ar(infinitive)

        elif infinitive.endswith("er"):
            conj = self.regular_er(infinitive)

        elif infinitive.endswith("ir"):
            conj = self.regular_ir(infinitive)

        else:
            print("unknown")
        return conj

    def show_regular(self, verb_rule: VerbConjugationRule):

        if verb_rule.infinitive.endswith("ar"):
            conj = self.regular_ar(verb_rule.infinitive)
            rule = "Regular -ar"

        elif verb_rule.infinitive.endswith("er"):
            conj = self.regular_er(verb_rule.infinitive)
            rule = "Regular -er"

        elif verb_rule.infinitive.endswith("ir"):
            conj = self.regular_ir(verb_rule.infinitive)
            rule = "Regular -ir"

        else:
            conj = []
            rule = "unknown"
            print("unknown")

        print(rule)
        print(conj)

    def __init__(self):
        print("starting PreteriteTenseRules...")


if __name__ == "__main__":
    print("Starting")
    vt = PreteriteTenseRules()
    regular_verbs = ["hablar", "vivir", "comer"]
    for verb in regular_verbs:
        conj = vt.get_regular_conjugation(verb)
        print(conj)
    # vt.get_present_regular_conjugate("vivir")
