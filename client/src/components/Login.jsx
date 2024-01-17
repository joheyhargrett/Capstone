import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          password: password,
        }),
      });

      if (!response.ok) {
        console.error('Server responded with status:', response.status);
        const text = await response.text(); // Handles non-JSON responses
        console.error('Response received:', text);
        alert('Login failed');
        return;
      }

      const data = await response.json();
      console.log('Login successful:', data);
      navigate('/');
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div>
      <label>Email:</label>
      <input 
        type="text" 
        value={email} 
        onChange={(e) => setEmail(e.target.value)} 
      />

      <label>Password:</label>
      <input 
        type="password" 
        value={password} 
        onChange={(e) => setPassword(e.target.value)} 
      />

      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
