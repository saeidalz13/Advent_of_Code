import pandas as pd
import numpy as np

PATHNAME = r'input.txt'
PATH_OUTPUT = r'output'


def read_input(
                pathname:str,
                ):

    text = pd.read_csv(pathname, header=None)
    text.columns = ['text']
    return text

def analyze_data(df):
    df['directories'] = None
    df['files'] = None
    df['commands'] = None
    df['size']=None
    df['ls']=None
    df['command']=None
    df['all_dirs_checked']=None

    df.loc[ df['text'].str.contains('dir') ,'directories'] = df['text']
    df['directories'] = df['directories'].apply(lambda x: x.split(' ')[1] if pd.notnull(x) else x)

    df.loc[ df['text'].str.contains('\$ ls'),'ls'] = 'list_check'
    df.loc[ df['text'].str.contains('\$ cd'),'command'] = 'cd_check'
    
    idx = 0
    for row in range(len(df)):
        if df.loc[row, 'ls'] == 'list_check':
            idx += 1
        df.loc[row,'all_dirs_checked'] = str(idx)
    

    df.loc[ (~df['text'].str.contains('dir|cd|ls')) & (df['text'].str.contains('.')) ,'files'] = df['text']
    df['files'] = df['files'].apply(lambda x: x.split(' ')[1] if pd.notnull(x) else x)

    df.loc[ df['text'].str.contains('\$') , 'commands'] = df['text']
    df.loc[ df['text'].str.contains('1|2|3|4|5|6|7|8|9') ,'size'] = df['text']
    df['size'] = df['size'].apply(lambda x: x.split(' ')[0] if pd.notnull(x) else x)
    
    df['size'].fillna(np.nan, inplace=True)
    df['size'] = df['size'].astype('float')

    dirs = pd.unique(df['directories'])
    files = pd.unique(df['files'])
    size = pd.unique(df['size'])

    dirs = pd.DataFrame([dirs]).T
    dirs.dropna(inplace=True)
    dirs.columns = ['Dirs']

    files_size = pd.DataFrame([files, size]).T
    files_size.dropna(inplace=True)
    files_size.columns = ['Name','Size']

    lt_100000 = pd.DataFrame()
    grp= df.groupby(by = 'all_dirs_checked').sum()

    grp = grp[grp['size'] < 100_000].sum()

    parent_dirs = df.loc[df['all_dirs_checked'] == '1', 'directories']
    parent_dirs.dropna(inplace=True)
    parent_dirs.reset_index(drop=True, inplace = True)

    parent_dirs_ls = list(parent_dirs)

    df['parent_dirs'] = None
    df.loc[ (df['directories'].isin(parent_dirs_ls)) & ((df['all_dirs_checked'] != '0') | (df['all_dirs_checked'] != '1')),'parent_dirs'] = 'parent'

    return df, dirs, files_size, grp, parent_dirs_ls


def write_output(
    path_output,
    df,
        ):
    file = path_output + r'/MainDF.csv'
    df.to_csv(file, header =True, index = False)
    pass


def main():
    TEXT = read_input(pathname=PATHNAME)
    DF, DIRS, FILES_SIZE, GRP, PARENT_DIRS = analyze_data(TEXT)
    print(DF.head(30))
    # print(GRP)
    # print(DIRS)
    # print(FILES_SIZE)
    print(PARENT_DIRS)
    # write_output(
    #     path_output=PATH_OUTPUT,
    #     df= DF
    # )
    pass


if __name__ == '__main__': main()