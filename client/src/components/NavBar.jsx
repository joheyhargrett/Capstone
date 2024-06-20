import React from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
import { useUser } from './UserContext';
import LogoutButton from "./LogOut"; // Ensure this is the correct import path

const NavBar = () => {
  const { user } = useUser();
  const state = useSelector((state) => state.handleCart);

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light py-3 shadow-sm sticky-top">
      <div className="container">
        <Link className="navbar-brand fw-bold fs-4" to="/">
          TIMELESS TRENDS
        </Link>
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
              <Link className="nav-link" aria-current="page" to="/">
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
            {user ? (
              <>
                <span className="navbar-text me-2">
                  Welcome, {user.first_name}!
                </span>
                <Link to="/CustomerDetails" className="btn btn-outline-dark edit-info-btn me-2">
                  Edit Profile
                </Link>
                <LogoutButton />
              </>
            ) : (
              <>
                <Link to="/Login" className="btn btn-outline-dark">
                  <i className="fa fa-sign-in me-1"></i> Login
                </Link>
                <Link to="/SignUp" className="btn btn-outline-dark ms-2">
                  <i className="fa fa-user-plus me-1"></i> Sign Up
                </Link>
              </>
            )}
            <Link to="/Cart" className="btn btn-outline-dark ms-2">
              <i className="fa fa-shopping-cart me-1"></i> Cart ({state.length})
            </Link>
            <Link to="/Admin" className="btn btn-outline-dark ms-2">
              <i className="fa fa-shopping-cart me-1"></i> Admin
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
