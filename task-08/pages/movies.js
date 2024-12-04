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
    <div>
      <MovieGrid movies={movies} />
      <div className="pagination-container">
        {currentPage > 1 && (
          <button onClick={handlePreviousPage}>Previous</button>
        )}
        {currentPage < totalPages && (
          <button onClick={handleNextPage}>Next</button>
        )}
      </div>
    </div>
  );
};

export default Movies;
