// NavBar.jsx
import React from "react";
import { Link, Outlet } from "react-router-dom";


const NavBar = () => {
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-light bg-light py-3 shadow-sm">
        <div className="container">
          <a className="navbar-brand fw-bold fs-4" href="#">
          TIMELESS TRENDS
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mx-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <Link className="nav-link " aria-current="page" to="/">
                  Home
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/Products">
                  Products
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/About">
                  About
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/Contact">
                  Contact
                </Link>
              </li>
            </ul>
            <div className="buttons">
              <Link to="/Login" className="btn btn-outline-dark">
                <i className="fa fa-sign-in me-1"></i> Login
              </Link>
              <Link to="/SignUp" className="btn btn-outline-dark ms-2">
                <i className="fa fa-user-plus me-1"></i> Sign Up
              </Link>
              <Link to="/Cart" className="btn btn-outline-dark ms-2">
                <i className="fa fa-shopping-cart me-1"></i> Cart (0)
              </Link>
              <Link to="/Admin" className="btn btn-outline-dark ms-2">
                <i className="fa fa-shopping-cart me-1"></i> Admin
              </Link>

            </div>
          </div>
        </div>
      </nav>
    </>
  );
};

export default NavBar;
{
  /* <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/Login">Login</Link>
        </li>
        <li>
          <Link to="/SignUp">Sign Up</Link>
        </li>
      </ul>
    </nav>
    <Outlet /> */
}
