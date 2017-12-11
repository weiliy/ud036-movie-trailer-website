class Movie():
    """Create a Movie"""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Initialize self.
        Args:
            movie_title (str): the movie title
            poster_image (str): the movie pster image url
            trailer_youtube (str): the movie trailer's youtube url
	"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

