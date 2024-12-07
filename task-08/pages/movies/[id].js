import { useRouter } from "next/router";
import { useEffect, useState, useContext } from "react";
import { AuthContext } from "../../context/auth";
import api from "../../utils/api";

import Layout from "../../components/Layout";
import { CancelToken } from "axios";

export default function MovieDetails() {
  const router = useRouter();
  const { id } = router.query;
  const { user } = useContext(AuthContext);
  const [movie, setMovie] = useState(null);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    if (id) {
      api
        .get(`/movies/${id}`)
        .then((response) => setMovie(response.data))
        .catch(() => setError("Failed to load movie details"));
    }
  }, [id]);

  useEffect(() => {
    if (id) {
      api
        .get(`/movies/${id}/comments`)
        .then((response) => setComments(response.data))
        .catch((err) => console.error("Failed to load comments:", err));
    }
  }, [id]);

  if (error) return <p className="text-center text-red-500">{error}</p>;
  if (!movie) return <p className="text-center text-gray-500">Loading...</p>;

  const handleAddComment = async (e) => {
    e.preventDefault(); // Prevent the default form submission

    // Check if the `newComment` field is empty
    if (!newComment.trim()) {
      setError("Comment cannot be empty.");
      return;
    }

    try {
      const token = localStorage.getItem("access_token"); // JWT Token

      // POST request to add a new comment
      await api.post(
        `/movies/${id}/comments`, // Replace `id` with the movie's ID
        { content: newComment }, // Ensure `content` is included here
        {
          headers: {
            "Content-Type": "application/json", // Explicitly set the content type
            Authorization: `Bearer ${token}`, // Pass the JWT token for authentication
          },
        }
      );

      const response = await api.get(`/movies/${id}/comments`);
      console.log("comment resposne", response);
      setComments(response.data); // Update the comments in state
      setNewComment(""); // Clear the input field
    } catch (err) {}
  };

  return (
    <div>
      <Layout>
        <div className="min-h-screen bg-gray-50 py-8 px-4">
          <div className="container mx-auto max-w-4xl bg-white shadow-md rounded-lg overflow-hidden">
            <div className="flex flex-col items-center text-center">
              <img
                src={movie.poster || "/placeholder.jpg"}
                alt={movie.title}
                className="w-full sm:w-2/3 lg:w-1/2 object-cover rounded-lg shadow-md"
              />
              <h1 className="text-3xl font-bold text-gray-800 mt-6">
                {movie.title}
              </h1>
              <p className="text-gray-500 italic mt-2">
                {movie.release_date || "Unknown Release Date"}
              </p>
              <p className="text-gray-700 mt-4 px-4">{movie.overview}</p>
            </div>

            <div className="mt-8 px-6">
              <h2 className="text-xl font-bold text-gray-800 border-b pb-2 mb-4">
                Comments
              </h2>
              <ul className="space-y-4">
                {comments.length > 0 ? (
                  comments.map((comment, index) => (
                    <li
                      key={index}
                      className="bg-gray-100 p-3 rounded-lg shadow-md text-gray-700"
                    >
                      <strong>{comment.username || "Unknown"}:</strong>{" "}
                      {comment.content}
                    </li>
                  ))
                ) : (
                  <p className="text-gray-500">
                    No comments yet. Be the first to comment!
                  </p>
                )}
              </ul>

              {user ? (
                <div className="mt-6">
                  <textarea
                    className="w-full bg-gray-100 border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800"
                    rows="3"
                    placeholder="Add a comment..."
                    value={newComment}
                    onChange={(e) => setNewComment(e.target.value)}
                  ></textarea>
                  <button
                    onClick={handleAddComment}
                    className="bg-blue-500 text-white px-4 py-2 mt-4 rounded-lg shadow hover:bg-blue-600"
                  >
                    Post Comment
                  </button>
                </div>
              ) : (
                <p className="text-gray-500 mt-6">
                  <button
                    onClick={() => router.push("/login")}
                    className="text-blue-500 hover:underline"
                  >
                    Log in
                  </button>{" "}
                  to add a comment.
                </p>
              )}
            </div>
          </div>
        </div>
      </Layout>
    </div>
  );
}
