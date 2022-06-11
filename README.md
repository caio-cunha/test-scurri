# Program that prints the numbers from 1 to 100 (Question 02)

## Functions developmented

> Formatting PostCode choose by user:

Function:

```plaintext
def print_numbers(n)
```

Example of use:

```plaintext
python3 question-02.py
```

Response:

```plaintext
Number of 0 untill 100, multiples of 3 print “Three”, multiple of 5 print “Five”, multiples of both 3 and 5 print “ThreeFive”. 
```

## Install and run project

**1. Create and enter in one folder:**
 ```
 mkdir test
 cd test
 ```
 
 **2. Clone the projetct:**
 ```
 git clone https://github.com/caio-cunha/test-scurri.git
 ```
 
 **3. Enter project folder:**
 ```
 cd test-scurri
 ```
 
 **4. Run question-02.py:**
 ```
 python3 question-02.py
 ```

# Validar e Formatar PostCode (Question 03)

This lib is for validate, formate, and get data in API http://api.postcodes.io/ about **PostCode** in the United Kingdom.

## Functions developmented

> Formatting PostCode choose by user:

Function:

```plaintext
def formating_postcode(postcode)
```

Example of use:

```plaintext
    from library.postcode.validating_formating import *
    
    postcode = "B1 1HQ"
    formated_post_code = formating_postcode(postcode)
    print(formated_post_code)
```

Response:

```plaintext
{"formatted_post_code": "code formated", "message": "Formatted"}
or 
{"formatted_post_code": "", "error": "error message"}
```

> Validating PostCode choose by user:

Function:

```plaintext
def validation_postcode(postcode)
```

Example of use:

```plaintext
    from library.postcode.validating_formating import *
    
    postcode = "B1 1HQ"
    validating_post_code = validation_postcode(postcode)
    print(validating_post_code)
```

Response:

```plaintext
True
or 
False
```

> Get data in API http://api.postcodes.io/ about **PostCode** in the United Kingdom.

Function:

```plaintext
def get_data_api(postcode)
```

Example of use:

```plaintext
    from library.postcode.validating_formating import *
    
    postcode = "B1 1HQ"
    
    formated_post_code = formating_postcode(postcode)
    validating_post_code = validation_postcode(formated_post_code["formatted_post_code"])
    if formatted_post_code:
        data = get_data_api(formated_post_code["formatted_post_code"])
        print(data)
```

Response:

```plaintext
Json with data about PostCode choose
or 
Error message
```

## Install and run project

 **1. Enter project folder:**
 ```
 cd test-scurri
 ```
  **_NOTE:_** The project already was download in question-02, then is only enter in test_scurri folder...
 
 **4. Create one file python:**
 ```
 touch "new_file.py"
 ```
 
 **5. Import lib in new_file.py:**
 ```
 from library.postcode.validating_formating import *
 ```
 
 **5. Put code in new_file.py:**
 ```
 from library.postcode.validating_formating import *
 
 postcode = "B1 1HQ"
 
 postcode_formated = formating_postcode(postcode)
 postcode_validated = validation_postcode(postcode_formated["formatted_post_code"])
 if postcode_validated:
    data_api = get_data_api(postcode_formated["formatted_post_code"])
    print(data_api)
 ```
 
 **6. Run new_file.py:**
 ```
 python3 new_file.py
 ```
 
## Run tests

**1. Run tests:**

 ```
 python3 library/setup.py pytest
 ```
