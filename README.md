we combine all tags into a big string and extract top 5000 most common words
then we make a table with 5000 columns, each column is a word, and each row is a movie
                          
                          w1 w2 w3 w4 w5 ... w5000
                    m1    1  0  1  0  1 ...  0
                    m2    0  0  1  0  1 ...  0
                    m3    0  0  0  0  1 ...  0
                    m4    1  0  0  0  0 ...  0
                
it means w1 is present 1 time in movie m1, 0 times in movie m2, 0 times in movie m3, 1 time in movie m4's tags
each movie is converted into a fixed size vector now 5000 movies and 5000 words so 5000*5000 matrix will be there
if we plot this matrix we will get a 5000 dimensional space, in which we can plot all our movies
and if I like m1 suppose and I want to get all the movies similar to m1 then I will calculate the distance between m1 and all other movies in this 5000 dimensional space and return closest 5 or 10 movies as closest movies to m1 vector

Now that we have every movie in vector form we will find cosine similarity of each movie other movie , it is basically inverse of cosine distance , instead of using euclidean distance
to find distance between movie vector we use cosine distance in 5000 by 5000 dim space as its more reliable , similarity is inversely proportional to distance so less the 
distance between movies more similar they are ,  so for a movie we recommend 5 movies which have most cosine similarity wrt to a movie , cosine similarity of a movie with 
itself is 0 .   

          
                          m1    m2   m3   m4  m5  ... m5000
                    m1    1.0  0.4  0.5  0.4  0.1 ...  0
                    m2    0.4  1.0  0.5  0.4  0.1 ...  0
                    m3    0.4  0.4  1.0  0.4  0.1 ...  0
                    m4    0.3  0.4  0.5  1.0  0.1 ...  0