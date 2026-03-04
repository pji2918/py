"""
I want to go home
"""

import random


def getStatement(min: int = 1, max: int = 19721121) -> str:
    """
    evaluate 가능한 무작위 수학 식을 반환합니다.

    :type min: int
    :param min: 최소 값
    :type max: int
    :param max: 최대 값
    :rtype: str
    :return: 생성된 수학 수식
    """

    return f"{random.randint(min, max)} {random.choice(['+', '-', '*', '/'])} {random.randint(min, max)}"


def blackColorMap(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(79 100%% 0%%)"
