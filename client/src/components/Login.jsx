import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useUser } from './UserContext';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { setUser } = useUser();
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:5555/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        console.error('Server responded with status:', response.status);
        const text = await response.text(); 
        console.error('Response received:', text);
        alert('Login failed');
        return;
      }

      const data = await response.json();
      console.log('Login successful:', data);
      setUser(data); 
      navigate('/CustomerDetails');
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <h2 className="text-center mb-4">Login</h2>
          <div className="card">
            <div className="card-body">
              <form>
                <div className="mb-3">
                  <label htmlFor="emailInput" className="form-label">Email</label>
                  <input
                    type="email"
                    className="form-control py-2" // py-2 for taller input fields
                    id="emailInput"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter your email"
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="passwordInput" className="form-label">Password</label>
                  <input
                    type="password"
                    className="form-control py-2" // py-2 for taller input fields
                    id="passwordInput"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Enter your password"
                  />
                </div>
                <div className="d-grid gap-2 mb-3">
                  <button className="btn btn-primary" type="button" onClick={handleLogin}>Login</button>
                </div>
                <div className="text-center mb-3">
                  <a href="/forgot-password">Forgot Password?</a>
                </div>
                <div className="text-center">
                  <p>Or login with:</p>
                  <a href="https://facebook.com" className="btn btn-outline-primary me-2">
                    <i className="fab fa-facebook-f"></i> Facebook
                  </a>
                  <a href="https://instagram.com" className="btn btn-outline-primary me-2">
                    <i className="fab fa-instagram"></i> Instagram
                  </a>
                  <a href="https://twitter.com" className="btn btn-outline-primary">
                    <i className="fab fa-twitter"></i> Twitter
                  </a>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
