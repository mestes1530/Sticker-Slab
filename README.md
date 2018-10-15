# **Sticker-Slab**

## Project Overview

Sticker Slab will be a simplistic static social media site where users will be given a webpage where they can upload images, text files or links and it will be displayed with as a sticker like icon on their webpage. There will be no feed or backlog of user’s posts, so it will be up to the user to manually remove older items to makes sure their webpage only has the most relevent items. I also hope to allow the user to have some access to the html file that renders their Sticker Slab profile so they can edit it's layout and style. 


## Functionality

A user profile will be a single webpage with small clickable sticker icons spread across it. Each sticker will correlate to an image, string or link the user has saved as a sticker to their profile. When a sticker is clicked it will be rendered on the page “Display” ether as an image, text or in a small web window (if it’s a link). The website will consits of the following pages:
- **Home/Index-** This page will primarily act as a central hub that can link users to the necessary parts of the website depending on their needs. It will contain enough info and graphics to give users a basic idea of the site and will link to more detailed pages with info about the site and managing slabs/profiles.
- **About-** A more in-depth explanation about the website, info on creating an account and how it could be used.
- **Register/Sign In-** This page will be used for new users creating accounts and existing users signing into their accounts. Each username must be unique so if the user tries to create username that is already taken it will return an error.
- **Profile-** Will display the user’s webpage with all saved stickers that are displayed on a “Display” page when clicked. If the user has edited the html, the changes will be applied here otherwise a default template will be rendered.
- **Display-** A webpage specifically used for displaying or loading the contents of the sticker clicked on by the user on the previous “Profile” page. 
- **Edit-** The edit tab/page displays a list of all the users currently saved icons allowing the user to delete and edit them, as well as another section where the user could add a new image, text or link to their wall. It will also be the place where the user would have access to their html file if they wished to customize it.
- **Browse-** A way to search/display Sticker Slab accounts so users can view and interact with others Sticker Slabs.
- **Random-** Loads a random Sticker Slab webpage in profile mode, so you can view and interact with it but not edit it.
- **Help-** Has troubleshooting information as well as advice and links on how to edit stickers and html.


## Data Model

**Users-** A model built into the Django library that creates a User object.
- Username: Must be unique, used in url to load indivdual Sticker Slabs.
- Email: (Optional), used for changing passwords and claiming accounts.
- Password: Password used to sign into Sticker Slab account.
**Stickers-** An clickable icon saved by the user that loads an image, text or a link in display.html.
- Text: Field to strore text string if it is a text sticker (blank otherwise).
- Image: Stores the location of a image to be rendered if image sticker (blank otherwise).
- Link: Stores the url of a website and links to it when sticker clicked (blank otherwise).
- User: Forign key used to specify which user created the sticker. 


## Schedule

- **October 22, 2018:** Have a Django project set up that allows a user to create and account and navigate through the necessary pages.
- **October 29, 2018:** Allow the user to post pictures, text and links to their wall and then display them when clicked on.
- **November 6, 2018:** Give the user access to parts of the html so they customize their wall and the changes will be applied whenever it is rendered.
- **November 13, 2018:** Add content and style to the home, about, help pages. 
- **After End Of Class:** Add tools to make editing html and slab easier, polish website as a whole and a python compiler so people could add a sticker that could run a single python file.
