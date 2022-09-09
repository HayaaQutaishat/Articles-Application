# CS50W-Project 4-Final

## CS50 Web - Programming with Python and JavaScript. 

### Project purpose :

This website is an articles platform. This was the final project of HarvardX's CS50W course in 2022 and was built using Python, Django, Javascript ,CSS, HTML and Bootstrap.

This web application is not similar to anything we have already worked on. It's not a social media app nor an e-commerce website. In this website users will be able to read, rate, comment on those articles, and add any of them to "read later" so they can easily find them later. 


### Project Structure :

-In the Home page, users can search text in any part of articles title by typing any words in the input box, and click "Search" button.

-If users just want to read any article, they can just click "Random Article" button on the top, and they will get one random article in a particular topc. Additionally, they don't need to log in for those actions. 

-When users click on "Categories", they will be taken to a page that shows all the categories in the website. (Health, Environmental Issues, Food, Animals and Art). Each category contains number of articles related to the topic. Clicking on any of those categories will take the user to a new page which has all the related articles. 

-Logged users have the ability to create a new article and add it to the other existing articles, add article to "Read Later" where can read the article anytime later, and also they can add comments on any article in the web page.

-Also, logged user can add any article to "Read Later" where they can read it anytime by just clicking on "Read Later" in the main page of the website.


## Project Pages :

### Login Page :

This is the entry page to the website that requires user identification and authentication, regularly performed by entering a username and password combination.

<img width="1440" alt="Screen Shot 2022-08-16 at 2 50 56 PM" src="https://user-images.githubusercontent.com/95029840/184884014-12d23310-f2d8-440c-82a1-89b93c52f0f3.png">

### Register Page :

This signup page (also known as a registration page) enables users and organizations to independently register and gain access to your system. 

<img width="1439" alt="Screen Shot 2022-08-16 at 2 52 05 PM" src="https://user-images.githubusercontent.com/95029840/184884129-c3e19006-b68b-4df1-baa9-77890fd11b99.png">


### Logout Page :

This page informs the computer or website that the current user wishes to end the login session. 

### Home Page :

-In this page, you can search text in title of articles by input any word in the center input box, and click "Search" button.

<img width="1440" alt="im1" src="https://user-images.githubusercontent.com/95029840/184348451-745b9a42-c786-434c-9630-de065f73860a.png">

-In addition, if you just want to read something new, just click "Random Article" button on the top, and you will get some articles randomly. 

-There's no need to be logged in in order to do those actions. 

-I also added some Tooltips With Only CSS, using data attribute. So when the user hover on the "Search Icon", the following text will pop-up.


<img width="1440" alt="Screen Shot 2022-08-16 at 10 58 29 AM" src="https://user-images.githubusercontent.com/95029840/184840970-a6d80467-dd73-4825-bd6b-455c26ef6ae5.png">


### Categories Page :

-This page shows all the topics in the website. (Health, Environmental Issues, Food, Animals and Art). Each category contains number of articles related to the topic. Clicking on any of those categories will take the user to a new page which has all the related articles.

<img width="1440" alt="Screen Shot 2022-08-12 at 1 56 13 PM" src="https://user-images.githubusercontent.com/95029840/184349345-d80537bd-bbfb-46d6-adef-066155d3958f.png">


### Articles Page :

-In this page, you can get all the articles with title, a simple brief, the author, and the date of publishing this article.

-If the user is interested in any of those articles, he can click at the article at any place in the card, and he will be redirected to the full article page or he can just click on "Click here to read more".


<img width="1440" alt="Screen Shot 2022-08-12 at 1 58 46 PM" src="https://user-images.githubusercontent.com/95029840/184350596-7044017e-f395-4d4f-9b3a-76398faa9f42.png">

### Article Page :

-In the article page, the user will be able to see all the details about one article, such as the title, author, publish date, category of that article, and the entire text of the article. In the bottom of the page, all users can see all the comments on this particular article, who added that comment and the time of adding it.

-Only logged in users will have the ability to press "Add to Read Later" button which will allow them to add this article to "Read Later" page so they can find it easily later and read it at any time.


<img width="1427" alt="Screen Shot 2022-08-12 at 2 00 30 PM" src="https://user-images.githubusercontent.com/95029840/184350490-30654eb7-54ac-48e0-a08b-20aef46200e1.png">

-Also, logged in users can add comments on articles. Besides, each user can edit his comment. When a user clicks “Edit” for one of their own comments, the content of their comment should be replaced with a textarea where the user can edit the content of their comment. Then, the user should then be able to “Save” the edited comment, then the new comment will appear in the page.


<img width="1440" alt="Screen Shot 2022-08-12 at 5 12 00 PM" src="https://user-images.githubusercontent.com/95029840/184386190-617e0c7f-3f86-4760-9624-af203342dd96.png">



<img width="1440" alt="Screen Shot 2022-08-12 at 2 10 28 PM" src="https://user-images.githubusercontent.com/95029840/184351314-eae45bf9-0a6d-476a-8d30-ce15b151abe0.png">

-If the current logged in user is the author of the article which means he is the user who created that article, he can delete the article by pressing on "Delete" button. Clicking on that button will show a pop-up window created with bootstrap Modal to make sure that the user really wants to delete that article.


<img width="1440" alt="Screen Shot 2022-08-12 at 3 44 22 PM" src="https://user-images.githubusercontent.com/95029840/184366824-3c58f433-f4fd-453e-8062-d4c3f63ba1c2.png">


-This page also has a system of one to five stars for articles ratings, with five stars being the highest rating. Logged users have the ability to rate articles by clicking on any the star that represent their rating. When they rate the article the follwoing message will be shown under the rating system.


<img width="1440" alt="Screen Shot 2022-08-16 at 1 36 32 PM" src="https://user-images.githubusercontent.com/95029840/184871355-0e87ff35-b470-46bb-ad50-8ee611b41c2a.png">


### Read Later Page :

-In this page, users can see all the articles they added to be read later. So this will make it very easy to remember which articles they are interested in. 


### Author Page :

-This page shows some information about all authors in the website. Informations like the name of the author, short summary about him and all the articles that he published. 

<img width="1440" alt="Screen Shot 2022-08-12 at 2 47 58 PM" src="https://user-images.githubusercontent.com/95029840/184357882-dfce6ebd-bc8a-46e9-b570-a15c2ae88331.png">


### Create New Article Page :

-Only logged in users have the ability to create new articles and publish them in the website.

-The following picture shows the form that the users will submit in order to create a new article. Each article should has title, brief, and the content of the article itself. Also users should select the category of the article.


<img width="1440" alt="Screen Shot 2022-08-12 at 3 28 42 PM" src="https://user-images.githubusercontent.com/95029840/184363780-cfe2f78e-a05a-4a69-9208-bbb2a4f23ce0.png">

<img width="1440" alt="Screen Shot 2022-08-12 at 3 35 15 PM" src="https://user-images.githubusercontent.com/95029840/184364948-289849bf-cec5-46e3-8f83-e6412df219f3.png">

### Mobile Responsive :

-This web application is mobile responsive application, it's content automatically changes to fit the device you're reading it on. 
-Mobile responsive websites provide the best possible user experience. 

-The following pictures shows a screenshots from different pages in this web application to show that it is a mobile repsonsive app:
 - The home page:

<img width="644" alt="Screen Shot 2022-08-16 at 4 58 42 PM" src="https://user-images.githubusercontent.com/95029840/184912171-74c35ee2-25c7-4ef1-9c42-af1d67646e6a.png">

- Create New Article Page:

<img width="892" alt="Screen Shot 2022-08-16 at 6 37 59 PM" src="https://user-images.githubusercontent.com/95029840/184933146-f7ebfe2c-8659-4fe3-add3-d7e23d48c61c.png">

- Register Page:

<img width="932" alt="Screen Shot 2022-08-16 at 6 42 42 PM" src="https://user-images.githubusercontent.com/95029840/184933786-375659e6-2feb-4195-b67b-ef406123bd17.png">


### Files Information :

- In views.py there is all of the backend code. The main functions are:
  - Login view: If you have an authenticated user you want to attach to the current session - this is done with a login() function. To log a user in, from a view, use login() . It takes an HttpRequest object and a User object. login() saves the user's ID in the session, using Django's session framework.
  - Logout view: Logging out informs the website that the current user wishes to end the login session.
  - register view: This view enables users and organizations to independently register and gain access to your system.
  - categories view: This view brings all categories from database, (Health, Environmental Issues, Food, Animals and Art).Each category contains number of articles related to the topic. 
  - category view: This view brings all the articles related to the clicked category from the database  in reverse chronological order using get() QuerySet method and render them to the user.
  - article view: This view brings the article object from the database so users can see all details about this article using this article object methods and properties. 
  - new_article view: This view create new article object using create() method, and save it to the database using save() method. 
  - search view: This view searches some data in the database with user input in the search form.
  - author view: This view brings author object from database and render all details of this object to the user. 
  - random view: This view returns articles in which the words appear in title or description.
  - read_later_add view: This view adds the article that the user clicked on its "Add To Read Later" button to the list of read later for that user and update the database. 
  - read_later_remove view: This view removes the article that the user clicked on its "Add To Read Later" button to the list of read later for that user and update the database.
  - edit_comment view: This view grabs user's input when click on edit button, and update the databse by the new comment text that the user typed. 
  - delete_article view: This view allow users to delete article objects from database using delete() method. 
  - rating view: This view allow users to rate an article and add this rate to tha database.
- models.py:
  - User model: It's a custom user model (a subclass) of the AbstractUser model. 
  - Categories model: It contains image and type fields. 
  - Article model: It contains title, author, brief, text, date, category, read_later fields. It also contains @classmethod decorator which is an expression that gets evaluated after your function is defined. In this case I'm using this @classmethod to create article objects and save them to the database. 
  - Comment model: It contains comment, article, user and time fields. It also contains @classmethod decorator in order to create comment objects and save them to the database.
  - Profile model: It contains user and about fields.
  - Rating model: It contains user, article and score fields. It also contains @classmethod decorator in order to create rating objects and save them to the database. 
 
- Static files: 
  - styles.css file: This css file contains all of the css used to style this web application. Techniques like flexbox and grid are used. This file stores all the style informations that all the pages share to create a great user experience.
  - index.js file: This file adds a dynamic and interactive elements to all webpages. This file contains all the functions that I want to include on each of this site's webpages. This file also use fetch() method to send asynchronous requests to the server and load the information on the webpages. The request can be of any APIs that return the data of the format JSON.

- Other less important files like urls, admin, settings. 

## Distinctiveness and Complexity :

I believe this project satisfies all the distinctiveness and complexity requirements as it is a platform for searching and reading new articles. It is not similar to anything we have already created in this course. It's not a social media app nor an e-commerce website. It's not similar to other years projects either.

In terms of complexity, I used Django with more than one model (User, Categories, Article, Comment, Profile and Rating explained above in details) each model maps to a single database table, to define the structure of the stored data, including the field types and possibly also their maximum size and default values. All models are stored in models.py file. 

Django supports relational databases which allows us to establish relations between different models. In my project I used all three types of relational fields which Django supports: many-to-one, many-to-many and one-to-one. 

In some of my models I used @classmethod which is basically a method of a class having access to every attribute of the class it was called on. This method use cls, which should be the first argument of every class method. So a class method is a method that is bound to the class and not the object of the class. In my case I used it to create objects in my views.

Additionally, I used javascript to the frontend and to create all the logic in this web application, also Javascript helped me make this web application pages more interactive and allows the screens to respond to clicks and keystrokes made by the user by using events and events handler.

Besides, I used the Fetch() API method to allow to asynchronously HTTP request for a resource so I can retrieve data from a URL without having to do a full page refresh. The fetch() method returns a promise that resolves into a Response object, to get the actual data, I called one of the methods of the Response object (text() or json()). These methods resolve into the actual data.
However, I wrote all my scripts in signel separate file (index.js) and I refered to it using the src attribute in the <script> tag.

Finally, all of the web application pages are completely mobile responsive, so that all the content of the page automatically responds and adapts based on the size of screen they are presented on. 

## Setup :

Requires Python3 and the package installer for Python (pip) to run:

- Create new migrations based on the changes in models: python3 manage.py makemigrations
- Apply the migrations to the database: python3 manage.py migrate
- Create a superuser to be able to use Django Admin Interface: python3 manage.py createsuperuser
- Run the app locally: python3 manage.py runserver
- Visit the site: http://localhost:8000


## Topics :

Built with Python, Django, HTML, CSS, Javascript and Bootstrap.


## Django administration :

- This application has 5 models in addition to the User model: one for categories, one for articles, one for authors profile page , one for comments and one for ratings made on articles.

<img width="1440" alt="Screen Shot 2022-08-16 at 3 09 07 PM" src="https://user-images.githubusercontent.com/95029840/184887996-3cb349cd-013e-4b5a-a539-872b9e510a71.png">

# Back End

## Super User

Super user is a feature provided by Django. The super user can manipulate all data in the Backend Management Dashboard.


Super user can also view all the details of all users.


## Requirements:
Python 3
Pip (Python package manager)



