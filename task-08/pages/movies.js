import React, { useState, useEffect } from "react";
import MovieGrid from "../components/MovieGrid";
import api from "../utils/api";

const Movies = () => {
  const [movies, setMovies] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchMovies = async () => {
    const response = await api.get("/movies", {
      params: {
        page: currentPage,
        limit: 3,
      },
    });

    console.log("API Response Data:", response.data);
    const data = response.data;
    setMovies(data.movies);
    setTotalPages(data.totalPages);
  };

  useEffect(() => {
    fetchMovies();
  }, [currentPage]);

  const handleNextPage = () => {
    setCurrentPage(currentPage + 1);
  };

  const handlePreviousPage = () => {
    setCurrentPage(currentPage - 1);
  };

  return (
    <div className="max-w-12xl mx-auto mt-8">
      <div className="flex justify-between items-center mb-4">
        <button
          onClick={handlePreviousPage}
          disabled={currentPage <= 1}
          className={`px-4 py-2 mb-4 bg-blue-600 text-white font-medium rounded ${
            currentPage <= 1
              ? "opacity-50 cursor-not-allowed"
              : "hover:bg-blue-700"
          }`}
        >
          Previous
        </button>

        <button
          onClick={handleNextPage}
          disabled={currentPage >= totalPages}
          className={`px-4 py-2 mb-4 bg-blue-600 text-white font-medium rounded ${
            currentPage >= totalPages
              ? "opacity-50 cursor-not-allowed"
              : "hover:bg-blue-700"
          }`}
        >
          Next
        </button>
      </div>
      <MovieGrid movies={movies} />
    </div>
  );
};

export default Movies;