import React, { useState, useEffect } from "react";
import api from "../utils/api";

import Layout from "../components/Layout";
import Movies from "./movies";

const HomePage = () => {
  return (
    <div>
      <Layout>
        <Movies />
      </Layout>
    </div>
  );
};

export default HomePage;
