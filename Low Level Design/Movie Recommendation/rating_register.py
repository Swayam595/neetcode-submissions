from user import User
from movie import Movie
from movie_rating import MovieRating
from uuid import UUID

class RatingRegister:
    def __init__(self):
        self.__user_movies: dict[UUID, list[Movie]] = dict()
        self.__movie_ratings: dict[UUID, dict[UUID, MovieRating]] = dict()

        self.__movies: list[Movie] = list()
        self.__users: list[User]  = list()

    def add_rating(self, user: User, movie: Movie, rating: MovieRating) -> None:
        if movie.get_id() not in self.__movie_ratings:
            self.__movie_ratings[movie.get_id()] = dict()
            self.__movies.append(movie)

        if user.get_id() not in self.__user_movies:
            self.__user_movies[user.get_id()] = list()
            self.__users.append(user)

        self.__user_movies[user.get_id()].append(movie)
        self.__movie_ratings[movie.get_id()][user.get_id()] = rating

    def get_average_rating(self, movie: Movie) -> float:
        if movie.get_id() not in self.__movie_ratings:
            return MovieRating.NOT_RATED.value

        ratings = self.__movie_ratings[movie.get_id()].values()
        ratings_values = [rating.value for rating in ratings]

        return sum(ratings_values) / len(ratings)

    def get_users(self) -> list[User]:
        return self.__users

    def get_movies(self) -> list[Movie]:
        return self.__movies

    def get_user_movies(self, user: User) -> list[Movie]:
        return self.__user_movies.get(user.get_id(), list())

    def get_movie_ratings(self, movie: Movie) -> dict[UUID, dict[UUID, MovieRating]]:
        return self.__movie_ratings.get(movie.get_id(), dict())