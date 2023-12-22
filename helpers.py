import pandas as pd
import os
import zipfile
import numpy as np
import scipy.stats as stats
from SPARQLWrapper import SPARQLWrapper, JSON
from bs4 import BeautifulSoup
import requests
import ast
import statsmodels.formula.api as smf
import statsmodels.api as sm
import patsy
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
import gensim
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess

def query_wikidata_for_qnumber(freebase_id):
    """
    Query Wikidata to get the Q-number (identifier) for a given Freebase ID.

    Parameters:
    freebase_id (str): The Freebase ID of the entity.

    Returns:
    str: The Q-number from Wikidata corresponding to the Freebase ID.
         Returns "Q-number not found" if no match is found.
    """
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    query = """
    SELECT ?item WHERE {
      ?item wdt:P646 "%s".
    }
    """ % freebase_id

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        return result["item"]["value"].split('/')[-1]  

    return "Q-number not found"

def get_ethnicity_from_wikidata(q_number):
    """
    Retrieve the ethnicity of an entity from Wikidata using its Q-number.

    Parameters:
    q_number (str): The Q-number of the entity in Wikidata.

    Returns:
    str: The ethnicity of the entity. Returns "Ethnicity not found" if not available,
         or "Other Ethnicities" in case of a failed HTTP request.
    """
    url = f"https://www.wikidata.org/wiki/{q_number}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title')
        return title.text.split(' - ')[0] if title else "Ethnicity not found"
    else:
        return "Other Ethnicities"

def analyze_correlation(series1, series2):
    """
    Analyze and print the Pearson and Spearman correlations between two data series.

    Parameters:
    series1 (iterable): The first data series.
    series2 (iterable): The second data series.

    Returns:
    None: Prints the correlation results and their significance.
    """
    # Calculate Pearson correlation
    corr_pearsonr = stats.pearsonr(series1, series2)
    print('Pearson correlation: ', corr_pearsonr)

    # Calculate Spearman correlation
    corr_spearmanr = stats.spearmanr(series1, series2)
    print('Spearman correlation: ', corr_spearmanr)

    # Interpret the results for Pearson correlation
    if corr_pearsonr[1] < 0.05:
        print('The Pearson correlation is significant.')
    else:
        print('The Pearson correlation is not significant.')

    # Interpret the results for Spearman correlation
    if corr_spearmanr[1] < 0.05:
        print('The Spearman correlation is significant.')
    else:
        print('The Spearman correlation is not significant.')

def extract_items(genre_dict):
    """
    Extract and return a list of genres from a dictionary representation.

    Parameters:
    genre_dict (str): A string representation of a dictionary containing genres.

    Returns:
    list: A list of genres extracted from the dictionary.
    """
    return list(ast.literal_eval(genre_dict).values())

def convert_release_date(date_str):
    return pd.to_datetime(date_str, errors='coerce')
        
def extract_zip(zip_file_name):
    """
    Extracts the contents of a zip file from 'data/zip_files/' to 'data/' directory.

    Parameters:
    zip_file_name (str): Name of the zip file.
    """
    zip_file_path = f'data/zip_files/{zip_file_name}'
    extract_path = 'data/'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('data/')
    
    print("Extraction completed!")

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def get_sorted_last_row(group):
    # Filter out rows where 'year' is NaN
    filtered_group = group.dropna(subset=['year'])

    # Sort the filtered group
    sorted_group = filtered_group.sort_values(by='year', ascending=True)

    # Return the last row if the group is not empty
    return sorted_group.iloc[-1] if not sorted_group.empty else None

# Function to extract the most frequent genre
def get_majority_genre(genres):
    if genres:
        return pd.Series(genres).mode()[0]
    return None

def calculate_importance(row):
    credits_str = str(row["credits"])
    actors_list = credits_str.split('-')
    try:
        # Finding the position of the actor in the credits
        position = actors_list.index(row['Actor name']) + 1
        # Calculating the importance (you can modify this formula as needed)
        importance = 1/position
    except ValueError:
        # In case the actor is not found in the credits
        importance = 0
    return importance

def read_regions_and_countries(file_path):
    region_country_map = {}
    current_region = None

    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line is a region (indented)
            if line.startswith("\t"):
                current_region = line.strip()
            else:
                # It's a country, map it to the current region
                country = line.strip()
                if country:  # Check if the line is not empty
                    region_country_map[country] = current_region

    return region_country_map

def extract_country_and_map_to_region(country_column_entry, country_region_map):
    # Directly use the country_column_entry as the country name
    return country_region_map.get(country_column_entry, 'Unknown')


def run_and_report_regression(formula, data):
    """
    Runs a regression analysis based on the provided formula and data (set to regression_df by default) and prints the results.

    Args:
    - formula (str): A string representing the regression formula.
    - data (DataFrame): A pandas DataFrame containing the data.
    """
    # Prepare the model using patsy.dmatrices because 
    y, X = patsy.dmatrices(formula, data=data, return_type='dataframe')

    # Fit and print the model
    model = sm.OLS(y, X).fit()
    print(model.summary())

    # Calculate VIF
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Check for VIFs greater than 5 and print them
    high_vif = vif_data[vif_data["VIF"] > 5]
    if not high_vif.empty:
        print("\nVariables with VIF greater than 5:")
        print(high_vif)
    else:
        print("\nNo variable has a VIF greater than 5.")

def calculate_common_movies(actor_pairs, actors_won):

    def find_common_movies(row):
        movies1 = set(actors_won[actors_won['Freebase actor ID'] == row['Actor1']]['freebase_id'].values[0])
        movies2 = set(actors_won[actors_won['Freebase actor ID'] == row['Actor2']]['freebase_id'].values[0])
        return list(movies1 & movies2)
    return actor_pairs.apply(find_common_movies, axis=1)


def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  

# Remove stop words
def remove_stopwords(texts):
    stop_words = set(stopwords.words('english'))
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def get_dominant_topic(topic_list):
    return max(topic_list, key=lambda x: x[1])[0]  # Returns the topic number with the highest proportion

def calculate_importance(row):
    credits_str = str(row["credits"])
    actors_list = credits_str.split('-')
    try:
        # Finding the position of the actor in the credits
        position = actors_list.index(row['Actor name']) + 1
        # Calculating the importance 
        importance = 1/position
    except ValueError:
        # In case the actor is not found in the credits
        importance = 0
    return importance
    




