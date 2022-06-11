import requests
import json
import re

def get_data_api(postcode):
    """
        Function for get data about PostCode of Uk.

            API: http://postcodes.io/

        Args: \n

            poscode - PostCode chosse by user.

        Returns: \n

            postcode_data - Json with data returned by API.
    """

    try:
        
        url = requests.get('https://api.postcodes.io/postcodes/' +
                               postcode)

        postcode_data = json.loads(url.text)

        return postcode_data

    except requests.exceptions.RequestException as e:
        
        raise("Connection failed!")


def validation_postcode(postcode):
    """
        Regular expressions for validated inward and outward code.

        The regular expression was get in
             https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting

        Args: \n

            postcode - code for validate

        Returns: \n

            True or False
    """

    if re.match("^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$", postcode) is None:
        
        return False

    else:

        return True

def formating_postcode(postcode):
    """
        Function to format the post code and return the formatted value with inward and outward code

        Args: \n

            postcode - code for format

        Returns: \n

            postcode - code formated
    """

    postcode = postcode.replace(" ", "")
    response = {}

    if len(postcode) < 5 or len(postcode) > 7:

        response["error"] = "PostCode wrong! 5 to 7 characters only!"

        return response
    
    if (bool(re.match('^[a-zA-Z0-9]*$',postcode))==False):

        response["error"] = "PostCode wrong! Special caracters found!"

        return response

    postcode = postcode.upper()

    outward_code = postcode[:-3]

    inward_code = postcode[-3:]

    response["formatted_post_code"] = outward_code + " " + inward_code
    response["message"] = "Formatted..."

    return response
