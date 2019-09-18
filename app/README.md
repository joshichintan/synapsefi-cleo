# synapsefi_Cleo

### Description
* These apis built using flask restful for Cleo chat has minimal user interation and has abstracted development complexity using synapsefi Apis


## Installation(Prefered)
- Git clone repository
* Get Client_id and Secret_key from synapseFi sandbox Dashboard and add it to config.py
* Navigate to directory synapsefi_cleo/app  
* #### Run following commands to start virtual env and to install dependencies
  ``` 
    python3 -m venv env 
    brew tap mongodb/brew
    brew install mongodb-community
    source env/bin/activate 
    pip install -r requirements.txt```

* 
    #### Run the following command in a seperate terminal window to start mongodb

    ```
     mongod --config /usr/local/etc/mongod.conf
* #### Start App
  ```python
    python3 start.py
  ```
## Testing
 * Import  **submit.postman_collection** file from root directory in **Postman** for testing purposes
  
#### Alternative Docker installation and setup info
* Install docker(for more details follow this link: https://docs.docker.com/docker-for-mac/install/)
* Navigate to synapsefi_cleo directory
* Run following command 
    ```python
      docker build app
      #Successfully built "78947a002b6fat"<- here is your image_id , this will be generated make sure to copy it, need it in next step 
      docker run image_id #e.g 78947a002b6fa
    ```


## API Documentation

* [POST] Create User 
    - http://localhost:5000/users/
    
    ```json
    {
      "logins": [
        {
          "email": "test@synapsefi.com"
        }
      ],
      "phone_numbers": [
        "901.111.1111",
        "test@synapsefi.com"
      ],
      "legal_names": [
        "Hello WOrld2"
      ],
      "documents": [
        {
          "email": "test@synapsefi.com",
          "phone_number": "901.111.1111",
          "ip": "::1",
          "name": "Hello World2",
          "alias": "",
          "entity_type": "LLC",
          "entity_scope": "Arts & Entertainment",
          "day": 2,
          "month": 5,
          "year": 1989,
          "address_street": "1 Market St.",
          "address_city": "SF",
          "address_subdivision": "CA",
          "address_postal_code": "94105",
          "address_country_code": "US",
          "virtual_docs": [],
          "physical_docs": [],
          "social_docs": []
        }
      ],
      "extra": {
        "supp_id": "122eddfgbeafrfvbbb",
        "cip_tag": 1,
        "is_business": true
      }
    }
    ```  

* [GET] User
    - http://localhost:5000/users/<string:user_id=>

* [PATCH] Update User data
    - http://localhost:5000/users/<string:user_id>

    ```json 
    {
      "permission":"MAKE-IT-GO-AWAY"
    }
    
    ```

#### Other API endpoints:
- [ GET|CREATE|DELETE ]  USER_ACCOUNT   
   - endpoint: 'http://localhost:5000/account/(string:user_id)'
   - Creates at least two ACH Accounts with different nicknames to make transactions
 
- [ GET|POST]            Transaction    
    - endpoint: 'http://localhost:5000/transaction/(string:user_id)' 
    - creates transaction 
    


