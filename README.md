# Artist Analizer

## How it works:
With this application you will be able to calculate the average amount of words in different albums, just input the artist's name and select the album you want to analyze and the app will do the rest for you.!

## How to install it:

* The app was programmed using python Python 3.8.5 

* If using conda you can run this to download it

`conda create -n mypython3env python=3`
* Then please clone the repository and cd into it

`git clone https://github.com/Valentinolucas/LucasFantini.git`

* Install the dependencies

`pip install -r requirements.txt`

* Run the application

`python application.py`

* Browse to your local host on port 5000 (http://localhost:5000/)

## Some considerations
* The API im using to get the lyrics is public with a limit of 100 requests per minute.

## Future Work
Some ideas to improve the application...

* Use Concurrent.futures to create a multi-thread pool and make the API calls in parallel.

* Create much more robust unit test cases to catch bugs and errors.

* Calculate the average for the discography of an artist, using N random tracks from the recordings and appling inferential statistics. We can say that the number of words in N random songs follows a normal distribution so that it is possible to calculate the average for the discography within a confidence interval.

* Implement a database to store the results from a given search so the app can search first in the database for the result and if the result is not there, go ahead and make the request to the API. This will make the app faster and release the public API's from unncesesary requests.

* Create some interactive data visualization using bokeh!

* Create an attractive front-end and user experience (this was not my main focus as you can see!) using Bootstrap and maybe Sass for easy css styling?

* Test the flask application using pytest.

* Implement more functionality (one that can be added with the existing code is render the lyrics from the songs)



