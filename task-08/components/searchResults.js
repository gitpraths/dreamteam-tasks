import React from "react";
import MovieGrid from "../components/MovieGrid";
const SearchResults = ({ results, searchTerm, resetSearch }) => {
  return (
    <div className="container mx-auto px-4 sm:px-6 md:px-8 py-8">
      <button
        onClick={resetSearch} // Reset to the default movie list
        className="mb-4 px-4 py-2 bg-gray-300 rounded-md hover:bg-gray-400 text-gray-800"
      >
        Back to Default Movies
      </button>

      <h2 className="text-xl font-bold text-gray-800 mb-4">
        Search Results for "{searchTerm}"
      </h2>

      {results.length > 0 ? (
        <MovieGrid movies={results} />
      ) : (
        <p className="text-gray-600">No results found for "{searchTerm}".</p>
      )}
    </div>
  );
};

export default SearchResults;
