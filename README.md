# 🥖 Bakes Between Friends

## Table of Contents

- [About the Project](#about-the-project)
- [Initial Plan](#initial-plan)
- [Description](#description)
- [Agile and User Stories](#agile-and-user-stories)
- [Wireframes](#wireframes)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


## About the Project  
**Bakes Between Friends** is a community-driven platform where users can share, discover, and interact with recipes. Inspired by *Jake’s Bakes*, this project expands the love of baking and cooking into an interactive experience where anyone can contribute their favourite recipes.  

## Initial Plan
### Project Intentions
This project aims to:  
- Create a user-friendly platform for sharing and discovering recipes.  
- Implement full CRUD functionality (Create, Read, Update, Delete) for recipes.  
- Foster a sense of community by allowing users to like, comment, and engage with shared recipes.  
- Provide an intuitive search feature to help users find recipes based on ingredients or keywords.  
- Offer a responsive and accessible design for seamless use on mobile and desktop.  

### Features (Planned)
- User authentication (Sign Up, Login, Logout)  
- Recipe submission with title, ingredients, instructions, and images  
- Ability to edit and delete user-owned recipes  
- Search and filter functionality for recipes  
- Like and comment system for community engagement  

### Tech Stack  
- **Frontend:** HTML, CSS, JavaScript (with a Bootstrap framework)  
- **Backend:** Python 
- **Database:** PostgreSQL
- **Hosting:** Heroku  

### User Experience Design  
The design process focuses on creating an intuitive and visually appealing interface. Key considerations include:  
- **User Personas:** Identifying target users such as home bakers, professional chefs, and food enthusiasts.  
- **Wireframes:** Initial sketches and prototypes to map out the layout and functionality.  
- **Accessibility:** Ensuring the platform is usable for individuals with disabilities by adhering to WCAG guidelines.  
- **Responsiveness:** Designing for seamless use across devices, including mobile, tablet, and desktop.

## Description


## Agile and User Stories
The project follows Agile methodologies to ensure iterative development and continuous improvement.   
- **Kanban (Project) Board:** In line with Agile methodology, I wrote user stories in the planning and development of our website. The full details of these can be found on our project board.

![User Stories Project Board](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Project-board.png)

- **Daily Standups and Standdowns:** Regular updates to report on progress  


## Wireframes
Before starting the project, a couple of basic wireframes were created to visualise the final product. Both mobile and desktop wireframes were developed.


## Entity Relationship Diagram
When planning out the models for this project, I created the following ERD

![ERD](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/ERD.png)

## Features 
The platform includes the following features:  
**Responsive Design** 
The website is responsive and works on various devices, including desktops, tablets, and smartphones. This ensures that users have a consistent and enjoyable experience regardless of the device they are using. The responsive design adapts to different screen sizes and orientations, providing optimal usability and accessibility.
Homepage
![Homepage Responsiveness](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Responsive-homepage.png)
Recipes List
![Recipes Responsiveness](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Responsive-recipes.png)
Detailed Recipe View
![Detailed Recipes Responsiveness](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Responsive-recipe_detail.png)

- **Authentication:** 
Secure user registration, login, and logout. The navbar changes depending on logged in status

Registration
![Sign up page](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Sign-up.png)

Log in
![Sign in page](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Sign-in.png)

Nav Bar Changes
![Logged out Navbar](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Logged-out.png)
![Logged in Navbar](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/Logged-in.png)

- **Recipe Management:** Full CRUD functionality for recipes.  
- **Community Engagement:** Like and comment on recipes.  
- **Rich Text Editor:** Use of Django Summernote for formatting recipe ingredients and instructions.
- **Beginning of search:** Use of Categories to provide a simple search functionality with potential for more  


## Technologies Used

1. **HTML5** - The structure of the site was created using HTML5.
2. **CSS3** - The styling of the site was created using CSS3.
3. **JavaScript** - The site uses JavaScript for interactivity.
4. **Python** - The site uses Python for the backend.
5. **Django** - The site uses the Django web framework.
6. **Bootstrap** - The site uses the Bootstrap framework for styling.
7. **Font Awesome** - The site uses Font Awesome for icons.
8. **Google Fonts** - The site uses Google Fonts for typography.
9. **Heroku** - The site is deployed on Heroku.
10. **PostgreSQL** - The site uses a PostgreSQL database.
11. **Cloudinary** - The site uses Cloudinary for image hosting.


## Testing  
Testing is conducted to ensure the platform is robust and user-friendly.  
| **Validator**       | **Comments**                                                                 | **Screenshot**       |
|----------------------|-----------------------------------------------------------------------------|----------------------|
| HTML Validator       | Errors were found but only in richtext generated by summernote field       | ![HTML Validation](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/HTML-validation.png) |
| CSS Validator        | No errors found. Only 1 warning about imported CSS Librarys            | ![CSS Validator](https://github.com/JakeCRichards/BakesBetweenFriends/blob/main/static/assets/images/readme/CSS-validation.png)  |
| Lighthouse           | Performance score: 90, Accessibility score: 95, SEO score: 100.             | ![Lighthouse](#)     |
| Python Validator     | Code adheres to PEP8 standards; one minor warning about line length.         | ![Python Validator](#) |
| Browser Dev Tools    | Identified one missing alt attribute in an image tag.                       | ![Dev Tools](#)      |

### Manual Testing  
Manual testing was conducted to ensure the functionality and usability of the platform. The following tests were performed:  

- **Navigation Links:**  
    - Verified that all navigation links in the navbar and footer direct to the correct pages.  
    - Checked that the navbar updates dynamically based on the user's authentication status (logged in vs logged out).  

- **Authentication:**  
    - Tested user registration, login, and logout functionality.  
    - Ensured error messages display correctly for invalid inputs (e.g., incorrect password).  

- **Recipe Management:**  
    - Verified that users can create, edit, and delete recipes.  
    - Checked that only the recipe owner can edit or delete their recipes.  

- **Community Features:**  
    - Tested the like and comment functionality on recipes.  
    - Ensured comments are displayed in chronological order.  

- **Search and Categories:**  
    - Verified that the category-based search filters recipes correctly.  

- **Responsiveness:**  
    - Tested the website on various devices (desktop, tablet, mobile) to ensure responsive design.  

- **Error Handling:**  
    - Checked that 404 and 500 error pages display correctly when accessing invalid URLs.    

- **Forms:**  
    - Ensured all forms (e.g., recipe submission, login, registration) validate inputs and display appropriate error messages for invalid data.  



- **User story evaluation**  
### User Story Evaluation Summary  

| **User Story Summaries**                                      | **Achieved** | **Comments**                                                                 |
|----------------------------------------------------------|--------------|-------------------------------------------------------------------------------|
| As a user, I want to register an account                 | Yes          | Users can successfully register and create an account.                       |
| As a user, I want to log in and log out                  | Yes          | Login and logout functionality works as expected.                            |
| As a user, I want to create a recipe                     | Yes          | Users can submit recipes with all required fields.                           |
| As a user, I want to view recipes                 | Yes          | Users can views recipes.                                        |
| As a user, I want to edit recipes                 | Yes          | Users can edit their own recipes.                                        |
| As a admin, I want to publish recipes               | Yes          | Adminds can publish recipes.                                      |
| As a user, I want to like recipes                        | Yes          | Users can like recipes, and the like count updates dynamically.              |
| As a user, I want to comment on recipes                  | Yes          | Users can leave comments, which are displayed in chronological order.        |
| As a user, I want to edit/delete comment on recipes                  | Yes          | Users can edit/delete their comments.        |
| As a user, I want the website to be responsive           | Yes          | The website is fully responsive across devices.                              |
| As a user, I want to view recipes shared by others       | Yes          | Users can browse and view recipes shared by the community.                   |
| As a user, I want to navigate the website easily         | Yes          | Navigation links are intuitive and functional.                               |
| As a user, I want to be able to search the website            | Partially    | No search functionality but listed by category to allow easier searching |

- **Automated Testing:** I did not carry out automated testing due to a lack of time

## Deployment  
The project is deployed using the following steps:  
1. **Heroku** 
The site was deployed to Heroku from the main branch of the repository early in the development stage for continuous deployment and checking.

The Heroku app is setup with 3 environment variables, repalcing the environment variables stored in env.py (which doesn't get pushed to github).

In order to create an Heroku app:

1.  Click on New in the Heroku dashboard, and Create new app from the menu dropdown.

2.  Give your new app a unique name, and choose a region, preferably one that is geographically closest to you.

3.  Click "Create app"

4.  In your app settings, click on "Reveal Config Vars" and add the environment variables for your app. These are:

        - DATABASE_URL - your database connection string
        - SECRET_Key - the secret key for your app
        - CLOUDINARY_URL - the cloudinary url for your image store

The PostgreSQL database is served from ElephantSQL

Once the app setup is complete, click on the Deploy tab and:

    1. Connect to the required GitHub account
    2. Select the repository to deploy from
    3. Click the Deploy Branch button to start the deployment.
    4. Once deployment finishes the app can be launched.

The app can be accessed at the following link:[Bakes Between Friends](https://bakes-between-friends-a9965fdf43a6.herokuapp.com/)


2. **Version Control:** Code is managed using Git and GitHub.  


The GitHub Repository can be found here: [Bakes Between Friends GitHub](https://github.com/JakeCRichards/BakesBetweenFriends)

## Credits  
Special thanks to:  
- **Code Institute:** For providing the foundational knowledge and resources.  
- **Django Documentation:** For guidance on implementing features.  
- **Open Source Libraries:** 


