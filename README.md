# MOVIEOPOLIS PROJECT
A project I worked on that utilizes the  [TMDB API](https://www.themoviedb.org/documentation/api?language=en-US) to create a Netflix-like movie catalog of different movies and tv shows. 


Link to project: [https://movieopolis.web.app/home](https://movieopolis-714f2.web.app/home).

## Project Stack
- Frontend: HTML, CSS, JavaScript, Vuejs
- Backend: Python (Django)

The backbone of the project was to build a similar platform to a streaming service (e.g. Netflix, Disney+, etc) that would show information about a movie/tv show. 

#### Backend:
The backend was written in Python using the Django framework. Python was chosen for its rather simplicity in writing and reading code as well as the rich and diverse support in terms of libraries. The purpose of the backend was to rely information and handle any data manipulation from the TMDB API to the frontend using API endpoints.

#### Frontend:
The selected choice to build the frontend was Vuejs due to my experience with it. The data stored on the frontend was handled using Pinia, a state management library. 


## Features
- Display Trending, Popular Movies/Shows, Upcoming Movies, Highly Rated Movies
- Display Movies (with infinite scroll)
- Display TV Shows (with infinite scroll)
- Discover option - discover new movies/tv based on filter settings!

## Take Away
#### UI/UX:
The UI/UX was done mostly using a CSS component library as to mostly not embarrass myself with my UI/UX design work. A possible future improvement would be to add more custom UI/UX components.

#### Optimization:
An improvement in the project optimization lies in the data handling. An example of this is using the infinite scroll. It's great in terms of UI/UX, but you load a bunch of data when it's not needed anymore. A solution for this would be to unload old/far results after a user reached a certain point. 

#### What I learned
- The importance of stepping back if you can't get something to work
- Working with lots of data and displaying it
- UI/UX design 
- Getting more comfortable using JavaScript (Asynchronous functions, API calls) and Python

#### Future Improvements
- Make searchbar more usable in terms if UI (displaying results) and functionality
- Make the discover better (add in keywords, multiple genres options)


