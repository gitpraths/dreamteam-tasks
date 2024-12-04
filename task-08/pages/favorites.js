import { useEffect, useState } from "react";
import api from "../utils/api";

export default function FavoritesPage() {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    api
      .get("/favorites")
      .then((response) => setFavorites(response.data))
      .catch((err) => console.error("Error fetching favorites:", err));
  }, []);

  return (
    <div>
      <h1>Your Favorites</h1>
      <ul>
        {favorites.map((movie) => (
          <li key={movie.movie_id}>
            <h2>{movie.title}</h2>
            <p>{movie.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
