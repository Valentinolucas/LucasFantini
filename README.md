# LucasFantini

## How it works:
Whit this application you will be able to calculate the average amount of words in different albums, just input the artist name and select the album you want to analize and the app will do the rest for you.!

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

## Future Work
Some ideas to improve the application...

* Calculate the average for the discography of an artist  N random tracks from the recordings and appling inferential statistics. We can say that the number of words in N random songs follows a Normal distribution so its posible to calculate the average for the discography within a confidence interval.

* Implement a database to store the results from a given search so the app can search first in the database for the result and if the result is not there go ahead and made the request to the API. This will make the app faster and release the public API's from unncesesary requests.

* Create some interactive data visualization using bokeh!




