import matplotlib.pyplot as plt
import numpy as np

plt.title("the favourite sports of 300 students of a school")
plt.xlabel("Sports")
plt.ylabel("No. of Students")



x = np.array(["Cricket","Fottball","Hockey","Badminton","Swimming","Tennis"])
y = np.array([80,40,20,30,45,75])

plt.bar(x, y, color = "red",width = .2)
plt.show()