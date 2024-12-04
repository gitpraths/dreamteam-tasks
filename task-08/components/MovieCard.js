import React from "react";

export default function MovieCard({
  title,
  posterUrl,
  synopsis,
  onAddToFavorites,
  onViewDetails,
}) {
  return (
    <div className="bg-gray-800 text-white rounded-lg shadow-md overflow-hidden hover:scale-105 transform transition duration-300">
      {/* Movie Poster */}
      <img
        src={posterUrl}
        alt={`${title} Poster`}
        className="w-full h-60 object-cover"
      />

      {/* Movie Details */}
      <div className="p-4">
        <h2 className="text-lg font-bold text-primary truncate">{title}</h2>
        <p className="text-sm text-gray-400 mt-2 truncate">{synopsis}</p>

        {/* Action Buttons */}
        <div className="flex justify-between mt-4">
          <button
            className="bg-primary hover:bg-red-600 text-white py-2 px-4 rounded"
            onClick={onAddToFavorites}
          >
            Add to Favorites
          </button>
          <button
            className="bg-gray-700 hover:bg-gray-600 text-white py-2 px-4 rounded"
            onClick={onViewDetails}
          >
            View Details
          </button>
        </div>
      </div>
    </div>
  );
}
