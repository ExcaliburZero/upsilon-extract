# Author:     Dae-Won Kim
# License:    MIT License
# Paper:      Kim & Bailer-Jones 2015
#             https://arxiv.org/abs/1512.01611
# Repository: https://github.com/dwkim78/py3-upsilon
# History:    https://github.com/dwkim78/py3-upsilon/commits/2c3e1da134014bf75fd672044f03f3b650045b10/upsilon/extract_features/feature_set.py
def get_feature_set():
    """
    Return a list of features' names.

    Features' name that are used to train a model and predict a class.
    Sorted by the names.

    Returns
    -------
    feature_names : list
        A list of features' names.
    """

    features = ['amplitude', 'hl_amp_ratio', 'kurtosis', 'period',
        'phase_cusum', 'phase_eta', 'phi21', 'phi31', 'quartile31',
        'r21', 'r31', 'shapiro_w', 'skewness', 'slope_per10',
        'slope_per90', 'stetson_k']
    features.sort()

    return features


def get_feature_set_all():
    """
    Return a list of entire features.

    A set of entire features regardless of being used to train a model or
    predict a class.

    Returns
    -------
    feature_names : list
        A list of features' names.
    """

    features = get_feature_set()

    features.append('cusum')
    features.append('eta')
    features.append('n_points')
    features.append('period_SNR')
    features.append('period_log10FAP')
    features.append('period_uncertainty')
    features.append('weighted_mean')
    features.append('weighted_std')

    features.sort()

    return features


if __name__ == '__main__':
    print(get_feature_set())
