import seaborn as sns
import matplotlib.pyplot as plt
from pyparsing import alphas

car_crashes = sns.load_dataset("car_crashes")

car_crashes.sort_values("total", ascending=False, inplace=True)


"""
total : 전체 사고 건수
speeding : 과속 비율
alcohol : 음주 비율
not_distracted : 다른데 정신팔린
no_previous : 이전에 사고가 없었던 운전자 비율
ins_premium : 자동차 보험료
ins_losses : 운전자 1인당 충돌사고로 보험사가 입은 피해
abbrev : 미국 주 약자
"""

plt.figure(figsize=(15, 10))

# 미국의 각 주에서 발생한 전체 사고
sns.barplot(data=car_crashes, x='abbrev', y='total', facecolor="w", edgecolor="black")

sns.barplot(data=car_crashes, x='abbrev', y='speeding', linewidth=3, color='r', label='speeding', alpha=0.3)
sns.barplot(data=car_crashes, x='abbrev', y='alcohol', linewidth=3, color='g', label='alcohol', alpha=0.3)
sns.barplot(data=car_crashes, x='abbrev', y='no_previous', linewidth=3, color='b', label='no_previous', alpha=0.3)

plt.xlim(-1, 51)

plt.show()