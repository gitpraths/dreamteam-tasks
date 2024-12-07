import React from "react";
import MovieCard from "./MovieCard";
import { useRouter } from "next/router";
import api from "../utils/api";

export default function MovieGrid({ movies }) {
  const router = useRouter();

  const handleViewDetails = (movie) => {
    router.push(`/movies/${movie.id}`);
  };
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {movies && movies.length > 0 ? (
          movies.map((movie) => (
            <MovieCard
              key={movie.id}
              title={movie.title}
              posterUrl={movie.poster}
              synopsis={movie.overview}
              onAddToFavorites={() => handleAddToFavorites(movie)}
              onViewDetails={() => handleViewDetails(movie)}
            />
          ))
        ) : (
          <p className="text-center text-gray-400 col-span-full">
            No movies to display.
          </p>
        )}
      </div>
    </div>
  );

  function handleAddToFavorites(movie) {
    const token = localStorage.getItem("access_token");

    if (!token) {
      alert("Please log in to add to favorites.");
      return;
    }

    api
      .post(
        "/favorites",
        { movie_id: movie.id },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      )
      .then((response) => {
        alert(response.data.message);
      })
      .catch((err) => {
        console.error(err.response.data || err.message);
        alert("Failed to add to favorites.");
      });
  }
}
