################### User Config ###################
# Choose which section to be solved (Choice of 1 or 2)
SECTION = 1

# NOTE: Logger will overwrite the log.file
###################################################

import logging
import itertools
from typing import List, NoReturn, Dict

PATH_OUTPUT = r'output'
PATHNAME_CRATE = r'input.txt'
PATHNAME_MOVE = r'move.csv'

logger = logging.getLogger(__name__)




def initialize_logging(filename: str, logging_level=logging.DEBUG) -> NoReturn:
    """
    Initialzing the logger
    """
    logging.basicConfig(
                            filename=filename,
                            level=logging_level,
                            format= '%(asctime)s | %(name)s | %(funcName)s -->  %(message)s',
                            datefmt= '%Y-%m-%d %H:%M:%S %Z',
                            filemode='w',
                        )
    pass


def read_crates(pathname:str) -> List[str]:
    """
    Reading in the input file for crates info
    """
    with open('input.txt', 'r') as f:
        crates = list(f.readlines())
    return crates


def edit_crates(crates:List[str]) -> List[List[str]]:
    """
    Editing the crates list elements
    1. Removing the brackets and char \n in the crates lists
    2. Transposing the parent list to have every slot of crates as a list
    """

    crates = [string.replace(']','').replace('[','').replace('\n','').replace(' ','').split(',') for string in crates]
    edited_crates = (list(map(list, itertools.zip_longest(*crates, fillvalue=None))))

    edited_crates = [list(reversed(ls)) for ls in edited_crates]
    return edited_crates
    


def read_moves(pathname:str) -> List[str]:
    """
    Reading in the required actions/moves input text file
    """
    with open(pathname, 'r') as f:
        moves = list(f.readlines())
    return moves



def edit_moves(moves:List[str]) -> Dict:
    """
    Putting the required actions dictated by the input file\
        into a dictionary with their corresponding keys

    This would help us to access the actions for each column/slot \
        of crates more easily
    """
    actions = dict()
    _moves = list()
    _from = list()
    _to = list()

    moves = list(map(lambda x: x.replace('\n','').replace(' ',',').split(','), moves))
    for action in moves:
        _moves.append(action[1])
        _from.append(action[3])
        _to.append(action[5])

    actions.update(
                    {
                        'moves':_moves,
                        'from':_from,
                        'to': _to
                    }
                    )
    return actions



def solve(
        crates: List[List[str]], 
        actions :Dict,
        which_section: int,
        ) -> List[str]:
    """
    Using the actions dictionary and crates list to solve the problem
    """
    for n, ls in enumerate(crates):
        ls_edited = [s for s in ls if s]
        crates[n] = ls_edited
    
    numbers_to_move = actions['moves']
    move_from = actions['from']
    move_to = actions['to']

    if which_section == 1:
        for i, (_n_to_move, _from, _to) in enumerate(zip(numbers_to_move, move_from, move_to), start=1):
            logger.info(f'Iteration No. {i}')

            col_fr_ls = crates[int(_from)-1]
            col_to_ls = crates[int(_to)-1]
            _n_to_move = int(_n_to_move)

            try:
                logger.info(f'from_col --> Initial state: {crates[int(_from)-1]}')
                logger.info(f'to_col --> Initial state: {crates[int(_to)-1]}')
                
                if col_fr_ls:
                    if _n_to_move +1 > len(col_fr_ls):
                        transfer = list(reversed(col_fr_ls))
                        col_fr_ls = []

                    else:
                        transfer = col_fr_ls[len(col_fr_ls) - _n_to_move:]
                        transfer = list(reversed(transfer))    
                        col_fr_ls = col_fr_ls[:len(col_fr_ls) - _n_to_move ]

                    col_to_ls.extend(transfer)

                    crates[int(_from)-1] = col_fr_ls
                    crates[int(_to)-1] = col_to_ls

                    logger.info(f'from_col --> Current state: {crates[int(_from)-1]}')
                    logger.info(f'to_col --> Current state: {crates[int(_to)-1]}')
                    logger.info('Iteration complete! \n')
                else:
                    pass
            except Exception as e:
                logger.exception('ERROR! This list is empty, there is no non-empty string in it')

    elif which_section == 2:
        for i, (_n_to_move, _from, _to) in enumerate(zip(numbers_to_move, move_from, move_to), start=1):
            logger.info(f'Iteration No. {i}')

            col_fr_ls = crates[int(_from)-1]
            col_to_ls = crates[int(_to)-1]
            _n_to_move = int(_n_to_move)

            try:
                logger.info(f'from_col --> Initial state: {crates[int(_from)-1]}')
                logger.info(f'to_col --> Initial state: {crates[int(_to)-1]}')
                
                if col_fr_ls:
                    if _n_to_move +1 > len(col_fr_ls):
                        transfer = col_fr_ls
                        col_fr_ls = []

                    else:                      
                        transfer = col_fr_ls[len(col_fr_ls) - _n_to_move:]
                        col_fr_ls = col_fr_ls[:len(col_fr_ls) - _n_to_move ]

                    col_to_ls.extend(transfer)

                    crates[int(_from)-1] = col_fr_ls
                    crates[int(_to)-1] = col_to_ls

                    logger.info(f'from_col --> Current state: {crates[int(_from)-1]}')
                    logger.info(f'to_col --> Current state: {crates[int(_to)-1]}')
                    logger.info('Iteration complete! \n')

                elif not col_fr_ls:
                    pass
            except Exception as e:
                logger.exception('ERROR! This list is empty, there is no non-empty string in it')

    solution = list()
    for ls in crates:
        solution.append(next(s for s in reversed(ls) if s))

    return solution



def write_output(
                    path_output: str,
                    solution: List[str],
                    section: int,
                ) -> NoReturn:
    
    file = path_output + fr'/solutions_{section}.txt'
    with open(file, 'w') as f:

        f.write(f'The solution, Section {section}:\n')
        f.write('\n')
        f.write(f'{solution}')
        pass


def main():

    LOG_FILE = PATH_OUTPUT + fr'/lists_{SECTION}.log'
    initialize_logging(LOG_FILE)  

    CRATES_RAW = read_crates(PATHNAME_CRATE)
    CRATES = edit_crates(CRATES_RAW)
    MOVES_RAW = read_moves(PATHNAME_MOVE)
    MOVES = edit_moves(MOVES_RAW)
    SOLUTION = solve(CRATES, MOVES, SECTION)
    
    write_output(
        path_output=PATH_OUTPUT,
        solution=SOLUTION,
        section=SECTION,
        )
    
    pass



if __name__ == '__main__': main()