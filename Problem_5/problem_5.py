import pandas as pd
import logging
from tqdm import tqdm

PATH_OUTPUT = r'output'
PATHNAME = r'input.txt'
PATHNAME_MOVE = r'move.csv'



logger = logging.getLogger(__name__)
def initialize_logging(filename: str, logging_level=logging.DEBUG):

    logging.basicConfig(
                        filename=filename,
                        level=logging_level,
                        format= '%(asctime)s | %(name)s | %(funcName)s -->  %(message)s',
                        datefmt= '%Y-%m-%d %H:%M:%S %Z'
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


    base = all_cols
    for n,ls in enumerate(base):
        base[n] = [s for s in ls if s]
 
    for _iter, (n, f, t) in tqdm(enumerate(zip(numbers, col_from, col_to), start=1), total = len(numbers)):
        col_fr_ls = base[int(f)-1]
        col_to_ls = base[int(t)-1]
        try:
            last_valid_idx_fr = max([index for index, item in enumerate(col_fr_ls) if item != ''])
            logger.debug(f'{_iter} last non_empty index is {last_valid_idx_fr}')
        except Exception as e:
            pass
            print(f'Error --> {e}')
        else:

################################################ First Section ################################################
            tt = col_fr_ls[last_valid_idx_fr+1-n: last_valid_idx_fr+1]
            transfer= list(reversed(tt))            

################################################ Second Section ################################################
            # transfer = col_fr_ls[last_valid_idx_fr+1-n: last_valid_idx_fr+1]
           
            col_to_ls.extend(transfer)
            col_fr_ls = col_fr_ls[:last_valid_idx_fr+1-n]
            base[int(f)-1] = col_fr_ls
            base[int(t)-1] = col_to_ls
            logger.debug(f'{_iter} from_col is{base[int(f)-1]}')
            logger.debug(f'{_iter} to_col is{base[int(t)-1]}')
        


    final_list = list()
    for ls in base:
        final_list.append(next(s for s in reversed(ls) if s))

    base = pd.DataFrame(base).T
    return numbers , transfer, base, final_list


def main():
    LOG_FILE = PATH_OUTPUT + fr'/lists.log'
    initialize_logging(LOG_FILE)   
    DF_LETTERS = read_data_letters(PATHNAME)
    MOVE = read_moves(PATHNAME_MOVE)
    NUM, TRANSFER, ALL_COLS, FINAL_LIST = solve(DF_LETTERS, MOVE)
    # print(list(_1[8]))

    print(TRANSFER)
    print(FINAL_LIST)
    print(ALL_COLS)
    # print(MOVE)
    # print(DF_LETTERS)
    pass


if __name__ == '__main__': main()