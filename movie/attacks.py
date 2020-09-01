from movie.data import df_movies


def insert_random_attack(df, target_movie_id, attack_size=50, filler_size_percent=1, target_rate=5):
    timestamp = df[(df.MovieID == target_movie_id)].sort_values(by='Timestamp')['Timestamp'].median()
    mean_rate = df["Rating"].mean()
    # target rating
    last_user_id = df.loc[df['UserID'].idxmax()].UserID
    for i in range(attack_size):
        timestamp += 1000
        new_row = {'UserID': last_user_id + i,
                   'MovieID': target_movie_id,
                   'Rating': target_rate,
                   'Timestamp': timestamp}
        df = df.append(new_row, ignore_index=True)
        # random fill item rating
        df_random_movies = df_movies.sample(frac=0.01)
        movie_list = df_random_movies.Id.unique().tolist()
        for movie_id in movie_list:
            if movie_id == target_movie_id:
                continue
            new_row = {'UserID': last_user_id + i,
                       'MovieID': movie_id,
                       'Rating': int(mean_rate),
                       'Timestamp': timestamp}
            df = df.append(new_row, ignore_index=True)
    return df
