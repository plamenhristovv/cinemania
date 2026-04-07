# Cinemania

Cinemania is a comprehensive movie tracking application designed for cinephiles who want to organize their cinematic journey.

## Project Motivation

This project was born out of a passion for cinema. For people who love watching movies, keeping track of what they've seen and whose work they've followed can be a challenge. Cinemania helps users:
- **Track Movies:** Keep a personal record of every movie watched.
- **Follow Directors:** Maintain a database of directors and explore their filmography.
- **Create Personalized Lists:** Organize movies into custom lists (e.g., "Must Watch," "All-time Favorites," "Genre Classics") to keep their collection structured.

## Installation Instructions

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/your-username/cinemania.git
cd cinemania
```

### 2. Create and Activate a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies.

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Database Setup
The project uses **PostgreSQL**. Ensure you have a database named `cinemania_db` created on your local PostgreSQL server. You can update the database credentials in `cinemania/settings.py` if they differ from the defaults.

Run the migrations to set up the database schema:
```bash
python manage.py migrate
```

### 5. Run the Project
Start the Django development server:
```bash
python manage.py runserver
```
You can now access the application at `http://127.0.0.1:8000/`.

## Project Walkthrough


### Home Page
![Home Page](screenshots/home.png)
* The home page welcomes you to Cinemania and provides an overview of the application's features. You can navigate to different sections using the navigation bar at the top.
* If you are not logged in, you can click on **Login** to access your account or **Sign up** to create a new account.

### Signing up
Using the sign-up form, you can create a new account to start your journey.
![Sign Up](screenshots/sign_up.png)

### Logging in
If you already have an account, you can log in using the login form.
![Login](screenshots/login.png)

### Movie Management  

#### Viewing Movies
* Click on **Movies** in the navigation to view the movies added to the database. There you can manage the movies and explore their details.  
* Click on **Add Movie** to add a new movie to the database. Only users that have logged in and have the appropriate permissions can add movies to the database.
* Type in the search bar to filter movies by title. Click on **Search** to apply the filter.
* Click on the **movie poster** to view details about the movie. 
![Movies List](screenshots/movies_list.png)

#### Movie Details 
Here you can view the movie details.  
Only users that have **logged in** and have the appropriate **permissions** can edit or delete movies from the database.
* Click on **Edit Movie** to edit the movie details.  
* Click on **Delete** to delete the movie.  
* Click on **add to watched** to add the movie to your watched movies.
* If the movie has studios associated with it, click on the studio name to view details about the studio.
* Click on **Directed by** to view the director's details.
* Click on **Back to Movies** to return to the movies.

![Movie Details](screenshots/movie_details.png)


#### Movie Editing 
Click on **Save Changes** to save the changes you made to the movie details.  
Click on **Cancel** to discard the changes you made to the movie details.

![Edit Movie](screenshots/edit_movie.png)


#### Movie Deletion
* Click on **Yes, delete movie** to confirm the deletion.  
* Click on **No, keep movie** to cancel the deletion.

![Delete Movie](screenshots/delete_movie.png)


### Movie Addition
* Fill in the movie details and click on **Save Movie** to add the movie to your collection.  
* Click on **Cancel** to discard the movie details and return to the movies list.
![Add Movie](screenshots/add_movie.png)

### Director Tracking
Keep track of all the directors whose work you have seen.
* Click on **Directors** in the navigation to view the directors you have added.
* Only users that are logged in and have the appropriate permissions can add and edit directors.
* Click on **Add Director** to add a new director to your collection.
* Type in the search bar to filter directors by name. Click on **Search** to apply the filter.
* Click on the director's picture to view details about the director.
![Directors](screenshots/directors_list.png)

#### Director Details
Here you can view the director's details and their filmography that have been added to the database.
Only users that have **logged in** and have the appropriate **permissions** can edit or delete directors from the database.
* Click on **Edit** to edit the director details.  
* Click on **Delete** to delete the director.  
* Click on **Back to Directors** to return to the directors list.
* Click on the **movie poster** to view details of the directors movies you have added.
![Director Details](screenshots/director_details.png)

#### Director Editing
* Click on **Save Changes** to save the changes you made to the director details.  
* Click on **Cancel** to discard the changes you made to the director details.
![Edit Director](screenshots/director_edit.png)


#### Director Deletion
Click on **Confirm** to confirm the deletion.  
Click on **Go back to director** to cancel the deletion.
![Delete Director](screenshots/director_delete.png)

### Personalized Lists
* Organize your favorites into custom lists.
* Click on **Lists** in the navigation to view your custom lists.  
* Click on **Add List** to create a new custom list.  
* Type in the search bar to filter lists by name. Click on **Search** to apply the filter.
* Click on the list to view the movies in the list.
![Custom Lists](screenshots/lists.png)

#### List Details
Here you can view the movies in the list.  
* Click on **Edit List** to edit the list details and add movies.  
* Click on **Delete** to delete the list.  
* Click on **Back to All Lists** to return to the lists.
* Click on the **movie poster** to view details of the movies in the list.
![List Details](screenshots/list_details.png)

#### List Editing
Click on **Update List Info** to save the changes you made to the list details.  
Click on **Discard Changes** to discard the changes you made to the list details.
![Edit List](screenshots/list_edit.png)


#### List Deletion
Click on **Yes, delete list** to confirm the deletion.  
Click on **No, keep list** to cancel the deletion.
![Delete List](screenshots/list_delete.png)

### Studios
* Click on **Studios** in the navigation to view the studios added to the database.
* Only users that have logged in and have the appropriate permissions can add and edit studios.
* Clcik on **API documentation** to add studios to the database using the API endpoint.
* Click on the particular studio to view details about the studio and the movies associated with it.
![Studios View](screenshots/studios_list.png)

#### Studio Details
Here you can view the studio details and the movies associated with it.
![Studio Details](screenshots/studio_detail.png)