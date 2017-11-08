# Analysis-of-structured-information-in-Yelp-data-for-recommendation-

Objective: The objective of this project is to build an application, which focuses on recommending set of users (friends) to user by making use of features that indicate similarity between users. The similarity between the users is determined by performing the clustering using the K-NN algorithm. The clusters of user who has same taste will be created based on calculating the difference between the attribute of each users and the minimum difference between the users, indicates the user have same taste and will be added in a single cluster.

Data set: The data provided by Yelp is made up of a collection of JSON objects which represent users, businesses, reviews, etc. This is a significantly large dataset with 687K users, 86K businesses, 4.2M social edges and 2.7M reviews.

K-NN algorithm was used to perform clustering and above attribute are used to find the hamming distance between each users. "K " in K-NN is the positive integer, which indicate the number of elements nearest to the centroid of the cluster.To test the performance of the application two parameter were used:
-> Precession
-> Recall
