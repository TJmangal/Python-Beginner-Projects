from SampleMadlibs import MadLib1, MadLib2, MadLib3, MadLib4
from random import choice

if __name__ == "__main__":
    mad_lib = choice([MadLib1, MadLib2, MadLib3, MadLib4])
    mad_lib.madlib()
