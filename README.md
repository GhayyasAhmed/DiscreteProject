# Highways of Pakistan(National, Motorways, Expressways)

# Introduction

In this project we have graphically represented all the national highways of Pakistan.Edges are the roads and nodes are different cities of Pakistan. While construting the data we learned what actually is the difference between national highways, motorways, and expressways and we have also constructed the data of different motorways and expressways but garph is only showing information about national highways.

# Data Collection

We have used these websites/links for data collection:

• https://en.wikipedia.org/wiki/National_Highways_of_Pakistan

• https://en.wikipedia.org/wiki/Motorways_of_Pakistan

• https://en.wikipedia.org/wiki/List_of_expressways_of_Pakistan

Note: Name of some highways that are given in the above-mentioned websites are not available completely so we have not considered these highways while constructing our data.

# Arrangement

• Edgelist2, Edgelist3, Edgelist4, Edgelist5, Edgelist6 are the individual txt files representing top 5 degree nodes.

# Network Analysis of Complete Data

• Total cities are 183(nodes).

• Total routes are 188(edges).

• Average degree is 2 which means that on average every city has 2 routes or 2 other are cities directly connected with it.

Note: Our graph was not completely connected(we can't reach every city starting from any city), so for further interpretations we extracted largest connnected component from our data.

# Network Analysis of Largest Connected Component

• Largest connected component means that we can reach every city starting from any city.

• Total cities are 174(nodes).

• Total routes are 181(edges).

• Average degree is 2 which means that on average every city has 2 routes or 2 other cities are directly connected with it.

• Average path length of largest connected component is 19(approx) which means that on average if we want to go from one city to another then we have to pass through 18 other cities.

• Diameter is 51 means that if we are travelling from anyone city to another then we have to cover maximum of 51 roads in between them and the maximum checkpoints will be 50.

• There is no clustring.
