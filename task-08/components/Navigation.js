import React from "react";
import { useRouter } from "next/router";
import Login from "../pages/login";
import Register from "../pages/register";
import Movies from "../pages/movies";

const Navigation = () => {
  const router = useRouter();
  console.log("routes", router.pathname);
  switch (router.pathname) {
    case "/login":
      return <Login />;
    case "/register":
      return <Register />;
    default:
      return <Movies />;
  }
};

export default Navigation;
