import React, { useContext } from "react";
import Link from "next/link"; //Fix applying the className and other props to the <Link> component
import { AuthContext } from "../context/auth";

export default function Layout({ children }) {
  const { logout, user } = useContext(AuthContext);

  return (
    <div className="bg-background text-white min-h-screen">
      {/* Header */}
      <header className="bg-black py-4 px-6 flex justify-between items-center">
        <h1 className="text-primary text-xl font-bold">MovieApp</h1>
        <nav>
          <Link href="/" className="mx-4 text-white hover:text-primary">
            Home
          </Link>

          {user ? (
            <>
              <Link
                href="/favorites"
                className="mx-4 text-white hover:text-primary"
              >
                Profile
              </Link>

              <span className="mx-4 text-white">Welcome {user}</span>

              <button
                onClick={logout}
                className="mx-4 text-white hover:text-primary"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link
                href="/login"
                className="mx-4 text-white hover:text-primary"
              >
                Login
              </Link>

              <Link
                href="/register"
                className="mx-4 text-white hover:text-primary"
              >
                Register
              </Link>
            </>
          )}
        </nav>
      </header>

      <main className="container mx-auto px-4 sm:px-6 md:px-8 py-8">
        {children}
      </main>

      <footer className="bg-black text-center py-4 text-sm text-gray-400">
        © 2024 MovieApp. All rights reserved.
      </footer>
    </div>
  );
}
