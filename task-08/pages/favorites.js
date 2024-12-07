import React, { useState, useEffect } from "react";
import api from "../utils/api";
import Layout from "../components/Layout";

export default function FavoriteMovies() {
  const [favorites, setFavorites] = useState([]);
  const [search, setSearch] = useState("");
  const [sortBy, setSortBy] = useState("title");
  const [sortOrder, setSortOrder] = useState("asc");
  const [loading, setLoading] = useState(false);
  const [user, setUser] = useState([]);

  const profile = async () => {
    const token = localStorage.getItem("access_token");

    try {
      const response = await api.get("/profile", {
        headers: { Authorization: `Bearer ${token}` },
      });
      console.log("respone", JSON.stringify(response.data.profile));
      setUser(response.data.profile);
    } catch (error) {
      console.error("Error fetching favorites:", error);
    } finally {
    }
  };

  const fetchFavorites = async () => {
    setLoading(true);
    const token = localStorage.getItem("access_token");

    try {
      const response = await api.get(
        `/favorites?search=${search}&sort_by=${sortBy}&order=${sortOrder}`,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      setFavorites(response.data);
    } catch (error) {
      console.error("Error fetching favorites:", error);
    } finally {
      setLoading(false);
    }
  };

  const removeFavorite = async (movieId) => {
    try {
      const token = localStorage.getItem("access_token");

      const response = await api.delete(`/favorites/${movieId}`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      const result = response.data;

      alert(result.message);

      fetchFavorites();
    } catch (error) {
      console.error("Error removing favorite:", error);
    }
  };

  useEffect(() => {
    fetchFavorites();
  }, [search, sortBy, sortOrder]);

  useEffect(() => {
    profile();
  }, []);

  return (
    <div>
      <Layout>
        <div className="container text-gray-800 mt-4">
          <h1>{user.username}'s Profile</h1>
          <p>Email: {user.email}</p>
          <h1>Your Favorite Movies</h1>{" "}
          <div className="mb-3 d-flex py-4">
            <select
              className="form-select"
              value={sortOrder}
              onChange={(e) => setSortOrder(e.target.value)}
            >
              <option value="asc">Ascending</option>
              <option value="desc">Descending</option>
            </select>
          </div>
          {loading ? (
            <p>Loading...</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {favorites.map((favorite) => (
                <div key={favorite.id} className="card">
                  <img
                    src={favorite.poster || "/placeholder.jpg"}
                    alt={favorite.title}
                    className="w-full h-48 object-cover rounded-lg mb-2"
                  />
                  <div className="card-body">
                    <h5 className="card-title">{favorite.title}</h5>
                    <p className="card-text">{favorite.overview}</p>
                    <p className="text-sm">{`Release Date: ${favorite.release_date}`}</p>
                    <button
                      onClick={() => removeFavorite(favorite.id)}
                      className="btn btn-danger w-full mt-2"
                    >
                      Remove
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </Layout>
    </div>
  );
}