
Accuarcy test is used to find the top K (K is the positve integer) number people that have similar taste to the given user and this is calculated by finding the Hamming distance between the users. Below are the factors that are used to determine the hamming distance between the user:
-> Number of fans
-> Category the user reviewed the most
-> City the user resides
-> Average star given to the user
-> Review count
-> Number of mutaul friends

Then using the list of people who shares the similar interest with the given user, we calculate the precession and recall. Below is the formula used to calculate the precession and recall.
• Precision = (Number of friends in K) / K  
• Recall = Number of friends in K / Total number of friends (K is the parameter in K-NN)
