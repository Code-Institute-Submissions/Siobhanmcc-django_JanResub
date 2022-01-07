## Milestone Project - 4

This is the last milestone project for the Fullstack Web Developer course with Code Institute. The aim of the project is to showcase my skills learnt throughout this course.

Throughout this project I have used Python, a high-end programming language along with Django, a python framework.

The deployed site can be found [here](https://ms-4.herokuapp.com/)

## Table Of Contents

1. [UX](#ux)

- [User Stories](#user-stories)
- [Design](#design)
- [Framework](#framework)
- [Colour Scheme](#colour-scheme)
- [Icons](#icons)
- [Typography](#typography)
- [Wireframes](#wireframes)

2. [Features](#features)

- [Existing Features](#existing-features)

3. [Technologies Used](#technologies-used)

- [Front-End Technologies](#front-end-technologies)
- [Back-End Technologies](#back-end-technologies)

4. [Testing](#testing)

5. [Github Repository](#github-repository)

6. [Deployment](#deployment)

- [Heroku Deployment](#heroku-deployment)
- [Setting Up S3](#setting-up-s3)
- [Setting Up IAM](#setting-up-iam)
- [Connect Django to S3](#connect-django-to-s3)
- [Adding and Committing Files](#adding-and-committing-files)
- [Cloning](#cloning)

7. [Credits](#credits)

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

### Colour Scheme
For the colour scheme, I've used davy's grey #555555 and black #000000 in the navbar and most pages. I chose green #198754 and blue #2596be for some icons to highlight. Overall, I tried to keep a simple classic look.

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

- [Python 3.2.0](https://www.python.org/) - Used as the back-end programming language.
- [Django](https://docs.djangoproject.com/en/3.2/) - Used as my Python web framework.
- [Heroku](https://dashboard.heroku.com/) - for deployment
- [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.
- [AWS S3 Bucket](https://aws.amazon.com/) - Used to store images entered into the database.


## Testing

### Validation Services
HTML: I have used https://validator.w3.org/ in order to validate the HTML code.

CSS: I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.

JavaScript: I have used https://jshint.com/ in order to check the JavaScript code.

Python: I have used http://pep8online.com/ to validate Python code. 

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

## Deployment
### Heroku deployment
This project is hosted by Heroku but is still deployed from the master branch of a GitHub repository. The following steps were taken to deploy this project to Heroku:

1. Went to Heroku and logged in.
2. Created a new app by clicking create new app from the drop down menu labelled "new".
3. Gave my app a name and selected the region from the dropdown menu that was closest geographically.
4. Clicked the create app button where I was directed to the dashboard for the new app.
5. Clicked on the resources tab on the dashboard. Added Heroku Postgres to the app by searching and then selecting it. I then selected the Hobby Dev – Free plan.
6. As I didn't use fixtures to populate my development database I now created three json files, which act as fixtures and will help transfer the data across to the Postgres database.
- python3 manage.py dumpdata products.Category > categories.json
- python3 manage.py dumpdata products.Product > products.json
7. Installed dj_database_url and psycopg2-binary using pip3 install.
8. In settings.py I imported dj_database_url at the top of the file.
9. Then replaced the default DATABASE setting with:
`DATABASES = {
        'default': dj_database_url.parse(<DATABASE_URL>)
    }`
The <DATABASE_URL> is found in the Heroku apps Config Vars. It's important that you don't commit this url into version control!

10. I ran migrations using python3 manage.py migrate to create the models in the new database.
11. I now used the json files created in step 6 to populate the new database. 
- python3 manage.py loaddata categories.json
- python3 manage.py loaddata products.json
11. Then I created a new superuser, this was done by using python3 manage.py createsuperuser and then following the instructions shown in the terminal.
12. Installed gunicorn using pip3 install.
13. Used pip3 freeze > requirements.txt, this stores all our apps requirements.
14. Created a Procfile and populated it with:
`web: gunicorn <app_name>.wsgi:application`
15. I logged into Heroku but this time via the terminal using heroku login -i.
16. Then I used heroku config:set COLLECTSTATIC=1 --app <app_name> to disable static files from being collected. This is only a temporary measure.
17. Added the hostname of the Heroku app to ALLOWED_HOSTS in settings.py
`ALLOWED_HOSTS = ['<hostname>', 'localhost']`
18. Returned to the Heroku dashboard, clicked on the deploy tab, scrolled down to the “Deployment method” section and clicked the connect to GitHub button.
19. I searched for my repository in the “Connect to GitHub” section, found it and clicked connect.
I then enabled Automatic Deploys.
20. At the top of the dashboard I selected the settings tab. Scrolled down to the Config Vars section and populated the section with the key value pairs of the following:
- AWS_ACCESS_KEY_ID - I get this when I set up AWS.
- AWS_SECRET_ACCESS_KEY - I get this when I set up AWS.
- DATABASE_URL - Prepopulated.
- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET
- USE_AWS - True
- EMAIL_HOST_USER
- EMAIL_HOST_PASS
21. I changed the default DATABASE setting we created in step 9 in settings.py so that it now retrieves the value from Heroku:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    ```
22. Added, committed and pushed all files via the terminal.
23. Heroku is now set up and the app visible. It will automatically update whenever commits are pushed to Github via the IDE.

### Setting Up S3
1. Create an AWS account.
2. Navigate to the management console, search for "S3" to be taken to the S3 dashboard.
3. Click create bucket button.
 - Give it a name and select the region closest to you.
 - Allow public access.
4. In the bucket's properties select static website hosting.
- Select "use this bucket to host a website".
- Give it the default values of index.html and error.html then save.
5. For the buckets permissions CORS configuration use:
`[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]`
6. For the buckets permissions policy:
- Copy the Amazon resource name (ARN) from the top of the page.
- Click "policy generator".
- Select type of policy as "S3 Bucket Policy".
- Allow all principals by using *.
- Set action to "GetObject".
- Paste in the ARN.
- Click Add statement. Then Generate policy and copy the json file shown.
- Paste this json file to bucket policy.
- Add /* at the end of the 'Resource' key.
- Save.
7. For the access control list:
- Set list objects to everyone.

### Setting up IAM (Identity and Access Management)
1. From the AWS management console, search for "IAM" to be taken to the IAM dashboard.
2. Creating a group:
- Select "Groups" from the menu.
- Click the Create new group button.
- Name the group.
3. Creating a policy:
- Select "Policies" from the menu.
- Click the Create policy button.
- Select the JSON tab and click the "import managed policy" link.
- Find and import Amazon S3 Full Access.
- In the 'Resource' key of the json code shown paste in the ARN from the bucket policy twice forming a list.
- Add /* to the end of one.
- Review the policy and give it a name and a description.
- Create policy.
4. Attaching the policy to the group:
- Select "Groups" from the menu and select the group created in step 2.
- Click the Attach policy button.
- Select the policy created in step 3.
- Attach policy.
5. Creating a user:
- Select "Users" from the menu.
- Click the Add user button.
- Create a user by giving them a name.
- Grant the programatic access and click Next.
- Select the group shown that has the policy attached.
- Create user.
6. Download the .csv file.

### Connect Django to S3
1. Install boto3 by using pip3 install boto3.
2. Install django-storages by using pip3 install django-storages.
3. Run pip3 freeze > requirements.txt.
4. Add 'storages' to the apps list in settings.py.
5. Add the values of AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to Config Vars in Heroku.
- These values are in the downloaded .csv file.
6. Delete the DISABLE_COLLECTSTATIC variable.
7. Create a file called custom_storages.py and populate it like so:

~~~
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION


8. Add the following to settings.py.
~~~
   if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = '<aws_bucket_name>'
    AWS_S3_REGION_NAME = '<aws_region>'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/' ~~~

9. Add, commit and push all via the terminal.

### Adding and committing files
I’ve been using Gitpod to write my code and using the terminal to add, commit and push code from my workspace to GitHub where it is stored remotely as shown in the course content.

1. Typing git add into the terminal will move files to the staging area. You should normally do this once a couple of minor additions or changes have been made or one large change or addition has been made. git add . will add all files that have been modified, the full stop here means all. If I want to be more selective I can type in the file name e.g. index.html or the files pathway e.g. assets/css/style.css instead of the full stop e.g. git add index.html.
2. To send these changes to the local repository we use git commit. Normally you'll want to include a brief description of these changes so instead use git commit –m “ ”. Between the “ ” write a clear, concise message detailing what this commit has done.
3. To view the changes on Heroku or when you want to send your work to the remote repository (GitHub in this instance) then use the git push command. This pushes all the previous commits made to the remote repository. While deploying to Heroku we set it so it'll automatically pick up any changes pushed to our GitHub repository and once Heroku has finished building (this takes a couple of mins) it'll display the most up to date version of the site.

### Cloning
You can clone a repository so that it can be worked on locally in an IDE such as VSCode by following these steps:

1. Log in to GitHub and navigate to the repository you wish to clone.
2. Click the button that reads code. This button is situated to the left of the green Gitpod button near the top of the page.
3. To clone the repository using HTTPS, copy the link shown whilst HTTPS is selected. The link will look something like this: https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
4. Open your local IDE and in the terminal navigate to the working directory of where you wish to insert the cloned directory.
5. Type git clone followed by the link you copied in step 3 into the terminal, this will look something like this: git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
6. Press enter and the clone will be created in your selected / current working directory (cwd).
7. A new env.py file will have to be created to include all the environment variables used throughout and should look like below.
- Both STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY can be found on the Developers dashboard once logged into Stripe.
- The STRIPE_WH_SECRET can be found once a new endpoint has been created in Developers > Webooks.
 a. Click on the 'Add endpoint' button.
 b. Enter the URL of your localhost followed by /checkout/wh/ as your endpoint URL.
 c. Select all events to listen to and click on the 'Add endpoint' button.
 d. The value for STRIPE_WH_SECRET can now be found by clicking the 'reveal' link under the signing secret tab on the webhook's dashboard.
- Add env.py to the .gitignore file so it doesn’t get published in version control.

    import os

    os.environ.setdefault(“SECRET_KEY”,  “<secret key>”)
    os.environ.setdefault(“DEVELOPMENT”, “True”)
    os.environ.setdefault(“STRIPE_PUBLIC_KEY”, “<key from stripe developers dashboard>”)
    os.environ.setdefault(“STRIPE_SECRET_KEY”, “<key from stripe developers dashboard>”)
    os.environ.setdefault(“STRIPE_WH_SECRET”, “<key from individual webhook>”)

8. You will need to reinstall all the dependencies used, you can do this by running the following pip3 install -r requirements.txt in the terminal.
9. You will then need to migrate the database by typing python3 manage.py migrate in the terminal.
10. A new superuser will now need to be created, this can be done by typing python3 manage.py createsuperuser in the terminal and following the instructions shown.
11. The site is now cloned… Use the command python3 manage.py runserver to run it.

## Credits

### Content

The Project- Boutique Ado module in the Code Institute Full Stack Diploma in Software Development Program formed the basis for this project. 

This site [Tick Tock watches](https://ticktockwatches.herokuapp.com/) also provided me with some ideas.

## Acknowledgement
The tutors, mentors and support staff at Code Institute

Special thanks to Guido Cecilio Garcia, my Code Institute mentor, for his guidance and advice whilst working on this project.
