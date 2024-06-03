import matplotlib.pyplot as plt
import numpy as np

#data values
classes = ["BUSN 160", "CIS 140", "CIS 249", "CSCI 202", "CSCI 215", "CSCI 232", "MATH 81", "CIS 155", "ENGL& 101" ]
gpa_total = [4.0, 4.0, 4.0, 3.8, 4.0, 3.8, 3.8, 4.0, 4.0]

#creating stem graph
plt.figure(figsize=(10, 6))
markerline, stemlines, baseline = plt.stem(classes, gpa_total, linefmt="b--", markerfmt="bo", basefmt="r")

#adding labels
plt.xlabel("Classes")
plt.ylabel("GPA")
plt.title("GPA by Class")

#adding ticks
plt.yticks(np.arange(0, 4.5, 0.5))

#show graph
plt.show()