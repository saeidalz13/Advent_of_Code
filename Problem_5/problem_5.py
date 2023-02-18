import pandas as pd
import logging
from time import time

PATH_OUTPUT = r'output'
PATHNAME = r'input.txt'
PATHNAME_MOVE = r'move.csv'

# NOTE: Logger will overwrite the log.file


logger = logging.getLogger(__name__)
def initialize_logging(filename: str, logging_level=logging.DEBUG):

    logging.basicConfig(
                        filename=filename,
                        level=logging_level,
                        format= '%(asctime)s | %(name)s | %(funcName)s -->  %(message)s',
                        datefmt= '%Y-%m-%d %H:%M:%S %Z',
                        filemode='w',
                        )

    pass


def read_data_letters(
        pathname:str
            ):
   
    df = pd.read_csv(pathname, header=None)
    cols = []
    for i in range(1,10):
        cols.append(str(i))
    df.columns= cols
    for col in df:
        df[col]= df[col].values[::-1]
        df[col] = df[col].str.replace('[','', regex=True)
        df[col] = df[col].str.replace(']','', regex=True)

    return df


def read_moves(pathname):
    df = pd.read_csv(pathname, header=None)
    df = df[0].str.split(' ', n=-1, expand=True)
    df.columns = ['junk1','number','junk2','col_from','junk3','col_to']
    df = df.astype({'number': int, 'col_from': int, 'col_to':int})
    return df


def solve(df_letters, df_move):
    numbers = df_move.loc[:,'number']
    col_from = df_move.loc[:,'col_from']
    col_to = df_move.loc[:,'col_to']

    all_cols = list()
    for col in df_letters:
        ls =list(df_letters.loc[:,col])
        ls = [s.strip() for s in ls]
        all_cols.append(ls)


    crates = all_cols
    for n,ls in enumerate(crates):
        crates[n] = [s for s in ls if s]
 
    for _iter, (n, f, t) in (enumerate(zip(numbers, col_from, col_to), start=1)):
        col_fr_ls = crates[int(f)-1]
        col_to_ls = crates[int(t)-1]
        try:
            last_valid_idx_fr = max([index for index, item in enumerate(col_fr_ls) if item != ''])
            logger.info(f'Iteration No. {_iter}')
            logger.info(f'last non_empty index is {last_valid_idx_fr}')
        except Exception as e:
            logger.exception('ERROR! This list is empty, there is no non-empty string in it')
        else:

################################################ First Section ################################################
            # tt = col_fr_ls[last_valid_idx_fr+1-n: last_valid_idx_fr+1]
            # transfer= list(reversed(tt))            

################################################ Second Section ################################################
            transfer = col_fr_ls[last_valid_idx_fr+1-n: last_valid_idx_fr+1]
           
            col_to_ls.extend(transfer)
            col_fr_ls = col_fr_ls[:last_valid_idx_fr+1-n]
            crates[int(f)-1] = col_fr_ls
            crates[int(t)-1] = col_to_ls
            logger.info(f'from_col is {crates[int(f)-1]}')
            logger.info(f'to_col is {crates[int(t)-1]}')
            logger.info('Iteration complete! \n')
        


    final_list = list()
    for ls in crates:
        final_list.append(next(s for s in reversed(ls) if s))

    crates = pd.DataFrame(crates).T
    return numbers , transfer, crates, final_list


def write_output(
                    path_output,
                    final_list,
                    section,
                ):
    
    file = path_output + fr'/solutions_{section}.txt'
    with open(file, 'w') as f:
        f.write('==============================================================================\n\n')
        f.write('The solution, Section 1:\n')
        f.write('\n')
        f.write(f'--> {final_list}')

        pass


def main():
    START = time()
    LOG_FILE = PATH_OUTPUT + fr'/lists_2.log'
    initialize_logging(LOG_FILE)   
    DF_LETTERS = read_data_letters(PATHNAME)
    MOVE = read_moves(PATHNAME_MOVE)
    NUM, TRANSFER, BASE, FINAL_LIST = solve(DF_LETTERS, MOVE)

    write_output(
        path_output=PATH_OUTPUT,
        final_list=FINAL_LIST,
        section=2,
        )
    
    END = time()
    print(f'Elapsed time is: {END - START}')
    pass


if __name__ == '__main__': main()