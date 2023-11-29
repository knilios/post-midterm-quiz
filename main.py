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