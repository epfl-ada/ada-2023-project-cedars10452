# ada-2023-project-cedars10452
# Behind the screen: Unraveling the Dynamics of Star Power, Ethnicity, and Collaborative Influence in Film Success

## Abstract

The global film industry, estimated to be worth over $136 billion, represents an intricate tapestry of cultural, economic, and artistic elements. This project delves into the nuanced realms of actor success, movie performance, and the impact of ethnicity and collaboration in the industry. 

Firstly, This research investigates how casting high-profile actors, influences a movie's success and the career trajectory of co-stars. Furthermore, the study explores the effects of an actor's ethnicity on both their personal success and the international reception of their films, considering the evolving global audience demographics. 
The influence of accolades, such as Oscars and Golden Globes, on an actor's subsequent roles and career longevity forms a critical aspect of this analysis. 
Additionally, collaboration with renowned directors and producers is scrutinized for its role in shaping an actor's career, akin to Leonardo DiCaprio's frequent partnerships with Martin Scorsese.

Using comprehensive databases like the CMU Movie Summary Corpus, as well as other sources, this research aims to decode patterns in the careers of successful actors and the evolution of their role choices.

Please visit our data story [here](https://sergeohanesian.github.io/https-github.com-epfl-ada-ada-2023-project-cedars10452-website/).

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

In addressing the question, we operated under the assumption that high-profile actors are those who have won awards. With this definition as our guide, we evaluated the impact of collaborating with high-profile, award-winning actors.

This impact was initially assessed on two distinct groups: actors who have participated in projects with award-winning actors and those who have not. For this part, we compared the average box office revenues and popularity of actors who participated with award-winning actors against those who did not. To discern the differences in these values, we employed t-tests and utilized boxplots for visualization.

We then focused on actors who have collaborated but have not won awards themselves. For these actors, we conducted a time series analysis to compare their average revenue and popularity before and after their collaborations. The differences in these values, before and after the collaboration, were again confirmed through boxplots and t-tests. Additionally, we constructed a network to link participating actors with the award-winning actors.

The influence of collaboration was further evaluated in terms of the likelihood of winning an award post-collaboration. To do this, we limited our analysis to award-winning actors and engineered a variable representing beneficial collaborations. We then analyzed how many beneficial collaborations these actors had engaged in before winning their awards. In this phase, we also created a network by merging dataframes to link the collaborating actors.

### Research question 2

After cross-referencing Freebase IDs with ethnicities via Wikidata queries, we grouped these ethnicities into broader, globally representative regions such as North America, Western Europe, Oceania, etc. This grouping allowed us to examine if there's a correlation between the ethnicities of the cast—defined by these "ethnicity regions"—and the regions where the movies were released, which we determined from the release countries. Furthermore, we assessed an actor's significance based on their billing in the movie credits, inversely related to their listing order (with the lead actor being 1, the second lead 2, and so on), where a lower number indicates higher importance. We then crafted variables like 'weighted_avg_ethnicity_match' and 'main_actor_match' to perform regression analysis on movie revenue. This analysis aimed to evaluate the impact of the main actor's and the broader cast's ethnic congruence with the movie’s release region on its box office success, all while factoring in significant confounders like budget and popularity. To ensure the most accurate model, we compared various regression models to best capture the influence of our variables of interest.

### Research question 3

Our research began with an initial analysis aimed at understanding the effects of receiving major awards, or even being nominated for them, on actors' careers. This phase involved a comparative study of important metrics like box office earnings and IMDb ratings, measured both before and after the actors achieved award recognition. We further explored how these key indicators tended to evolve over time following an award win or nomination.

Next, we segmented our actors into two groups for a more nuanced analysis: the treatment group, consisting of actors who had been acknowledged with an award, and the control group. To ensure a robust comparison, we carefully matched these groups based on several critical factors. This included the actors' years of experience at the time of award recognition, their cumulative filmography, and the predominant genre of their movies. This approach was designed to mitigate the impact of potential confounding variables.

It's important to note that our control group was unique in its composition. Instead of different actors, it included various career stages of the same actors, represented by their involvement in different films. This distinction was crucial due to the temporal dimension introduced by our study. Additionally, our analysis was focused on American films released after 1990, ensuring relevance and comparability in our data.

With this structured framework, we performed a t-test on the average box office revenues of movies released within a 10-year window post-award recognition (or the equivalent career stage for the control group). This test was pivotal in assessing the long-term impact of award recognition on actors' commercial success in the film industry.

### Research question 4

In this question, we delved into the impact of crew awards on movies and the careers of actors, with a specific focus on understanding the broader effects in the film industry. We used advanced data analysis and network (igraph) construction techniques to explore these relationships.

Network Construction and Analysis: We began by compiling a comprehensive dataset, including actors and their collaborations with directors, writers, and production companies. This dataset was enriched with information on awards and nominations, which was crucial in identifying and categorizing acclaimed crew members. Utilizing this data, we constructed an intricate network graph. In this network, nodes represented industry professionals such as actors, directors, writers and production companies, while edges symbolized their collaborative relationships.

Centrality and Comparative Group Analysis: A key part of our analysis involved calculating the degree of neighbor centrality for each actor within the network. We then divided the actors into two groups: those who had collaborated with award-winning/nominated crew members and those who had not. By employing the statistical test, we compared these groups to evaluate the potential impact of such high-profile collaborations on an actor's (crew) network centrality.

In-Depth Regression Analysis: To further understand the relationship we conducted multiple linear regression analyses. These analyses focused on various success metrics, including average film ratings, box office revenues, and audience vote counts. We carefully adjusted these models to control for possible confounding factors, such as the total number of movies an actor had appeared in.

Our methodology was designed to unravel the complex dynamics of professional relationships in the film industry and their influence on the success of movies and the careers of actors. By conducting this comprehensive network analysis, we aimed to shed light on the intricate patterns of collaboration among key industry players. Our goal was to understand how these connections shape career trajectories, contribute to film success, and foster innovation in filmmaking.


### Research question 5

In our analysis of actors' career evolution in terms of movie genres, we merged actor and movie metadata to calculate actors' ages at the time of movie releases and categorized these ages into bins for segmented analysis. We extracted and visualized movie genres within each age group, using stacked bar charts. We normalized genre counts within each age group to compare proportional distributions, revealing trends in genre participation throughout actors' careers. We also looked at a specific case of a prominent actor's career evolution. For further analysis, we can explore time-series analysis to observe historical shifts, comparative analysis across demographics, correlation studies linking genre shifts to external factors like box office success and network analysis to map complex actor-genre relationships.

Continuing our in-depth analysis of actors' career evolution, we expanded our approach to incorporate an exploration of movie topics. Utilizing the same methodology of merging actor and movie metadata, we calculated the actors' ages at the time of movie releases and categorized these ages into bins for segmented analysis. This time, however, our focus shifted to understanding how movie topics, as characterized by a topic model like LDA, varied within each age group. Using stacked bar charts, we visualized the distribution of movie topics across different age groups. By normalizing the topic counts within each age category, we were able to compare proportional distributions, thereby unveiling the patterns of topic participation that emerged throughout the careers of actors.

Moreover, we delved into investigating whether these shifts in movie topics chosen by actors were correlated with changes in revenue or popularity. To achieve this, we employed bar charts to effectively visualize how the popularity and box office revenue varied across different topics within each age group. This aspect of the analysis provided an intriguing perspective on how actors' choices in movie topics potentially influence their commercial success and public appeal at various stages of their careers.

## Proposed Timeline


November 20 - November 24, 2023: Investigating the impact of co-starring with high-profile actors on an individual actor's success and the movie's overall performance.

November 25 - November 29, 2023: Analyzing how an actor's ethnicity affects their success and the international reception of their films.

November 30 - December 4, 2023: Examining the influence of winning or being nominated for major awards on an actor's future roles and overall career success.

December 5 - December 9, 2023: Assessing how collaboration with acclaimed directors and producers shapes an actor's career.

December 10 - December 14, 2023: Identifying patterns in the career trajectories of successful actors and how their role choices evolve over time.

December 15 - December 22, 2023: Final Analysis



## Organization within the team

<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Serge Ohanesian</td>
    <td class="tg-0lax">Worked on research question 2<br><br>Crawled web to gather information<br><br>Created the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Thomas Srour</td>
    <td class="tg-0lax">Worked on research question 2<br><br>Worked on research question 3<br><br>Worked on research question 5</td>
  </tr>
  <tr>
    <td class="tg-0lax">Adam Dandachi</td>
    <td class="tg-0lax">Worked on research question 3<br><br>Worked on research question 4<br><br>Created the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Assem Abou Ali</td>
    <td class="tg-0lax">Work on research question 2<br><br>Worked on research question 5<br><br>Created the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Paul Maroun</td>
    <td class="tg-0lax">Worked on research question 1<br><br>Worked on research question 3<br><br>Worked on research question 5</td>
  </tr>
</tbody>
</table>