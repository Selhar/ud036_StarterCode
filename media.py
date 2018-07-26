# -*- coding: utf-8 -*-


class Movie():
    "Classe para definição da estrutura de um filme"

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
