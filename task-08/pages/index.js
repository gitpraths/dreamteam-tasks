import React, { useState, useEffect } from "react";
import api from "../utils/api";

import Layout from "../components/Layout";
import Movies from "./movies";
import SearchResults from "../components/searchResults";

const HomePage = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [isSearching, setIsSearching] = useState(false);

  const handleSearch = async () => {
    if (!searchTerm.trim()) return;

    setLoading(true);

    try {
      const response = await api.get("/movies/search", {
        params: { q: searchTerm, page: 1, per_page: 10 },
      });

      setSearchResults(response.data.movies);
      setIsSearching(true);
    } catch (err) {
      console.error("Search error:", err);
      setSearchResults([]);
    } finally {
      setLoading(false);
    }
  };

  const resetSearch = () => {
    setSearchTerm("");

    setIsSearching(false);
  };

  return (
    <div>
      <Layout>
        <div className="flex justify-center bg-gray-100 py-4">
          <input
            type="text"
            placeholder="Search for movies..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-1/3 px-3 py-2 border rounded-md bg-gray-50 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSearch}
            disabled={loading}
            className={`ml-4 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none transition ${
              loading ? "opacity-50 cursor-not-allowed" : ""
            }`}
          >
            {loading ? "Searching..." : "Search"}
          </button>
        </div>

        {isSearching ? (
          <SearchResults
            results={searchResults}
            searchTerm={searchTerm}
            resetSearch={resetSearch}
          />
        ) : (
          <Movies />
        )}
      </Layout>
    </div>
  );
};

export default HomePage;
