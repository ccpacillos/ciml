from typing import List
from ..lib.tree import Tree
from ..lib.table import Table
from .. import data
from statistics import mode
import ramda as R


def train(data: Table):
    features = R.filter(lambda i: i != 'rating', data.headers)

    labels = get_labels(data.rows)
    guess = mode(labels)

    if len(set(labels)) == 1 or len(features) == 0:
        return Tree(value=guess)

    scores = R.map(lambda feature: get_feature_score(feature, data), features)

    top_feature = R.head(R.sort(
        lambda a, b: b['score'] - a['score'], scores))['feature']

    headers = R.filter(lambda feature: feature !=
                       top_feature, data.headers)

    yes_set = data.filter(top_feature, 'y').pick_columns(headers)
    no_set = data.filter(top_feature, 'n').pick_columns(headers)

    right = train(yes_set)
    left = train(no_set)

    return Tree(value=top_feature, left=left, right=right)


def get_feature_score(feature: str, data: Table):
    values = data.get_values_by_headers(
        [feature, 'rating']).rows

    sets = R.group_by(
        lambda i: 'yes' if i[feature] == 'y' else 'no', values)

    yes_values = get_labels((sets['yes']))
    no_values = get_labels((sets['no']))

    guess_if_yes = mode(yes_values)
    guess_if_no = mode(no_values)

    def count_correct_guesses(set, guess):
        return len(R.filter(lambda i: i == guess, set))

    correct_yes_guesses = count_correct_guesses(yes_values, guess_if_yes)
    correct_no_guesses = count_correct_guesses(no_values, guess_if_no)

    score = ((correct_yes_guesses + correct_no_guesses) /
             len(values)) * 100

    return dict(score=score, feature=feature)


def get_labels(set):
    return R.map(lambda i: 'like' if i['rating'] >= 0 else 'nah', set)
