# WEBSITE NAME  
**Atalanta BC Fan Hub**

## GitHub Repository  
The source code for this project is available on GitHub:  
[https://github.com/dramaticamo/atalanta_fan_site](https://github.com/dramaticamo/atalanta_fan_site)

## Identification  
**Name:** Aung Myo Oo  
**P-number:** P-462183  
**Course code:** IY4103

## Declaration of Own Work  
I confirm that this assignment is my own work.  
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.

## Introduction  
The Atalanta BC Fan Hub is a fun and easy-to-use website made for fans of the Italian football club Atalanta BC. It lets users explore everything about the team in one place. Fans can see upcoming matches with a live countdown, check out player stats, view past and future fixtures, and even shop for team gear in the online store.

The site has a clean and modern design that works well on all devices. Users can vote for their favorite player, see the Serie A league table, and interact with the site in real time. The online store includes jerseys and accessories, and users can add items to the cart and see the total cost before checkout.

Built with Flask, HTML, CSS, JavaScript, and SQLite, the app shows how different tools work together to create a dynamic and interactive fan experience. Everything is organized and easy to use, so fans can enjoy browsing and supporting their team online.

The website includes:
- A home page with match countdown and featured players
- A detailed team stats section
- Fixtures with scorers
- An interactive online store with cart system

The goal is to create a fan-friendly experience and showcase core web development skills like Flask routing, database integration, dynamic content rendering, and UI design.

## Installation  
- To run this website, you will need Python 3.x installed on your computer.
- Once Python is ready, install all the required packages by running this command in your terminal:
pip install -r requirements.txt
- This will make sure everything the app needs is installed and ready to go.

## How to Run the website
- Start by running the Flask app. In your terminal, use the command:
python web.py
- Once it starts, open your browser and go to: 
http://127.0.0.1:5000

- On the Home page, you can view the latest news, countdown to the next match, featured players, and vote for Player of the Month.
- Go to the Players page to see all Atalanta players, grouped by position. Click on any player to see detailed stats and info.
- Visit the Fixtures page to check past and upcoming matches. You can also click to see who scored in each match.
- On the Team Stats page, you can view the full Serie A table. Atalanta is highlighted for easy reference.
- Head to the Store to browse team jerseys, accessories, and gear. You can filter items, add products to your cart, and see the total price instantly.
- Enjoy a smooth and responsive experience throughout the site, with easy navigation and modern design.
- This website is designed to be user-friendly and fun for all Atalanta fans!

## Application Elements
- Database Integration (SQLite): Player data, match fixtures, stats, and store items are stored in a database and shown on the website dynamically.
- Dynamic Routing: Pages like player profiles and match details change based on what the user clicks, using Flask routes.
- Template Inheritance: All pages use a base template for consistent layout, making it easy to manage navigation and styling.
- JavaScript Functions:
- Match countdown timer on the home page.
- Interactive voting for "Player of the Month".
- Store cart system to add/remove items and calculate total cost.
- CSS Styling: A mix of custom CSS and Bootstrap is used for a clean and responsive design that works on all screen sizes.
- User Interface: Easy-to-use and designed with Atalanta’s blue-and-black branding to make it feel like a real fan site.

## Libraries Used
The following libraries are used in this project:

- Flask: Used as the main backend web framework for routing and serving pages.
- SQLite3: Used as the database to store player stats, fixtures, and store data.
- Jinja2: Used with Flask to create dynamic HTML templates.
- Bootstrap: For responsive and clean front-end design.
- JavaScript (Vanilla): Adds interactivity like countdown timer, voting, and cart system.
- HTML/CSS: Used for structuring and styling the pages.

## Project Structure
- web.py: The main Flask application file that controls routing, data processing, and dynamic page rendering.
- templates/: Contains all HTML templates used for different pages.
- index.html: The main page with countdown, news, and player highlights.
- players.html: Shows all Atalanta players and their details.
- playerdetail.html: Displays detailed stats and info for an individual player.
- fixtures.html: Displays upcoming and past match fixtures with goal scorers toggle.
- stats.html: Displays the Serie A standings with Atalanta highlighted.
- store.html: Fan store with jersey and gear listings, cart system, and price updates.
- navbar.html: The navigation bar used across all pages (included in each page template for consistency).
- static/: Stores all static files such as CSS and images.
- static/css/: Contains stylesheets for layout, colors, and responsiveness.
- static/images/: Holds images like team logos, player photos, and store item pictures.
- database.db: The SQLite database file that stores data for players, fixtures, stats, and products.
- requirements.txt: Lists all Python libraries required to run the project.
- README.md: This file. It gives setup steps, usage instructions, and project overview.
