import React from "react";
import { useUser } from "./UserContext";

const LogoutButton = () => {
  const { handleLogout } = useUser();

  const handleLogoutClick = async () => {
    try {
      const response = await fetch("http://localhost:5555/logout", { method: 'POST' });
      if (response.ok) {
        handleLogout();
      }
    } catch (error) {
      console.error("Error during logout:", error);
    }
  };

  return <button onClick={handleLogoutClick}>Logout</button>;
};

export default LogoutButton;
