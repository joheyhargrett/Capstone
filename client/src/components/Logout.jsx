import React from "react";

const LogoutButton = ({ onLogout }) => {
  const handleLogout = async () => {
    try {
      const response = await fetch("http://localhost:5555/logout");

      if (response.ok) {
        onLogout();
      } else {
        console.error("Logout failed:", response.statusText);
      }
    } catch (error) {
      console.error("Error during logout:", error);
    }
  };

  return (
    <div>
      <button type="button" className="btn btn-primary"  onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default LogoutButton;
