########################## USER CONFIG ##########################
# Enter the number of section you want to be solved? (Choices of 1 or 2)
SECTION = 1
#################################################################

from time import time

PATH_OUTPUT = r'output'
PATHNAME = r'input.csv'
SCORES = {
            'rock':1,
            'paper':2,
            'sci':3
        }


def read_data_list(pathname):
    ls_opp = []
    ls_my_choice = []

    with open(pathname, 'r') as f:
        for line in f.readlines():
            ls_opp.append(line.split(' ')[0])
            ls_my_choice.append(line.split(' ')[1].replace('\n',''))

    return ls_opp, ls_my_choice


def set_initial_vars_first(opp, my_choice):
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
            choice_score.append(SCORES['rock'])
        elif element == 'Y':
            new_my_choice.append('paper')
            choice_score.append(SCORES['paper'])
        elif element == 'Z':
            new_my_choice.append('sci')
            choice_score.append(SCORES['sci'])

    return new_opp, new_my_choice, choice_score


def set_match_score_first(opp, choice):
    match_scores = []

    for _opp, _choice in zip(opp, choice):
        if _opp == _choice:
            match_scores.append(3)
        elif (_opp == 'rock' and _choice =='sci') or (_opp == 'paper' and _choice =='rock') or (_opp == 'sci' and _choice =='paper'):
            match_scores.append(0)
        elif (_opp == 'sci' and _choice =='rock') or (_opp == 'rock' and _choice =='paper') or (_opp == 'paper' and _choice =='sci'):
            match_scores.append(6)
    
    return match_scores



def set_initial_vars_second(opp, outcomes):
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


def identify_choice_second(opp, match_scores):
    choices = []

    choices_scores = []
    for _opp, _score in zip(opp,match_scores):
        if _score == 3:
            choices.append(_opp)
            choices_scores.append(SCORES[_opp])
        elif _score == 0 and _opp == 'rock':
            choices.append('sci')
            choices_scores.append(SCORES['sci'])
        elif _score == 0 and _opp == 'paper':
            choices.append('rock')
            choices_scores.append(SCORES['rock'])
        elif _score == 0 and _opp == 'sci':
            choices.append('paper')
            choices_scores.append(SCORES['paper'])

        elif _score == 6 and _opp == 'rock':
            choices.append('paper')
            choices_scores.append(SCORES['paper'])
        elif _score == 6 and _opp == 'paper':
            choices.append('sci')
            choices_scores.append(SCORES['sci'])
        elif _score == 6 and _opp == 'sci':
            choices.append('rock')
            choices_scores.append(SCORES['rock'])
    
    return choices_scores
        

def final_score(choice_scores, match_scores):
    m_score = sum(match_scores)
    ch_score = sum(choice_scores)
    final_score = m_score + ch_score

    return final_score



def main():
    S = time()

    if SECTION == 1:

        OPP, MY_CHOICE = read_data_list(PATHNAME)
        NEW_OPP, NEW_MY_CHOICE, CHOICE_SCORES = set_initial_vars_first(OPP, MY_CHOICE)
        MATCH_SCORES = set_match_score_first(NEW_OPP,NEW_MY_CHOICE)
        SOLUTION = final_score(CHOICE_SCORES,MATCH_SCORES)

    elif SECTION == 2:

        OPP, OUTCOMES = read_data_list(PATHNAME)
        NEW_OPP, MATCH_SCORES = set_initial_vars_second(OPP,OUTCOMES)
        CHOICE_SCORES = identify_choice_second(NEW_OPP, MATCH_SCORES)
        SOLUTION = final_score(CHOICE_SCORES, MATCH_SCORES)

    E = time()
    print(SOLUTION, f'TIME is: {E-S}')

    pass


if __name__ == '__main__': main()