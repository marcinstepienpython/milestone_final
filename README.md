# ADART - an auction place /Django Full Stack/

The project goal was to build an auction place to sell historical artifacts. External user’s goal is to find, learn about and acquire artifacts they are interested in. The goal of the site owner is earn money on selling the artifacts (the site owner is the seller)

![alt text](https://github.com/marcinstepienpython/milestone_final/blob/master/static_cdn/static_root/img/adart.png)

The website is available here: https://adart.herokuapp.com/

## Features

The website provides a functionality to search, bid, buy and review historical artifacts.

### Existing Features

The application gives users a possibility to:

Visitors:

- browse items
- serch for items
- make bids on items (registered users)
- buy items ( integration with Stripe payments)
- review purchased items (registered users)

Site owner
 - add items (admin panel)
 - add tags => eg. furniture, paintings, new, trending, discounted etc
 - see orders, anonymous buyers, billing, addresses
 - manage users (admin panel)

### Features Left to Implement

Bids:
- we have only basic functionality of bids (addig and showing the bids). The next iteration will introduce logic to disable items with highest bids etc.

Emails:
- Introduction of confirmation emails.

## UX

The adart auction place is a simple design portal consisting of:

THE LAYOUT:


- MAIN NAVIGATION:
  (Anonymous user)
  - User will have a possibiliy to navigate to:
    - Artifacts -> List of all available artifacts
    - Featured -> List of artifacts featured by site owner
    - Bids -> List of bids placed by regitered users
    - Search 
    - Cart
    - Login/Register
  
  (Authenticated user)
  - User will have a possibiliy to navigate to:
    - Artifacts
    - Featured
    - Bids
    - Reviews -> List of reviews. Authenticated users can create new reviews (however only on items         they have purchased).
    - Search
    - Logout


- MAIN SECTION:
  /artifacts/
    - Displaying cards of artifacts (img, title, description and 'details' button)
  /featured/
  - Displaying cards of featured artifacts (img, title, description and 'details' button)
  /bids/
  - List of bids (ordered by date)
  /reviews/
  - Displaying cards of reviewed artifacts (img, title, description and 'details' button)
  - Displaying section "Review your purchased items"
  /cart/
  - Displaying purchase section /items => address => payment method => payment => success page/
  /login/register/
  - Displaying login/register forms


## Technologies Used

HolidayPal uses following frameworks:

- [Bootstrap](https://getbootstrap.com/)

  - The project uses **Bootstrap** to simplify managing layout and CSS elements.

- [Google Fonts](https://fonts.google.com/)

  - The project uses **Google Fonts** to display beautiful and free fonts.

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation.

- [Font Awesome](https://fontawesome.com)
  - The project uses **Font Awesome** for displaying beautiful fonts.

- [Stripe](https://stripe.com)
  - The project uses **Stripe** for processing payments.

- [Django](https://https://www.djangoproject.com/)
  - The project uses **Django** as a web framework.

- [AWS](https://aws.amazon.com)
  - The project uses **AWS** for static files storage.


The site has been created using:

- Django
- Python
- HTML
- CSS
- JavaScript

## Testing

Layout:

1. Testing site responsiveness:

   - google developer tools:
     - site has been tested on all available devices (Galaxy, iPhone, iPad)
   - Firefox, Chrome, Edge, Safari
   - mobile phones (Huawei P8, iPhone 8, iPhone 6, iPhone 7)
   - tablets (Samsung Galaxy Tab)

2. HTML Validator
   The page has been validated using the following tool:

   https://validator.w3.org/nu/?doc=https%3A%2F%2Fadart.herokuapp.com%2F resulted in


Functionality:

USER SCENARIOS:

As a SITE_OWNER:, 
1. I want to add new artifact => checked
2. I want to delete/edit artifact => checked
3. I want to create/edit/delete user => checked
4. I want to add/edit/delete tag ==> checked ('trending')
5. I want to see anonymous users email after purchase => checked

As a LOGGED_IN_USER,
1. I want to make a bid => checked
2. I want to add review after I purchased an item => checked
3. I want to add/remove item to my cart => checked
4. I want to add payment method => checked
5. I want to add shipping addres => checked
6. I want to make the payment => checked


As an ANONYMOUS_USER: 
1. I want to buy item without registration => checked
2. I want to register => checked

## Deployment

The application has been deployed to heroku.

Deployment process:

Heroku
1. Created production environment
2. Created requirements.txt file
3. Created free heroku account (https://heroku.com)
4. Login to heroku using CLI
5. Create a new app using: heroku create adart
6. Created Procfile
7. Installing necessary libs: pip install psycopg2-binary dj-database-url gunicorn
8. Created runtime.txt (Python version)
9. Created heroku database with: heroku addons:create heroku-postgresql:hobby-dev
10. Updated production.py with posgreSQL db on heroku
11. Disabling static files: heroku config:set DISABLE_COLLECTSTATIC=1
11. Sending files to heroku: git push heroku master
12. Then heroku run bash / python manage.py migrate
13. Create superuser
14. as a result: heroku open

AWS (static files):
1. Created AWS account (https://aws.amazon.com)
2. Created user, policy and group
3. Created bucket
4. Django configuration: pip install boto3 django-storages boto
5. Creating asw folder, __init__.py, utils.py
6. Importing AWS confids into settings
7. Run python manage.py collectstatic
8. Changing the SECURITY_KEYS for production


The deployed application is available on: https://adart.herokuapp.com/

Deployment issues:

- Secure connection on iOS. There are some security inssues with Apple platform.


### Content

The page uses information and images found on Wikipedia.

### Project summary

1. Django Full Stack Project 
2. Multiple Apps
3. Data Modeling (2 custome models: reviews and bids)
4. User Authentication
5. User Interaction (bids, reviews)
6. Use of Stripe
7. Structure and Navigation
8. Use of JavaScript (ZoomIn, ZoomOut mechanism on the artifact details)
9. Documentation: 
10. Version Control (Git & GitHub) 
11. Attribution
12. Deployment (Heroku, AWS) 
13. Security: 



