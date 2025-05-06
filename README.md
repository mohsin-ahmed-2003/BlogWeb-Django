# BlogWeb-Using-Django
It is Dynamic webpage developed using a Django <br>
Here User dont need to update the html code whenever then want to upload a blog<br>
User only need to Upload the blog on admin page of website , it will automatically update the html page and show the content on webpage<br>
# Steps to follow for setting up the Code:
**1. Clone the Repository **<br>
Open your terminal or command prompt.<br>
git clone https://github.com/mohsin-ahmed-2003/BlogWeb-Django/<br>

**2. Navigate to the Project Directory:** <br>

Change your current directory in the terminal to the newly created project directory:<br>
cd NT <br>
**3. Install Dependencies:** <br>
pip install -r requirements.txt <br>
# UPDATE CODE FOR CONTACT FORM IN WEBPAGE
In NT folder click the **settings.py** file and scroll down to the line **137** <br>
**Enter your gmail id** there and also the **App password** that is provided in your google 2-set-verification in google settings: <br>
<img width="960" alt="image" src="https://github.com/user-attachments/assets/278886b4-a14f-45a5-bcb8-5dcb8b95a55f" />

<br>

**4. Apply Migrations:** <br>
Django uses migrations to manage database schema changes. This will create the necessary database tables based on the models defined in the Django app(s).<br>
Run the following command to apply any pending migrations:<br>
python manage.py migrate<br>

**5. Create a Superuser** <br>
The blog has an admin interface, you'll likely need a superuser account to access it. Create one using: <br>
**6. python manage.py createsuperuser** <br>
<br>
Follow the prompts to enter a username, email address (optional), and password.<br>
**7. Start the Development Server:**
python manage.py runserver <br>
You should see output in your terminal indicating that the server has started, usually at http://127.0.0.1:8000/. <br>
**8. Access the Blog in Your Browser:** <br>
Open your web browser and navigate to the address provided by the runserver command (usually http://127.0.0.1:8000/).<br>
# OUTPUT <br>

![WB1](https://github.com/user-attachments/assets/62d52c99-46ff-40e7-9b8e-1d68daafc2c7)
<br>
# Access the Admin Interface
Enter /admin/ in link <br>
http://127.0.0.1:8000/admin/<br>
<br>
<br>
![WB5](https://github.com/user-attachments/assets/b7e71f69-9671-4bd8-9607-07a880aa6b28)

**i) Enter author name by clicking Author > Add Author**
<br>
<br>
![WB6](https://github.com/user-attachments/assets/24d4ed28-d1a6-4bc4-8031-6054435b9fee)

**ii) Now enter the Blog Details**(e.g., Blog image, title, created date, Content, etc.)<br>
<br>
<br>
![WB8](https://github.com/user-attachments/assets/560b2dd5-ec7d-4c4e-a4fc-b32ee38896f8)

**Then refresh the homepage and the blog will be shown**
<br>
<br>
![WB1](https://github.com/user-attachments/assets/1199b0dd-4982-440f-a1e3-bf6b2c1c2ab8)
<br>
when you click on any page the blog detail page will be opened:
<br>
![WB3](https://github.com/user-attachments/assets/3757e806-b6c4-456b-a18e-80b951b050d3)
<br>
<br>
# Contact form
<br>
<br>
![WB2](https://github.com/user-attachments/assets/c462aab9-ecbd-4953-a266-abbf3978d8c6)
<br>
**OUTPUT FOR CONTACT FORM**
<br>
<br>

![image](https://github.com/user-attachments/assets/87b7c13e-bef4-42bd-afaa-6d8582a775d5)

<br>
<br>
After sending Message succesfully the alert is shown at the top of the page with successfully sent message!
<br>
<br>

![WB4](https://github.com/user-attachments/assets/aacd2ca2-4a51-43f0-ae24-244b7a48fb41)

<br>
<br>

**NOTE: For Any query contact me**
