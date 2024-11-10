print("\t MOVIE SUGGESTION")
genre=input("Tell me which type of movie you want to see (horror/sci-fi): ").lower()
duration=input("Tell me which type of movie you want to see (short/long): ").lower()
if genre=="horror" and duration=="short":
    movie="Guest"
elif genre=="horror" and duration=="long":
    movie="Don't Move"
elif genre=="sci-fi" and duration=="short":
    movie="The Err|Dust"
elif genre=="sci-fi" and duration=="long":
    movie="The Tommorow War"
else:
    movie="*Sorry don't have suggestion for this but you can watch Titanic*"
    
print("movie Name:",movie)
