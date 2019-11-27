# ADART - an auction place /Django Full Stack/

The project goal was to build an auction place to sell historical artifacts. External user’s goal is to find, learn about and acquire artifacts they are interested in. The goal of the site owner is earn money on selling the artifacts (the site owner is the seller)

![alt text](https://github.com/marcinstepienpython/milestone_final/blob/master/static_cdn/static_root/img/adart.png)

The website is available here: 

## UX

The Monkees website is a simple design consising of three sections.

THE LAYOUT:

- MAIN NAVIGATION:

  - User will have a possibiliy to navigate to:
    - The Monkees => index.html
    - The Band => band.html (info about the band and samples od music/video)
    - News => news.html (info about current chenages and news about the band)
    - Concerts => concerts.html (info about coming live shows and links to buying tickets)
    - Book a Show => book.html (form to book the band for a private show)
    - Shop => shop.html (links to amazon.com where users may acquire band's albums)

- DISPLAY SECTION:

  - Displaying main content of given sub-page => eg. news, book form, concerts dates and tickets links.

- SOCIAL LINKS:

  - Displaying links to all social platforms related to the band (facebook, instagram, twitter).

USER STORIES:

As a < type of user >, I want < some goal > so that < some reason >.

1. Buy tickets: visitors can see 'buy tickets' link right on the main page. Apart from 'news' buying tickets will be the most frequent action on the page. Users have also special section dedicated to buying tickets for upcomming events.



## Features

The website makes it easy for visitors to purchase tickets, albums and book the band for private shows. The info about the band and news are also accessible.

### Existing Features

The website sections and subpages:

- Showcase photos, audio and video clips from the band's catalog.
- Publicise the band's upcoming shows and/or availability to perform at events such as weddings and corporate parties.
- Provide links to external resources, such as the band's social media profiles (can point anywhere at all).

### Features Left to Implement

Shop:

- It would be a good idea to implement own shop, where vistors might purchase band's related products (t-shirts, posters, dvds).

Calendar:

- Implementation of a booking system where visitors might find open time spots for possible private shows.

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

The site has been created using:

- Django
- Python
- HTML
- CSS
- JavaScript

## Testing

Basic set-up:

1. Added boostrap framework and tested by creating simple container and jumbotron classes.
2. Added google fonts and tested Fixed the '|' issues in rel link.

Layout:

1. Testing site responsiveness:

   - google developer tools:
     - site has been tested on all available devices (Galaxy, iPhone, iPad)
   - mobile phones (Huawei P8, iPhone 8, iPhone 6)
   - tablets (Samsung Galaxy Tab)

2. Validators
   The page has been validated using the following tools:

- (html) https://validator.w3.org/ => resulted in: Document checking completed. No errors or warnings to show.
- (html) https://html5.validator.nu/ => resulted in: The document is valid HTML5 + ARIA + SVG 1.1 + MathML 2.0 (subject to the utter previewness of this service).
- (css) https://jigsaw.w3.org/css-validator/ => resulted in: 

## Deployment

The application has been deployed to heroku.

Deployment process:
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
11. 



The application is available here: https://adart.herokuapp.com/

Deployment issues:

- 

### Content

The page uses information found on Wikipedia. It applies to the section about band history. All the info has been copied from Wikipedia.

### Media


