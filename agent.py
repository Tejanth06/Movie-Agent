from omdb import search_movie
from gemini import ask_gemini


class MovieAgent:

    def __init__(self):
        print("🎬 Movie Agent is ready!")

    def chat(self, message):

        if "recommend" in message.lower():
            return ask_gemini(message)

        movie = search_movie(message)

        if movie.get("Response") == "True":

            return f"""
🎬 Title: {movie['Title']}

📅 Year: {movie['Year']}

⭐ IMDb Rating: {movie['imdbRating']}

🎭 Genre: {movie['Genre']}

🎬 Director: {movie['Director']}

📝 Plot:
{movie['Plot']}
"""

        else:
            return "❌ Sorry, I couldn't find that movie."