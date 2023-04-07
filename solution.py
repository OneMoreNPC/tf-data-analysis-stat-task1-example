import numpy as np


chat_id = 49479018 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    from scipy.stats import expon
    return (x.mean() - expon.mean(loc=-39)) / 10 # Ваш ответ
