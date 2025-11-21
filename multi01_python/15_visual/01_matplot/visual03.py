import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 5))
# ax = fig.subplots()
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(1, 2, 2)
# fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y01 = list(map(lambda x: x**2, x))
y02 = list(map(lambda x: x**3, x))

ax01.plot([1, 2, 3, 4, 5], y01, color="red", label="pow2")
ax02.plot([1, 2, 3, 4, 5], y02, color="blue", label="pow3")

# plt.legend()
ax01.legend()
ax02.legend()

ax01.set_title("x ** 2")
ax02.set_title("x ** 3")

plt.show()