import  { useEffect } from "react";
import { useUser } from "./UserContext";

const SessionChecker = () => {
  const { user, setUser} = useUser();

  useEffect(() => {
    const checkSession = async () => {
      try {
        const response = await fetch("http://localhost:5555/check_session" , {credentials: "include"});
        if (response.ok) {
          const data = await response.json();
          handleLogin(data);
        }
      } catch (error) {
        console.error("Error during session check:", error);
      }
    };

    checkSession();
  }, [handleLogin]);

  return null; 
};

export default SessionChecker;
