movie_titles = ["Shrek","Shrek 2","Shrek 3","Shrek 4"]
f = open("movies.txt","w")
for i in range(len(movie_titles)):
    f.write(movie_titles[i]+"\n")

f.close()