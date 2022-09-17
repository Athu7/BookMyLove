**Don’t judge a book by its cover but look at the back and read the synopsis to judge it.**
This database is mainly focused on the task of *predicting the genre of the book*  based  on the *synopsis* of the book.
All the top websites for book readers such as amazon, goodreads rely mainly on the user votes to classify a book to a particular genre. 
But can we automate this process with a good accuracy!! That would be fun.
So with this in mind the data scraped from the goodreads website using selenium which contains the synopsis, genre and other features of books from different genres.
For those not interested in NLP you can try and create a model which can predict the rating of the book based on other attributes in the dataset such as the followers of the author, number of reviews on the book  which are present in the dataset.
So what are you waiting for just go for it.
Columns description
title -> This represents the title of the book 
rating -> This represents the rating of the book (maximum rating is 5)
name -> This is the name of the author
num_ratings -> The number of users who have rated the book 
num_reviews -> The number of users who have reviewed the book
num_followers -> The number of followers of the author 
synopsis -> synopsis/ summary/description of the book 
genre -> The genre the book belongs to.