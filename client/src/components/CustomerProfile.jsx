import React, { useState, useEffect } from 'react';
import { useUser } from './UserContext';
import { useNavigate } from 'react-router-dom';

const CustomerDetails = () => {
  // Initialize state variables
  const [customer, setCustomer] = useState({});
  const [editMode, setEditMode] = useState(false);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [address, setAddress] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  
  const { user } = useUser();
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate("/Login");
      return;
    }
    
    const fetchCustomerDetails = async () => {
      try {
        const response = await fetch(`http://localhost:5555/customers/${user.id}`);
        if (response.ok) {
          const data = await response.json();
          setCustomer(data);
          setFirstName(data.first_name || '');
          setLastName(data.last_name || '');
          setAddress(data.address || '');
          setPhoneNumber(data.phone_number || '');
        }
      } catch (error) {
        console.error('Error fetching customer details:', error);
      }
    };

    fetchCustomerDetails();
  }, [user, navigate]);

  const handleUpdate = () => {
    const updatedCustomer = {
      first_name: firstName,
      last_name: lastName,
      address,
      phone_number: phoneNumber,
    };

    fetch(`http://localhost:5555/customers/${user.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updatedCustomer),
    })
      .then((response) => {
        if (response.ok) {
          setEditMode(false);
        } else {
          console.error('Update failed:', response.status, response.statusText);
        }
      })
      .catch((error) => {
        console.error('Error during update:', error);
      });
  };

  const handleDeleteAccount = () => {
    fetch(`http://localhost:5555/customers/${user.id}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.ok) {
          navigate("/Login");
        } else {
          console.error('Deletion failed:', response.status, response.statusText);
        }
      })
      .catch((error) => {
        console.error('Error during deletion:', error);
      });
  };

  if (!user) {
    return null;
  }

  return (
    <div className="container my-5">
      <div className="text-center mb-4">
        <h1>Customer Details</h1>
        <p>Your account information:</p>
      </div>

      {editMode ? (
        <>
          <div className="mb-3">
            <label className="form-label">First Name:</label>
            <input
              type="text"
              className="form-control"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Last Name:</label>
            <input
              type="text"
              className="form-control"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Address:</label>
            <input
              type="text"
              className="form-control"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Phone Number:</label>
            <input
              type="text"
              className="form-control"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
            />
          </div>
          <div className="text-center mb-3">
            <button className="btn btn-primary" onClick={handleUpdate}>
              Save Changes
            </button>
          </div>
        </>
      ) : (
        <>
          <div className="mb-3">
            <label className="form-label">First Name:</label>
            <input type="text" className="form-control" value={firstName} readOnly />
          </div>
          <div className="mb-3">
            <label className="form-label">Last Name:</label>
            <input type="text" className="form-control" value={lastName} readOnly />
          </div>
          <div className="mb-3">
            <label className="form-label">Address:</label>
            <input type="text" className="form-control" value={address} readOnly />
          </div>
          <div className="mb-3">
            <label className="form-label">Phone Number:</label>
            <input type="text" className="form-control" value={phoneNumber} readOnly />
          </div>
          <div className="text-center mb-3">
            <button className="btn btn-primary" onClick={() => setEditMode(true)}>
              Edit Customer Details
            </button>
          </div>
        </>
      )}

      <div className="text-center">
        <button className="btn btn-danger" onClick={handleDeleteAccount}>
          Delete Account
        </button>
      </div>

      {/* Social Media Buttons */}
      <div className="text-center mt-4">
        <p>Follow us on social media:</p>
        <div className="d-flex justify-content-center mb-2">
          <a href="https://facebook.com/timelesstrends" className="btn btn-outline-primary me-2" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-facebook-f"></i> Facebook
          </a>
          <a href="https://instagram.com/timelesstrends" className="btn btn-outline-primary me-2" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-instagram"></i> Instagram
          </a>
          <a href="https://twitter.com/timelesstrends" className="btn btn-outline-primary" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-twitter"></i> Twitter
          </a>
        </div>
      </div>
    </div>
  );
};

export default CustomerDetails;
