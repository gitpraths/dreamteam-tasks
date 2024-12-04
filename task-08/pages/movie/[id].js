import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import api from "../../utils/api";

export default function MovieDetails() {
  const router = useRouter();
  const { id } = router.query;
  const [movie, setMovie] = useState(null);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    if (id) {
      api.get(`/movies/${id}`).then((response) => setMovie(response.data));

      api
        .get(`/movies/${id}/comments`)
        .then((response) => setComments(response.data));
    }
  }, [id]);

  const handleCommentSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post(`/movies/${id}/comments`, { comment: newComment });
      const response = await api.get(`/movies/${id}/comments`); // Reload comments
      setComments(response.data);
      setNewComment("");
    } catch (err) {
      setError("Unable to post comment. Are you logged in?");
    }
  };

  if (!movie) return <p>Loading...</p>;

  return (
    <div>
      <h1>{movie.title}</h1>
      <p>{movie.description}</p>

      <h2>Comments</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {comments.map((comment) => (
          <li key={comment.id}>
            {comment.comment} - User #{comment.user_id}
          </li>
        ))}
      </ul>

      <form onSubmit={handleCommentSubmit}>
        <textarea
          placeholder="Add a comment"
          value={newComment}
          onChange={(e) => setNewComment(e.target.value)}
        />
        <button type="submit">Post Comment</button>
      </form>
    </div>
  );
}
