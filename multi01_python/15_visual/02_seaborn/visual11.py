import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# sns.pairplot(penguins)

# 같은 컬럼 => KDE
# sns.pairplot(penguins, hue="sex")

# kind : scatter, kde, hist, reg
# sns.pairplot(penguins, kind="reg")

# corner ??
# 기본값은 False
sns.pairplot(penguins, kind="reg", corner=True)

plt.show()