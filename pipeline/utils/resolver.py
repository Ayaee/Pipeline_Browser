import glob


def get_cats(movie):
    """
    Return a list of entity for category
    """
    path_cats = "D:/ABYGAELLE_FABRE/MicroFilm_Browser/{movie}/ASSETS".format(movie=movie)
    files = glob.glob(path_cats + "/*")
    return files


if __name__ == '__main__':
    for file in get_cats("MOVIE"):
        print(file)