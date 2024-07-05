"""
7. Input and Output
https://docs.python.org/3/tutorial/inputoutput.html
also
https://docs.python.org/3/library/string.html#module-string
"""

def the7_1_1_Fancier_Output_Formatting():
    yes_votes = 42_572_654
    total_votes = 85_705_149
    percentage = yes_votes / total_votes
    print('{:-9} YES votes  {:2.3%}'.format(yes_votes, percentage))
    print('{:-19} YES votes  {:2.3}'.format(yes_votes, percentage))
    # ' 42572654 YES votes  49.67%'

# https://habr.com/ru/companies/wunderfund/articles/674866/
def fstrings():
    x = 10
    print(f"{x=:.3f}")

if __name__ == "__main__":
    # the7_1_1_Fancier_Output_Formatting()
    fstrings()