# Visualizing Mode Choice

## Introduction
* The goal of this project was to determine the costs of different modes of transportation to campus, more specifically it was to compare the travel times to UCF based across 10 shuttle routes, 3 modes of transportation (shuttle, bike, driving), and 25 time intervals (7am - 7pm.)

* The approach taken was to gather two kinds of data and combine the values to give an accurate representation of mode times.

**Hard Data**
* The origin/destination pairs are based on 15 shuttle routes UCF offers off campus students (top 10 routes used in analysis). 
* Utilizing [Google Maps Distance Matrix APIs](https://developers.google.com/maps/documentation/distance-matrix/start) to collect the travel time per route based on **origins, destinations, units, mode, departure times,** and a **[Google API Key](https://developers.google.com/maps/documentation/distance-matrix/get-api-key)**.

![Screen Shot 2020-01-05 at 7 12 37 PM](https://user-images.githubusercontent.com/55423732/71788366-81d30180-2fef-11ea-9f45-2d9081c2efe5.png)


* Utilizing [Postman API](https://www.getpostman.com/), the Collection Runner was used to automate the process of gathering all the travel times in a fraction of the time it would take manually. A collection is run with the JSON file set equal to the [Routes,](https://github.com/tenaciousR/Visualizing_Mode_Choice/blob/master/origins_destinations.json). 
* 



## Setup/Usage

## Data

## Process
