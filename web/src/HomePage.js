import React from "react";

// import { NavLink } from "react-router-dom";

export default function HomePage() {
  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      <p>This is the content of the home page.</p>
      <nav>
        <ul>
          <li>
            <a href="/other-page">Go to Other Page</a>
          </li>
        </ul>
      </nav>
    </div>
  );
}