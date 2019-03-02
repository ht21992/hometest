class Movies:
    def __init__(self, name,production_year):
        self.name=name
        self.production_year=production_year
    def __str__(self):
        return self.name+":"+str(self.production_year)
    __repr__=__str__
def Grouping(movies):
    """it will make groups depend on each movie's production_year"""
    classic_movies=[]
    new_movies=[]
    for movie in movies:
        if movie.production_year<1990:
            classic_movies.append(movie)
        else:
            new_movies.append(movie)
    print("classic movies: "+str(classic_movies))
    print("new movies: "+str(new_movies))
movies=[Movies("Gone With The Wind",1939),Movies("Band of angels",1957),Movies("Green Book",2018),Movies("The Great Gatsby",2013)]
Grouping(movies)
