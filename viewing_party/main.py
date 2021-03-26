def create_movie(movie_title, genre, rating): 
    new_movie = {
                "title": movie_title,
                "genre": genre,
                "rating": rating         
                }
    for value in new_movie.values(): 
        # if genre is None: 
        #     import pdb; pdb.set_trace()
        if value == None:
            new_movie = None
        
    return new_movie

def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie): 
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]: 
        if movie["title"] == title: 
            user_data["watchlist"].remove(movie) 
            user_data["watched"].append(movie) 
    
    return user_data

def get_watched_avg_rating(user_data): 
    total_rating = 0.0
    average_rating = 0.0
    watched_movie_amount = 0

    for movie in user_data["watched"]: 
        total_rating += movie["rating"]
        watched_movie_amount += 1
    
    if watched_movie_amount > 0: 
        average_rating = total_rating / watched_movie_amount
    else: 
        average_rating == 0.0
    
    return average_rating

def get_most_watched_genre(user_data): 
    watched_genre_counts ={} 
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]: 
            if movie["genre"] not in watched_genre_counts: 
                watched_genre_counts[movie["genre"]] = 1 
            elif movie["genre"] in watched_genre_counts:
                watched_genre_counts[movie["genre"]] += 1
    else:
        popular_genre = None

    for genre, count in watched_genre_counts.items(): 
        if count == max(watched_genre_counts.values()):
            popular_genre = genre 
    
    return popular_genre

# get user watched movies
def get_user_most_watched(user_data): 
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
    return user_watched

# get friends watched movies 
def get_friends_most_watched(user_data): 
    friends_watched =[]
    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched.append(movie)
    
    return friends_watched

# calls get user watched movies and get friends watched movie, and return
# the movies that are watched by user but not their friends 
def get_unique_watched(user_data): 
    user_watched = get_user_most_watched(user_data)  
    friends_watched = get_friends_most_watched(user_data)
    unique_user_watched = []
    
    for movie in user_watched: 
        if movie not in friends_watched and movie not in unique_user_watched:
            unique_user_watched.append(movie)
    return unique_user_watched
    
def get_friends_unique_watched(user_data): 
    user_watched = get_user_most_watched(user_data)  
    friends_watched = get_friends_most_watched(user_data)
    unique_friends_watched = []
    
    for movie in friends_watched: 
        if movie not in user_watched and movie not in unique_friends_watched: 
            unique_friends_watched.append(movie)
    return unique_friends_watched

def get_available_recs(user_data): 
    unique_friends_watched = get_friends_unique_watched(user_data)
    movie_recs = []

    for movie in unique_friends_watched: 
        if movie["host"] in user_data["subscriptions"] and movie["title"] not in movie_recs: 
            movie_recs.append(movie) 
    
    return movie_recs

def get_new_rec_by_genre(user_data):
    unique_friends_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    movie_recs_by_genre =[]

    for movie in unique_friends_watched:
        if movie["genre"] is most_watched_genre and movie not in movie_recs_by_genre:
            movie_recs_by_genre.append(movie)
    
    return movie_recs_by_genre

def get_rec_from_favorites(user_data): 
    unique_user_watched = get_unique_watched(user_data)
    movie_recs_from_favorites = []

    for movie in user_data["favorites"]: 
        if movie in unique_user_watched and movie not in movie_recs_from_favorites: 
            movie_recs_from_favorites.append(movie)
    
    return movie_recs_from_favorites
    


    

