import fresh_tomatoes
import media

toy_story= media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://www.imdb.com/title/tt0114709/mediaviewer/rm3813007616", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar= media.Movie("Avatar", "A marine on an alien Life", "http://www.imdb.com/title/tt0499549/mediaviewer/rm843615744", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print (avatar.storyline)
#avatar.show_trailer()
aynabaji= media.Movie("Aynabaji", "Ayna is an actor and the prison is his stage.", "http://www.thedailystar.net/sites/default/files/feature/images/aynabaji.jpg", "https://www.youtube.com/watch?v=eiV38JCtcss")
third_person_singular_number= media.Movie("Third Person Singular Number", "A woman breaks with traditional Muslim cultureen the relationship ends,", "C:\Users\Sayeef\Documents\Python\Movies\Third_Person_Singular_Number.jpg","https://www.youtube.com/watch?v=E2L1eXbo760&index=2&list=PLVdn2nTYb4iRaOtuIKNr9Ey3oAkqhQzU2")
oggyatonama= media.Movie("Oggyatonama", "The coffin of an expatriate worker with manipulated identity intense the identity crisis when another person's corpse is found inside", "https://images-na.ssl-images-amazon.com/images/M/MV5BNDU0MjViZmQtNzdmZS00YjhlLWE4ZGMtMDJlODAzMGI5ODIwXkEyXkFqcGdeQXVyNDI3NjcxMDA@._V1_.jpg", "https://www.youtube.com/watch?v=iZmcPGr9J2c")
shikari=media.Movie("Shikari", "A disguised professional assassin with mysterious past, tasked with assassinating a top government official.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjkzYzJlZmUtYzMzYy00ZjRmLTllZDgtYzdlNzA0YjdiMjg1XkEyXkFqcGdeQXVyNTA4NDgzNTU@._V1_.jpg", "https://www.youtube.com/watch?v=NSDTfsZXRJg")

movies= [toy_story, avatar, aynabaji,third_person_singular_number, oggyatonama, shikari]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
