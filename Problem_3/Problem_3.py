import pandas as pd
from string import ascii_lowercase
from string import ascii_uppercase
import string

PATH_OUTPUT = r'output'
PATHNAME = r'input.csv'

def read_data(
                pathname:str
                ):
    df = pd.read_csv(pathname, header=None)
    df.columns = ['text']
    return df

def split_half_first(string):
    l = len(string)
    half= int(l/2)
    return string[:half]

def split_half_sec(string):
    l = len(string)
    half= int(l/2)
    return string[half:]

def solve(df):
  

    ######################## First Section ########################
    df['first_half'] = None
    df['sec_half'] = None

    df['first_half'] = df['text'].apply(split_half_first)
    df['sec_half'] = df['text'].apply(split_half_sec)

    df['similar_letter'] = None
    for row in range(len(df)):
        first_ele = df.loc[row, 'first_half']
        sec_ele = df.loc[row, 'sec_half']
        df.loc[row, 'similar_letter'] = next(iter(set(first_ele).intersection(sec_ele)))

    df['upper_lower'] = df['similar_letter'].apply(lambda x: x.isupper())
    df['score'] = None
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)

    num_alp_low = range(1,27)
    num_alp_up = range(27,53)

    for n,l in zip(num_alp_low, lower):
        for row in range(len(df)):
            if df.loc[row, 'similar_letter'] == l:
                df.loc[row, 'score'] = n

    for n,l in zip(num_alp_up, upper):
        for row in range(len(df)):
            if df.loc[row, 'similar_letter'] == l:
                df.loc[row, 'score'] = n

    solution_1 = df.score.sum() 


    ######################## Second Section ########################
    df['similar_letter'] = None

    first_three = list()
    rg = [val for val in range(3,len(df)+1,3)]
    start = 0
    for val in rg:
        f3 = list(df.iloc[start :val, 0])
        first_three.append(f3)
        start += 3
        
    
    similar_letters = list()
    for ls in first_three:
        the_letter = next(iter(set.intersection(set(ls[0]), set(ls[1]) ,set(ls[2]))))
        similar_letters.append(the_letter)

    part2_df = pd.DataFrame(similar_letters, columns=['similar_letters'])


    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)

    num_alp_low = range(1,27)
    num_alp_up = range(27,53)

    for n,l in zip(num_alp_low, lower):
        for row in range(len(part2_df)):
            if part2_df.loc[row, 'similar_letters'] == l:
                part2_df.loc[row, 'score'] = n

    for n,l in zip(num_alp_up, upper):
        for row in range(len(part2_df)):
            if part2_df.loc[row, 'similar_letters'] == l:
                part2_df.loc[row, 'score'] = n

    solution_2 = part2_df.score.sum()
    return df, solution_1, solution_2, 
#
    
def main():
    DF = read_data(pathname=PATHNAME)
    _, SOLUTION_1, SOLUTION_2 = solve(df=DF)
    # print(DF_FINAL)
    print(f'The solution to the first section is: {SOLUTION_1}')
    print(f'The solution to the second section is: {SOLUTION_2}')

    pass


if __name__ == '__main__': main()