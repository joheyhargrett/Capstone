import React, { useState, useEffect } from "react";

const SessionChecker = ({ onSessionCheck }) => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkSession = async () => {
      try {
        const response = await fetch("http://localhost:5555/check_session");

        if (response.ok) {
          const data = await response.json();
          onSessionCheck(data);
        } else {
          console.error("Session check failed:", response.statusText);
        }
      } catch (error) {
        console.error("Error during session check:", error);
      } finally {
        setLoading(false);
      }
    };

    checkSession();
  }, [onSessionCheck]);

  if (loading) {
    return <p>Loading...</p>;
  }

  return <div>
    
  </div>;
};

export default SessionChecker;
