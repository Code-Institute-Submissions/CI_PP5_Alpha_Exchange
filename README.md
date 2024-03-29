# Alpha-Exchange
(Developer: Benjamin Draper)

![Mock-up image](documentation/wireframes/am-i-responsive.jpg)

[Live webpage](https://alpha-exchange.herokuapp.com/)

## About
Alpha Exchange is an E-commerce website aimed at B2C sales with a drop shipping style model, this website mainly features clothing, home-wear and accessories. the website is designed to allow users to experience a fully featured shopping experience where you can easily find known products, search for new or similar products, filter by categories or browse through the new arrivals and clearance sections.

### User Information
A regular user has been setup with the following details for testing the website.
- Username: test_user
- Password: TestPassword123

### Card Information
- Test Card Number: 4242 4242 4242 4242 
- Expiration Date: Any future date (e.g. 02/42) 
- CVC: Any three digits (e.g. 424)

## Table of Content
1. [Project Goals](#project-goals)
    1. [Website User Goals](#website-user-goals)
    2. [Website Owner Goals](#website-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [Business Model](#business-model)
    4. [SEO](#seo)
    5. [Marketing](#marketing)
3. [User Stories](#user-stories)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Database](#database)
    6. [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
6. [Features](#features)
7. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [JavaScript Validation](#javascript-validation)
    4. [Python Validation](#python-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Device Testing](#device-testing)
    8. [Browser Compatibility](#browser-compatibility)
8. [Testing user stories](#testing-user-stories)
9. [Automated Testing](#automated-testing)
10. [Bugs](#bugs)
11. [Google emails](#google-emails)
12. [Stripe](#stripe)
11. [Deployment](#deployment)
13. [Credits](#credits)
13. [Acknowledgements](#acknowledgements)

## Project Goals
### Website User Goals
- As a website user, I want to be able to have easy options to navigate around the website.
- As a website user, I want to be able to view the products available on the website.
- As a website user, I want to be able to apply filters to the products.
- As a website user, I want to be able to search for specific products.
- As a website user, I want to be able to contact the site owner if I have any questions.
- As a website user, I want to be able to add items to a basket and checkout my order.
- As a website user, I want to be able to register for an account.
- As a website user, I want to be able to log in and out of my existing account.
- As a website user, I want to be able to review past orders I have made from my account.
- As a website user, I want to be able to sign up to a newsletter.
- As a website user, I want to be able to view and edit my profile.

### Website Owner Goals
- As the website owner, I want to allow users to navigate the website with ease.
- As the website owner, I want to allow users to view the product details.
- As the website owner, I want to allow users to be able to add items to the basket and purchase items.
- As the website owner, I want to allow users to create an account.
- As the website owner, I want to allow users to sign in and out when they return to the website.
- As the website owner, I want to promote the website to new and existing users.
- As the website owner, I want to allow users to see their order history.
- As the website owner, I want to allow users to sign up for a news letter.
- As the website owner, I want to be able to add, edit and delete items from the website myself.

[Back to Table Of Content](#table-of-content)

## User Experience
### Target Audience
- This website is targets people are looking to buy clothing.
- This website is targets people are looking to buy accessories.
- This website is targets people are looking to buy gifts for friends and family.
- This website is targets people are looking to sign up to the newsletter.
- This website is targets people are looking to discover what we currently have to offer.

### User Requirements and Expectations
- The user can expect an intuitive and accessible navigation system.
- The user can expect to easily find the products available.
- The user can expect to easily find specific products they are looking for through filtering and the search function.
- The user can expect all links work as expected and functions perform their tasks correctly.
- The user can expect presentation is in line with the website guidelines and the website is visually appealing on all screen sizes.
- The user can expect easy to read headings to tell the users at a glance what they are looking at.
- The user can expect accessibility features to be clearly defined.
- The user can expect to be able to complete any purchase made and track previous orders through their account.
- The user can expect to be able to contact the business for further queries.

### Business Model
This website is primarily aimed at selling to consumers, for this I have chosen a B2C business model. To make the website more consumer friendly I have made sure that all design decisions, pictures, navigation and ease of purchase is made with the end user in mind.

The business model is that this website would able to be used as a dropshipping website where the website owner does not need to handle inventory and the products can be sent straight from the supplier to the customer.

As an alternative the website owner could buy the product and arrange the shipping of orders themselves, this does mean any returns also get handled by the website owner.
For This project I have chosen for the stock to be handled by a third party.

### SEO
Long tag keywords and short tag keywords were searched for in regards to SEO using Google tools and other online resources. These tags are included within the main HTML head and in the appropriate places within the project to name images and within main body text.

I also made included the categories within the meta tag keywords so that as these are updates the keywords will also be updated.

![SEO keywords HTML](/documentation/misc/keywords.jpg)

### Marketing
#### Facebook Page
To help market the website, the website includes a like to its own social media page in the footer where new products and announcements are made.
the Facebook page can be viewed [here](https://www.facebook.com/profile.php?id=100087950336068).

![Facebook Screenshot](/documentation/misc/facebook.jpg)

#### Newsletter Sign up
The website includes a sign up form to a newsletter so the business can keep in touch with anyone who want more information. I used [SendinBlue](https://www.sendinblue.com) to create a form and preform the automation required to reply with an email to the given address.

SendInBlue was used to make this form over any other service as i already had an account and i ran into issues during sign-up with other services at the time, hopefully these will be resolved in due course. SendInBlue has added a large performance hit seen later in Googles Lighthouse reports where the Newsletter form has a significant amount of JS that needs to load.

![Sign-up](/documentation/misc/email-signup.jpg)

![Email-success](/documentation/misc/email-success.jpg)

[Back to Table Of Content](#table-of-content)

## User Stories
### Unauthenticated Users
1. As a unauthenticated user, I would like to be able to navigate through the website easily so that it is easy to find the information I am looking for.
2. As a unauthenticated user, I would like to be able to sign up for an account so that I can view my profile and track my orders.
3. As a unauthenticated user, I would like to see the available products that are listed on the website so that I can see what is currently in available.
4. As a unauthenticated user, I would like to know how to find social media links so that I can find out about new products and news.
5. As a unauthenticated user, I would like to be able to search or filter the website for specific products and brands so that I can find exactly what i am looking.
6. As a unauthenticated user, I would like to be able to sort and view products by category so that I can find specific products easily.
7. As a unauthenticated user, I would like to be able to order the products on a page a variety of ways so that I can find what I am looking for easier.
8. As a unauthenticated user, I would like to be able to see detailed description of the products available so that i can make an informed purchase.
9. As a unauthenticated user, I would like to be able to add a product to my basket so that I can purchase them.
10. As a unauthenticated user, I would like to be able to see the products that are in my basket so that I don't spend too much.
11. As a unauthenticated user, I would like to be able to increase and decrease quantities and remove items from my basket so that I don't have to navigate to the store and add the item again each time.
12. As a unauthenticated user, I would like to be able to purchase the items in my basket so that I can complete my order.
13. As a unauthenticated user, I would like to be able to log in to / sign out of an existing account so that I can get updated on my orders.
14. As a unauthenticated user, I would like to be able contact the business so that I can ask any questions.
15. As a unauthenticated user, I would like to be able to sign up to the newsletter so that I can receive news and updates from the business.
### Authenticated Users
16. As a authenticated user, I would like to be able to view and update my personal information so that I do not have to fill it out each time I make an order.
17. As a authenticated user, I would like to be able to view my order history so that i can find products i have ordered before and would order again.
### Website Staff
18. As a website staff user, I would like to be able to use full CRUD functionality so that I can update the product range available.
19. As a website staff user, I would like to be able to manage product inventory so that I can adjust the available products.
20. As a website staff user, I would like to be able to view and update product categories so that the product range is up to date.
21. As a website staff user, I would like to be able to add product categories so that new products are available on the website.
22. As a website staff user, I would like to be able to delete product categories so that products that are no longer available are removed.
### Website Owner
23. As the website owner, I want the products divided into categories so that users looking for something specific can navigate easier.
24. As the website owner, I want the website to act responsively to all device sizes so that the website can be viewed across all devices.
25. As the website owner, I want users to get redirected to custom error pages so that they understand when when something has gone wrong and can be redirected back to the main website.
26. As the website owner, I want users to be able to navigate the website quickly and easily so that they are able to find what they are looking for.
27. As the website owner, I want users to be sign up to a newsletter to capture user information and bring users back to the website.
28. As the website owner, I want users to be able to view the business social media so that users are made aware of the products on offer and kept up to date with any news.
### All Users
29. As a user, I would like to have a confirmation message that my order has been successful so that I am made aware once the transaction has taken place successfully.
30. As a user, I would like to be shown descriptive messages telling me that my actions have been successful or unsuccessful when I preform an action so that I can act accordingly.
31. As a user, I would like to be able to navigate back to the main website structure if an error occurs and I end up on the 404 page so that i can continue shopping without issues.
32. As a user, I would like to be able to find a description of the business and an FAQ section so that I can find the answers I need.

### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/users/benjamindraper1996/projects/5/views/1)

[Back to Table Of Content](#table-of-content)

## Design
### Design Choices
The aim of the design of the website is to create an easy to navigate, clean, modern and responsive design. Any imagery featured on the website is used in a way that promotes the business values and creates a positive response from the user.

### Colour
For the color scheme I have opted to implement a dark and light theme while using colours that compliment the goals and ambitions of the website. To narrow down the choice of colours I used [coolors](https://coolors.co/) an example of both the dark and light theme are shown below.

#### Dark Mode
![Dark Mode Theme](documentation/features/colour-palette-dark.jpg)
#### Light Mode
![Light Mode Theme](documentation/features/colour-palette-light.jpg)

### Fonts
I am using Inter font with a backup of sans-serif across the website. This is used to maintain a Consistent and professional look with an easily readable format.

### Structure
The website has been built using a template engine so that all pages follow the same design to maintain the feel across the website.

The project was also built using a variety of apps constructed using django framework, these apps allow for easy update to a small area of the site without effecting the performance of other apps.

The Apps within the website are as follows:
- About - The about app is used to give the customer information about the business and easily update the FAQ section.

- Basket - The basket app is used to store the users current shopping basket, display the cost and calculate the sizes and quantity of each item.

- Checkout - The checkout app is used to take the items in the current shopping basket and place the order on the website, this utilizes Stripe's checkout functionality.

- Contact - The contact app is used to allow customers to send a message to the admin team, making use of the UserAccount if they are logged in to fill out some of the form.

- Home - The home app creates the main landing page for the website and includes links to the rest of the website, this is used to entice users into exploring our products further.

- Products - The products app is used to set up the categories, products and reviews that the user will see on the website. the categories and products are setup by the admin team and can be managed from both the admin panel or directly on the website when signed into an admin account. The reviews model provides a form for users to fill out if they want to tell everyone about how great a specific product is.

- Users - The users app is used to extend the functionality of the base django User model, this allows me to store the users personal and shipping details so they can be used to fill out other forms when needed.

In addition to these apps there are a number of files and directories used at the base level.
- Template - The templates allow for us to write less code by creating one basic page that all other pages can then extend with their own content.

- URL's - Each app has been given its own url file which is 'included' within the project level URLS's this helps with the modularity of the website and allows us to add or remove items when needed.

- Settings - The settings file is stored in the project directory so that any items that rely upon specific settings can be updated from one place instead of each app.

- static and media - there are a number of files stored at the base level, including the base CSS for the website, this contains most the code that is needed across the whole site or multiple apps, we also put some JS files in base folder so these will be available to all pages. We also have a number of media files that can be found at the root, these are best served from the root directory so that all pages can access the information it needs.

- Procfile - This is the file that will launch the website when using Heroku.

- Requirements - The requirements.txt file stores all the information about the packages needed for the website to function correctly.

The Pages are structured in a Regularly used, user friendly and well-known format. This makes each page easy to navigate, coupled with a responsive navbar and footer this gives the user many options for navigating around the website.

The website consists of 22 pages and 4 error pages(400, 403, 404, 500).
1. Home page
2. All products
3. Search products
4. Product details
5. Product categories
6. Categories page
7. Log in
8. Log out
9. Register
10. Profile page
11. Order history
12. Basket
13. Checkout
14. Checkout Success
15. Contact us
16. About us
17. Add products page
18. Edit products page
19. Delete products page
20. Add categories page
21. Edit categories page
22. Delete categories page
23. Error page(s)

### Database
The website was built using Python and the Django framework with a postgres database to store all of our information.
<details><summary>Database Diagram</summary>
<img src="documentation/wireframes/database.jpg">
</details>

The following models were created to represent the real database model structure within the website database.

### Faq
- The Faq model is used to hold the information for the FAQ section on the about us page.
- The Faq model is setup to hold a title, friendly title, question and answer to be displayed within the accordion.

### Order
- The Order model is used to hold information relating to each order placed on the website.
- The Order model holds information like, name, address, order details including the basket and stripe information and also a ForeignKey to the user's account.

### OrderLineItem
- The OrderLineItem Model is used to calculate the details of each item on the order.
- The OrderLineItem Model calculates the number of items on an order, by size and quantity, then passing the details to the order model to update the total price.

### Contact
- The Contact model is used to store messages from visitors to the website.
- The Contact model takes basic information like the name, address and message for the admin's to read later.

### Category
- The Category model sets up the categories available for visitors to browse through and split products into.
- The Category model contains a name, friendly name and image field.

### Product
- The product model contains information relating to the creation of new products.
- The product model information for the product name, category, sku, description, price, rating, image, sizes, use, number of likes and a featured field.
- The Product model is able to generate its sku number when a product is created if the user has not filled one in.

### Review
- The Review model is setup for users to be able to leave a review of a product.
- The Review model contains information author, message, time, title and approved status.
- The Review model uses the approved boolean field so that if a user puts a review on the website that should be removed, we can prevent the review appearing to visitors.

### UserAccount
 - The UserAccount model is used to extend the functionality of the base django User model
 - The UserAccount model adds functionality so that allows us to store the delivery information so users do not have to enter it every time.

### Wireframes

Some pages share the same design and thus are not shown, these include, the error pages where only the message changes, the product pages where the visible products change but the layout is the same and the category pages where the layout is the same but the information changes.

<details><summary>Home page</summary>
<img src="documentation/wireframes/home-page.png">
</details>
<details><summary>All products</summary>
<img src="documentation/wireframes/all-products.png">
</details>
<details><summary>Search products</summary>
<img src="documentation/wireframes/search-products.png">
</details>
<details><summary>Product details</summary>
<img src="documentation/wireframes/product-details.png">
</details>
<details><summary>Product categories list</summary>
<img src="documentation/wireframes/product-categories.png">
</details>
<details><summary>Category pages</summary>
<img src="documentation/wireframes/category-page.png">
</details>
<details><summary>Log in</summary>
<img src="documentation/wireframes/log-in.png">
</details>
<details><summary>Log out</summary>
<img src="documentation/wireframes/log-out.png">
</details>
<details><summary>Register</summary>
<img src="documentation/wireframes/register.png">
</details>
<details><summary>Profile page</summary>
<img src="documentation/wireframes/profile-page.png">
</details>
<details><summary>Order history</summary>
<img src="documentation/wireframes/order-history.png">
</details>
<details><summary>Basket</summary>
<img src="documentation/wireframes/basket.png">
</details>
<details><summary>Checkout</summary>
<img src="documentation/wireframes/checkout.png">
</details>
<details><summary>Checkout success</summary>
<img src="documentation/wireframes/checkout-success.png">
</details>
<details><summary>Contact us</summary>
<img src="documentation/wireframes/contact-us.png">
</details>
<details><summary>About us</summary>
<img src="documentation/wireframes/about-us.png">
</details>
<details><summary>Add products page</summary>
<img src="documentation/wireframes/add-product-page.png">
</details>
<details><summary>Edit products page</summary>
<img src="documentation/wireframes/edit-product-page.png">
</details>
<details><summary>Delete products page</summary>
<img src="documentation/wireframes/delete-product-page.png">
</details>
<details><summary>Add categories page</summary>
<img src="documentation/wireframes/add-categories-page.png">
</details>
<details><summary>Edit categories page</summary>
<img src="documentation/wireframes/edit-categories-page.png">
</details>
<details><summary>Delete categories page</summary>
<img src="documentation/wireframes/delete-categories-page.png">
</details>
<details><summary>Error page</summary>
<img src="documentation/wireframes/error-page.png">
</details>
<br>

[Back to Table Of Content](#table-of-content)

## Technologies Used
### Languages
- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [JavaScript](https://www.w3schools.com/js/default.asp)
- [Python](https://www.w3schools.com/python/default.asp)

### Frameworks and Tools
- [GitHub](https://github.com/) was used to maintain the version control and store the project remotely
- [Gitpod](https://gitpod.io/) was used to write all the code and to link up with Github to maintain the version control.
- [Balsamiq](https://balsamiq.com/) was use to create the wireframes for the website.
- [Google Fonts](https://fonts.google.com/) was used to pick out the fonts in use across the website.
- [Feather Icons](https://feathericons.com/) was used to select the favicon from their database.
- [Favicon](https://favicon.io/) was used to convert the raw svg file into a useable favicon image.
- [Coolors](https://coolors.co/) was used to generate a colour pallette.
- [Am I Responsive?](https://ui.dev/amiresponsive) was used to test the responsive nature of the website design.
- [Bootstrap](https://getbootstrap.com/) was used for the pre-defined components and responsive nature of the layout.
- [Heroku](https://dashboard.heroku.com/) was used to host the website for the additional back-end functionality.
- [Font Awesome](https://fontawesome.com/) - Font awesome was used for the icons on the website social media links.
- [JQuery](https://jquery.com) - JQuery was used in some javascript files for DOM manipulation.
- [W3C HTML Validator](https://validator.w3.org/) was used to validate the HTML
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
- [WAVE](https://wave.webaim.org/) was used to validate the accessibility of the website.
- [JShint](https://jshint.com/) was used to validate the Javascript.
- [Pycodestyle](https://pycodestyle.pycqa.org/en/latest/index.html) was used to validate the Python code.
- [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to validate the website performance, best practice and SEO.
- [Facebook](https://www.facebook.com) - was used to make a social media marketing page.
- [Stripe](https://stripe.com/gb) - was used to take payments for the website.
- [Amazon Web Services](https://aws.amazon.com/) - was used to host the static files.

### Libraries
- asgiref==3.5.2
- boto3==1.26.7
- botocore==1.29.7
- coverage==6.5.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- Django==3.2
- django-allauth==0.51.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-filter==22.1
- django-storages==1.13.1
- gunicorn==20.1.0
- jmespath==1.0.1
- oauthlib==3.2.1
- Pillow==9.2.0
- psycopg2==2.9.5
- PyJWT==2.5.0
- python3-openid==3.2.0
- pytz==2022.4
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- sqlparse==0.4.3
- stripe==5.0.0
- types-cryptography==3.3.23

[Back to Table Of Content](#table-of-content)

## Features
### Navbar / Dropdown Menu
- Featured on all pages across the website.
- The navbar / dropdown menu is fully responsive and changes to a hamburger style button for smaller screen sizes.
- The navbar / dropdown menu has a link to login or sign up for an account.
- The navbar / dropdown menu includes links to allow users to navigate around the website easily.
- The navbar / dropdown menu includes the dark theme switch toggler option for users that prefer to use a lighter of darker theme.
- user stories covered: 1, 24, 26
<details><summary>Navbar / Dropdown Menu Open</summary>
<img src="documentation/features/hamburger-open.jpg">
</details>
<details><summary>Navbar / Dropdown Menu Closed</summary>
<img src="documentation/features/hamburger-closed.jpg">
</details>
<details><summary>Navbar / Dropdown Menu Light</summary>
<img src="documentation/features/menu-light.jpg">
</details>
<details><summary>Navbar / Dropdown Menu Dark</summary>
<img src="documentation/features/menu-dark.jpg">
</details>
<br>

### Footer
- Featured across the whole website.
- The footer contains links to the websites social media handle.
- The footer contains Information on how to get in touch with support when needed.
- The footer is fully responsive down to mobile size devices.
- User stories covered: 1, 4, 14, 15, 24, 27, 28
<details><summary>Footer</summary>
<img src="documentation/features/footer.jpg">
</details>
<br>

### Newsletter E-mail List
- Featured across the whole website within the footer.
- The newsletter e-mail list allows users to sign up to a email list so that they can get updates on the products and news about the website.
- User stories covered: 15, 27
<details><summary>Newsletter E-mail List Sign up</summary>
<img src="documentation/misc/email-signup.jpg">
</details>
<details><summary>Newsletter E-mail Welcome</summary>
<img src="documentation/misc/email-success.jpg">
</details>
<br>

### Contact Us
- The contact us link is featured across the whole website within the navbar.
- The contact us page allows users to fill out that sends the team an email with their query.
- User stories covered: 14, 28
<details><summary>Contact Us</summary>
<img src="documentation/features/contact-us.jpg">
</details>
<br>

### About Us
- The about us link is featured across the whole website within the footer.
- The about us page features a description of the website and the business to entice users into buying the products available.
- The about us page also features a FAQ section to answer any regularly asked questions without the need to fill out the contact form.
- User stories covered: 32
<details><summary>About Us</summary>
<img src="documentation/features/about-us.jpg">
</details>
<br>

### User Registration
- The user registration form allows users to create an account to interact with the community.
- When a user registers for an account they are able to view and edit their profile information.
- When a user registers for an account they are able to view previous orders and the items attached to the order.
- The user registration form is fully responsive down to mobile size devices.
- User stories covered: 2
<details><summary>User Registration</summary>
<img src="documentation/features/user-registration.jpg">
</details>
<br>

### User Login
- The user login form allows users to login to an existing account to interact with the community.
- When a user login for an account they are able to view and edit their profile information.
- When a user login for an account they are able to view previous orders and the items attached to the order.
- The user login form is fully responsive down to mobile size devices.
- User stories covered: 13
<details><summary>User Login</summary>
<img src="documentation/features/user-login.jpg">
</details>
<br>

### Categories
- The categories are shown on separate a navbar allowing users to filter the products by what category are looking for.
- The categories navbar displays a list of only the current categories, if any are added or removed the list will update.
- User stories covered: 5, 6, 23, 26
<details><summary>Categories Page</summary>
<img src="documentation/features/categories-page.jpg">
</details>
<details><summary>Menu Categories</summary>
<img src="documentation/features/menu-categories.jpg">
</details>
<br>

### Category Management
- The category management option features in the staff and admin account options.
- The category management allows staff and admins to edit the current categories, add or remove new or old ones.
- User stories covered: 20, 21, 22
<details><summary>Add Category</summary>
<img src="documentation/features/category-add.jpg">
</details>
<details><summary>Update Category</summary>
<img src="documentation/features/category-update.jpg">
</details>
<details><summary>Delete Category</summary>
<img src="documentation/features/category-delete.jpg">
</details>
<br>

### All Products
- The product page is used to display all products that the website has available.
- The product page can be navigate to from the header and is ordered by rating as a default.
- User stories covered: 3, 5, 6, 7
<details><summary>All Products</summary>
<img src="documentation/features/all-products.jpg">
</details>
<br>

### Product Details
- The product details page is used to display the product details for a specific item.
- The product details page can be navigate to from any item on the store by selecting it.
- User stories covered: 3, 8
<details><summary>Product Details</summary>
<img src="documentation/features/product-details.jpg">
</details>
<br>

### User Reviews
- The User Reviews are featured on the Product Details page, underneath the product it relates to.
- The User Reviews allow customers to share their experience and give other shoppers a true representation of the product and what to expect so they arent spending too much time looking at the wrong items.
- User stories covered: 8, 26
<details><summary>User Reviews</summary>
<img src="documentation/features/user-reviews.jpg">
</details>
<br>

### Page Ordering
- The product pages used to display all products that the website has available can be re-ordered by the user to help them find what they are looking for.
- The product pages can be re-ordered from the dropdown box located on the products page.
- User stories covered: 6, 7
<details><summary>Page Ordering</summary>
<img src="documentation/features/page-ordering.jpg">
</details>
<br>

### Create Product
- The create product option features in the staff and admin account options.
- The create product option allows staff and admins to create new products for the store.
- User stories covered: 18, 19
<details><summary>Create Product</summary>
<img src="documentation/features/create-product.jpg">
</details>
<br>

### Edit Product
- The edit product option features on the products page only for staff and admin users.
- The edit product option allows staff and admins to update the details of the products on the store.
- User stories covered: 18, 19
<details><summary>Edit Product</summary>
<img src="documentation/features/product-update.jpg">
</details>
<br>

### Delete Product
- The delete product option features on the products page only for staff and admin users.
- The delete product option allows staff and admins to delete the products on the store with confirmation to avoid accidental deletion.
- User stories covered: 18, 19
<details><summary>Delete Product</summary>
<img src="documentation/features/delete-product.jpg">
</details>
<br>

### Product Search
- The product search is used to find specific products that the customer is looking for.
- The product search is part of the header and is featured on all pages of the website.
- The product search works by using keywords to filter the products to what it feels is relevant to the user.
- User stories covered: 1, 3, 5, 6, 7
<details><summary>Product Search Box</summary>
<img src="documentation/features/product-search-box.jpg">
</details>
<details><summary>Product Search Result</summary>
<img src="documentation/features/product-search-result.jpg">
</details>
<br>

### Shopping Basket
- The shopping basket is used to hold a list of products the user is looking to purchase.
- The shopping basket is can be used to adjust quantities and remove products from the basket entirely.
- The shopping basket can be found within the header on every page and links to a separate detailed page with all the items in the basket.
- User stories covered: 9, 10, 11, 12
<details><summary>Shopping Basket Desktop</summary>
<img src="documentation/features/shopping-basket-desktop.jpg">
</details>
<details><summary>Shopping Basket Mobile</summary>
<img src="documentation/features/shopping-basket-mobile.jpg">
</details>
<br>

### Stripe Checkout
- The stripe checkout page is used to securely handle card information.
- The stripe checkout link is part of the shopping basket page and the user can choose to checkout when ready.
- The stripe checkout page contains a form for users to fill out their payment details.
- The stripe checkout page form is pre-filled for authenticated users who have purchased products on the store before.
- The stripe checkout Page shows a list of the items in the basket and the total cost.
- User stories covered: 12, 16, 29
<details><summary>Stripe Checkout</summary>
<img src="documentation/features/stripe-checkout.jpg">
</details>
<br>

### Profile Page
- The profile page is used to view a users profile information, liked products and order history.
- From the profile page a user is able to update their personal details, navigate to their liked items and view a previous order details.
- User stories covered: 16, 17
<details><summary>Profile Page</summary>
<img src="documentation/features/profile-page.jpg">
</details>
<br>

### Order History
- From the profile page a user is able to see their order history and select the items they previously ordered.
- The order history includes all the details of the order including the order number, products, cost , delivery and billing information.
- User stories covered: 17
<details><summary>Order History</summary>
<img src="documentation/features/order-history.jpg">
</details>
<br>

### Message Popups
- The message popups feature is used to inform the user when a specified action has taken place and the action was applied.
- The message popups feature is used to inform the user when an error has happens and that the action has not been applied.
- The message popups feature is located in the top right corner of the screen and is closed manually by the user or on a new page load.
- User stories covered: 29, 30
<details><summary>Message Popups</summary>
<img src="documentation/features/message-popups.jpg">
</details>
<br>

### Error Pages
- The custom Error pages are used to replace the standard error pages from django.
- The custom Error pages cover 400, 404, 403 and 500 errors, these templates look the same with slight variance for the error.
- The featured recipes list is fully responsive down to mobile size devices.
- User stories covered: 1, 25, 26, 31
<details><summary>Error Pages</summary>
<img src="documentation/features/error-page.jpg">
</details>
<br>

[Back to Table Of Content](#table-of-content)

## Validation
### HTML Validation
I used the W3C Validation Service to validate the HTML of the website.
All pages passed with no errors, These were run by direct input after viewing the page source allowing django to combine the templates into the final version the browser will display.

<details><summary>Home page</summary>
<img src="documentation/validation/html/home-page.jpg">
</details>
<details><summary>All products</summary>
<img src="documentation/validation/html/all-products.jpg">
</details>
<details><summary>Search products</summary>
<img src="documentation/validation/html/search-products.jpg">
</details>
<details><summary>Product details</summary>
<img src="documentation/validation/html/product-details.jpg">
</details>
<details><summary>Product categories list</summary>
<img src="documentation/validation/html/product-categories.jpg">
</details>
<details><summary>Category pages</summary>
<img src="documentation/validation/html/category-page.jpg">
</details>
<details><summary>Log in</summary>
<img src="documentation/validation/html/log-in.jpg">
</details>
<details><summary>Log out</summary>
<img src="documentation/validation/html/log-out.jpg">
</details>
<details><summary>Register</summary>
<img src="documentation/validation/html/register.jpg">
</details>
<details><summary>Profile page</summary>
<img src="documentation/validation/html/profile-page.jpg">
</details>
<details><summary>Order history</summary>
<img src="documentation/validation/html/order-history.jpg">
</details>
<details><summary>Basket</summary>
<img src="documentation/validation/html/basket.jpg">
</details>
<details><summary>Checkout</summary>
<img src="documentation/validation/html/checkout.jpg">
</details>
<details><summary>Checkout success</summary>
<img src="documentation/validation/html/checkout-success.jpg">
</details>
<details><summary>Contact us</summary>
<img src="documentation/validation/html/contact-us.jpg">
</details>
<details><summary>About us</summary>
<img src="documentation/validation/html/about-us.jpg">
</details>
<details><summary>Add products page</summary>
<img src="documentation/validation/html/add-product-page.jpg">
</details>
<details><summary>Edit products page</summary>
<img src="documentation/validation/html/edit-product-page.jpg">
</details>
<details><summary>Delete products page</summary>
<img src="documentation/validation/html/delete-product-page.jpg">
</details>
<details><summary>Add categories page</summary>
<img src="documentation/validation/html/add-categories-page.jpg">
</details>
<details><summary>Edit categories page</summary>
<img src="documentation/validation/html/edit-categories-page.jpg">
</details>
<details><summary>Delete categories page</summary>
<img src="documentation/validation/html/delete-categories-page.jpg">
</details>
<details><summary>Error page</summary>
<img src="documentation/validation/html/error-page.jpg">
</details>
<br>

### CSS Validation
I used the W3C Jigsaw CSS Validation Service to validate the CSS of the website.
My CSS passed with no errors and warnings to show.
<details><summary>Base CSS</summary>
<img src="documentation/validation/css/base-css.jpg">
</details>
<details><summary>Basket CSS</summary>
<img src="documentation/validation/css/basket-css.jpg">
</details>
<details><summary>Checkout CSS</summary>
<img src="documentation/validation/css/checkout-css.jpg">
</details>
<details><summary>Contact CSS</summary>
<img src="documentation/validation/css/contact-css.jpg">
</details>
<details><summary>Products CSS</summary>
<img src="documentation/validation/css/products-css.jpg">
</details>
<details><summary>Users CSS</summary>
<img src="documentation/validation/css/users-css.jpg">
</details>
<br>

### JavaScript Validation
JSHint Static Code Analysis Tool for JavaScript was used to validate the Javascript file.
All files with no errors.

The warnings from the stripe.js toasts.js and sendinblue.js are caused by unused variables however these are called from outside of the script, on the html and so this is not an issue.

Thw warnings from the qty-box.js are from the if/else loops where the code cycles and finds the values already defined, this is nto a problem as it will overwrite any previous values and during testing this preformed well.

<details><summary>Theme Switch</summary>
<img src="documentation/validation/js/theme.jpg">
</details>
<details><summary>Toasts</summary>
<img src="documentation/validation/js/toasts.jpg">
</details>
<details><summary>SendinBlue</summary>
<img src="documentation/validation/js/sendinblue.jpg">
</details>
<details><summary>Qty Box</summary>
<img src="documentation/validation/js/qty-box.jpg">
</details>
<details><summary>Sort Box</summary>
<img src="documentation/validation/js/sort-box.jpg">
</details>
<details><summary>Stripe Elements</summary>
<img src="documentation/validation/js/stripe-elements.jpg">
</details>
<details><summary>Basket Qty</summary>
<img src="documentation/validation/js/basket-qty.jpg">
</details>
<br>

### Python Validation
I used the PEP8 Validation Service from CI to validate the python code for the website.
My code passed with no errors and warnings to show.

<details><summary>About App</summary>
<details><summary>admin.py</summary>
<img src="documentation/validation/python/about-admin.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/about-views.jpg">
</details>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/about-urls.jpg">
</details>
<details><summary>models.py</summary>
<img src="documentation/validation/python/about-models.jpg">
</details>
</details>
<br>
<details><summary>Basket App</summary>
<details><summary>context_processor.py</summary>
<img src="documentation/validation/python/basket-context-processor.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/basket-views.jpg">
</details>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/basket-urls.jpg">
</details>
</details>
<br>
<details><summary>Checkout App</summary>
<details><summary>admin.py</summary>
<img src="documentation/validation/python/checkout-admin.jpg">
</details>
<details><summary>forms.py</summary>
<img src="documentation/validation/python/checkout-forms.jpg">
</details>
<details><summary>models.py</summary>
<img src="documentation/validation/python/checkout-models.jpg">
</details>
<details><summary>signals.py</summary>
<img src="documentation/validation/python/checkout-signals.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/checkout-views.jpg">
</details>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/checkout-urls.jpg">
</details>
<details><summary>webhook_handler.py</summary>
<img src="documentation/validation/python/checkout-webhook-handler.jpg">
</details>
<details><summary>webhooks.py</summary>
<img src="documentation/validation/python/checkout-webhooks.jpg">
</details>
</details>
<br>
<details><summary>Contact App</summary>
<details><summary>admin.py</summary>
<img src="documentation/validation/python/contact-admin.jpg">
</details>
<details><summary>forms.py</summary>
<img src="documentation/validation/python/contact-forms.jpg">
</details>
<details><summary>models.py</summary>
<img src="documentation/validation/python/contact-models.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/contact-views.jpg">
</details>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/contact-urls.jpg">
</details>
</details>
<br>
<details><summary>Home App</summary>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/home-urls.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/home-views.jpg">
</details>
</details>
<br>
<details><summary>Products App</summary>
<details><summary>admin.py</summary>
<img src="documentation/validation/python/products-admin.jpg">
</details>
<details><summary>context_processor.py</summary>
<img src="documentation/validation/python/products-context-processor.jpg">
</details>
<details><summary>forms.py</summary>
<img src="documentation/validation/python/products-forms.jpg">
</details>
<details><summary>models.py</summary>
<img src="documentation/validation/python/products-models.jpg">
</details>
<details><summary>product_filters.py</summary>
<img src="documentation/validation/python/products-product-filters.jpg">
</details>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/products-urls.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/products-views.jpg">
</details>
</details>
<br>
<details><summary>Users App</summary>
<details><summary>urls.py</summary>
<img src="documentation/validation/python/users-urls.jpg">
</details>
<details><summary>views.py</summary>
<img src="documentation/validation/python/users-views.jpg">
</details>
<details><summary>forms.py</summary>
<img src="documentation/validation/python/users-forms.jpg">
</details>
<details><summary>models.py</summary>
<img src="documentation/validation/python/users-models.jpg">
</details>
</details>
<br>

### Accessibility
I used WAVE WebAIM web accessibility evaluation tool to ensure the website met high accessibility standards.

All pages passed with no errors, I was using the WAVE web extension to run check all the pages as some of them would not verify due to the need to be logged in or require a session.

I also ran the website through both color themes to make sure there were no conflicts between the contrast on either themes.
<details><summary>Home page</summary>
<img src="documentation/validation/accessibility/home-page.jpg">
</details>
<details><summary>All products</summary>
<img src="documentation/validation/accessibility/all-products.jpg">
</details>
<details><summary>Search products</summary>
<img src="documentation/validation/accessibility/search-products.jpg">
</details>
<details><summary>Product details</summary>
<img src="documentation/validation/accessibility/product-details.jpg">
</details>
<details><summary>Product categories list</summary>
<img src="documentation/validation/accessibility/product-categories.jpg">
</details>
<details><summary>Category pages</summary>
<img src="documentation/validation/accessibility/category-page.jpg">
</details>
<details><summary>Log in</summary>
<img src="documentation/validation/accessibility/log-in.jpg">
</details>
<details><summary>Log out</summary>
<img src="documentation/validation/accessibility/log-out.jpg">
</details>
<details><summary>Register</summary>
<img src="documentation/validation/accessibility/register.jpg">
</details>
<details><summary>Profile page</summary>
<img src="documentation/validation/accessibility/profile-page.jpg">
</details>
<details><summary>Order history</summary>
<img src="documentation/validation/accessibility/order-history.jpg">
</details>
<details><summary>Basket</summary>
<img src="documentation/validation/accessibility/basket.jpg">
</details>
<details><summary>Checkout</summary>
<img src="documentation/validation/accessibility/checkout.jpg">
</details>
<details><summary>Checkout success</summary>
<img src="documentation/validation/accessibility/checkout-success.jpg">
</details>
<details><summary>Contact us</summary>
<img src="documentation/validation/accessibility/contact-us.jpg">
</details>
<details><summary>About us</summary>
<img src="documentation/validation/accessibility/about-us.jpg">
</details>
<details><summary>Add products page</summary>
<img src="documentation/validation/accessibility/add-product-page.jpg">
</details>
<details><summary>Edit products page</summary>
<img src="documentation/validation/accessibility/edit-product-page.jpg">
</details>
<details><summary>Delete products page</summary>
<img src="documentation/validation/accessibility/delete-product-page.jpg">
</details>
<details><summary>Add categories page</summary>
<img src="documentation/validation/accessibility/add-categories-page.jpg">
</details>
<details><summary>Edit categories page</summary>
<img src="documentation/validation/accessibility/edit-categories-page.jpg">
</details>
<details><summary>Delete categories page</summary>
<img src="documentation/validation/accessibility/delete-categories-page.jpg">
</details>
<details><summary>Error page</summary>
<img src="documentation/validation/accessibility/error-page.jpg">
</details>
<br>

### Performance
Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. As previously mentioned, the SendInBlue Newsletter sign-up JS is slowing down the page loading significantly and effecting the performance score.
<details><summary>Home page</summary>
<img src="documentation/validation/lighthouse/home-page.jpg">
</details>
<details><summary>All products</summary>
<img src="documentation/validation/lighthouse/all-products.jpg">
</details>
<details><summary>Search products</summary>
<img src="documentation/validation/lighthouse/search-products.jpg">
</details>
<details><summary>Product details</summary>
<img src="documentation/validation/lighthouse/product-details.jpg">
</details>
<details><summary>Product categories list</summary>
<img src="documentation/validation/lighthouse/product-categories.jpg">
</details>
<details><summary>Category pages</summary>
<img src="documentation/validation/lighthouse/category-page.jpg">
</details>
<details><summary>Log in</summary>
<img src="documentation/validation/lighthouse/log-in.jpg">
</details>
<details><summary>Log out</summary>
<img src="documentation/validation/lighthouse/log-out.jpg">
</details>
<details><summary>Register</summary>
<img src="documentation/validation/lighthouse/register.jpg">
</details>
<details><summary>Profile page</summary>
<img src="documentation/validation/lighthouse/profile-page.jpg">
</details>
<details><summary>Order history</summary>
<img src="documentation/validation/lighthouse/order-history.jpg">
</details>
<details><summary>Basket</summary>
<img src="documentation/validation/lighthouse/basket.jpg">
</details>
<details><summary>Checkout</summary>
<img src="documentation/validation/lighthouse/checkout.jpg">
</details>
<details><summary>Checkout success</summary>
<img src="documentation/validation/lighthouse/checkout-success.jpg">
</details>
<details><summary>Contact us</summary>
<img src="documentation/validation/lighthouse/contact-us.jpg">
</details>
<details><summary>About us</summary>
<img src="documentation/validation/lighthouse/about-us.jpg">
</details>
<details><summary>Add products page</summary>
<img src="documentation/validation/lighthouse/add-product-page.jpg">
</details>
<details><summary>Edit products page</summary>
<img src="documentation/validation/lighthouse/edit-product-page.jpg">
</details>
<details><summary>Delete products page</summary>
<img src="documentation/validation/lighthouse/delete-product-page.jpg">
</details>
<details><summary>Add categories page</summary>
<img src="documentation/validation/lighthouse/add-categories-page.jpg">
</details>
<details><summary>Edit categories page</summary>
<img src="documentation/validation/lighthouse/edit-categories-page.jpg">
</details>
<details><summary>Delete categories page</summary>
<img src="documentation/validation/lighthouse/delete-categories-page.jpg">
</details>
<br>

### Device Testing
The website was tested on the following devices:
- Huawei Matebook D15
- MacBook Pro 13” 2019
- Samsung Galaxy S22 Plus
- Samsung Galaxy S20 FE 5G
In addition, the website was tested using Google Chrome Developer Tools Device Toggling option for all available device options.

### Browser Compatibility
The website was tested on the following browsers in both regular and incognito modes:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge

## Testing user stories
1. As a unauthenticated user, I would like to be able to navigate through the website easily so that it is easy to find the information I am looking for.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar / Dropdown Menu | Use the Navbar to navigate to another page | The page selected from the Navbar loads | Works As Expected |
| Product Search | Use the search bar within the header to search for the name, recommended use or a keyword of a product | The user is redirected to a page with the search results | Works As Expected |
| Error Pages | Edit the website URL from any page to form an invalid URL. On the error page use the built in navigation to navigate back to the main website. | The user is redirected to a custom error page and is able to navigate on their own back to the main website. | Works As Expected |
|  |  |  |  |
<details><summary>Navbar / Dropdown Menu</summary>
<img src="documentation/user-story-testing/user-story-1-1.jpg">
</details>
<details><summary>Product Search</summary>
<img src="documentation/user-story-testing/user-story-1-2.jpg">
</details>
<details><summary>Error Pages</summary>
<img src="documentation/user-story-testing/user-story-1-3.jpg">
</details>
<br>

2. As a unauthenticated user, I would like to be able to sign up for an account so that I can view my profile and track my orders.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| User Registration | Fill out the User Registration form to create an account | A user account is created for the user and they are sent an email to verify their email, after this they are redirected to the sign in page. | Works As Expected |
|  |  |  |  |
<details><summary>User Registration</summary>
<img src="documentation/user-story-testing/user-story-2.jpg">
</details>
<br>

3. As a unauthenticated user, I would like to see the available products that are listed on the website so that I can see what is currently in available.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| All Products | From any page of the website use the link in the header to navigate to the products page | The user is taken to the all products page | Works As Expected |
| Product Details | From any product page or category page select a product on the store | The user is redirected to the product details page | Works As Expected |
| Product Search | Use the search bar within the header to search for the name, recommended use or a keyword of a product | The user is redirected to a page with the search results | Works As Expected |
|  |  |  |  |
<details><summary>All Products</summary>
<img src="documentation/user-story-testing/user-story-1-1.jpg">
</details>
<details><summary>Product Details</summary>
<img src="documentation/user-story-testing/user-story-3.jpg">
</details>
<details><summary>Product Search</summary>
<img src="documentation/user-story-testing/user-story-1-2.jpg">
</details>
<br>

4. As a unauthenticated user, I would like to know how to find social media links so that I can find out about new products and news.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Footer | From any page on the website, scroll to the bottom of the page, locate and use the social media handle within the website footer | The user is redirected to the website social media page, opening in a new tab. | Works As Expected |
|  |  |  |  |
<details><summary>Footer</summary>
<img src="documentation/user-story-testing/user-story-4.jpg">
</details>
<br>

5. As a unauthenticated user, I would like to be able to search or filter the website for specific products and brands so that I can find exactly what i am looking.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Categories | From any page of the website use one of the links in the header to navigate to the selected category page | The user is taken to the selected category page | Works As Expected |
| All Products | From any page of the website use the link in the header to navigate to the products page | The user is taken to the all products page | Works As Expected |
| Product Search | Use the search bar within the header to search for the name, recommended use or a keyword of a product | The user is redirected to a page with the search results | Works As Expected |
|  |  |  |  |
<details><summary>Categories</summary>
<img src="documentation/user-story-testing/user-story-5.jpg">
</details>
<details><summary>All Products</summary>
<img src="documentation/user-story-testing/user-story-1-1.jpg">
</details>
<details><summary>Product Search</summary>
<img src="documentation/user-story-testing/user-story-1-2.jpg">
</details>
<br>

6. As a unauthenticated user, I would like to be able to sort and view products by category so that I can find specific products easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Categories | From any page of the website use one of the links in the header to navigate to the selected category page | The user is taken to the selected category page | Works As Expected |
| All Products | From any page of the website use the link in the header to navigate to the products page | The user is taken to the all products page | Works As Expected |
| Page Ordering | From any page containing a list of products use the dropdown box to change how the page is ordered. | The products on the page are re-ordered by the new selection | Works As Expected |
| Product Search | Use the search bar within the header to search for the name, recommended use or a keyword of a product | The user is redirected to a page with the search results | Works As Expected |
|  |  |  |  |
<details><summary>Categories</summary>
<img src="documentation/user-story-testing/user-story-5.jpg">
</details>
<details><summary>All Products</summary>
<img src="documentation/user-story-testing/user-story-1-1.jpg">
</details>
<details><summary>Page Ordering</summary>
<img src="documentation/user-story-testing/user-story-6.jpg">
</details>
<details><summary>Product Search</summary>
<img src="documentation/user-story-testing/user-story-1-2.jpg">
</details>
<br>

7. As a unauthenticated user, I would like to be able to order the products on a page a variety of ways so that I can find what I am looking for easier.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| All Products | From the all products page use the dropdown box to change how the page is ordered. | The products on the page are re-ordered by the new selection | Works As Expected |
| Page Ordering | From any page containing a list of products use the dropdown box to change how the page is ordered. | The products on the page are re-ordered by the new selection | Works As Expected |
| Product Search | From the search results page use the dropdown box to change how the page is ordered. | The products on the page are re-ordered by the new selection | Works As Expected |
|  |  |  |  |
<details><summary>All Products</summary>
<img src="documentation/user-story-testing/user-story-6.jpg">
</details>
<details><summary>Page Ordering</summary>
<img src="documentation/user-story-testing/user-story-6.jpg">
</details>
<details><summary>Product Search</summary>
<img src="documentation/user-story-testing/user-story-7.jpg">
</details>
<br>

8. As a unauthenticated user, I would like to be able to see detailed description of the products available so that i can make an informed purchase.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Product Details | From any page containing a list of products select a product to view | The user is redirected to a product details page containing all the product information | Works As Expected |
|  |  |  |  |
<details><summary>Product Details</summary>
<img src="documentation/user-story-testing/user-story-3.jpg">
</details>
<br>

9. As a unauthenticated user, I would like to be able to add a product to my basket so that I can purchase them.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Shopping Basket | From any page containing a list of products hover over any item you want to purchase and select the "Add To Basket" button | The item is added to the basket | Works As Expected |
| Shopping Basket | From the products detail page select the "Add To Basket" button | The item is added to the basket | Works As Expected |
|  |  |  |  |
<details><summary>Shopping Basket 1</summary>
<img src="documentation/user-story-testing/user-story-9-1.jpg">
</details>
<details><summary>Shopping Basket 2</summary>
<img src="documentation/user-story-testing/user-story-9-2.jpg">
</details>
<br>

10. As a unauthenticated user, I would like to be able to see the products that are in my basket so that I don't spend too much.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Shopping Basket | From any page, select the basket icon on the navbar to navigate to the shopping basket page | View the items in the shopping basket. | Works As Expected |
|  |  |  |  |
<details><summary>Shopping Basket</summary>
<img src="documentation/user-story-testing/user-story-10.jpg">
</details>
<br>

11. As a unauthenticated user, I would like to be able to increase or decrease quantities and remove items from my basket so that I don't have to navigate to the store and add the item again each time.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Shopping Basket | From any page, select the basket icon on the navbar to navigate to the shopping basket page and select the increase or decrease buttons next to the product then click the update to confirm the new quantity. | The quantity of the product in the basket is adjusted. | Works As Expected |
|  |  |  |  |
<details><summary>Shopping Basket</summary>
<img src="documentation/user-story-testing/user-story-11.jpg">
</details>
<br>

12. As a unauthenticated user, I would like to be able to purchase the items in my basket so that I can complete my order.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Shopping Basket | From the Shopping basket page, once the user is happy with their order, select the checkout option and filling their details | The user is redirected to the checkout page where they can fill out the checkout details and purchase their products. | Works As Expected |
| Stripe Checkout | On the checkout page the user should fill out their details to finish the purchase of the items in the current basket | The user purchases the items they placed into the basket | Works As Expected |
|  |  |  |  |
<details><summary>Shopping Basket</summary>
<img src="documentation/user-story-testing/user-story-12-1.jpg">
</details>
<details><summary>Stripe Checkout</summary>
<img src="documentation/user-story-testing/user-story-12-2.jpg">
</details>
<br>

13. As a unauthenticated user, I would like to be able to log in to / sign out of an existing account so that I can get updated on my orders.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| User Login | From any page of the website use the login link within the accounts section on the navbar and fill out the login form. | The user is redirected to the login page and once the form is filled out they are logged into the website. | Works As Expected |
|  |  |  |  |
<details><summary>User Login</summary>
<img src="documentation/user-story-testing/user-story-13.jpg">
</details>
<br>

14. As a unauthenticated user, I would like to be able contact the business so that I can ask any questions or make a complaint.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Us | From any page on the website, scroll to the bottom of the page, locate the contact us section | The user is presented with a form to fill out that sends the admin team a message with their issues | Works As Expected |
|  |  |  |  |
<details><summary>Contact Us</summary>
<img src="documentation/user-story-testing/user-story-14.jpg">
</details>
<br>


15. As a unauthenticated user, I would like to be able to sign up to the newsletter so that I can receive news and updates from the business.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Newsletter E-mail List | From any page on the website, scroll to the bottom of the page, locate the newsletter sign up section. | The user is signed up for the email marketing and newsletters. | Works As Expected |
|  |  |  |  |
<details><summary>Newsletter E-mail List</summary>
<img src="documentation/user-story-testing/user-story-15.jpg">
</details>
<br>

16. As a authenticated user, I would like to be able to view and update my personal information so that I do not have to fill it out each time I make an order.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Stripe Checkout | When a user makes an order there is a checkbox to save the information for the next time, if this box is checked the details currently filled out will be saved to the user profile and appear on the profile page. | the details filled out on the checkout page appear on the profile page  | Works As Expected |
| Profile Page | From the profile page, update the form with the new personal information and click the update button | the form saves and the page reloads with the new information saved in the database and displayed in the form | Works As Expected |
|  |  |  |  |
<details><summary>Stripe Checkout</summary>
<img src="documentation/user-story-testing/user-story-16-1.jpg">
</details>
<details><summary>Profile Page</summary>
<img src="documentation/user-story-testing/user-story-16-2.jpg">
</details>
<br>

17. As a authenticated user, I would like to be able to view my order history so that i can find products i have ordered before and would order again.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Profile Page | From any page use the profile page link within the accounts section on the navbar to navigate to the profile page | On the profile page see a list of previous orders and the products ont he orders | Works As Expected |
| Order History | On the profile page locate the order history, click on an order to open up a detailed view of the items, quantity and more information relating to the order. | The user is redirected to a new page with detailed information relating to the the order selected. | Works As Expected |
|  |  |  |  |
<details><summary>Profile Page</summary>
<img src="documentation/user-story-testing/user-story-17-1.jpg">
</details>
<details><summary>Order History</summary>
<img src="documentation/user-story-testing/user-story-17-2.jpg">
</details>
<br>

18. As a website staff user, I would like to be able to use full CRUD functionality so that I can update the product range available.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Create Product | When logged in as website staff, use the accounts section on the navbar to navigate to the create a product page, from here fill out the details for the new product. | When the staff member clicks the link to create a new product the staff member is redirected to a new page with a form for creating products, once the form is filled out and submitted a new product is created | Works As Expected |
| Edit Product | When signed in as a staff member and from any page containing a list of products select the link underneath any product to edit the product | The staff member is redirected to the edit product page where there is a form pre-populated with the current information for the staff member to update and resubmit | Works As Expected |
| Delete Product | When signed in as a staff member and from any page containing a list of products select the link underneath any product to delete the product | The staff member is redirected to a page confirming if they want to deleted the product, when confirmed, the selected product is deleted from the database. | Works As Expected |
|  |  |  |  |
<details><summary>Create Product</summary>
<img src="documentation/user-story-testing/user-story-18-1.jpg">
</details>
<details><summary>Edit Product</summary>
<img src="documentation/user-story-testing/user-story-18-2.jpg">
</details>
<details><summary>Delete Product</summary>
<img src="documentation/user-story-testing/user-story-18-3.jpg">
</details>
<br>

19. As a website staff user, I would like to be able to manage product inventory so that I can adjust the available products.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Create Product | When logged in as website staff, use the accounts section on the navbar to navigate to the create a product page, from here fill out the details for the new product. | When the staff member clicks the link to create a new product the staff member is redirected to a new page with a form for creating products, once the form is filled out and submitted a new product is created | Works As Expected |
| Edit Product | When signed in as a staff member and from any page containing a list of products select the link underneath any product to edit the product | the staff member is redirected to the edit product page where there is a form pre-populated with the current information for the staff member to update and resubmit | Works As Expected |
| Delete Product | When signed in as a staff member and from any page containing a list of products select the link underneath any product to delete the product | The selected product is deleted from the database. | Works As Expected |
|  |  |  |  |
<details><summary>Create Product</summary>
<img src="documentation/user-story-testing/user-story-18-1.jpg">
</details>
<details><summary>Edit Product</summary>
<img src="documentation/user-story-testing/user-story-18-2.jpg">
</details>
<details><summary>Delete Product</summary>
<img src="documentation/user-story-testing/user-story-18-3.jpg">
</details>
<br>

20. As a website staff user, I would like to be able to view and update product categories so that the product range is up to date.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Category Management | When logged in as website staff, use the Navbar to go to the categories page and select the edit button underneath the category to edit. | When the staff member clicks the edit link the staff member is redirected to a new page with a form for editing the current category, once the form is filled out and submitted the category selected is updated | Works As Expected |
|  |  |  |  |
<details><summary>Category Management</summary>
<img src="documentation/user-story-testing/user-story-20.jpg">
</details>
<br>

21. As a website staff user, I would like to be able to add product categories so that new products are available on the website.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Category Management | When logged in as website staff, use the accounts section on the navbar to navigate to the category management page, from here you can choose to add a new category, fill out the form and select submit. | When the staff member clicks the link to the category management page the staff member is redirected to a new page with a form for creating categories, once the form is filled out and submitted the category selected is created | Works As Expected |
|  |  |  |  |
<details><summary>Category Management</summary>
<img src="documentation/user-story-testing/user-story-21.jpg">
</details>
<br>

22. As a website staff user, I would like to be able to delete product categories so that products that are no longer available are removed.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Category Management | When logged in as website staff, use the accounts section on the navbar to navigate to the category management page, from here select the deleted category button. | When the staff member clicks the link to the category management page the staff member is redirected to a new page with a form for editing the current categories, When the staff member clicks the delete category button the staff member will be returned to the category management page and the category deleted. | Works As Expected |
|  |  |  |  |
<details><summary>Category Management</summary>
<img src="documentation/user-story-testing/user-story-22.jpg">
</details>
<br>

23. As the website owner, I want the products divided into categories so that users looking for something specific can navigate easier.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Categories | From any page use the navbar to locate the categories page or the individual categories and select a category to go to. | The current user is taken to the category of choice. | Works As Expected |
|  |  |  |  |
<details><summary>Categories</summary>
<img src="documentation/user-story-testing/user-story-23.jpg">
</details>
<br>

24. As the website owner, I want the website to act responsively to all device sizes so that the website can be viewed across all devices.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar / Dropdown Menu | Using google chrome, open the Developer tools and enable the device toolbar, to resize the window to smaller sizes | The Header is appropriately sized across all sizes of devices. | Works As Expected |
| Footer | Using google chrome, open the Developer tools and enable the device toolbar, to resize the window to smaller sizes | The Footer is appropriately sized across all sizes of devices. | Works As Expected |
|  |  |  |  |
<details><summary>Navbar / Dropdown Menu</summary>
<img src="documentation/user-story-testing/user-story-24-1.jpg">
</details>
<details><summary>Footer</summary>
<img src="documentation/user-story-testing/user-story-24-2.jpg">
</details>
<br>

25. As the website owner, I want users to get redirected to custom error pages so that they understand when when something has gone wrong and can be redirected back to the main website.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Error Pages | From any page, edit the URL to form a invalid URL path within the domain. | The custom error page loads as appropriate. | Works As Expected |
|  |  |  |  |
<details><summary>Error Pages</summary>
<img src="documentation/user-story-testing/user-story-1-3.jpg">
</details>
<br>

26. As the website owner, I want users to be able to navigate the website quickly and easily so that they are able to find what they are looking for.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar / Dropdown Menu | Use the Navbar to navigate to another page | The desired page loads correctly | Works As Expected |
| Categories | From any page use the navbar to locate the categories page or the individual categories and select a category to go to. | The current user is taken to the category of choice. | Works As Expected |
| Error Pages | Edit the website URL from any page to form an invalid URL. On the error page use the built in navigation to navigate back to the main website. | The user is redirected to a custom error page and is able to navigate on their own back to the main website. | Works As Expected |
|  |  |  |  |
<details><summary>Navbar / Dropdown Menu</summary>
<img src="documentation/user-story-testing/user-story-1-1.jpg">
</details>
<details><summary>Categories</summary>
<img src="documentation/user-story-testing/user-story-5.jpg">
</details>
<details><summary>Error Pages</summary>
<img src="documentation/user-story-testing/user-story-1-3.jpg">
</details>
<br>

27. As the website owner, I want users to be sign up to a newsletter to capture user information and bring users back to the website.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Newsletter E-mail List | From any page on the website, scroll to the bottom of the page, locate the newsletter sign up section. | The user is signed up for the email marketing and newsletters. | Works As Expected |
|  |  |  |  |
<details><summary>Newsletter E-mail List</summary>
<img src="documentation/user-story-testing/user-story-15.jpg">
</details>
<br>

28. As the website owner, I want users to be able to view the business social media so that users are made aware of the products on offer and kept up to date with any news.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Footer | From any page on the website, scroll to the bottom of the page, locate and use the social media handle within the website footer | The user is redirected to the website social media page, opening in a new tab. | Works As Expected |
|  |  |  |  |
<details><summary>Footer</summary>
<img src="documentation/user-story-testing/user-story-4.jpg">
</details>
<br>

29. As a user, I would like to have a confirmation message that my order has been successful so that I am made aware once the transaction has taken place successfully.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Stripe Checkout | When a user finishes placing an order and all the details are correct a message will appear. | A message telling the user weather the order was placed successfully or not will appear when the user finishes placing the order. | Works As Expected |
| Message Popups | When a user finishes placing an order and all the details are correct a message will appear. | A message telling the user weather the order was placed successfully or not will appear when the user finishes placing the order. | Works As Expected |
|  |  |  |  |
<details><summary>Stripe Checkout</summary>
<img src="documentation/user-story-testing/user-story-29-1.jpg">
</details>
<details><summary>Message Popups</summary>
<img src="documentation/user-story-testing/user-story-29-2.jpg">
</details>
<br>

30. As a user, I would like to be shown descriptive messages telling me that my actions have been successful or unsuccessful when I preform an action so that I can act accordingly.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Message Popups | When a user performs an action(placing an order, updating products, adding items to the cart) a message will appear to confirm weather it was successful or not. | A message telling the user weather the action was successful or not will appear when the user performs a task. | Works As Expected |
|  |  |  |  |
<details><summary>Message Popups</summary>
<img src="documentation/user-story-testing/user-story-30.jpg">
</details>
<br>

31. As a user, I would like to be able to navigate back to the main website structure if an error occurs and I end up on the 404 page so that i can continue shopping without issues.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Error Pages | Edit the website URL from any page to form an invalid URL. On the error page use the built in navigation to navigate back to the main website. | The user is redirected to a custom error page and is able to navigate on their own back to the main website. | Works As Expected |
|  |  |  |  |
<details><summary>Error Pages</summary>
<img src="documentation/user-story-testing/user-story-1-3.jpg">
</details>
<br>

32. As a user, I would like to be able to find a description of the business and an FAQ section so that I can find the answers I need.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| About Us | From any page on the website, scroll to the bottom of the page, locate the about us link within the footer | The user is redirected to a new page with a brief description about the business and to find out more is directed towards the social media handle, there is also a FAQ section to answer commonly asked questions. | Works As Expected |
|  |  |  |  |
<details><summary>About Us</summary>
<img src="documentation/user-story-testing/user-story-32.jpg">
</details>
<br>

## Automated Testing

As part of this project I have produced some automated tests Django's testing framework which is based on python unittest.

I have demonstrated some proficiency in using these tests but the code does not have full coverage due to the complex nature of some parts of the website. If there are future releases I could endeavor to increase the number of tests and coverage of the code.

#### About
1. Test if the About page loads
2. Test is we can create a new Faq.

#### Contact
1. Test if the Contact page loads
2. Test the contact form posts
3. Test if we can create contact models

#### Home
1. Test if the Home page loads

#### Products
1. Test if the Product Detail page loads
2. Test if the Product List loads
3. Test if the Search Results page loads with no search query
4. Test if the Search Results page loads with a search query
5. Test is the Categories Page loads
6. Test if the Category Page loads
7. Test if the Create Product Page loads with admin user
8. Test if the Create Product Page loads without admin user
9. Test if the Update Product Page loads with admin user
10. Test if the Update Product Page loads without admin user
11. Test if the Delete Product Page loads with admin user
12. Test if the Delete Product Page loads without admin user
13. Test if the Create Category Page loads with admin user
14. Test if the Create Category Page loads without admin user
15. Test if the Update Category Page loads with admin user
16. Test if the Update Category Page loads without admin user
17. Test if the Delete Category Page loads with admin user
18. Test if the Delete Category Page loads without admin user
19. Test load all products page then navigate to page two
20. Test load all products page every different way
21. Test load search results products page every different way

#### Basket
1. Test if the empty basket page will load
2. Test adding an item with no size, followed by a second item
3. Test adding an item with size, followed by an item of the same size and another of different size.
4. Tests adjusting the quantity of an item in the basket from 2 down to 1 then again to 0 without a size
5. Tests adjusting the quantity of an item in the basket from 2 down to 1 then again to 0 with a size
6. Tests removing an item from the basket with size
7. Tests removing an item from the basket without size
8. Test removing an item that was removed from the website

#### Checkout
1. Test the checkout returning a user to the store if the basket is empty
2. Test creating an anonymous order through the checkout
3. Test the order details form validation
4. Test updating the order with a new orderlineitem above the delivery threshold
5. Test updating the order with a new orderlineitem below the delivery threshold

#### Users
1. Test profile page loading
2. Test profile page form post
3. Test order history page page loading

<br>![Auto test results](documentation/automated-testing/results.jpg)

[Back to Table Of Content](#table-of-content)

### Coverage

To show code coverage a python test plugin called coverage was used to generate the following results

<details><summary>Images</summary>
<img src="documentation/automated-testing/coverage1.jpg"><br>
<img src="documentation/automated-testing/coverage2.jpg"><br>
</details>

[Back to Table Of Content](#table-of-content)

## Bugs
| **Bug** | **Fix** |
| ------- | ------- |
| Issues with loading the filtered query page search along with pagination | Re-write views and used django-filters package as per guides detailed below. |
| Issues with too many GET requests from AWS servers | Added database_url to env.py by mistake, removed to stop linking to postgres database during development. |
| Category filtering not working using query filtering | Used category view to filter the products directly. |
| Django self updated to version 4.2 when preparing to deploy to heroku due to another library and also installed backports.zoneinfo | Rolled back Django to 3.2 for version support and uninstalled backports.zoneinfo |
|  |  |

[Back to Table Of Content](#table-of-content)

## Google emails
To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
<br>![App password](documentation/misc/gmail-password.jpg)
4. Click create and a 16 digit password will be generated, note the password down
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
7. Set and confirm the following values in the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>
8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

[Back to Table Of Content](#table-of-content)

## Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
<br>![API keys](documentation/misc/stripe-keys.jpg)
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://alpha-exchange.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>![Webhook](documentation/misc/stripe-webhook.jpg)
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting

[Back to Table Of Content](#table-of-content)

## Deployment

### Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create a new S3 bucket  with a globally unique name mine is "pp5-alpha-exchange"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
<br>![AWS Static](documentation/deployment/aws_static.jpg)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration
<br>![AWS CORS](documentation/deployment/aws_cors.jpg)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
<br>![AWS Bucket Policy](documentation/deployment/aws_bucket_policy.jpg)
8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "manage-alpha-exchange"
12. Add the "AmazonS3FullAccess" policy permission for the user group
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following
<br><code>"Resource": [</code>
<br><code>"arn:aws:s3:::pp5-alpha-exchange",</code>
<br><code>"arn:aws:s3:::pp5-alpha-exchange/*"</code>
<br><code>]</code>
16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
<br>![AWS Bucket Policy](documentation/deployment/aws_user_group.jpg)
18. Go to Users and create a new user
19. Add the user to the user group manage-alpha-exchange
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
22. The user is now created with the correct user group and policy
<br>![AWS User](documentation/deployment/aws_user.jpg)
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
<br>![AWS Settings](documentation/deployment/aws_settings.jpg)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "alpha-exchange") and choose your region
3. Click on create app
4. Under resources search for postgres, and add a Postgres database to the app
5. Install the plugins dj-database-url and psycopg2-binary
6. Install django and gunicorn
7. Add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
8. Create a Procfile in your app: 
   ```
   wsgi:PROJECT_NAME.wsgi
   ```
   (web: gunicorn alpha_exchange.wsgi)
9. In the setting.py file ensure you have connected to the Heroku postgres database
10. Ensure Debug is set to False in the settings.py file
11. Add localhost/127.0.0.1, and alpha-exchange.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
12. Go to Settings in your Heroku and set the environment variables in the Config Vars
![Config vars](documentation/deployment/heroku-config-vars.jpg)
13. Remove DISABLE_COLLECTSTATIC from Heroku settings
14. Push the code to Heroku using the command git push heroku main

Final Steps:
1. Go to "Deploy" in the menu bar on the top
2. Select the deployment method Github
![Deployment steps](documentation/deployment/heroku-deployment.jpg)
3. Search for the name of the Github Repository and connect
![Deployment steps](documentation/deployment/heroku-deployment-repo.jpg)
4. Scroll down and enable automatic deployment
![Deployment steps](documentation/deployment/heroku-deployment-deploy.jpg)

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Content](#table-of-content)

## Credits
### Media
All of the media featured on the website is not owned by the developer. 

Any further recipes and images added by third parties and individuals have been obtained by the third party.

| **Link to Asset** | **Created By** | **Web Source** |
| ----------------- | -------------- | -------------- |
| [shopping-cart.webp](/media/shopping-cart.webp) | [Alexas_Fotos](https://pixabay.com/users/alexas_fotos-686414/) | [Pixabay](https://pixabay.com/photos/shopping-business-retail-trade-1165437/) |
| [Favicon](/static/img/favicon_io/android-chrome-512x512.png) | [emirkhan bal](https://www.pexels.com/@emirkhan-bal-221704/) | [Pexels](https://www.pexels.com/photo/gray-and-blue-stainless-steel-shopping-cart-953862/) |
| [Categories](/products/fixtures/categories.json) | Mirroring the CI Boutique Ado fixtures, I updated these to fit my needs with new information pruned from a new Kaggle dataset. | [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small) |
| [Products](/products/fixtures/products.json) | Mirroring the CI Boutique Ado fixtures, i updated these to fit my needs with new information pruned from a new Kaggle dataset. | [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small) |
| Product Images | Pruned from the kaggle dataset to match the product details in the fixtures, these were then renamed for accessibility reasons. | [Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small) |
|  |  |  |
|  |  |  |

### Code
- The Django All-Auth code and webpages were used from the Django blog project and then customized for this project.
- The card design was based upon a guide found [HERE](https://www.youtube.com/watch?v=5DEq5cWNYt8&ab_channel=KevinPowell) by Kevin Powell on youtube, this was adapted to fit my use case.
- The pagination code used was referenced both from the CI course material and this blog post found [HERE](https://dontrepeatyourself.org/post/django-pagination-with-function-based-view/) 
- The code used in the [basket-qty.js](basket/static/basket/js/basket-qty.js) file is taken from the Boutique Ado walk through with minor alterations to fit my website. particually separating itinto its own file and fixing the bug pulling the csrf_token, Thanks to [John S on this post](https://stackoverflow.com/a/25346429) who helped me get the correct token from cookies.
- The CSS rules for the footer to make it stick to the bottom of the page when the content does not push it down far enough comes from this guide on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Sticky_footers#alternate_method).

- A massive thank you to [dannymagnus](https://github.com/dannymagnus) and [Aleksandra_alumna](https://code-institute-room.slack.com/archives/C010RUUFGDQ/p1650997281601259?thread_ts=1650970836.247149&cid=C010RUUFGDQ) on Github who's project and post on slack respectively, these two pointed me towards posts and examples to help fix my bugs with pagination and sorting/filtering my products. These resources can be found on a [Youtube Video](https://www.youtube.com/watch?v=dkJ3uqkdCcY&t=1138s&ab_channel=TauhidCodes), on a blog [post](https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html), and [stackoverflow post](https://stackoverflow.com/questions/47996963/that-page-number-is-less-than-1-django).

[Back to Table Of Content](#table-of-content)

## Acknowledgements

I would like to take the opportunity to thank:
- My mentor Mo Shami, for his professional feedback, advice, guidance, and support.
- My partner Megan Fox, for her support advice, help testing, inspiration for the project and allowing me the time to work on my project.
- To the Code Institute Slack community for providing help and support.

[Back to Table Of Content](#table-of-content)