import pandas as pd
from matplotlib import pyplot as plt

route1 = pd.read_csv('route1csv.csv')
route2 = pd.read_csv('route2csv.csv')
route4 = pd.read_csv('route4csv.csv')
route5 = pd.read_csv('route5csv.csv')
route7 = pd.read_csv('route7csv.csv')
route10 = pd.read_csv('route10csv.csv')
route11 = pd.read_csv('route11csv.csv')
route12 = pd.read_csv('route12csv.csv')
route13 = pd.read_csv('route13csv.csv')


def route_plotter(route_num):
	plt.plot(route_num.time, route_num.shuttle, linewidth=2)
	plt.plot(route_num.time, route_num.driving, linewidth=2)
	plt.plot(route_num.time, route_num.bike, linewidth=2)
	plt.legend(["Shuttle", "Driving", "Biking"])
	plt.grid(color="black", linestyle="-", linewidth=0.5)
	plt.xlim(left=0)
	plt.xlim(right=12)
	plt.ylabel("Travel Time (minutes)", fontname="Comic Sans MS", fontsize=12)
	plt.xlabel("Time of Day", fontname="Comic Sans MS", fontsize=12)
	plt.show()


plt.title("Route 1 (1.5 miles)", fontname="Comic Sans MS", fontsize=14, fontweight='bold')

route_plotter(route1)

