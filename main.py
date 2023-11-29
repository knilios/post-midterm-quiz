import data_processing as dp
import combination_gen as cg

def average(_list):
    return sum(_list) / len(_list)

reader = dp.CSV_reader()
movies_data = reader.read_data_from_file("movies.csv")
database = dp.DB()
movies_table = dp.Table("movies", movies_data)


funny_movies = movies_table.filter(lambda x: x["Genre"] == 'Comedy').select(['Worldwide Gross'])
avg_funny_gross = average([float(i["Worldwide Gross"]) for i in funny_movies])
print("Average comedy movies worldwide gross: ", avg_funny_gross)

drama_movies = movies_table.filter(lambda x: x["Genre"] == 'Drama').select(['Audience score %'])
min_drama_score = min([float(i["Audience score %"]) for i in drama_movies])
print("Minimum drama genre score: ", min_drama_score)

fantasy = movies_table.filter(lambda x: x["Genre"] == "Fantasy").select(["Film"])
count = 0
for i in fantasy:
    count =+ 1
print("Number of fantasy movies: ", count)

# insert movie
_dict = {}
_dict['Film'] = 'The Shape of Water'
_dict['Genre'] = 'Fantasy'
_dict['Lead Studio'] = 'Fox'
_dict['Audience score %'] = '72'
_dict['Profitability'] = '9.765'
_dict['Rotten Tomatoes %'] = '92'
_dict['Worldwide Gross'] = '195.3'
_dict['Year'] = '2017'

movies_table.insert_row(_dict)
print(movies_table)
