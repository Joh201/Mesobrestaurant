# Mesob Restaurant

<p>
Mesob restaurant is a nice restaurant located in Uppsala city which is known for being the center of education in Sweden. The city is home to Uppsala University where Prof.Carl Linneaus worked. He is renowed for his system of classifying and naming nature. The owner of Mesob restaurant wants to serve customers a delicious food from an east african country called Eritrea. Thus, the website was developed to enable Mesob restaurant owner to take bookings from customers, and to allow customers to book time at the restaurant so that they can dine there. It runs on Code Institute's mock terminal on Heroku.
</p>

[Here is the live version of my project](https://mesob21.herokuapp.com/)

![weblook of the site](/static/readmefiles/weblook.PNG)

## User stories

![User stories](/static/readmefiles/userstories.PNG)

## Wire frame

![Wire frame1](/static/wireframe/wireframe1.png)

![Wire frame2](/static/wireframe/wireframe2.png)

![Wire frame3](/static/wireframe/wireframe3.png)

![Wire frame4](/static/wireframe/wireframe4.png)

![Wire frame5](/static/wireframe/wireframe5.png)

![Wire frame6](/static/wireframe/wireframe6.png)

![Wire frame7](/static/wireframe/wireframe7.png)

![Wire frame8](/static/wireframe/wireframe8.png)


# Existing Features

## User section

### Home page

* The home page welcomes the user to the website.
* It informs the user to register or login to dine at Mesob restaurant.
* The footer of the home page provides the customer with information about the address, contact details,
  social media links and working hours of the restaurant.

![Home page](/static/readmefiles/homepage.PNG)

### The logo
* The logo of the restaurant is located at the top left corner of the home page.
* The logo 'Mesob' is infact the name of the food container in the background image of the home page.

![Logo](/static/readmefiles/logo.PNG)

### Register page

* This page contains a sign up form which allows the user to register inorder to book at Mesob restaurant.
* The user signs up by providing username, email(optional) and password.
* The username and password fields are required for the user to sign up.
* The user is also required to fill the password twice, and if it does not match the user gets appropriate information.
* If a user tries to register with the same username, the user gets an appropriate message that the user already exists.
* At the top of the sign up form there is a link for sign in if the user has ended up in the page by mistake, this helps the user to go to the login page directly.
* The sign up form contains a sign up button which the user uses to submit the form.

![Sign up page](/static/readmefiles/signuppage.PNG)


### Login page

* This page contains a sign in form which allows users to login to their accounts inorder to make a booking at the restaurant.
* The user logs in  by providing username and password.
* The username and password fields are required for the user to sign in.
* If the user makes a mistake while signing in, the user gets a feed back that the username or password is incorrect.
* At the top of the sign in form there is also a link for sign up page if the user has ended up in the page by mistake, upon clicking the link the user gets redirected to the register page.
* At the bottom of the sign in form there is a sign in button which enables the user to login.
* When users login, they get a feed back that they have sucessfully logged in.

![Login page](/static/readmefiles/signin.PNG)


### Booking list age

* When the user has registered or loged in, the user is directed to the booking list page.
* If the user has no previous bookings, the user reads a message 'You have no bookings, Please create a booking' and the user can create a booking by clicking the booking button in the page.
* If the user has previous bookings, the user can see a list of bookings on this page.
* In this page the users can see the name, number of guests, and date and time of their booking.
* The user can update or cancel the bookings by using the update and cancel buttons below each booking.

![No booking](/static/readmefiles/createbook.PNG)


![My booking](/static/readmefiles/mybookings.PNG)


### Booking page

* When the user has clicked the book button in the booking list page, the user is directed to the booking page.
* In the booking page the user is required to fill in all the fileds of the bookig form.
* If the user forgets to fill a field in the form the user is reminded to fill the field.
* The user can not make a booking without filling all the required fields of the booking form.
* The form allows the user to pick date and time from an interactive datetime calendar.
* If the user tries to book the same time as an existing booking, the user gets a feed back, which informs the user to book another time.
* Once the customer has filled in the form, the customer can add bookings by clicking the add booking button in the form, and gets redirected to the booking list page.

![Booking form](/static/readmefiles/addbook.png)


### Update booking page

* When the user has clicked the update button on the booking list page, the user is directed to this page.
* In the update booking page the customers can update their bookings.
* The user can not leave any of the update booking form fileds empty, and the user will be reminded of this if they forget to fill all the fields in the form
* Once the customer has changed the booking details, the customer can update bookings by clicking the Update booking button in the page, and gets redirected to the booking list page, where they can see their updated booking.

![Update booking](/static/readmefiles/update.PNG)

### Canceling a booking
* While the user is in the booking list page, the user can easily cancel a booking by clicking the cancel button under each booking.

![Cancel booking](/static/readmefiles/cancel.PNG)


### Logout page
* when the user tries to logout, the user is asked to confirm the sign out inorder to avoid accidental logouts.
* When users logout, they get a feed back that they have sucessfully logged out.

![Sign out](/static/readmefiles/signout.PNG)


## Site owner section

### Registered users

* The restaurant owner can see the list of registered customers in the admin panel of the website.
* The owner of the site can delete registered users if it is needed.
* The site owner can filter registered customers based on their status.

![Users](/static/readmefiles/registeruser.PNG)


### Bookings

* The restaurant owner can see the list of bookings made by customers in the admin panel of the website.
* The owner of the site can see a list display of the name, email, number of guests, and date and time of the customers bookings.
* The site owner can filter bookings from customers based on their first name, and date and time of booking.
* The site owner can search for bookings based on their first name or number of guests coming to the restaurant.

![search](/static/readmefiles/search.PNG)

* The owner of mesob restaurant can also delete bookings if it is necessary.

![Books](/static/readmefiles/booklist.PNG)


## Future Features
* When time allows I would like to include Menu
* Multiple table occupancies

## Database Model

<p> The database model includes the username, first name, last name, email, number of guests, and date and time of arrival. The username allows the site owner to identify the registered customers. Since, the username is a foreign key, it helps the owner to delete multiple bookings by one customer with one click. The view logic also uses this field to identify the user in the database, and to display and manage the bookings of a loged in user. First and last name fields provide information about the customers. The email field can be used by the restaurant owner to communicate with customers, for example, to provide offers or to notify customers about changes. The number of guests, and date and time of arrival allows the owner to make necessary plans to accommodate guests. The date and time fields are also used to avoid same time booking by customers.
</p>

![Database](/static/readmefiles/database.PNG)

## Testing

* I have manually tested the following:
* The website works on different browsers: Chrome, Microsoft Edge, Firefox.
* The website is responsive and works on the standard screen sizes of the devtools device toolbar.
* The above mentioned features work as expected.
* I have also tested on gitpod and Code Institute's Heroku Terminal.


## Validator Testing

<li>HTML
  <ul>
  <li> A warning and minor errors were detected when passing through the official (W3C) validator.</li>
  </ul>
</li>

   [Home page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmesob21.herokuapp.com%2F)

   [Register page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmesob21.herokuapp.com%2Faccounts%2Fsignup%2F)

   [Login page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmesob21.herokuapp.com%2Faccounts%2Flogin%2F)

  <li>CSS
   <ul>
   <li> No error was detected when passing through the official (Jigsaw) validator. </li>
   </ul>

   <li> Python code
  <ul>
  <li> No error was detected when passing through the official (PEP8) validator.</li>
  </ul>
</li>
</ul>

## Bugs

### Solved Bugs

* During the development of the project I encountered a typo bug that was preventing me from creating the list display in the admin panel, and the problem was fixed when I corrected the typo.

### Remaining Bugs
* There are no remaining bugs.

## Accessibility

<ul>
  <li> The acessibility was tested using lighthouse in the devtools and it shows that the colors and fonts used for the website are user friendly.</li>
  </ul>


  ### Home page accessibility

![Home page accessibility](/static/readmefiles/home.PNG)

### Register page accessibility

![Register page accessibility](/static/readmefiles/homeaccin.PNG)

### Login page accessibility

![Login page accessibility](/static/readmefiles/homeaccre.PNG)

### My bookings page accessibility

![My bookings](/static/readmefiles/booklistac.PNG)

### Booking page accessibility

![Book](/static/readmefiles/bookingac.PNG)


### Update page accessibility

![Book](/static/readmefiles/updateac.PNG)


# Deployment
* The project was deployed using Code Institute's Heroku mock terminal.
* The following steps were followed during deployment:

## Step 1: Installing Django and supporting libraries

**Key:**
For this project, **_PROJ_NAME_** is “MESOBRESTAURANT” and **_APP_NAME_** is “mesob”.

**In the Terminal:**

```
# Step Code
```
1. Install Django and gunicorn: pip3 install django gunicorn
2. Install supporting libraries: pip3 install dj_database_url psycopg
3. Install Cloudinary Libraries pip3 install dj3-cloudinary-storage
4. Create requirements file pip3 freeze --local > requirements.txt
5. Create Project django-admin startprojectPROJ_NAME**.**
    _(Don’t forget the. )_
6. Create App python3 manage.py startappAPP_NAME

**settings.py**

```
# Step Code
```
7. Add to **installed apps** ‘APP_NAME’,


**In the Terminal:**

```
# Step Code
```
8. Migrate Changes python3 manage.py migrate
9. Run Server to Test python3 manage.py runserver

## Step 2: Deploying an app to Heroku

4 stages:

1. Create the Heroku app
2. Attach the database
3. Prepare our environment and settings.py file
4. Get our static and media files stored on Cloudinary.

**2.1 Create the Heroku app**

**In Heroku:**

```
# Step Code
```
1. Create new Heroku App APP_NAME, Location =Europe
2. Add Database to App
    Resources

```
Located in the Resources Tab, Add-ons, search and
add e.g. ‘Heroku Postgres’
```
3. Copy DATABASE_URL Located in the Settings Tab, in Config Vars, Copy
    Text

**2.2 Attach the Database:**

**In gitpod**

```
# Step Code
```
4. Create new env.py file on top
    level directory

```
E.g. env.py
```

**In env.py**

```
# Step Code
```
5. Import os library import os
6. Set environment variables os.environ["DATABASE_URL"] = "Paste in Heroku
    DATABASE_URL Link"
7. Add in secret key os.environ["SECRET_KEY"] = "Make up a
    randomSecretKey"

**In heroku.com**

```
# Step Code
```
8. Add Secret Key to Config Vars SECRET_KEY, “randomSecretKey”

**2.3 Prepare our environment and settings.py file:**

**In settings.py**

```
# Step Code
```
9. Reference env.py _from pathlib import Path_
    import os
    import dj_database_url

```
if os.path.isfile("env.py"):
import env
```
10. Remove the insecure secret
    key and replace - _links to the_
    _secret key variable on Heroku_

```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
11. **Replace** DATABASES Section
    (Comment out the old
    DataBases Section)
    - _links to the DATATBASE_URL_
    _variable on Heroku_

### DATABASES = {

```
'default':
dj_database_url.parse(os.environ.get("DATABASE_
URL"))
}
```

**In the Terminal**

```
# Step Code
```
12. Make Migrations python3 manage.py migrate

**2.4 Get our static and media files stored on Cloudinary:**

**In Cloudinary:**

```
# Step Code
```
1. Copy your CLOUDINARY_URL
    e.g. API Environment Variable.

```
From Cloudinary Dashboard
```
**In env.py:**

```
# Step Code
```
2. Add Cloudinary URL to env.py _-_
    _be sure to paste in the correct_
    _section of the link_

```
os.environ["CLOUDINARY_URL"] =
"cloudinary://9444:SUZi@dbhyuj5mc"
```
**In Heroku:**

```
# Step Code
```
3. Add Cloudinary URL to Heroku
    Config Vars _- be sure to paste_
    _in the correct section of the link_

```
Add to Settings tab in Config Vars e.g.
COUDINARY_URL,
cloudinary://9444:SUZi@dbhyuj5mc
```
4. Add
    DISABLE_COLLECTSTATIC to
    Heroku Config Vars
    **(temporary step for the**
    **moment, must be removed**
    **before deployment)**

```
e.g. DISABLE_COLLECTSTATIC, 1
```

**In settings.py:**

```
# Step Code
```
5. Add Cloudinary Libraries to
    installed apps

### ...

```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
...
(note: order is important)
```
6. Tell Django to use Cloudinary
    to store media and static files
    _Place under the Static files_
    _Note_

```
STATIC_URL = '/static/'
STATICFILES_STORAGE =
'cloudinary_storage.storage.StaticHashedCloudinaryS
torage'
STATICFILES_DIRS = [os.path.join(BASE_DIR,
'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
```
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
```
7. Link file to the templates
    directory in Heroku
    _Place under the BASE_DIR_
    _line_

```
TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
8. Change the templates
    directory to TEMPLATES_DIR
    _Place within the TEMPLATES_
    _array_

### 'DIRS': [TEMPLATES_DIR]

9. Add Heroku Hostname to
    ALLOWED_HOSTS

### ALLOWED_HOSTS =

```
["PROJ_NAME.herokuapp.com", "localhost"]
```

**In Gitpod:**

```
# Step Code
```
10. Create 3 new folders on top
    level directory

```
media, static, templates
```
11. Create procfile on the top level
    directory

```
Procfile
```
**In Procfile**

```
# Step Code
```
12. Add code web: gunicornPROJ_NAME.wsgi

**In the Terminal:**

```
# Step Code
```
13. Add, Commit and Push git add.
    git commit -m “Deployment Commit”
    git push

**In Heroku:**

```
# Step Code
```
14. Deploy Content manually
    through heroku/

```
E.g Github as deployment method, on main branch
```

## Credits
* Code institute for the deployment process and deployment terminal.
* For converting pdf file to markdown: (https://pdf2md.morethan.io/)











