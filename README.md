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