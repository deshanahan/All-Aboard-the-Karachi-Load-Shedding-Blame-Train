# Modules we will need
import config
import datetime as DT
import twitter
import pandas as pd
import numpy as np

# Pulling credentials for python-twitter API
api = twitter.Api(consumer_key = config.api_key, consumer_secret = config.api_key_secret, access_token_key = config.access_token, access_token_secret = config.access_secret)

# Create variables that use datetime module to find today and one week ago
today = DT.date.today()
week_ago = today - DT.timedelta(days = 7)

# The search criteria we will need for all raw_query GetSearch twitter pulls
static_search = 'q=load shedding karachi'

# Create a list of all blamed entities in our program
blamed_list = ['Karachi Electric', 'Imran Khan', 'Asad Umar', 'NEPRA', 'Sui Gas', 'Naeem Rehman', 'Omar Ayub Khan', 'Tehreeki Insaaf']

# Set up the functions that we will need.

def name_setter(search):
    '''Returns set of twitter usernames who tweeted specified search criteria using GetSearch raw_query.  Contains no duplicates.'''
    name_set = {tweet.user.screen_name for tweet in search}
    return name_set

def name_set_length_lister(name_set_list):
    '''Returns a list of the lengths of a passed iterable.'''
    name_set_length_list = [len(name_set) for name_set in name_set_list]
    return name_set_length_list

def name_mbr_test(name_set_list, names):
    '''Returns dictionary of membership tests between two iterables.'''
    name_dict = {}
    for name in names:
        if name in name_set_list:
            name_dict[name] = True
        else:
            name_dict[name] = False
    return name_dict

# Search criteria for Karachi load shedding.

ke_search = api.GetSearch(raw_query = f'{static_search} #KE until%3A{today} since%3A{week_ago}&count=100')
KElectricPk_search = api.GetSearch(raw_query = f'{static_search} %40KElectricPk until%3A{today} since%3A{week_ago}&count=100')
imran_khan_search = api.GetSearch(raw_query = f'{static_search} %40ImranKhanPTI until%3A{today} since%3A{week_ago}&count=100')
asad_umar_search = api.GetSearch(raw_query = f'{static_search} %40Asad_Umar until%3A{today} since%3A{week_ago}&count=100')
nepra_search = api.GetSearch(raw_query = f'{static_search} #NEPRA until%3A{today} since%3A{week_ago}&count=100')
sui_search = api.GetSearch(raw_query = f'{static_search} sui until%3A{today} since%3A{week_ago}&count=100')
naeem_rehman_search = api.GetSearch(raw_query = f'{static_search} %40NaeemRehmanEngr until%3A{today} since%3A{week_ago}&count=100')
omar_ayub_khan_search = api.GetSearch(raw_query = f'{static_search} %40OmarAyubKhan until%3A{today} since%3A{week_ago}&count=100')
PTI_government_search = api.GetSearch(raw_query = f'{static_search} #PTI_government until%3A{today} since%3A{week_ago}&count=100')

# Take twitter user names for all of the searches
ke_set = name_setter(ke_search)
KElectricPk_set = name_setter(KElectricPk_search)
karachi_electric_set = ke_set.union(KElectricPk_set)
imran_khan_set = name_setter(imran_khan_search)
asad_umar_set = name_setter(asad_umar_search)
nepra_set = name_setter(nepra_search)
sui_set = name_setter(sui_search)
naeem_rehman_set = name_setter(naeem_rehman_search)
omar_ayub_khan_set = name_setter(omar_ayub_khan_search)
PTI_set = name_setter(PTI_government_search)

# Initiate a list of sets
name_set_list = [karachi_electric_set, imran_khan_set, asad_umar_set, nepra_set, sui_set, naeem_rehman_set, omar_ayub_khan_set, PTI_set]

# Combine all sets from name_set_list and leave into one set
blamer_set = set.union(*name_set_list)

# Find the length of the name_set_list
name_set_lengths = name_set_length_lister(name_set_list)

# Create a dictionary of the blamed entities and the number of times each entity is blamed
blamed_dict = dict(zip(blamed_list, name_set_lengths))
print(blamed_dict)

# Turn the set into a list
blame_list = list(blamer_set)


# Membership tests for all name sets
karachi_electric_blame_test = name_mbr_test(list(karachi_electric_set), blame_list)
imran_khan_blame_test = name_mbr_test(list(imran_khan_set), blame_list)
asad_umar_blame_test = name_mbr_test(list(asad_umar_set), blame_list)
nepra_blame_test = name_mbr_test(list(nepra_set), blame_list)
sui_blame_test = name_mbr_test(list(sui_set), blame_list)
naeem_rehman_blame_test = name_mbr_test(list(naeem_rehman_set), blame_list)
omar_ayub_khan_blame_test = name_mbr_test(list(omar_ayub_khan_set), blame_list)
PTI_blame_test = name_mbr_test(list(PTI_set), blame_list)

# Make sure we are getting a dictionary back
print(type(karachi_electric_blame_test))

# Make a list of all blame tests
blame_test_list = [karachi_electric_blame_test, imran_khan_blame_test, asad_umar_blame_test,\
                   nepra_blame_test, sui_blame_test, naeem_rehman_blame_test, omar_ayub_khan_blame_test, PTI_blame_test]

# Create a dataframe out of the membership tests
karachi_ls_df = pd.DataFrame(blame_test_list, index = blamed_list)

# Set column names to Tweeter plus the column index
karachi_ls_df.columns = ['Tweeter' + str(x) for x in range(0, len(karachi_ls_df.columns))]
karachi_ls_df

# Take previous data stored in csv
karachi_load_shedding = pd.DataFrame(pd.read_csv('karachi_ls_tweeters'))
karachi_load_shedding = karachi_load_shedding.set_index('Unnamed: 0')
karachi_load_shedding.index.name = ''

second_kls_search = pd.DataFrame(pd.read_csv('karachi_ls.csv'))
second_kls_search = second_kls_search.set_index('Blamed')
second_kls_search.index.name = ''

karachi_load_shedding2 = pd.concat([karachi_load_shedding, second_kls_search], axis = 1)
karachi_load_shedding2 = karachi_load_shedding2.loc[:,~karachi_load_shedding2.columns.duplicated()]

# Combine the dataframes into one
frames = [karachi_ls_df, karachi_load_shedding2]
kls_df = pd.concat(frames, axis = 1)
kls_df.columns = ['Tweeter' + str(x) for x in range(0, len(kls_df.columns))]

# Turn True/False values into integers
kls_df = kls_df * 1

# Change index name
kls_df.index.name = 'Blamed'

kls_df