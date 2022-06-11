import unittest
import json
from validating_formating import (
    formating_postcode, 
    validation_postcode,
    get_data_api
)


## valid Uk find in API
valid_post_code = [
    "B1 1HQ",
    "BN88 1AH",
    "E98 1SN",
    "EC4Y 0HQ",
    "EH99 1SP"
]

## postcode not formatted
post_code_not_formated = [
    "b1 1hq",
    "bn88 1AH",
    "e981SN",
    "ec4Y0HQ",
    "eh991SP"
]

## postcode not formatted wrongs
post_code_not_formated_wrong = [
    "b1 @1hq",
    "bn88 13231231AH",
    "e981321312@SN",
    "ec4Y0HQ2321321",
    "eh991SP @@@"
]

## postcode wrongs
post_code_wrongs = [
    '1111 1AA',  # all digits in Outward code (wrong)
    'AA1 AA',  # all letters in Inward code (wrong)
    'AJ1A 1BB',  # The letters IJZ are not used in the second position
    'XC1A 1BB',  # The letters QVX are not used in the first position
]

class TestLibPostCode(unittest.TestCase):

    def test_formated_validated_post_code(self):
        """
            Test of functions formating and validanting postcode 
        """

        for code in post_code_not_formated:
            
            formated_postcode = formating_postcode(code)
            valid_postcode = validation_postcode(formated_postcode["formatted_post_code"])
            self.assertTrue(valid_postcode)

    def test_not_formated_post_code(self):
        """
            Test with postcode not formated and wrongs.       
        """
 
        for code in post_code_not_formated_wrong:
            
            formated_postcode = formating_postcode(code)
            valid_postcode = validation_postcode(formated_postcode["formatted_post_code"])
            self.assertFalse(valid_postcode)

    def test_wrong_post_code(self):

        for code in post_code_wrongs:
            """
                Test with postcode not found in API.
            """
            
            formated_postcode = formating_postcode(code)
            valid_postcode = validation_postcode(formated_postcode["formatted_post_code"])
            
            if valid_postcode:

                data_api = get_data_api(formated_postcode["formatted_post_code"])
                self.assertEqual(data_api["status"], 404)
    
    def test_ok_post_code(self):
        """
            Test with poscode correct.
        """

        for code in valid_post_code:
            formated_postcode = formating_postcode(code)
            valid_postcode = validation_postcode(formated_postcode["formatted_post_code"])

            if valid_postcode:

                data_api = get_data_api(formated_postcode["formatted_post_code"])
                self.assertEqual(data_api["status"], 200)
