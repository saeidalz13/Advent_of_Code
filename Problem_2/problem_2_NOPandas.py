########################## USER CONFIG ##########################
# Enter the number of section you want to be solved? (Choices of 1 or 2)
SECTION = 1
#################################################################

from typing import List


PATH_OUTPUT = r'output'
PATHNAME = r'input.csv'
SCORES_CHOICE = {
                    'rock': 1,
                    'paper': 2,
                    'sci': 3
                }
SCORES_OUTCOME = {
                    'win': 6,
                    'draw': 3,
                    'lost': 0,
                }


def read_data_list(pathname:str):
    """
    Reading in input text
    Putting the opponent choice and second column in different lists
    """

    ls_opp = []
    ls_my_choice = []

    with open(pathname, 'r') as f:
        for line in f.readlines():
            ls_opp.append(line.split(' ')[0])
            ls_my_choice.append(line.split(' ')[1].replace('\n',''))

    return ls_opp, ls_my_choice


def set_initial_vars_first(opp: List[str], my_choice:List[str]) -> tuple:
    """
    Prepare the variables for section 1 of the problem
    1. Change the encrypted elements in the input into human-readable elements \
        of rock, paper, scissors
    2. Creates a list of scores of our choices
    
    """
    new_opp = []
    new_my_choice = []
    choice_score = []

    for element in opp:

        if element == 'A':
            new_opp.append('rock')
        elif element == 'B':
            new_opp.append('paper')
        elif element == 'C':
            new_opp.append('sci')
    
    for element in my_choice:

        if element == 'X':
            new_my_choice.append('rock')
            choice_score.append(SCORES_CHOICE['rock'])
        elif element == 'Y':
            new_my_choice.append('paper')
            choice_score.append(SCORES_CHOICE['paper'])
        elif element == 'Z':
            new_my_choice.append('sci')
            choice_score.append(SCORES_CHOICE['sci'])

    return new_opp, new_my_choice, choice_score


def set_match_score_first(opp: List[str], choice: List[str]) -> List[int]:
    """
    Using the opponent choice and our choice list to identify \
    the outcome scores for the first section of the problem
    """
    match_scores = []

    for _opp, _choice in zip(opp, choice):
        if _opp == _choice:
            match_scores.append(SCORES_OUTCOME['draw'])
        elif (_opp == 'rock' and _choice =='sci') or (_opp == 'paper' and _choice =='rock') or (_opp == 'sci' and _choice =='paper'):
            match_scores.append(SCORES_OUTCOME['lost'])
        elif (_opp == 'sci' and _choice =='rock') or (_opp == 'rock' and _choice =='paper') or (_opp == 'paper' and _choice =='sci'):
            match_scores.append(SCORES_OUTCOME['win'])
    
    return match_scores



def set_initial_vars_second(opp: List[str], outcomes: List[str]) -> tuple:
    """
    Prepare the variables for section 2 of the problem
    1. Change the encrypted elements in the input into human-readable elements \
        of rock, paper, scissors
    2. Creates a list of scores of our choices
    """
    new_opp = []
    match_scores = []

    for element in opp:

        if element == 'A':
            new_opp.append('rock')
        elif element == 'B':
            new_opp.append('paper')
        elif element == 'C':
            new_opp.append('sci')

    for outcome in outcomes:

        if outcome == 'X':
            match_scores.append(0)
        elif outcome == 'Y':
            match_scores.append(3)
        elif outcome == 'Z':
            match_scores.append(6) 
    

    return new_opp, match_scores


def identify_choice_second(opp:List[str], match_scores: List[int]) -> List[int]:
    """
    Identify the scores of our choice for section 2 of the problem
    """
    choices = []

    choices_scores = []
    for _opp, _score in zip(opp,match_scores):
        if _score == SCORES_OUTCOME['draw']:
            choices.append(_opp)
            choices_scores.append(SCORES_CHOICE[_opp])
        elif _score == SCORES_OUTCOME['lost'] and _opp == 'rock':
            choices.append('sci')
            choices_scores.append(SCORES_CHOICE['sci'])
        elif _score == SCORES_OUTCOME['lost'] and _opp == 'paper':
            choices.append('rock')
            choices_scores.append(SCORES_CHOICE['rock'])
        elif _score == SCORES_OUTCOME['lost'] and _opp == 'sci':
            choices.append('paper')
            choices_scores.append(SCORES_CHOICE['paper'])

        elif _score == SCORES_OUTCOME['win'] and _opp == 'rock':
            choices.append('paper')
            choices_scores.append(SCORES_CHOICE['paper'])
        elif _score == SCORES_OUTCOME['win'] and _opp == 'paper':
            choices.append('sci')
            choices_scores.append(SCORES_CHOICE['sci'])
        elif _score == SCORES_OUTCOME['win'] and _opp == 'sci':
            choices.append('rock')
            choices_scores.append(SCORES_CHOICE['rock'])
    
    return choices_scores
        

def final_score(choice_scores: List[int], match_scores: List[int]) -> int:
    """
    Calculating the final score for either of the sections
    """
    m_score = sum(match_scores)
    ch_score = sum(choice_scores)
    final_score = m_score + ch_score

    return final_score



def main():

    if SECTION == 1:

        OPP, MY_CHOICE = read_data_list(PATHNAME)
        NEW_OPP, NEW_MY_CHOICE, CHOICE_SCORES = set_initial_vars_first(OPP, MY_CHOICE)
        MATCH_SCORES = set_match_score_first(NEW_OPP,NEW_MY_CHOICE)

    elif SECTION == 2:

        OPP, OUTCOMES = read_data_list(PATHNAME)
        NEW_OPP, MATCH_SCORES = set_initial_vars_second(OPP,OUTCOMES)
        CHOICE_SCORES = identify_choice_second(NEW_OPP, MATCH_SCORES)

    SOLUTION = final_score(CHOICE_SCORES, MATCH_SCORES)

    pass


if __name__ == '__main__': main()