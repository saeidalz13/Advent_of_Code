import pandas as pd

PATH_OUTPUT = r'output'
PATHNAME = r'input.csv'


def read_data(
                pathname:str
                ):
    df = pd.read_csv(pathname, sep=' ', header=None)
    df.columns = ['opponent','mychoice']
    return df


def scores(df:pd.DataFrame):

    # A --> Rock
    # B --> Paper
    # C --> Scissors

    # X --> Rock 1
    # Y --> Paper 2
    # Z --> Scissors 3
    
    
    df['mychoice_score'] = None
    df['outcome'] = None
    df['finalscore'] = None

    df.loc[ df['opponent'] == 'A', 'opponent'] = 'rock'
    df.loc[ df['opponent'] == 'B', 'opponent'] = 'paper'
    df.loc[ df['opponent'] == 'C', 'opponent'] = 'sci'

    ######################## First Section ########################


    # df.loc[ df['mychoice'] == 'X', 'mychoice'] = 'rock'
    # df.loc[ df['mychoice'] == 'Y', 'mychoice'] = 'paper'
    # df.loc[ df['mychoice'] == 'Z', 'mychoice'] = 'sci'

    
    # df.loc[ df['mychoice'] == 'rock', 'mychoice_score'] = 1
    # df.loc[ df['mychoice'] == 'paper', 'mychoice_score'] = 2
    # df.loc[ df['mychoice'] == 'sci', 'mychoice_score'] = 3

    # # 3 is draw
    # df.loc[ df['mychoice'] == df['opponent'], 'outcome'] = 3

    # # 6 is win
    # df.loc[ (df['mychoice'] == 'rock' ) & (df['opponent'] == 'sci') , 'outcome'] = 6
    # df.loc[ (df['mychoice'] == 'sci' ) & (df['opponent'] == 'paper') , 'outcome'] = 6
    # df.loc[ (df['mychoice'] == 'paper' ) & (df['opponent'] == 'rock') , 'outcome'] = 6

    # # 0 is lost
    # df.loc[ (df['mychoice'] == 'sci') & (df['opponent'] == 'rock') , 'outcome'] = 0
    # df.loc[ (df['mychoice'] == 'paper') & (df['opponent'] == 'sci') , 'outcome'] = 0
    # df.loc[ (df['mychoice'] == 'rock') & (df['opponent'] == 'paper') , 'outcome'] = 0


    ######################## Second Section ########################

    df.loc[ df['mychoice'] == 'X', 'outcome'] = 0
    df.loc[ df['mychoice'] == 'Y', 'outcome'] = 3
    df.loc[ df['mychoice'] == 'Z', 'outcome'] = 6

    df.loc[:,'mychoice'] = None
    df.loc[df['outcome'] == 3 , 'mychoice'] = df['opponent']

    df.loc[ (df['outcome'] == 6) & (df['opponent'] == 'rock') , 'mychoice'] = 'paper'
    df.loc[ (df['outcome'] == 6) & (df['opponent'] == 'paper') , 'mychoice'] = 'sci'
    df.loc[ (df['outcome'] == 6) & (df['opponent'] == 'sci') , 'mychoice'] = 'rock'

    df.loc[ (df['outcome'] == 0) & (df['opponent'] == 'rock') , 'mychoice'] = 'sci'
    df.loc[ (df['outcome'] == 0) & (df['opponent'] == 'paper') , 'mychoice'] = 'rock'
    df.loc[ (df['outcome'] == 0) & (df['opponent'] == 'sci') , 'mychoice'] = 'paper'

    df.loc[ df['mychoice'] == 'rock', 'mychoice_score'] = 1
    df.loc[ df['mychoice'] == 'paper', 'mychoice_score'] = 2
    df.loc[ df['mychoice'] == 'sci', 'mychoice_score'] = 3

    df['finalscore'] = df['mychoice_score'] + df['outcome']
    final_sol = df['finalscore'].sum()

    return df, final_sol
  

def main():
    DF = read_data(pathname=PATHNAME)
    DF_FINAL, FINAL_SOL = scores(df=DF)
    # print(DF_FINAL)
    print(f'The final solution is: {FINAL_SOL}')
    pass


if __name__ == '__main__': main()