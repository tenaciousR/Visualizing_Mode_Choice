# Visualizing Mode Choice

## Introduction
* The goal of this project was to determine the costs of different modes of transportation to campus, more specifically it was to compare the travel times to UCF based across 10 shuttle routes, 3 modes of transportation (shuttle, bike, driving), and 25 time intervals (7am - 7pm.)

* The approach taken was to gather two kinds of data and combine the values to give an accurate representation of mode times.

### **Hard Data**
* The origin/destination pairs are based on 15 shuttle routes UCF offers off campus students (top 10 routes used in analysis).

* Utilizing [Google Maps Distance Matrix APIs](https://developers.google.com/maps/documentation/distance-matrix/start) to collect the travel time per route based on **origins, destinations, units, mode, departure times,** and a **[Google API Key](https://developers.google.com/maps/documentation/distance-matrix/get-api-key)**.

* Utilizing [Postman API](https://www.getpostman.com/), the Collection Runner was used to automate the process of gathering all the travel times. A collection is run with the JSON file set equal to the [Routes' Origin Destination pairs](https://github.com/tenaciousR/Visualizing_Mode_Choice/blob/master/route1_driving.json), the `departure_time` variable is also used in this JSON. Epochs of a randomly selected week day during normal campus operation hours were used in 30 minute intervals from 7am - 7pm. 

![image](https://user-images.githubusercontent.com/55423732/71788713-c4e2a400-2ff2-11ea-80be-b7d5bc1fe53b.png)

![Screen Shot 2020-01-05 at 7 12 37 PM](https://user-images.githubusercontent.com/55423732/71788366-81d30180-2fef-11ea-9f45-2d9081c2efe5.png)

* If done manually, the `departure_time` variable on Postman would be selected.

* Response Body example for one of the routes run at a certain time of day
![7D18764A-9A2A-449D-9DEF-4015C3A8BAC3_4_5005_c](https://user-images.githubusercontent.com/55423732/71788459-65839480-2ff0-11ea-997d-b0b5f3e71f9d.jpeg)

### **Survey Data**
* This data is derived from interviewing students around UCF campus. This [survey](https://forms.gle/MmWxnagEitfYXTjp6) allowed a cost to be determined for each mode choice (i.e. for driving the cost is parking time, for taking the shuttle the cost is waiting at the stop, etc). 
* One of six questions on the survey:








## Setup/Usage

## Data

## Process
