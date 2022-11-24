# Cocktail
![alt text](/static/images/amiresponsive.PNG)


Cocktail is a website dedicated to alcoholic and non alcoholic beverages mixes in the form of a blog post where users can interact. 
When registered and logged in, users can comment, like and view recipes and also share their own cocktail recipes with others. 

This website is designed to fulfill the full stack framework milestone project IV requirements of the Code Institute course, being built in Django using Python, JavaScript, CSS and HTML.

View the live website on [Heroku](https://cocktail2022.herokuapp.com/)

Note: To open any links in a new tab, press CTRL + Click

---------------------------------------------------------------------------------------------------

## User Experience Design (UX)

### Strategy Plane

With the core UX principles in mind I started with the outline of the website by firstly identifying target audience and the needs of the enduser.
In the brainstorming phase I focused on answering  questions like "What type of content/functionality is crucial on the website?", "What type of content/functionality would be nice, but not essential?".
To create a comprehensive and appealing website I researched other recipe websites content and structure. 
The overview of how the competition looks like allowed me decide what features and functionalities would be necesary for my own project. 

Next steps were whireframing the website's design and create the database scheme. Using the Agile principles, during development the database scheme and whireframes suffered modifications. Therefore, the ones you will find in the README.md file are the latest versions.


*The typical user for the website would be someone who:*

- is most likely an adult passionate about mixing alkoholic and nonalkoholic drinks.
- Is looking to expand their knowledge in this area
- Is willing to share his/her own recipes 
- Is willing to offer his/her tips and/or impressions to other users


*The users visiting the website are looking for:*

- A wide range of cocktail recipes from all around the world
- Browse cocktail recipes
- Interacting with the site content by creating a personal account
- Storing all their recipes and access just the one they when they want to
- Writing reviews for the cocktails they have made/tried 


*The SuperUser has to be able to:*

- Approve cocktail recipe uploads and comments
- Filter through recipes, comments, and users to ease control of the site


*Site Goals:*

- To provide users a single place to find all the above 
- To have  intuitive controls and layout
- Wide compatibility with every Browsers and Devices.
- Enables its users not only to read, but to create, edit and delete content



*Site Owner Goals:*

- To provide the user with a professional web application
- Connect people who are interested in cocktails
- Inspire other people to have a colorful way enjoying their free time
- To encourage users to register and activate their profile


### EPICS & User Stories

The **Agile** methodology was used to plan the project and [Github](), the tool to demonstrate it.

*Projects* were used to divide the project into three iterations with a simple Kanban board.
*Milestones* were used to create Epics with a custom template
*Issues* were used to create User Stories with a custom template. Eash user story is clearly described with a title, statement, acceptance criteria and tasks.They were there not only to record User Stories but also used to FIX, UPDATE and record DOCUMENTATION updates as well.
Each user story was linked to an Epic and placed within one of three Iterations. 



EPIC| ADMIN

As a site admin I can CRUD drafts of recipes so that I finish them later
As a site admin I can CRUD recipes so that I can manage the data at any given time
As a site admin I can manage user's comments so that I can I disaprove the ones breaking the website guidelines
As a site admin I can CRUD reviews to cocktail posts so that I open conversations between the users 


EPIC | CONTENT DISPLAY

As a user I can view a paginated list of cocktails so that I can choose what I will mix
As a user I can click on an item in the list so that I explore the entire cocktail recipe and its comments


EPIC | ACCOUNT

As a user I can make my own account so that I can CRUD myself cocktail recipes and reviews
As a registered user I can login and logout of the site so that I can CRUD myself cocktail recipes and reviews


Epic | LIKES & REVIEWS

As a user I can like/unlike posts so that I can share my preferance regarding certain cocktails
As a logged-in user I can review a recipe so that I can interact with the other users
As a logged-in user I can CRUD my own cocktail recipes and reviews so that I can be in charge of my content 


Epic | BROWSING

As a logged-in user user I can search cocktails by title and ingredients so that I comfortably find the right one
As a logged-in user I can see a paginated list of the cocktails I liked so that I keep track with my favourites


### Scope Plane

A scope was defined to identify what needed to be done to align features with the strategy previously defined. Due to the imbalance of scores above, there will be some trade-offs. The was broken into these categories:

Content Requirements

The UX must address these:
- A comprehensive list of recipes.
- A comprehensive set of instructions with ingredients to follow.
- A list of all comments made on a recipe.

The UX should accommodate these:
- Easy navigation of the site.
- Ability to comment and like recipes.

## Design

The site employs a simple UI, with many standard UI components already familiar to the user and little to distract from the content itself.
Wireframe sketches were drawn up in Balsamiq. These reflect basic layout considerations rather than aesthetics.

### Logo
The logo, which is situated on the Nav Bar was created in Paint and meant to have a minimalistic style. The logo also acts as a link to take the user back to the home page.


### Color scheme

The color scheme was chosen as it feels clean and stylish in order to match any style of  cocktail could be introduced to the users. At the same time, it is both visually unintimidating and easy on the eye. The button colors are consistent throughout the app to maintain consistency and increase the intuitiveness of the page.


### Imagey

The *Hero Image* has the purpose to greet the user and instantly provide the website's purpose, being static. 
The rest of the images will be uploaded by various users.


## Structure Plane

### Logic Flow Chart

![alt text](/static/images/website-map.PNG)

### Wireframes

Site moc-ups were designed using Balsamiq wireframes. The focus was on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as mobile, tablet and larger screens.
 

#### Desktop

- [Home Page](/static/images/whire-home.PNG)

- [Cocktail Detail](/static/images/whire-cocktail.PNG)

- [My Cocktails](/static/images/whire-mobile-mycocktails.PNG)

- [My Favourites](/static/images/whire-favourites.PNG)

- [Searched Cocktail](https://balsamiq.cloud/s3pzm93/pvfw80q/r61AA/bE3DE)

- [Sign Up](/static/images/whire-signup.PNG)

- [Log In](/static/images/whire-login.PNG)

- [Log Out](/static/images/whire-logout.PNG)

##### Mobile

- [Home Page](/static/images/whire-mobile-home.PNG)

- [Cocktail Detail](/static/images/whire-mobile-cocktail.PNG)

- [My Cocktails](/static/images/whire-mobile-mycocktails.PNG)

- [My Favourites](/static/images/whire-mobile-myfavourites.PNG)

- [Sign Up](/static/images/whire-mobile-signup.PNG)

- [Log In](/static/images/whire-mobile-login.PNG)

- [Log Out](/static/images/whire-mobile-logout.PNG)

---------------------------------------------------------------------------------
## Information Architecture

### Database Models

![alt text](/static/images/data-scheme.PNG)

-----------------------------------------------------------------------------------
### Features

* Existing Features


*Logo* 

 * Displayed on every page for easy navigation, the user can click it to go back to the home page. 

![alt text](https://res.cloudinary.com/dyjmpid6t/image/upload/v1667035117/logo_xou93d.png)


*Nav-Bar* 

* Displayed on every page for consistency and easy navigation through the site map.

![alt text](/static/images/navbar.PNG)


*Search Form*

* The user can search through the database by the cocktail's name or by ingredients.

![alt text](/static/images/search.PNG)


*Footer*

* Placed at the bottom of each page, displayes icons to social media accounts. By clicking them, a new separate page will open in order not to interfere with the actual website surfing.

![alt text](/static/images/footer.PNG)


*Cards* 

* paginated by six,they hold information of the cocktail recipe title, likes and an image. When an image was not uploaded by the user who posted a certain cocktail recipe, a placeholder image will be displayed on the card.

![alt text](/static/images/card.png)

*Add Button*

* A call to action button is clearly visible to the logged in user to 'Add Cocktail' and open a new Form recipe with just one click.

![alt text](/static/images/add-cocktail.PNG)


*Recipe Form*

* Users who holds an account and are logged in can access the Form and edit/delete their own recipes by manipulating information in all the fields.

![alt text](/static/images/form.PNG)

![alt text](/static/images/save-delete.PNG)


*Remark Form* 

* It can be found underneath each cocktail recipe when fully displayed. Logged in users can comment recipes, and also delete their own comments.

![alt text](/static/images/remark-form.PNG)


*Remarks Section* 

* All users can read all comments, the author and the date when was commented.

![alt text](/static/images/remarks.PNG)


*Like/Unlike Button*

* Accompanies each cocktail recipe. Only logged in users can like/unlike. But the number of likes are  displayed for all users to see.

![alt text](/static/images/like.png)


*Detailed Section* 

* Displayed when clicked on a card. Here all users (logged in or not), can view details about the cocktail. 
* This page also includes features to like and comment if you are a logged in user. 
* Only the author of a post can be redirected from this section to edit/delete his/her cocktail recipe.

![alt text](/static/images/cocktail-detail.PNG)


*Edit/Delete Options*

 * Only the author of the recipe can visualise the Edit button and update and/or delete their own recipes.

 ![alt text](/static/images/edit.PNG)


*Sign Up Section*

When wanting to register the user can make use of this formular providing a required username and password (optional email address).

![alt text](/static/images/signup.PNG)


*Log In/ Log Out Section* 

The login / out section is used to login / out users with an existing account.
A message will appear once a user successfully logsin / out accordingly to the action.
![alt text](/static/images/login.PNG)

![alt text](/static/images/logout.PNG)

-----------------------------------------------------------------------------

## Technologies Employed

### IDE
* Gitpod

### Languages
* Python
* HTML
* CSS
* JavaScript

### Frameworks, Templates & Libraries
* Django
* Bootstrap
* Font Awesome
* Google Fonts

### Storage & Hosting
* Heroku
* Github
* Cloudinary

### Databases
SQLite3 for development
PostgresSQL for the deployed site

### Other Tools

Google Dev Tools (including Lighthouse)
Pep8online.com (to check Python code for PEP 8 requirements)
W3C Validator (to check validity of HTML and CSS)
JSHint.com (to check JavaScript)
dbdiagram.io (to produce the MongoDB ERD)


### Django and Heroku
* To get the Django framework installed and set up I followed the Code Institute's Django Blog [Cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

## Credits

### Content

Most recipes created on this site were taken from [Barschool](https://www.barschool.net/blog/cocktails-101-history-and-types).

### Media
Most images that were used on the site were taken from [Pexels](https://www.pexels.com/royalty-free-images/) and [Unsplash](https://unsplash.com/s/photos/cocktails)
### Code
References used:

* Stack Overflow
* Django Documentation
* Bootstrap Documentation
* Summernote GitHub Docs

Projects of other fellow colleagues which inspired this website:
* https://github.com/Iris-Smok/The-Healthy-Family-PP4
* https://github.com/sherryrich/heard-it
* https://github.com/Delboy/EatMe
* https://github.com/siobhanlgorman/favoureats
* https://github.com/CluelessBiker/project4
* https://github.com/KarinOldbring/vegan-a-eat
* https://github.com/Sharpryan20/food-twisters

-----------------------------------------------------------------------------

## Acknowledgements

 For inpiration in general, for code and advice, I'd like to give thanks to:

* Martina Terlevic

* Kasia Bogucka

### Sources

Code Institute student template for Gitpod, where all of the toolsto get started were preinstalled.

