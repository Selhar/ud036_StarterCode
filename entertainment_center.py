# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# Objetos com todos os filmes que serão exibidos na página
castaway_on_the_moon = media.Movie(
    "Castaway on the Moon",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Castaway_on_the_Moon_poster.jpg",
    "https://www.youtube.com/watch?v=QgQCnLag_AY"
)

enter_the_void = media.Movie(
    "Enter the Void",
    "https://upload.wikimedia.org/wikipedia/en/3/39/Enter-the-void-poster.png",
    "https://www.youtube.com/watch?v=_tG_b5zaT9Y"
)

fear_and_loathing = media.Movie(
    "Fear and Loathing in Las Vegas",
    "https://upload.wikimedia.org/wikipedia/en/6/6f/FandlinLV.jpg",
    "https://www.youtube.com/watch?v=8m662obIvhY"
)

filmes = [castaway_on_the_moon, fear_and_loathing, enter_the_void]
fresh_tomatoes.open_movies_page(filmes)
