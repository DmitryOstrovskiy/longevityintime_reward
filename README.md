### **Activity reward System for the Disease Tracker Pro app** _Longevity In Time_

### Description

**The project is a separate Rewards application for rewarding activity on the site.**
 
### Functionality

- **For an unregistered user.** For an unregistered user, only the main page and an accessible interactive link to the page about the site and to the main site of our project are displayed. As well as the register and log in buttons.
- **Home page.** General information about the functionality and the need to register is displayed.
- **About page.** More detailed information about what steps will need to be done to use the functionality.
- **Registration.** Upon successful registration, the user automatically authenticates and is redirected to the home page.
- **For a registered user.** In addition, interactive buttons for adding Wallet and TestCard data open in the site menu. First you have to add wallet data using the "Add Wallet" button. One user can add only 1 Wallet. When trying to create it again, it is redirected to the profile page, where the already created wallet address and balance are displayed. After adding Wallet data, you can add Test Card data using the "Add Test Card" button
- **Reward.** If the Test Card is successfully added, a reward of 1 LONG will be added to the wallet balance. The user will be redirected to the profile page, which will display the already updated balance. For each added Test Card, a reward of 1 LONG will be accrued.
- **Log out.** By clicking on the Logout button, the account is logged out and redirected to the Log In page

### Technologies

- Python 3.9
- Django 4.2.7
- Django Rest Framework 3.14.0
- pytz 2023.3.post1
- sqlparse 0.4.4
- typing_extensions 4.8.0
- tzdata 2023.3

###  The project is launched at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/ - admin page

### Project launch

Clone the repository and navigate to it in the command line:
```sh
git clone https://github.com/DmitryOstrovskiy/longevityintime_reward && cd longevityintime_reward
```
Install the virtual environment, activate it and install dependencies:
```sh
python -m venv venv && Windows: ```source venv\Scripts\activate```; Linux/Mac: ```sorce venv/bin/activate``` && pip install -r requirements.txt
```
Perform migrations:
```sh
python manage.py migrate
```
Create a superuser:
```sh
python manage.py createsuperuser
```
Start the server:
```sh
python manage.py runserver
```

### The appearance of the pages

### _Home page for an unregistered user_

![Снимок экрана 2023-12-01 142153](https://github.com/DmitryOstrovskiy/longevityintime_reward/assets/114443093/09bd622a-03fd-4ee9-9853-405a963ab6e6)

### _Getting a JWT token_
**POST**: http://127.0.0.1:8000/api/auth/jwt/create/   
Request example:
```json
{
"email": "ivan@yandex.ru",
"password": "UserIvan1"
}  
```
Response example:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzkyMjE5NCwianRpIjoiOTg0NzFiYTg1MDgyNDIzN2I1NDZjMTYyZTczNzM2MzUiLCJ1c2VyX2lkIjoyfQ.AA7j0s3gdmfPLamYy9FxomsN00zXfs73-8RGkWFWs2E",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzOTIyMTk0LCJqdGkiOiJhZTNiMDM0ZjRmMGQ0MmU5OWJhMGVjNTRiODRlMDQ5OCIsInVzZXJfaWQiOjJ9.Rvcm8ZfiRUGi0XsBglMXLzhQn5jV2L40V53X-RZHQbs"
}
```

### _Getting a user profile_
**GET**: http://127.0.0.1:8000/api/auth/users/2/ - In the Authorization tab, you need to pass an access token
Response example:
```json
{
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "username": "IvanIvanov",
    "password": "pbkdf2_sha256$260000$Zn7FJL7NbWZve3dbPbqMGJ$/1EmKlUMQ0SfGGClHnxjrSH4xH8PBekFuJAmBjuO048=",
    "id": 2,
    "email": "ivan@yandex.ru"
}
```

### _Updating the user profile_
**PUT**: http://127.0.0.1:8000/api/auth/users/2/ - In the Authorization tab, you need to pass an access token
Request example:
```json
{
"first_name": "Ivan",
"last_name": "Ivanov",
"username": "SuperIvan",
"password": "UserIvan1234",
"email": "ivan@yandex.ru"
} 
```
Response example:
```json
{
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "username": "SuperIvan",
    "password": "UserIvan1234",
    "id": 2,
    "email": "ivan@yandex.ru"
}
```

### _Deleting a user profile_
**DELETE**: http://127.0.0.1:8000/api/auth/users/2/ - In the Authorization tab, you need to pass an access token
Request example:
```json
{
"current_password": "UserIvan1234"
}
```

### Author - Dmitry Ostrovsky

