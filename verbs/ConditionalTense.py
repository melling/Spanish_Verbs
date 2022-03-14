from VerbConjugationRule import VerbConjugationRule
# import Utils


class ConditionalTense:
    suffixes = ["ía", "ías", "ía", "íamos", "íais", "ían"]

    verb_rule_msg = {
        "regular": "Conditional Regular"
    }

    @staticmethod
    def conjugate(infinitive: str, suffixes: [str]):
        # root = infinitive[:-2]
        conjuagtion = [infinitive + suffix for suffix in suffixes]
        return conjuagtion

    def get_regular_conjugation(self, infinitive):
        conjuagtion = self.conjugate(infinitive, ConditionalTense.suffixes)
        return conjuagtion

    def show_regular(self, verb_rule: VerbConjugationRule):
        conjuagtion = self.get_regular_conjugation(verb_rule.infinitive)
        print(conjuagtion)

    def __init__(self):
        print("starting FutureTense...")


if __name__ == "__main__":
    print("Starting")
    vt = ConditionalTense()
    regular_verbs = ["hablar", "vivir", "comer"]
    for verb in regular_verbs:
        conj = vt.get_regular_conjugation(verb)
        print(conj)
    # vt.get_present_regular_conjugate("vivir")
    
