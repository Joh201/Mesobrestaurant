# Mesob Restaurant

<p>
Mesob restaurant is a nice restaurant located in Uppsala city which is known for being the center of education in Sweden. The city is home to Uppsala University where Prof.Carl Linneaus worked. He is renowed for his system of classifying and naming nature. The owner of Mesob restaurant wants to serve customers with delicious food from an east african country called Eritrea. Thus, the website was developed to enable Mesob restaurant owner to take bookings from customers, and to allow customers to book time at the restaurant so that they can dine there. It runs on Code Institute's mock terminal on Heroku.
</p>

[Here is the live version of my project](https://mesob21.herokuapp.com/)

![weblook of the site](/static/readmefiles/websitelook.PNG)

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
* At the top of the sign up form there is also a link for sign in if the user has ended up in the page by mistake, this helps the user to go to the login page directly without leaving the page.
* The sign up form contains a sign up button which the user uses to submit the form

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

* When the user has clicked the book button on the booking list page, the user is directed to the booking page.
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

<p> The database model includes the username, first name, last name, email, number of guests, and date and time of arrival. The username allows the site owner to identify the registered customers. Since, the username is a foreign key, it helps the owner to delete multiple bookings by one customer with one click. The database also uses this field to display and manage the bookings of a loged in user. First and last name fields provide information about the customers. The email field can be used by the restaurant owner to communicate with customers, for example, to provide offers or to notify customers about changes. The number of guests, and date and time of arrival allows the owner to make necessary plans to accommodate guests.
</p>

![Database](/static/readmefiles/database.PNG)

## Testing

* I have manually tested the following:
* The website works on different browsers: Chrome, Microsoft Edge, Firefox.
* The website is responsive and works on the standard screen sizes of the devtools device toolbar.
* The above mentioned features work as expected.
* I have also tested on gitpod and Code Institute's Heroku Terminal.


## Validator Testing

### HTML
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










