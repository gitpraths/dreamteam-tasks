import react, { useContext, useState } from "react";
import { AuthContext } from "../context/auth";
import { useRouter } from "next/router";
import Layout from "../components/Layout";

export default function LoginPage() {
  const { login } = useContext(AuthContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      await login(username, password);
      router.push("/");
    } catch (error) {
      console.error("Login failed:", error.message);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Layout>
        <div className="bg-gray-100 min-h-screen flex items-center justify-center">
          <div className="w-full max-w-sm bg-white rounded-lg shadow-md p-6">
            <h1 className="text-xl font-semibold text-gray-800 text-center mb-4">
              Login
            </h1>

            {error && <p className="text-red-500 text-center mb-4">{error}</p>}

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label
                  htmlFor="username"
                  className="block text-sm font-medium "
                >
                  Username
                </label>
                <input
                  type="text"
                  id="username"
                  placeholder="Username"
                  value={username}
                  onChange={(e) => {
                    setError("");
                    setUsername(e.target.value);
                  }}
                  required
                  className="w-full px-3 py-2 border rounded-md bg-gray-50 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label
                  htmlFor="password"
                  className="block text-sm font-medium text-gray-700"
                >
                  Password
                </label>
                <input
                  type="password"
                  id="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => {
                    setError("");
                    setPassword(e.target.value);
                  }}
                  required
                  className="w-full px-3 py-2 border rounded-md bg-gray-50 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <button
                type="submit"
                disabled={loading}
                className={`w-full bg-blue-500 text-white font-semibold py-2 px-4 rounded-md ${
                  loading
                    ? "cursor-not-allowed bg-blue-300"
                    : "hover:bg-blue-600 transition"
                }`}
              >
                {loading ? "Logging in..." : "Login"}
              </button>
            </form>
          </div>
        </div>
      </Layout>
    </div>
  );
}
