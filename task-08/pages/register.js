import { useState } from "react";
import { useRouter } from "next/router";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css"; // Make sure to include this CSS file for Toastify
import api from "../utils/api";
import Layout from "../components/Layout";

export default function RegisterPage() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/register", { username, email, password });
      toast.success("Registration successful!");
      router.push("/login");
    } catch (err) {
      const errorMessage =
        err.response?.data?.message || "Failed to register. Please try again.";
      setError(errorMessage);
      toast.error(errorMessage);
    }
  };

  return (
    <div>
      <Layout>
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
          <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 w-full max-w-md">
            <h1 className="text-2xl font-bold mb-6 text-gray-800 text-center">
              Register
            </h1>
            {error && <p className="text-red-500 text-center mb-4">{error}</p>}
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <input
                  type="text"
                  placeholder="Username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="w-full px-3 py-2 border rounded shadow-sm text-gray-700 focus:ring focus:ring-blue-300"
                  required
                />
              </div>
              <div>
                <input
                  type="email"
                  placeholder="Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full px-3 py-2 border rounded shadow-sm text-gray-700 focus:ring focus:ring-blue-300"
                  required
                />
              </div>
              <div>
                <input
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full px-3 py-2 border rounded shadow-sm text-gray-700 focus:ring focus:ring-blue-300"
                  required
                />
              </div>
              <button
                type="submit"
                className="w-full px-4 py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-600 transition"
              >
                Register
              </button>
            </form>
            <ToastContainer />
          </div>
        </div>
      </Layout>
    </div>
  );
}
