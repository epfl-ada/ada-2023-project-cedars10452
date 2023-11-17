# ada-2023-project-cedars10452
# Behind the screen: Unraveling the Dynamics of Star Power, Ethnicity, and Collaborative Influence in Film Success

## Abstract

The global film industry, estimated to be worth over $136 billion, represents an intricate tapestry of cultural, economic, and artistic elements. This project delves into the nuanced realms of actor success, movie performance, and the impact of ethnicity and collaboration in the industry. 

Firstly, This research investigates how casting high-profile actors, influences a movie's success and the career trajectory of co-stars. Furthermore, the study explores the effects of an actor's ethnicity on both their personal success and the international reception of their films, considering the evolving global audience demographics. 
The influence of accolades, such as Oscars and Golden Globes, on an actor's subsequent roles and career longevity forms a critical aspect of this analysis. 
Additionally, collaboration with renowned directors and producers is scrutinized for its role in shaping an actor's career, akin to Leonardo DiCaprio's frequent partnerships with Martin Scorsese.

Using comprehensive databases like the CMU Movie Summary Corpus, as well as other sources, this research aims to decode patterns in the careers of successful actors and the evolution of their role choices

## Research Questions

1- How does co-starring with high-profile actors impact an individual actor's success ?

2- In what ways does an actor's ethnicity affect their success and the international reception of their films?

3- What is the influence of winning or being nominated for major awards on an actor's future roles and overall career success?

4- How does collaboration with acclaimed directors and producers shape an actor's career?

5- What patterns emerge in the career trajectories of successful actors, and how do their role choices evolve over time?

## Additional Datasets

### IMDb Non-Commercial Datasets
 This dataset notably provides information on  movie ratings. It will gives us an alternative to the box office for measuring overall success of the films that actors have been part of.
### Kaggle Dataset for Golden Globes and Oscars:
 These datasets contain detailed historical data on award nominations and wins, as well as another dataset of movies that we will join with the given ones in order to obtain more data on movie revenue. They will be instrumental in understanding the impact of these prestigious awards on actors' careers and the subsequent success of the movies they feature in.


## Methods

### Data Processing

We first imported and loaded the CMU dataset and noticed that we have a big amount of N/A values of revenues (almost 90%). Therefore, we decided to search for new datasets that would help us fill in those N/A values. merging new dataset values with our CMU dataset we were able to fill in those values and decrease the percentage of N/A values of revenues to around 63%. Moreover, we converted release_date columns' values to datetime type and converted "startYear" and "runtimeMinutes" values that equaled "\N" to NaN. On another hand, we converted freebase IDs of ethnicities to their real meaningfull values. That being done we merged several datasets that allowed us to add award winners and nominations to the dataset.

### Research question 1

For this milestone, we assumed that high-profile actors are those who have won awards. With this definition in mind, we managed to evaluate the impact of collaborating with high-profile actors on two distinct groups: actors who have participated in projects with award-winning actors and actors who have never participated with award-winning actors.

In later steps an interesting step would be to design a network of actors using NetworkX. Once this network is established, we can then conduct a time series analysis to evaluate the popularity and revenues of movies that actors have participated in, both before and after collaborating with high-profile actors. By transitioning our basic analysis to a time series framework, we can more effectively assess the impact of co-starring with high-profile actors over time.

### Research question 2

We mapped the Freebase IDs given to ethnicities by querying Wikidata and worked on those ethnicities as the base of our analysis. As a preliminary step, we looked at the most popular ethnicities in our dataset, the highest ethnicity groups in terms of average movie revenue per actor in that ethnicity group and in terms of average movie rating in that ethnicity group. For future plans, we would like to compare the revenue generated in different regions or countries to see if films featuring actors of certain ethnicities perform better in specific markets. Ideally, we can also map ethnicities, after compiling them into more extensive and representative ethnicity groups, to countries or continents of origin. This will allow for further comparison between the movie performance of actors that release movies in their own countries and those that release in different countries. This would basically be a proxy for determining audience demographics and preferences: to see if there are correlations between audience ethnicity (country of movie release) and preferences for actors’ ethnicities (country of the actor that we will attempt to map).

### Research question 3

We have conducted a preliminary analysis to investigate the impact of winning or being nominated for major awards on an actor's career. This included comparing key metrics like box office revenues and IMDb ratings before and after actors received awards or nominations.  In the next phase, we intend to apply more sophisticated statistical methods to better understand these relationships. This will help us to more accurately determine the extent of the impact of awards on actors' careers.


### Research question 4

In our study, we're investigating the impact of crew awards on movies and actors, focusing on the case of Tom Hardy. Our analysis revealed a significant career shift for Hardy post his involvement in award-winning projects like "Inception." We observed that his subsequent films, associated with acclaimed directors and producers, not only achieved critical and commercial success but also enhanced his career trajectory. In our forthcoming research, we will delve into creating a sophisticated network that encompasses actors, directors, writers, and production companies. Utilizing advanced Python tools like NetworkX, we aim to construct a network where each node represents an individual actor, director, writer, or production company. The edges in this network will signify collaborative ties among these entities. This endeavor seeks to unravel the complex interplay of professional relationships in the film industry and their influence on the success and evolution of cinematic projects. Our analysis is geared toward uncovering the nuanced patterns of collaboration among these key industry players, thereby illuminating how these connections contribute to shaping career trajectories, enhancing film success, and driving innovation in filmmaking. This comprehensive network analysis will provide a deeper understanding of the collaborative ecosystem in the film industry, highlighting the critical role of collective creative efforts in the realm of cinema.


### Research question 5

In our analysis of actors' career evolution in terms of movie genres, we merged actor and movie metadata to calculate actors' ages at the time of movie releases and categorized these ages into bins for segmented analysis. We extracted and visualized movie genres within each age group, using stacked bar charts. We normalized genre counts within each age group to compare proportional distributions, revealing trends in genre participation throughout actors' careers. We also looked at a specific case of a prominent actor's career evolution. For further analysis, we can explore time-series analysis to observe historical shifts, comparative analysis across demographics, correlation studies linking genre shifts to external factors like box office success and network analysis to map complex actor-genre relationships.

 ## Proposed Timeline

 November 20 - November 24, 2023: Investigating the impact of co-starring with high-profile actors on an individual actor's success and the movie's overall performance.

November 25 - November 29, 2023: Analyzing how an actor's ethnicity affects their success and the international reception of their films.

November 30 - December 4, 2023: Examining the influence of winning or being nominated for major awards on an actor's future roles and overall career success.

December 5 - December 9, 2023: Assessing how collaboration with acclaimed directors and producers shapes an actor's career.

December 10 - December 14, 2023: Identifying patterns in the career trajectories of successful actors and how their role choices evolve over time.

December 15 - December 22, 2023: Final Analysis

## Organization within the team

Datastory: Everybody
Website UI: Serge and Assem
Visualizations: Paul and Thomas
Methods: Everybody

