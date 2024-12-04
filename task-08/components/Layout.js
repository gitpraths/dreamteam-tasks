import React, { useContext } from "react";
import useAuth from "../hooks/useAuth";
import { AuthContext } from "../context/auth";

export default function Layout({ children }) {
  const { logout, user } = useContext(AuthContext);

  return (
    <div className="bg-background text-white min-h-screen">
      {/* Header */}
      <header className="bg-black py-4 px-6 flex justify-between items-center">
        <h1 className="text-primary text-xl font-bold">MovieApp</h1>
        <nav>
          <a href="/" className="mx-4 text-white hover:text-primary">
            Home
          </a>
          {user ? (
            <>
              <a
                href="/favorites"
                className="mx-4 text-white hover:text-primary"
              >
                Favorites
              </a>

              <a href="/profile" className="mx-4 text-white hover:text-primary">
                Profile
              </a>
              <span className="mx-4 text-white">{user.username}</span>
              <button
                onClick={logout}
                className="mx-4 text-white hover:text-primary"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <a href="/login" className="mx-4 text-white hover:text-primary">
                Login
              </a>
              <a
                href="/register"
                className="mx-4 text-white hover:text-primary"
              >
                Register
              </a>
            </>
          )}
        </nav>
      </header>

      <main className="container mx-auto px- sm:px-6 md:px-8 py-8">
        {children}
      </main>

      <footer className="bg-black text-center py-4 text-sm text-gray-400">
        © 2024 MovieApp. All rights reserved.
      </footer>
    </div>
  );
}
