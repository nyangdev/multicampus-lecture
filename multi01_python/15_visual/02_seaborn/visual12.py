import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

fig = plt.figure(figsize=(10, 7))
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 4)

# 밑에 두개는 seaborn이 그린거
sns.histplot(data=penguins, x="body_mass_g", ax=ax01)
sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", ax=ax02)

# matplotlib가 그린거
# 결측치가 있으면 못 그려줌
# ax03.boxplot(penguins["body_mass_g"])

# 결측치 있을때 처리
# fillna ??
# ax03.boxplot(penguins["body_mass_g"].fillna(penguins["body_mass_g"].mean()))

sns.boxplot(data=penguins, y="body_mass_g", ax=ax03)

plt.tight_layout()
plt.show()