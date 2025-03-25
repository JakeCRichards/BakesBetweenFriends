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

## Testing  
Testing is conducted to ensure the platform is robust and user-friendly.  
| **Validator**       | **Comments**                                                                 | **Screenshot**       |
|----------------------|-----------------------------------------------------------------------------|----------------------|
| HTML Validator       | No errors found; all HTML elements are properly nested and structured.       | ![HTML Validator](#) |
| CSS Validator        | One warning about unused CSS rules; no critical errors detected.            | ![CSS Validator](#)  |
| Lighthouse           | Performance score: 90, Accessibility score: 95, SEO score: 100.             | ![Lighthouse](#)     |
| Python Validator     | Code adheres to PEP8 standards; one minor warning about line length.         | ![Python Validator](#) |
| Browser Dev Tools    | Identified one missing alt attribute in an image tag.                       | ![Dev Tools](#)      |

- **Manual Testing:** Ensure seamless interaction between components. 
- **User story evaluation**  
- **Automated Testing:** I did not carry out automated testing

## Deployment  
The project is deployed using the following steps:  
1. **Hosting Platform:** The application is hosted on [Heroku].  
2. **Version Control:** Code is managed using Git and GitHub.  

The live link can be found here: [Bakes Between Friends](https://bakes-between-friends-a9965fdf43a6.herokuapp.com/)
The GitHub Repository can be found here: 

## Credits  
Special thanks to:  
- **Code Institute:** For providing the foundational knowledge and resources.  
- **Django Documentation:** For guidance on implementing features.  
- **Open Source Libraries:** 


