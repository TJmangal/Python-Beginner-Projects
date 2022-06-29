from Utility import MadLibLogic


def madlib():

    mad_lib = "Today I went to the zoo. I saw a(n) {} {} jumping up and down in its tree. He {} {} through the large \n" \
              "tunnel that led to its {} {}. I got some peanuts and passed them through the cage to a gigantic gray {}\n"\
              " towering above my head. Feeding that animal made me hungry. I went to get a {} scoop of ice cream. It \n"\
              "filled my stomach. Afterwards I had to {} {} to catch our bus. When I got home I {} my mom for a day at\n"\
              " the zoo.\n"

    prompts = ["adjective", "Noun", "verb, past tense", "adverb", "adjective", "noun", "noun", "adjective", "verb",
               "adverb", "verb, past tense", "adjective"]

    MadLibLogic.logic(prompts, mad_lib)
