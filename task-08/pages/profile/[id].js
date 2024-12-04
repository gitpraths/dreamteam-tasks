import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import api from "../../utils/api";

export default function ProfilePage() {
  const router = useRouter();
  const { id } = router.query;
  const [user, setUser] = useState(null);
  const [bio, setBio] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    if (id) {
      api.get(`/users/${id}`).then((response) => setUser(response.data));
    }
  }, [id]);

  const handleUpdateBio = async () => {
    try {
      await api.put(`/users/profile`, { bio });
      setMessage("Bio updated successfully!");
    } catch (err) {
      setMessage("Error updating bio.");
    }
  };

  if (!user) return <p>Loading...</p>;

  return (
    <div>
      <h1>{user.username}'s Profile</h1>
      <p>Email: {user.email}</p>
      <p>Bio: {user.bio}</p>

      <textarea
        placeholder="Update your bio"
        value={bio}
        onChange={(e) => setBio(e.target.value)}
      />
      <button onClick={handleUpdateBio}>Update Bio</button>
      {message && <p>{message}</p>}
    </div>
  );
}
