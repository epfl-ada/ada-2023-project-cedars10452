import pandas as pd
import os
import zipfile
import scipy.stats as stats
from SPARQLWrapper import SPARQLWrapper, JSON
from bs4 import BeautifulSoup
import requests
import ast

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

def extract_genres(genre_dict):
    """
    Extract and return a list of genres from a dictionary representation.

    Parameters:
    genre_dict (str): A string representation of a dictionary containing genres.

    Returns:
    list: A list of genres extracted from the dictionary.
    """
    return list(ast.literal_eval(genre_dict).values())


def convert_release_date(date_str):
    try:
        # Try converting with full date format
        return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
    except ValueError:
        try:
            # Try converting with year-month format
            return pd.to_datetime(date_str, format='%Y-%m', errors='coerce')
        except ValueError:
            # Fallback to year-only format
            return pd.to_datetime(date_str, format='%Y', errors='coerce')
        
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

