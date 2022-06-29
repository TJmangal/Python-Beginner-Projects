from Utility import MadLibLogic


def madlib():

    mad_lib = "The day I saw the Monkey King {} was one of the most interesting days of the year. After he did that,\n"\
              "the king played chess on his brother's {} and then combed his {} hair with a comb made out of old fish\n"\
              "bones. Later that same day, I saw the Monkey King dance {} in front of an audience of kangaroos and\n"\
              " wombats.\n"

    prompts = ["verb", "noun", "adjective", "adverb"]

    MadLibLogic.logic(prompts, mad_lib)


