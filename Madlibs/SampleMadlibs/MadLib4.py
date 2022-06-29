from Utility import MadLibLogic


def madlib():

    mad_lib = 'After hiding the painting in his {} for two years, he grew {} and tried to sell it to a/an {} in \n' \
              'Florence, but was caught\n' \

    prompts = ["noun", "adjective", "noun"]

    MadLibLogic.logic(prompts, mad_lib)
