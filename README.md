# Analysis-of-structured-information-in-Yelp-data-for-recommendation-

Objective: The objective of this project is to build an application, which focuses on recommending set of users (friends) to user by making use of features that indicate similarity between users. The similarity between the users is determined by performing the clustering using the K-NN algorithm. The clusters of user who has same taste will be created based on calculating the difference between the attribute of each users and the minimum difference between the users, indicates the user have same taste and will be added in a single cluster.

Data set: The data provided by Yelp is made up of a collection of JSON objects which represent users, businesses, reviews, etc. This is a significantly large dataset with 687K users, 86K businesses, 4.2M social edges and 2.7M reviews.Responsibility: Below are the attribute that were used to find the similarity between the users:

•	City : City the user reside
•	State : State the user reside
•	Votes : Number of votes given by the user
•	Category: The category in which the user write the reviews. 
•	Fans_range: The fans range for each user. Used the range difference of 100 fans.
•	Average_stars: The number of stars given to the user
•	Mutual friends: This attribute, compares friends between each user and calculated the percentage of the mutual friends. 

K-NN algorithm was used to perform clustering and above attribute are used to find the hamming distance between each users. "K " in K-NN is the positive integer, which indicate the number of elements nearest to the centroid of the cluster.To test the performance of the application two parameter were used:•	Precision = (Number of friends in K) / K  •	Recall = Number of friends in K / Total number of friends (K is the parameter in K-NN)
