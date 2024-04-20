
import numpy as np


post = {0:[8],
        1:[2],
        2:[3],
        3:[6],
        4:[5],
        5:[4],
        6:[0],
        7:[8],
        8:[7]}

chairs_xy= [3,3]
chairs = {}
chair = 0

for l in range(chairs_xy[0]):
    for r in range(chairs_xy[1]):
        chairs[chair] = [l,r]
        chair += 1


from itertools import permutations

x = 9

per_loss = 0
pr_loss = 0
old_loss = 99999999999999999999999999999999999999999999999
sc_pattern = ()
# 0からxまでの数字の全ての並び替えのパターンを生成
all_permutations = permutations(range(x))

def calculate_distance(points):
    # pointsは [[x1, y1], [x2, y2]] の形式のリスト
    x1, y1 = points[0]
    x2, y2 = points[1]
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# 生成した各パターンをfor文で一つずつ表示
for pattern in all_permutations:

    for i in pattern: # できたランダムな座席表から一人抜き出す
        

        fv_list = post[i]
        pers_xy = chairs[i]
        per_loss += pr_loss / len(fv_list)
        pr_loss = 0


        for g in fv_list: # その人のfvの座標を出す
            fv_xy = chairs[pattern.index(g)]
            distance = calculate_distance([pers_xy,fv_xy])
            pr_loss += distance
    
    print(pattern)
    print(per_loss)
    if per_loss < old_loss:
        sc_pattern = pattern
        old_loss = per_loss
        print(f"Latest fast chaers = {sc_pattern,per_loss}")


    
    per_loss = 0

print(f"\n\n席替えの最適解:{sc_pattern } 不満度:{ old_loss}\n\n\n\n\n\n\n")