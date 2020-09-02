import seaborn as sns
from movie.attacks import insert_random_attack
from movie.data import df_ratings
from movie.utils import get_optimal_chunk_size, get_sample_entropy_list, \
    get_sample_average_list, z_score_entropy_plot, optimum_chunk_size

df = df_ratings
attack_size = 100
target_movie_id = 70
df_target_movie = df[(df.MovieID == target_movie_id)]
new_df = insert_random_attack(df, target_movie_id, attack_size)
sns.countplot(x='Rating', data=df_target_movie)
df_attacked_movie = new_df[(new_df.MovieID == target_movie_id)].sort_values(by='Timestamp')
df_target_movie['Rating'].mean()
sns.countplot(x='Rating', data=df_attacked_movie)
df_attacked_movie['Rating'].mean()

chunk_size = get_optimal_chunk_size(attack_size)
# chunk_size = 20
print("chunk_size: ", chunk_size)

sample_entropy_list, entropy_chunk_list = get_sample_entropy_list(df_attacked_movie, chunk_size=chunk_size)
sample_average_list, average_chunk_list = get_sample_average_list(df_attacked_movie, chunk_size=chunk_size)
z_score_entropy_plot(sample_entropy_list)
chunk_size = optimum_chunk_size(df_attacked_movie)
