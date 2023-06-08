def Medal_tally(df):
    Medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    Medal_tally = Medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                             ascending=False).reset_index()

    Medal_tally['total'] = Medal_tally['Gold'] + Medal_tally['Silver'] + Medal_tally['Bronze']

    return Medal_tally