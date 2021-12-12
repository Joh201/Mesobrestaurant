# Mesob Restaurant

<p>
Mesob restaurant is a nice restaurant located in Uppsala city which is known for being the center of education in Sweden. The city is home to Uppsala University where Prof.Carl Linneaus worked. He is renowed for his system of classifying and naming nature. The owner of Mesob restaurant wants to serve customers with delicious food from an east african country called Eritrea. Thus, the website was developed to enable Mesob restaurant owner to take bookings from customers, and to allow customers to book time at the restaurant so that they can dine there. It runs on Code Institute's mock terminal on Heroku.
</p>

[Here is the live version of my project](https://mesob21.herokuapp.com/)

![weblook of the site](/static/readmefiles/websitelook.PNG)


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
* The form allows the user to pick date and time from an interactive datetime picker calendar.
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
* when the user tries to logout, the user is asked to confirm the sign out inorder to avoid accidental logouts

![Sign out](/static/readmefiles/signout.PNG)


## Site owner section






