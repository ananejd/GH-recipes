# GH_Recipes

The project is a database-driven online collection of Ghanaian Dishes. The project utilises Flask to
create the application, using MongoDB as a data store, with a back-end functionality written in python.

The project seeks to adopt the CRUD functionality in its setup, allowing a user to create, read,
update and delete recipes.

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

#### Add Recipe

A user is able to fill out a form and add a recipe to the database and therefore
the site using MongoDBs insert-one() function.

The upvotes section is not seen on the form, a JavaScript function is used to
produce a number between 0-10000 and applied to the recipe. This is to show how
the functionality would work with a live website.

#### Edit Recipe

A user is able to make edits to recipes found on the website. MongoDB allocates
each entry into a collection with an object ID and this is what is used to 
locate the individual recipe the user wants to edit and pre-fill the form
for the user. After the user has made the necessary changes they submit the form
and MongoDB's update() method to update the recipe.

#### Delete Recipe

Each recipe has a 'Delete Recipe' button found at the bottom of the page. Once
clicked it uses the remove() mongoDB method.


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
- Ensure the adding of new ingredients and steps rows through JavaScript is
working and that they are creating the correct names within the documents 
in MongoDB.
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

#### Other Tests

- Make sure the 'delete recipe' functionality is removing the correct document.
- Ensure that newly added cuisines become available on the add recipe form.
- Make sure removing a cuisine that recipes have as their cuisine doesn't cause
the website to crash.
- Test responsiveness of each page on different screen sizes and ensure all
elements stay readable.

## Database Schema

The database is structured with two collections, recipes  The two
collections are related as recipes contains a 'cuisine name' key that
corresponds the cuisine documents.

The recipes document itself contains unstuctured data. With key/value pairs
that make up a description of the recipe. The ingredient name, quantity and
value all have the same number within the key, and they are grouped through the
use of sorting by number and sliced for data representation.

An example of a recipe document can be found in static/images/doc_example.png


## Deployment

To Clone the project from github:

```python
$ git clone 
```

I recommend deploying the project in a virtual envioronment:

```python
$ cd directory-name
$ python3 -m venv virtual-env-name
```

You will need to install the dependencies found in the requirements.txt file:

```python
$ pip3 install -r requirements.txt 
```

To run the project locally use:

```python
$ python3 run.py
```

You can also run the app through Heroku.

The project was deployed to Heroku with config vars:

- IP = 0.0.0.0
- PORT = 5000

https:

There are no differences between the development and deployed versions.

Note the project is written with Python3 and not Python2.
