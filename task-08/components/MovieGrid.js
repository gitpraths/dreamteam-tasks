import React from "react";
import MovieCard from "./MovieCard";

export default function MovieGrid({ movies }) {
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
    alert(`"${movie.title}" has been added to your favorites!`);
  }

  function handleViewDetails(movie) {
    alert(`Viewing details for "${movie.title}":\n${movie.synopsis}`);
  }
}
