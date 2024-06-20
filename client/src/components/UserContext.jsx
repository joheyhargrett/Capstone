import React, { createContext, useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const UserContext = createContext(null);

export const useUser = () => useContext(UserContext);

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const checkSession = async () => {
      try {
        const response = await fetch("http://localhost:5555/check_session", {
          credentials: "include",
        });
        if (response.ok) {
          const data = await response.json();
          setUser(data);
        } else if (response.status === 401) {
          console.log('Unauthorized: User is not logged in');
        }
      } catch (error) {
        console.error("Error during session check:", error);
      } finally {
        setIsLoading(false);
      }
    };

    checkSession();
  }, []);

  const handleLogout = async () => {
    try {
      const response = await fetch("http://localhost:5555/logout", {
        method: 'DELETE',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      if (response.ok) {
        setUser(null);
        navigate("/Login");
      } else {
        console.error("Logout failed:", response.status);
      }
    } catch (error) {
      console.error("Error during logout:", error);
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <UserContext.Provider value={{ user, setUser, handleLogout }}>
      {children}
    </UserContext.Provider>
  );
};
