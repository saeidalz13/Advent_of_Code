import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

PATH_OUTPUT = 'output'
PATHNAME = r'output/input.txt'

def get_data():
    r = requests.get(r'https://adventofcode.com/2022/day/1/input')
    return r



def parse_data(
        r,
        path_output
        ):
    soup = BeautifulSoup(r.text, 'html.parser')
    with open(path_output + r'/input', 'w') as f:
        f.write(soup.text)
    pass

def read_data(
        pathname:str,
            ):
    with open(pathname, 'r') as f:
        content = f.readlines()
        df = pd.DataFrame(content)
        df = df.apply(lambda x: x.str.replace('\n',''))
        df.columns = ['values']
        df.fillna(np.nan,inplace=True)
        df[df['values'] == ''] = np.nan
        df['marker'] = None
    
        df = df.astype({'values': 'float32'})
        df.loc[df['values'].isna(), 'marker'] = 'checkpoint'

        idx = 0
        df['index'] = None
        for row in np.arange(len(df)):
            if df.loc[row, 'marker'] == 'checkpoint':
                idx += 1
            df.loc[row,'index'] = str(idx)
        
        df.loc[df['marker'] == 'checkpoint','index'] = str(9999)
        df.to_csv('DF.csv', header=True, index=False)
        grp = df.groupby(by = 'index').sum()
        grp.to_csv('GRP.csv', header=True, index=False)

        problem_1 = grp['values'].max()
        sorted_df = grp['values'].sort_values(ascending=False)

        problem_2 = sorted_df.iloc[0] + sorted_df.iloc[1] + sorted_df.iloc[2]
    return df, grp, problem_1, problem_2


def solve_problem():
    pass


def main():
    # R = get_data()
    # parse_data(R, path_output=PATH_OUTPUT)
    DF, GRP, PROBLEM_1, PROBLEM_2 = read_data(pathname=PATHNAME)
    print(DF.head(30))
    print(GRP)
    print(f'Solution to problem 1 is = {PROBLEM_1}')
    print(f'Solution to problem 2 is = {PROBLEM_2}')
    pass


if __name__ == '__main__': main()