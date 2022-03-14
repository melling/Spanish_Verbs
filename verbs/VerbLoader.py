from VerbConjugationRule import VerbConjugationRule


def load_verbs(file_name):
    with open(file_name) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content


# TODO: Remove
def load_all_verbs000(file_name):
    verb_list = load_verbs(file_name)
    print(verb_list)
    for verb in verb_list:
        # print(verb)
        v = verb.split(",")
        print("{} {}".format(v[0], v[1]))


def load_all_verb_rules(fname):
    verb_list = load_verbs(fname)
    print(verb_list)
    verb_rules = []
    for verb in verb_list:
        if not verb.startswith("#"):
            # print(verb)
            v = verb.split(",")
            infinitive = v[0]
            present_rule = v[1]
            preterite_rule = v[2]
            imperfecto_rule = v[3]
            print("{}, present={}, preterite={}".format(infinitive, present_rule,
                                                        preterite_rule))
            vrule = VerbConjugationRule(infinitive, present_rule, preterite_rule,
                                        imperfecto_rule)
            verb_rules.append(vrule)
    # print(v)
    return verb_rules


print("Starting VerbLoader")
