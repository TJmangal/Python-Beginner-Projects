from Utility import MadLibLogic


def madlib():

    mad_lib = 'it was a {}, cold November day. I woke up to the {} smell of {} roasting in the {} downstairs. I {} \n' \
              'down the stairs to see if I could help {} the dinner. My mom said, "See if {} needs a fresh {}." So I\n' \
              'carried a tray of glasses full of {} into the {} room. WHen I got there, I couldn\'t believe my {}!.\n' \
              'There were {} {} on the {}\n!'

    prompts = ["adjective", "adjective", "type of bird", "room in a house", "verb (past tense)", "verb",
               "relative's name", "noun", "a liquid", "verb ending in -ing", "part of body (plural)", "plural noun",
               "verb ending in -ing", "noun"]

    MadLibLogic.logic(prompts, mad_lib)
