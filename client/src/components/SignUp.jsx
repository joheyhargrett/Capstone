import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
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
    <div>
      <form onSubmit={handleSignUp}>

      <label>First Name:</label>
      <input type="text" name="first_name" value={formData.first_name} onChange={handleInputChange} required/>

      <label>Last Name:</label>
      <input type="text" name="last_name" value={formData.last_name} onChange={handleInputChange}  required/>

      <label>Email:</label>
      <input type="text" name="email" value={formData.email} onChange={handleInputChange} required/>

      <label>Address:</label>
      <input type="text" name="address" value={formData.address} onChange={handleInputChange} required />

      <label>Phone Number:</label>
      <input type="text" name="phone_number" value={formData.phone_number} onChange={handleInputChange}  required/>

      <label>Create A Password:</label>
      <input type="password" name="password" value={formData.password} onChange={handleInputChange} required />

      
      <button onClick={handleSignUp}>Sign Up</button> 
      </form>
      <h1>Sign Up</h1>

     
    </div>
  );
};

export default SignUp;
