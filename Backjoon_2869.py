#달팽이가 땅에서 출발해서 높이가 V인 나무 막대를
#모두 올라가려면 며칠이 걸리는지 구하는 프로그램
#막대 높이: V, 낮에 올라갈수있는 거리: A, 밤에 미끄러지는 거리: B

import math

input_a, input_b, input_v = input().split()
count_days = (int(input_v) - int(input_b)) / (int(input_a) - int(input_b))
print(int(math.ceil(count_days)))