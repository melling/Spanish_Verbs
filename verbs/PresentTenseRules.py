# from VerbConjugation import VerbConjugation
# from VerbTense import VerbTense
from VerbConjugationRule import VerbConjugationRule
import Utils


class PresentTenseRules:
    present_ar_suffixes = ["o", "as", "a", "amos", "áis", "an"]
    present_er_suffixes = ["o", "es", "e", "emos", "éis", "en"]
    present_ir_suffixes = ["o", "es", "e", "imos", "ís", "en"]

    verb_rule_msg = {
        "regular": "Present Regular",
        "e->ie": "Present Rule #2: e->ie, except nos/vos",
        "i->y": "Present Rule #3: i->y, except nos/vos",
        "c->z(yo)": "Present Rule #4: c->z(yo)",
        "g->j(yo)": "Present Rule #5: g->j(yo)",
        "u->ú": "Present Rule #6: u->ú, except nos/vos",
        "o->ue": "Present Rule #7: o->ue, except nos/vos",
        "gu->g(yo)": "Present Rule #8: gu->g(yo)",
        "e->i": "Present Rule #9: e->i, except nos/vos",
        "quepo(yo)": "Present Rule #10: quepo(yo)",
        "cir/cer->zc(yo)": "Present Rule #11: cir/cer->zc(yo)",
        "i->í": "Present Rule #12: tilde on í, except nos/vos",
        "gu->g(yo);e->i": "Present Rule #13: gu->g(yo) and e->i except nos/vos",
        "o->hue": "Present Rule #14: o->hue, except nos/vos"
    }

    @staticmethod
    def conjugate(infinitive: str, suffixes: [str]):
        root = infinitive[:-2]
        conj = [root + suffix for suffix in suffixes]
        return conj

    def regular_with_sub_in_yo(self, infinitive, letter: str, replacement: str):
        # assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.get_present_regular_conjugation(infinitive)
        yo = conj[0]
        conj[0] = Utils.rreplace(yo, letter, replacement, 1)
        return conj

    # Rule 2: e -> ie, except nosotros/vosotros
    # root1 - adjusted root
    # root2 - original root nos/vos

    @staticmethod
    def two_roots_ar(infinitive: str, root1: str, root2: str, ending: str):
        yo = root1 + "o"
        tu = root1 + "as"
        ud = root1 + "a"
        nos = root2 + "amos"
        vos = root2 + "áis"
        uds = root1 + "an"

        return [yo, tu, ud, nos, vos, uds]

    @staticmethod
    def two_roots_er(infinitive: str,
                     root1: str,
                     root2: str,
                     ending: str):
        yo = root1 + "o"
        tu = root1 + "es"
        ud = root1 + "e"
        nos = root2 + "emos"
        vos = root2 + "éis"
        uds = root1 + "en"

        return [yo, tu, ud, nos, vos, uds]

    @staticmethod
    def two_roots_ir(infinitive: str,
                     root1: str,
                     root2: str,
                     ending: str):
        yo = root1 + "o"
        tu = root1 + "es"
        ud = root1 + "e"
        nos = root2 + "imos"
        vos = root2 + "ís"
        uds = root1 + "en"

        return [yo, tu, ud, nos, vos, uds]

    # ========
    # Rule 3: i -> y, except nosotros/vosotros
    # Example verbs: concluir, construir, contribuir
    #
    # Precondition(Must be ir verb)

    @staticmethod
    def i2y(infinitive):
        assert infinitive[-2:] == "ir", "Must be -ir verb"
        root = infinitive[:-2]
        yo = root + "y" + "o"
        tu = root + "y" + "es"
        ud = root + "y" + "e"
        nos = root + "imos"
        vos = root + "ís"
        uds = root + "y" + "en"

        return [yo, tu, ud, nos, vos, uds]

    # ========
    # Rule 4: c->z(yo)
    # Example verbs: convencer, ejercer, vencer
    #
    # Precondition(Must be er verb?)

    def c2z_yo(self, infinitive):
        assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.regular_er(infinitive)
        yo = conj[0]
        conj[0] = Utils.rreplace(yo, "c", "z", 1)
        return conj

    # ========

    # Rule 5: g->j(yo)
    # Example verbs: acoger, coger, corregir, dirigir

    def g2j_yo(self, infinitive):
        # assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.get_regular_conjugation(infinitive)
        yo = conj[0]
        conj[0] = Utils.rreplace(yo, "g", "j", 1)
        return conj

    # Rule 6: u->ú, except nosotros/vosotros
    # Example verbs: acentuar, actuar, continuar

    def u2ú(self, infinitive):
        # assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.get_regular_conjugation(infinitive)
        yo = conj[0]
        conj[0] = Utils.rreplace(yo, "u", "ú", 1)
        return conj

    # Rule 7: u->ú, except nosotros/vosotros
    # Example verbs:

    def o2ue(self, infinitive):
        # assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.get_regular_conjugation(infinitive)
        yo = conj[0]
        conj[0] = Utils.rreplace(yo, "o", "ue", 1)
        return conj

    # gu->g(yo)
    # Rule 8: u->ú, except nosotros/vosotros
    # Example verbs:

    def gu2g_yo(self, infinitive):
        # assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.get_regular_conjugation(infinitive)
        yo = conj[0]
        conj[0] = Utils.rreplace(yo, "gu", "g", 1)
        return conj

    # Rule 10: u->ú, except nosotros/vosotros
    # Example verbs:

    def quepo_yo(self, infinitive):
        # assert infinitive[-2:] == "er", "Must be -er verb"
        conj = self.get_regular_conjugation(infinitive)
        # yo = conj[0]
        conj[0] = "quepo"  # Utils.rreplace(yo, "gu", "g", 1)
        return conj

    # =======
    #
    # 7: "Present Rule #7: o->ue",
    # 	8: "Present Rule #8: gu->g(yo)",
    # 	9: "Present Rule #9: e->i",
    # 	10: "Present Rule #10: quepo(yo)",
    # 	11: "Present Rule #11: cir/cer->zc(yo)",
    # 	12: "Present Rule #12: tilde on í, except nos/vos",
    # 	13: "Present Rule #13: gu->g(yo) and e->i except nos/vos",
    # 	14: "Present Rule #14: o->hue, except nos/vos"

    def regular_ar(self, infinitive: str):
        # root = infinitive[:-2]
        # yo = root + "o"
        # tu = root + "as"
        # ud = root + "a"
        # nos = root + "amos"
        # vos = root + "áis"
        # uds = root + "an"
        conj = self.conjugate(infinitive, PresentTenseRules.present_ar_suffixes)
        # print(conj0)
        # conj = VerbConjugation(infinitive, VerbTense.present, conj0)
        # [yo, tu, ud, nos, vos,uds])
        return conj

    def regular_er(self, infinitive: str):
        # root = infinitive[:-2]
        # yo = root + "o"
        # tu = root + "es"
        # ud = root + "e"
        # nos = root + "emos"
        # vos = root + "éis"
        # uds = root + "en"
        conj = self.conjugate(infinitive, PresentTenseRules.present_er_suffixes)
        # conj = VerbConjugation(infinitive, VerbTense.present, conj0)
        # [yo, tu, ud, nos, vos, uds])
        return conj

    def regular_ir(self, infinitive: str):
        conj = self.conjugate(infinitive, PresentTenseRules.present_ir_suffixes)
        # conj = VerbConjugation(infinitive, VerbTense.present, conj0)
        # [yo, tu, ud, nos, vos, uds])
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

    def show_present_regular(self, verb_rule: VerbConjugationRule):

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

    def show_present_tense(self, verb_rule: VerbConjugationRule):
        infinitive = verb_rule.infinitive
        print(f"=== {verb_rule.infinitive} ===")

        if verb_rule.present == 1:
            conj = self.show_present_regular(verb_rule.infinitive)

        elif verb_rule.present == 2:
            print("Present Rule #2: e -> ie")
            root = verb_rule.infinitive[:-2]
            ending = verb_rule.infinitive[-2:]
            root2 = Utils.rreplace(root, "e", "ie", 1)
            # v2 = root2 + ending
            if ending == "ar":
                conj = self.two_roots_ar(infinitive, root2, root, ending)

            elif ending == "er":
                conj = self.two_roots_er(infinitive, root2, root, ending)

            elif ending == "ir":
                conj = self.two_roots_ir(infinitive, root2, root, ending)
            else:
                print("ERROR")
                conj = []

        elif verb_rule.present == 3:
            print("Present Rule #3: i->y")
            # print("{} + {} / {} / {}".format(root, ending, root2, v2))
            conj = self.i2y(infinitive)

        elif verb_rule.present == 4:
            conj = self.c2z_yo(infinitive)

        elif verb_rule.present == 5:
            conj = self.g2j_yo(infinitive)

        elif verb_rule.present == 6:
            conj = self.u2ú(infinitive)

        elif verb_rule.present == 7:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 8:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 9:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 10:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 11:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 12:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 13:

            conj = self.u2ú(infinitive)

        elif verb_rule.present == 14:

            conj = self.u2ú(infinitive)
        else:
            print("ERROR: No rule: {}".format(verb_rule.present))
            conj = []

        msg = PresentTenseRules.verb_rule_msg.get(verb_rule.present, "No rule")
        print(msg)
        print(conj)

    def __init__(self):
        print("init'ing' PresentTenseRules...")


if __name__ == "__main__":
    print("Starting PresentTenseRules.py")
    vt = PresentTenseRules()
    regular_verbs = ["hablar", "vivir", "comer"]
    for verb in regular_verbs:
        conj = vt.get_regular_conjugation(verb)
        print(conj)
