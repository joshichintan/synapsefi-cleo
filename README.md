# synapsefi_Cleo
------
### Description
> Build flask restful apis for Cleo chat with minimal user interation and abstracting development complexity using synapsefi Apis
### STACK 
* Mongodb
* Docker
* Flask Restful
* Synapsefi APIs
-----
## Installation using Docker  (Prefered)

#### Install Docker:

1. [Download Docker](https://download.docker.com/mac/beta/Docker.dmg)
2. Double-click the DMG file, and drag-and-drop Docker into your Applications folder.
3. You need to authorize the installation with your system password.
4. Double-click `Docker.app` to start Docker.
5. The whale in your status bar indicates Docker is running and accessible.
6. Docker presents some information on completing common tasks and links to the documentation.
#### Running APP:
1. Clone repository
2. navigate to directory `synapsefi_cleo/app`
3. update CLIENT_ID, CLIENT_SECRET in  `config.py`
4. Build and run Docker 
  
    ```
      $ docker-compose up --build
    ```

------
## Testing
- Import  **submit.postman_collection** file from root directory in **Postman** for testing purposes
 ---------
### [OPTIONAL] Maunual installation and setup info (in case docker fails)
1. Run following commands to start virtual env and to install dependencies
   
   ``` 
     $ python3 -m venv env
   ```
   ```
     $ python3 -m venv env
   ```
   ```
     $ brew tap mongodb/brew 
   ```
   ```
     $ brew install mongodb-community
   ```
   ```
     $ source env/bin/activate 
   ```
   ```
     $ pip install -r requirements.txt
   ```

2. Run the following command in a new instance terminal window(not the virtualenv) to start mongodb
   ```
      mongod --config /usr/local/etc/mongod.conf
   ```
3. Go Back to virtualenv Start App
    ```
       python3 start.py
    ```
-----

## API Documentation

> The api endpoints are built to work in a certain way. Unable to follow the steps may lead to exceptions and app failure. Follow the order suggested below to excute the endpoint successfully. Make sure to include the **request body presented here** with each endpoints as jsons and set **Content-type: application/json**

---
> #### Step 1: Create USER
* [POST] Create User 
* endpoint: **http://localhost:5000/users/**
    >save the **'user_id'** received in the respones for the next steps
    
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
> #### Step 2: GET USER
* [GET] User
* endpoint:  **http://localhost:5000/users/`<`string:user_id`>`**
    >replace <string:user_id> with the available **'user_id'** 

> #### Step 3: PATCH USER
* [PATCH] Update User data
* endpoint:  **http://localhost:5000/users/`<`string:user_id`>`**
    > replace <string:user_id> with the available**'_id'**
    
    ```json 
    {
      "permission":"MAKE-IT-GO-AWAY"
    }
    ```

#### Other API endpoints:

> #### Step 4: CREATE ACCOUNT/NODE
* [POST] CREATE USER ACCOUNT
* endpoint:  ** http://localhost:5000/account/`<`string:user_id`>`**
    > replace <string:user_id> with the available**'_id'**
    
    > **Create 2  accounts** with different nickname e.g **Fake Account1** & **Fake Account2**
    --> **Save any one**  accounts **'node_id'** for future steps
    
    ```json 
    {
        "nickname": "Fake Account",
        "account_num": "1232225674134",
        "routing_num": "051000017",
        "type": "PERSONAL",
        "class": "CHECKING"
    }
    ```
> #### Step 5: GET ACCOUNT
* [GET] GET USER ACCOUNT
* endpoint:  **http://localhost:5000/account/`<`string:user_id`>`**
    > replace <string:user_id> with the available**'_id'**
    
    ```json 
    {
      "nickname": "Fake Account1"
    }
    ```
> #### Step 6: POST TRANSACTION
* [POST] CREATE TRANSACTION
* endpoint:  **http://localhost:5000/transaction/`<`string:user_id`>`**
    > replace <string:user_id> with the available**'_id'**
    
    > use the nickname used for your own accounts
    
    ```json 
    {
        "to_account": "Fake Account1",
        "from_account":"Fake Account2",
        "amount": 100
    }
    ```
    
> #### Step 7: GET TRANSACTION
* [GET] GET ALL USER TRANSACTION
* endpoint:  **http://localhost:5000/transaction/`<`string:user_id`>`**
    > replace <string:user_id> with the available**'_id'**

> #### Step 8: DELETE ACCOUNT
* [DELETE] DELETE USER ACCOUNT
* endpoint:  **http://localhost:5000/account/`<`string:user_id`>`**
    > replace <string:user_id> with the available**'_id'**
    
    > use the acc_id from the previous steps
    
    ```json 
    {
        "node_id": acc_id 
    }
    ```

----------------------------
## Brief Documentation of APIS
- [ GET|CREATE|PATCH ]  USERS   
    >   endpoint: http://localhost:5000/users/ `<`string:user_id`>`
 
- [ GET|CREATE|DELETE ]  NODES   
    >   endpoint: http://localhost:5000/account/ `<`string:user_id`>`
 
- [ GET|POST]  Transaction    
    > endpoint: http://localhost:5000/transaction/`<`string:user_id`>`
