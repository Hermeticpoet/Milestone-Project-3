# Milestone Project 3 | Data Centric Development

## What 2 Eat - Recipe App

### The Brief
> 
Create a web application that allows users to store and easily access cooking recipes
Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation.
Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large
Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages
Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)
>

## UX
The User Interface is built with [Materialize]() framework to allow for responsiveness, while also creating an aesthetically pleasing experience for the users. 
In today's world decision fatigue has become a real problem, therefore, with that in mind, I decided to limit to scope of the application menu and its
search functionality. I chose six of large scale, well known cuisines for users to choose from, as well as, giving them a further breakdown of choice
between course meals; breakfast, lunch, dinner, dessert and snacks. 
### Design Theme
Ideas have been garnered from browsing online for other food recipe web applications.

#### Colours
The colour scheme is my own original preferences based solely on what I felt was engaging from my online research.

#### User Stories
As a visitor to What 2 Eat:

* ... I am immediately aware of the application's purpose.
* ... I can explore the application using its navigation features.
* ... I can filter my search results for specific recipes based on multiple queries.
* ... I can access the site on different devices while retaining a similar experience to that of the desktop app.
* ... I can create a user profile with password that allows me to personalise any return experience.
* ... I can create, edit and delete recipes while saving favourites my own profile for quick retrieval at a later date. 

## Database
I chose the "..." database as the source of all my recipes and images.

### Designing the Database
The first job was to decide upon the categorization of my database. How I would structure the recipe hierarchy, by country of origin, ingredients, speed of preparation and / or cost. A more indepth inspection of the database itself would highlight fields of commonality that would inform my hierarchy and allow for best filtering.

## Application Structure
The aim here was to separate the code into modules. This would allow for better readabilty, while also allowing for smaller functions to be reused. Therefore, sub-directories were used for ...

## Features

### Navigation

### Filters

### Profile & Login

### Recipe CRUD

### Comments

## Features Left to Implement
As the range of available stock on the menu has been purposely limited so as to reduce decision fatigue for the users, I am also aware that a more wide
ranging menu would be better suited to a larger audience. Therefore, more options should be added to the database but I would warn that this will reduce
the scope of the original application that had a primary goal of reducing anxiety of choice around what should be the simple decision of finding a nice
meal or snack to consume.

## Technologies Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
HTML was used for the semantic structure and layout of the site.

* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
CSS was used to style the application and improve the aestheticss.

* [Javascript](https://www.ecma-international.org/)
Javascript was used to do some DOM manipulation in order to improve user experience. It was also used for event handlers on some components.

* [Python](https://docs.python.org/3/)
Python is used as the backend language for creating helper functions, logic and routes
Various modules were used to assist with parsing, math, json operations and file manipulation

* [Flask](http://flask.pocoo.org/)
Flask was used as a micro framework for constructing the backend.
It also provided useful functions that I could use to help with routing, errors and messages.

* [Jinja](http://jinja.pocoo.org/)
Jinja is the templating language used by flask. It allowed me the ability to construct partial templates and inject them into the HTML.

* [WTForms](https://flask-wtf.readthedocs.io/en/stable/)
WTForms was employed for user sign up and login. It done most of the heavy lifting when creating user profiles.

* [SSLify](https://github.com/kennethreitz/flask-sslify)
SSLify was used to ensure that all requests were carried out over secure https.

* [JSON](https://www.ecma-international.org/)
JSON is used as the primary data structure. It is one of the most common data strucures used in web development today.

* [PyMongo](https://api.mongodb.com/python/current/)
PyMongo was used to work with MongoDB through Python. 

* [GIT](https://git-scm.com/)
GIT was used throughout the development process for saving versions of my code base...

## Testing
### Automated Written Tests

### Cross Browser Testing

### User Tests

#### Bugs
I had constant issues with the jQuery for Materialize not recognizing the functions needed to make the sidenav or select dropdowns for
the add recipes form to work. When I initially built the sidenav, it worked fine. Therefore, I had not tested it again till after a long
way further down the road, by which time I noticed it was no longer working and giving an error. I rechecked my code in Materialize docs
and tried to use the suggested vanilla js instead but that too would not work. I checked to make sure the jQuery and JS dependencies for
Materialize were still loading before my JS script but they were fine. I have posted queries to Slack to assist with this issue?

## Deployment

## Credits
## Content & Media
The images used throughout the application were collected from [Pexels.com](https://www.pexels.com/), a free to use site for various images.