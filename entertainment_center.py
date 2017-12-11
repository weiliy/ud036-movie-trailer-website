# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# The movies
wonder_woman = media.Movie(
    'Wonder Woman',
    'https://cdn.traileraddict.com/content/'
    'warner-bros-pictures/wonder-woman-2017-5.jpg',
    'https://www.youtube.com/watch?v=ERvxrgUGK8A'
)

deadpoll_2 = media.Movie(
    'Deadpool 2',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BZTY1ZDllMTgtMzc2My00'
    'Y2Y1LTg1MzktYWJhZGM3Yjk2OWRiXkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_.jpg',
    'https://www.youtube.com/watch?v=gKR7O5B9qqg'
)

spider_man = media.Movie(
    'Spider-Man: Homecoming',
    'http://vignette1.wikia.nocookie.net/marvelcinematicuniverse/images/4/'
    '4e/Smh.png/revision/latest?cb=20161007215022',
    'https://www.youtube.com/watch?v=n9DwoQ7HWvI'
)

alien_covenant = media.Movie(
    'Alien: Covenant',
    'http://t3.gstatic.com/images?q=tbn:ANd9GcSHQJaXWT-hsnhTsBkpYGK-'
    'gJjZGEFuXhiemZ6nlsfaG0MU9Bdh',
    'https://www.youtube.com/watch?v=u5KPP6lxRVg'
)

despicable_me_3 = media.Movie(
    'Despicable Me 3',
    'http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700'
    'jNW_GTAd-e9DAV_QIWvMYq8v3mVx',
    'https://www.youtube.com/watch?v=Rlq39IC07qA'
)

the_dark_tower = media.Movie(
    'The Dark Tower',
    'http://t2.gstatic.com/images?q=tbn:ANd9GcS0LamXndyvB7CS6sJNF8no'
    'royqryzLYVACZ7KdBxYNKb0mpr_i',
    'https://www.youtube.com/watch?v=r4bXsOK6JKo'
)

# Show those movies
fresh_tomatoes.open_movies_page([
    wonder_woman,
    deadpoll_2,
    alien_covenant,
    despicable_me_3,
    the_dark_tower,
])
