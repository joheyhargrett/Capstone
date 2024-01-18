import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';

const SignUp = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    first_name: '',
    last_name: '',
    address: '',
    phone_number: '',
  });

  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSignUp = async () => {
    try {
      const response = await fetch('http://localhost:5555/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Signup successful:', data);
        alert('Signup successful');
        navigate('/Login');
      } else {
        const errorData = await response.json();
        console.error('Signup failed:', errorData);
        alert('Signup failed');
      }
    } catch (error) {
      console.error('Error during signup:', error);
    }
  };

  return (
    <div className="container my-5 border p-4">
      <h1 className="text-center">Sign Up</h1>
      <form onSubmit={handleSignUp}>
        <div className="mb-3">
          <label className="form-label">First Name:</label>
          <input
            type="text"
            className="form-control"
            name="first_name"
            value={formData.first_name}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Last Name:</label>
          <input
            type="text"
            className="form-control"
            name="last_name"
            value={formData.last_name}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Email:</label>
          <input
            type="text"
            className="form-control"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Address:</label>
          <input
            type="text"
            className="form-control"
            name="address"
            value={formData.address}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Phone Number:</label>
          <input
            type="text"
            className="form-control"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Create A Password:</label>
          <input
            type="password"
            className="form-control"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="text-center mb-3">
          <button type="submit" className="btn btn-primary">
            Sign Up
          </button>
        </div>
      </form>

      <div className="text-center mt-3">
        <p>
          Already have an account? <Link to="/Login">Login</Link>
        </p>
      </div>

      <div className="text-center mt-3">
        <p>Sign up with social media:</p>
        <a href="https://facebook.com/timelesstrends" className="btn btn-outline-primary me-2">
          <i className="fab fa-facebook-f"></i> Facebook
        </a>
        <a href="https://instagram.com" className="btn btn-outline-primary me-2">
          <i className="fab fa-instagram"></i> Instagram
        </a>
        <a href="https://twitter.com" className="btn btn-outline-primary">
          <i className="fab fa-twitter"></i> Twitter
        </a>
      </div>
    </div>
  );
};

export default SignUp;
