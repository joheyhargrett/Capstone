import React from "react";
import { useUser } from "./UserContext";
import { Link } from "react-router-dom";

const LogoutButton = () => {
  const { handleLogout } = useUser();

  const handleLogoutClick = async (e) => {
    e.preventDefault();
    handleLogout();
  };

  return (
    <Link to="/Login" onClick={handleLogoutClick} className="btn btn-outline-dark">
      <i className="fa fa-sign-in me-1"></i> Logout
    </Link>
  );
};

export default LogoutButton;
