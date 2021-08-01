**Start the Quotes Generator Project**

1. Inside the terminal create a Django project named quotegenrator by running in terminal:
```console
~$ django-admin startproject quotegenerator
```
2. Change the directory to the project and  run a migration to configure the database used by the default apps:
```console
~$ python3 manage.py migrate
```
**Start the Quotes Generator App**

1. Crate new app:
```console
~$ python3 manage.py startapp randomquotes
```
2. In the settings.py add randomquotes in the INSTALLED_APPS

**Create a Template**

1. Inside the project app directory, randomquotes/, create a folder named, templates. Next, within the newly created, templates/, create a folder named randomquotes to namespace our template file.

2. Within the namespaced template folder, create an HTML file named, quotes.html. The new file will contain some markup to format our message. Paste in the following HTML which has some placeholder in the text which will allow us to see text in the browser:
```html
<!DOCTYPE html>
<html lang="en">
<head>
 <title>Django Quote Generator</title>
 <style>
   body {
     text-align: center;
   }
 </style>
</head>
<body>
 
 <h1>Here is your quote:</h1>
 
 <p>Place holder for quote</p>
 
</body>
</html>
```
**Create a View Function**

1. Inside the randomquote app, open views.py. Define a new function named quote() that takes a single parameter, request. In quote(), return the render function with two arguments, the request and the path to quote.html as a string, "randomquote/quote.html".

**Wire Up View**

1. Create a file named urls.py inside the app directory.
2. Inside urls.py, we’ll need to import a couple of things to call the view function when the URL is requested.
At the top of urls.py import:   
path module from django.urls      
the functions from views.py.
3. Create a list of patterns for Django to match URLs against. Create a list called urlpatterns and set it as a blank list.
4. Inside the list,add a route to the quote() function using the path() function.  
Since we want to have our random quote appear as our main page, provide an empty string, "", as the first argument to path(). Pass the view function, quote(), as the second argument.
5. Import the include module to include the URL configuration file.   
Inside quotegenerator/quotegenerator, import the include module from django.urls.
6. In the existing urlpatterns list, add another path() with the arguments:   
"" to reference the home page  
include() with randomfortune‘s URLs as a string.

**Sending a Context to the Template**
1. Create a list of fortunes named quoteList inside the app views.py file. Define it outside of the fortune() function.
2. To select a random fortune from the list we’ll use a built-in Python function, random.choice().  
Import the random module at the top of views.py. Then inside the quote() function create a variable named quote and set it equal to random.choice(quoteList).
3. Below where we set quote, create a dictionary named context. In the dictionary, create a key named "quote" and set quote as the value.
4. Add context as the third argument to the render() function that quote() returns.
5. Inside quote.html, between the ```<p> </p>``` tags,replace the text with {{ quote }}.