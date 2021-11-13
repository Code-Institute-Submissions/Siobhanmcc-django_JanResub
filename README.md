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
For the color scheme, I've used grey and black in the navbar and most pages. I chose green for some icons to highlight. Overall, I tried to keep a simple classic look.

### Icons
[Font Awesome 5.15](https://fontawesome.com/)

I used Font Awesome icons for throughout this project.

### Typography
The following fonts were used :

Helvetica Neue"
Helvetica 
sans-serif

Wireframes
Mock-ups were created early on in this project.

I've used Balsamiq Wireframes during the Scope Plane part of the design and planning process for this project.

All of my wireframes for this project can be found here

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

## Checkout App
### checkout.html

Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity.

The user needs to fill out the payment form in order to go for the payment.

Once the payment is successfull, a message will be displayed.

If there is an error with the payment, the user will be notified with an error message.

## Search App
This will allow the user to search for a product based on the title.

The search icon is visible from all the pages. 

## Base Template
Features available from all the pages

Navbar

In order to create the navbar I have used Bootstrap 4 and the navbar is available in all the pages.

The nabar features the logo and the product menu on the left.

On the right side of the navbar, the user can see the search bar, the My Account heading and the Shopping Cart icon.

A user who is currently logged in will see options to see their profile page or log out.

A user who is logged out will see options to register or log in to the website.

The shopping cart icon can lead to cart page. Once the user has added at least one item to their cart the $ value of the cart will appear under the shopping cart icon.

The search bar enables the user to type in their relevent product search.


