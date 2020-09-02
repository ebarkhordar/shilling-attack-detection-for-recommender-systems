import collections
import math
import matplotlib.pyplot as plt
import scipy.stats as stats


def sample_entropy(rate_list):
    """Calculates the sample entropy of a time_series."""
    S = len(rate_list)
    rate_set = set(rate_list)
    HX = 0
    for i in rate_set:
        ni = rate_list.count(i)
        HX += (ni / S) * (math.log(ni / S, 2))
    return -HX


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_optimal_chunk_size(n):
    return int((2 + math.sqrt(7)) / 6 * n)


def get_sample_entropy_list(df, chunk_size=5):
    sample_entropy_list = []
    chunk_list = []
    index_list = list(chunks(range(0, len(df) + 1), chunk_size))
    if len(index_list[-1]) < chunk_size:
        index_list = index_list[:-1]
    for i in index_list:
        chuck = df[i[0]:i[-1]]
        rate_list = chuck['Rating'].tolist()
        HX = sample_entropy(rate_list)
        sample_entropy_list.append(HX)
        chunk_list.append(chuck)
    return sample_entropy_list, chunk_list


def sample_average(rate_list):
    """Calculates the sample average of a time_series."""
    rate_dict = dict(collections.Counter(rate_list))
    S = sum(rate_dict.values())
    rate_multiple_repetitions = sum(p * c for p, c in rate_dict.items())
    return rate_multiple_repetitions / S


def get_sample_average_list(df, chunk_size=5):
    sample_entropy_list = []
    chunk_list = []
    index_list = list(chunks(range(0, len(df) + 1), chunk_size))
    if len(index_list[-1]) < chunk_size:
        index_list = index_list[:-1]
    for i in index_list:
        chuck = df[i[0]:i[-1]]
        rate_list = chuck['Rating'].tolist()
        MX = sample_average(rate_list)
        sample_entropy_list.append(MX)
        chunk_list.append(chuck)
    return sample_entropy_list, chunk_list


def z_score_entropy_plot(sample_entropy_list):
    z_score_sample_entropy_list = stats.zscore(sample_entropy_list)
    plt.figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(range(len(z_score_sample_entropy_list)), z_score_sample_entropy_list)
    plt.legend(["sample entropy"])
    plt.xlabel('window index', fontsize=12)
    plt.ylabel('z-score', fontsize=12)
    plt.show()


def optimum_chunk_size(df_attacked_movie):
    chunk_size = 20
    while True:
        sample_entropy_list = get_sample_entropy_list(df_attacked_movie, chunk_size=chunk_size)
        z_score_sample_entropy_list = stats.zscore(sample_entropy_list)
        peaks = [i for i in z_score_sample_entropy_list if abs(i) >= 2]
        if len(peaks) <= 1:
            break
        numbers_of_attacks = len(peaks) * chunk_size
        chunk_size = get_optimal_chunk_size(numbers_of_attacks)
    return chunk_size
