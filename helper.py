
import numpy as np


def fetch_medal_tally(df, year, country):
    Medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = Medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = Medal_df[Medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = Medal_df[Medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = Medal_df[(Medal_df['Year'] == year) & (Medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return(x)
def Medal_tally(df):
    Medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    Medal_tally = Medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                             ascending=False).reset_index()

    Medal_tally['total'] = Medal_tally['Gold'] + Medal_tally['Silver'] + Medal_tally['Bronze']

    Medal_tally['Gold'] = Medal_tally['Gold'].astype('int')
    Medal_tally['Silver'] = Medal_tally['Silver'].astype('int')
    Medal_tally['Bronze'] = Medal_tally['Bronze'].astype('int')
    Medal_tally['total'] = Medal_tally['total'].astype('int')


    return Medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years, country

def data_over_time(df,col):

    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('index')
    nations_over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)
    return nations_over_time


