def obtener_tweets_autor(lista_tweets, autor):
    tweets_autor = []
    for tweet in lista_tweets:
        # if tweet["autor"].lower() = autor.lower(): <--- una sola "="
        if tweet["autor"].lower() == autor.lower():
            tweets_autor.append(tweet)
    return tweets_autor
