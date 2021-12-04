## Milestone Project - 4

This is the last milestone project for the Fullstack Web Developer course with Code Institute. The aim of the project is to showcase my skills learnt throughout this course.

Throughout this project I have used Python, a high-end programming language along with Django, a python framework.

The deployed site can be found at [here](https://ms-4.herokuapp.com/)

## Table Of Contents

1. UX

- User Stories
- Design
- Framework
- Color Scheme
- Icons
- Typography
- Wireframes

2. Features

- Existing Features
- Features Left to Implement

3. Technologies Used

- Front-End Technologies
- Back-End Technologies

4. Testing

5. Github Repository

6. Deployment

- Local Deployment
- Heroku Deployment

7. Credits

## UX
This project is the final part of my Code Institute Full Stack Software Development program, specifically the Full Stack Frameworks module. The purpose of the project is to create a website for an online nutrition products e-commerce store where the company displays their products for customers. This website is designed in a simple and efficient way for the customers to have a seamless and enjoyable shopping experience.

## User Stories
- As a user I want to view the site from any device (mobile, tablet, desktop).
- As a user I want to see the products without login.
- As a user I want to create my account.
- As a user I want to view my profile.
- As a user I want to update my profile.
- As a user I want to login and logout.
- As a user I want to be able to change my password.
- As a user I want to filter the products based on category type.
- As a user I want to search for a product.
- As a user I want to be able to see the product details.
- As a user I want to be able add product to my cart and remove if I change my mind.
- As a user I can view my order summary before checkout.

## Design

### Framework

- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [jQuery 3.4.1](https://code.jquery.com/)
In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Django 3.23](https://docs.djangoproject.com/en/3.2/releases/)
Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap. 

### Color Scheme
For the color scheme, I've used davy's grey #555555 and black #000000 in the navbar and most pages. I chose green #198754 and blue #2596be for some icons to highlight. Overall, I tried to keep a simple classic look.

### Icons
[Font Awesome 5.15](https://fontawesome.com/)

I used Font Awesome icons for throughout this project.

### Typography
The following fonts were used :

- Helvetica Neue
- Helvetica 
- sans-serif

### Wireframes
Mock-ups were created early on in this project.

I've used Balsamiq Wireframes during the Scope Plane part of the design and planning process for this project.

All of my wireframes for this project can be found [here](https://github.com/Siobhanmcc/django/tree/master/documents/wireframes)

## Features
### Accounts App
The accounts app will allow users to register for free and create their own unique account. This is built using Django's authentication and authorization to validate profile data. Passwords are hashed for security purposes.

The users will register using the registration form. Registered users will be able to login by using the login form with their username and password or with their email and password.

The users can also reset their password if they forgot the original password using the reset password link on the login.html page.

### Products App
### index (Home Page)

Displays the Bestselling Products, and the product categories available in the shop.

### product.html

Displays all the products available in the website. Users can see the product image, name, price. Users can add the product to the cart. Users can go for more details if they click on the image.

### product_detail.html

On this page the user can see all the details about the product. The product title, Price and the product features. If the user want to add the product to the cart they can do from here as well.

### Checkout App
### checkout.html

Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity.

The user needs to fill out the payment form in order to go for the payment.

Once the payment is successfull, a message will be displayed.

If there is an error with the payment, the user will be notified with an error message.

### Search App
This will allow the user to search for a product based on the title.

The search icon is visible from all the pages. 

### Base Template
Features available from all the pages

Navbar

In order to create the navbar I have used Bootstrap 4 and the navbar is available in all the pages.

The nabar features the logo and the product menu on the left.

On the right side of the navbar, the user can see the search bar, the My Account heading and the Shopping Cart icon.

A user who is currently logged in will see options to see their profile page or log out.

A user who is logged out will see options to register or log in to the website.

The shopping cart icon can lead to cart page. Once the user has added at least one item to their cart the $ value of the cart will appear under the shopping cart icon.

The search bar enables the user to type in their relevent product search.

## Technologies Used
- [Gitpod](https://www.gitpod.io/) - The online IDE used for developing this project.
- [GitHub](https://github.com/) - Used to store and share all project code remotely.
- [Balsamiq](https://balsamiq.com/) - To create the wireframes for this project.

## Front-End Technologies

- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5) - Used as the base for markup text.
- [CSS3] (https://developer.mozilla.org/en-US/docs/Web/CSS) - Used to add styles to the HTML.
- [jQuery 3.4.1](https://releases.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Stripe] (https://stripe.com/gb) - Used to make secure payments.
- [Font Awesome](https://fontawesome.com/) - Used for icons in the website.
- [Bootstrap4](https://getbootstrap.com/) - Used to align the elements in the website using the grid system. And also used to create the hamburger button, the modals, the buttons, the badges, the alerts and to style the forms.

## Back-End Technologies

[Python 3.2.0](https://www.python.org/) - Used as the back-end programming language.
[Django](https://docs.djangoproject.com/en/3.2/) - Used as my Python web framework.
[Heroku](https://dashboard.heroku.com/) - for deployment
[PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.
[AWS S3 Bucket](https://aws.amazon.com/) - Used to store images entered into the database.


## Testing

### Validation Services
HTML: I have used https://validator.w3.org/ in order to validate the HTML code.

CSS: I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.

JavaScript: I have used https://jshint.com/ in order to check the JavaScript code.

### Manual Testing
I have a detailed checklist of all the manual testing that has been done to confirm all areas of the site work as expected.

Click [here](https://github.com/Siobhanmcc/django/blob/master/documents/Testing_file_1.pdf) to see the checklist that I have used to test the main features.

### Stripe payment testing
My checkout app is using the stripe payment for the payment option. I tested this by using Stripes test card (4242 4242 4242 4242) I tested the forms and ensured all my validation worked as expected and my logic was performing as expected. The checkout app works from the Stripe API.

Card number - 4242424242424242

CVC - Any 3 digit number.

Expiry date - Any date in the future.

### Responsiveness
Chrome DevTools and physical devices were used throughout development for a number of purposes, one of which was to test the responsiveness and rendering across a range of sizes and devices. As issues were found they were either fixed at the time or noted and returned to later.

The site has been tested successfully on

Apple Macbook Air - Safari browser

Apple iPhone 6,7 &8S - Safari Browser

iPad Mini - Safari Browser

Desktop - Chrome v.74
Desktop - Firefox v.67

### Development
### GitHub Repository
Created a repository in GitHub called: “Siobhanmcc/django” https://github.com/Siobhanmcc/django

Initialised git from the terminal using Git Bash:

git init

Created a .gitignore file and I have added the files and folders that won't need to push to GitHub (i.e. *.sqlite3, *.pyc, _pycache_)

Added the files that I was working on to the Staging area by using:

git add .

Run the commit command with the first commit

git commit -m “initial commit"

Copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:
git remote add origin git@github.com:Siobhanmcc/django.git

git push -u origin master

I've run regular commits after every important update to the code, and I pushed the changes to GitHub.

Deployment
How to run this project locally
To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: - An IDE such as Microsoft Visual Studio Code(or any IDE)

In order to run this project locally on your own system, you will need the following installed - PIP - Python 3 - Git

To allow you to access all functionality on the site locally, create free accounts with the following services: - Stripe - AWS and set up an S3 bucket

Instructions

Clone this GitHub repository by either clicking the green "Clone or download" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal: git clone https://github.com/Siobhanmcc/django

Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

Create a .env file with your own credentials.

python -m .venv venv NOTE: The python part of this command and the ones in other steps below assumes you are working with a windows operating system. Your Python command may differ, such as python3 or py

Activate the .venv with the command: .venv\Scripts\activate Again this command may differ depending on your operating system, please check the Python Documentation on virtual environments for further instructions.

Install all required modules with the command
pip -r requirements.txt.

Set up the following environment variables within your IDE.

  - STRIPE_WH_SECRET

  - STRIPE_SECRET_KEY

  - STRIPE_PUBLIC_KEY

In the IDE terminal, use the following command to launch the Django project: python manage.py runserver.

The Django server should be running locally now on http://127.0.0.1:8000 (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.

When you run the Django server for the first time, it should create a new SQLite3 database file: db.sqlite3.

Next, you'll need to make migrations to create the database schema: * python manage.py makemigrations * python manage.py migrate

Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:

python manage.py createsuperuser
Assign an admin username,email,and secure password.
Now you can run the program locally with the following command:

python manage.py runserver
Note - If you are having issues viewing static files you may need to collect static with the below command.

python3 manage.py collectstatic

### Heroku Deployment
To deploy FitnessPro  to heroku, take the following steps:
Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

Create a Procfile with the terminal command echo web: python app.py > Procfile.

git add and git commit the new requirements and Procfile and then git push the project to GitHub.

Sign up for a free Heroku account, Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub, and enable Automatic Deployment.

In the Heroku Resources tab, navigate to the Add-Ons section and search for Heroku Postgres. Select the free Hobby level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your .env file with your new database-url details. Confirm the linking of the heroku app to the correct GitHub repository.

In the heroku dashboard for the application, click on settings tab and then click on the Reveal config vars button to configure environmental variables.

Set the following config vars:

| Key |	Value |
|-----|-------|
|SECRET_KEY	|<your_secret_key>|
|STRIPE_PUBLIC_KEY |	<your_stripe_public_key> |
|STRIPE_SECRET_KEY |	<your_stripe_secret_key> |
|STRIPE_WH_SECRET | <your_stripe_wh_secret> |
| AWS_ACCESS_KEY_ID	| <your_secret_key> |
| AWS_SECRET_ACCESS_KEY	| <your_secret_key> |
| DATABASE_URL |	<your_postgres_database url> |
| EMAIL_HOST_USER	| <your_email_address> |
| EMAIL_HOST_PASS	| <your_password> |
| USE_AWS | <True> |
| DEVELOPMENT | <False> |

In the Heroku dashboard, click "Deploy"


In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

The site is now successfully deployed.


## Credits

### Content

The Project- Boutique Ado module in the Code Institute Full Stack Diploma in Software Development Program formed the basis for this project. 

This site [Tick Tock watches](https://ticktockwatches.herokuapp.com/) also provided me with some ideas.

## Acknowledgement
The tutors, mentors and support staff at Code Institute

Special thanks to Guido Cecilio Garcia, my Code Institute mentor, for his guidance and advice whilst working on this project.
