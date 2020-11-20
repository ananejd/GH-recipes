# GH_Recipes

The project is a database-driven online collection of Ghanaian Dishes. The project utilises Flask to
create the application, using MongoDB as a data store, with a back-end functionality written in python.

The project seeks to adopt the CRUD functionality in its setup, allowing a user to create, read,
update and delete recipes.

## Demo 
<hr>
Find a live version <a href=""http://ami.responsivedesign.is/?url=https:///gh-recipes.herokuapp.com/"">here</a>

![](assets/images/RM2.png)


## UX Design

My design was inspired by [the site builder report website](https://www.sitebuilderreport.com/inspiration/food-websites), 
which is basically a collection of website design. The intension for the design is to capture a first time users attention to the page 
by greeting the eyes with good looking food and for people who do not know anything about Ghana, this is perhaps a good way to present 
Ghana to your eyes by way of imagery as found on the home page. Users have the option of digging into the images that 
capture their attention by clicking to read recipe descripstions. the design also invites people with knowledege about 
Ghanaian foods to to sign up and add up to the collections on the site. 

The home page displays the navigation bar with the brand of GH-RECIPES on the left of the page
and four navigational icons on the right of the page. Immediately below that is a display imge of 
a ghanaian dish which a welcome inscription to the user. This is followed by a display of recipes in 
the body and finally a footer displaying the developer involved in the project

The recipe page displays a list of recipes for which upon full completion of the project users 
will be fully able to create, Read, Update and Delete recipes as they wish.

The Login navigational icon allows regualar users to get back into their profile 
to fully access their previous activities on the page as well as create new ones.

The sign up icon permits new users to establish a profile on the page.

To return to the home-page a user simply clicks the Logo which is a common convention in programming,
I also added a home button alongside the logo to make this clearer. The back to the top button at 
the bottom right of the home page allows users to navigate easily by way of a click to the navigation bar.

## Features

### home

the home feature is intended to be a showcase of recipes visitors to the site will be able to to 
click on and read about. It also offers users links to other functionalities of the site

### Recipe

It is intended that users read, add and make changes to recipes on display using this icon. it offers a 
link to the data store.

### Log in

previous users of the website can assess their previous activities by loging in. Thereupon they can 
proceed to contribute to the data in store.

#### Add Recipe

Upon a successful log in, users can proceed to acess the Add Recipe functionality of the page by clicking 
and keying in information they require.

### Signup

For new users of the site, the signup icon offers them the ability to sign up and offer their contribution 
to the recipe store available.

#### Edit Recipe

A user is able to make edits to recipes found on the website. MongoDB allocates
each entry into a collection with an object ID and this is what is used to 
locate the individual recipe the user wants to edit and pre-fill the form
for the user. After the user has made the necessary changes they submit the form
and MongoDB's update() method to update the recipe.

## Technologies Used

- Python 3.4.3
- Flask (Python Microframework)
- BootStrap 3
- JavaScript
- CSS
- HTML
- WTForms
- Materialize

## Testing

#### Testing Add Recipe Form

- Test that a new added recipe immediately appears on the website's homepage
- Go to form and try to submit empty fields and make sure WTForms 
InputRequired() is working
- Try to submit an empty ingredients list and make sure in-line validation is
working
- Try to submit a value in the Image URL field that is not a valid URL to make
sure the custom JavaScript validator is working
- Ensure that the random number JS function for upvotes is being created when 
adding new recipe.
- Making sure that the select fields are being populated with all of the 
correct choices
- Ensure that the removal of newly created rows for ingredients/preparation
steps is possible and make sure that all of the rows are unable to be deleted
with feedback for user if they try.

#### Testing Edit Recipe Form

- Make sure that the form is being populated with the correct data from the
MongoDB document when editing recipe.
- Ensure that adding/removing ingredient/preparation step rows is not causing
an issue with clashing names when submitted
- Ensure a recipe is able to be updated more than once without any bugs
occuring (such as fields going missing or name clashes causing issues)
- Test that the select fields are producing the correct options.

## Database Schema

The database is structured with 5 collections, recipes  The two
collections are related as recipes contains a 'cuisine name' key that
corresponds the cuisine documents.

The recipes document itself contains unstuctured data. With key/value pairs
that make up a description of the recipe. The ingredient name, quantity and
value all have the same number within the key, and they are grouped through the
use of sorting by number and sliced for data representation.

An example of a recipe document can be found in static/images/doc_example.png


## Deployment
This project was built using Python 3.8.6 and Flask 1.1.2.
1. The project was deployed to Heroku with config vars:
1. created requirements.txt that Heroku knows which packages are required for the application to run and install them.
1. created Procfile that Heroku knows what kind of application this is.
1. project eventually deployed at 
<a href="https://gh-recipes.herokuapp.com/">here</a>">

#### Challenges 
Several chanllenges came up in the cause of building this project which are still being addressed.
