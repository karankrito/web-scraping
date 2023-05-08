# web-scraping
Web scraping is the process of extracting data from websites. In this case, we want to extract information from the IMDb website about movies, such as their names, ratings, votes, and grosses.

Here are the steps involved in scraping the IMDb website:

1. Send a request to the IMDb website: To start, we need to send a request to the IMDb website to get its HTML content. This is done using a Python library called "requests".

2. Parse the HTML content: The HTML content we receive in response to our request needs to be parsed so that we can extract the relevant data. This is done using a Python library called "BeautifulSoup". BeautifulSoup takes the raw HTML content and turns it into a navigable tree-like structure that we can traverse and extract data from.

3. Find the relevant HTML tags: Once we have the parsed HTML content, we need to find the specific HTML tags that contain the information we want to extract. This is done using CSS selectors, which are a way of selecting HTML elements based on their attributes.

4. Extract the data: Once we have identified the HTML tags that contain the data we want to extract, we can use BeautifulSoup to extract that data. We can extract data such as movie names, ratings, votes, and grosses.

5. connecting to mysql server:creates a new table called "imdb" in the "krito" database using the pymysql library for MySQL connectivity in Python. Then, it loops through a Pandas DataFrame "df" and inserts each row of data from the DataFrame into the "imdb" table using an INSERT statement. The data inserted includes the movie name, year, rating, votes, and gross. Finally, the changes made to the database are committed and the connection to the database is closed.

6. Store the data: Finally, we can store the extracted data in a format of our choice, such as a CSV file or a database.
