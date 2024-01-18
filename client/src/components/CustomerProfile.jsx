import React, { useState, useEffect } from 'react';
import { useUser } from './UserContext'; 
import './CustomerProfile.css';

const CustomerDetails = () => {
  const { user } = useUser();
  const [customerData, setCustomerData] = useState(null);
  const [editData, setEditData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    if (user) {
      fetchCustomerData();
    }
  }, [user]);

  const fetchCustomerData = async () => {
    try {
      const response = await fetch(`http://localhost:5555/customers/${user.id}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setCustomerData(data);
      setEditData({...data}); // Copy data for editing
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  const handleEditChange = (e) => {
    setEditData({ ...editData, [e.target.name]: e.target.value });
  };

  const handleEditSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`http://localhost:5555/customers/${user.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(editData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      setIsEditing(false);
      fetchCustomerData(); 
    } catch (e) {
      setError(e.message);
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Customer Details</h2>
      {isEditing ? (
        <form onSubmit={handleEditSubmit}>
          <input name="email" value={editData.email || ''} onChange={handleEditChange} />
          <input name="first_name" value={editData.first_name || ''} onChange={handleEditChange} />
          <input name="last_name" value={editData.last_name || ''} onChange={handleEditChange} />
          <input name="address" value={editData.address || ''} onChange={handleEditChange} />
          <input name="phone_number" value={editData.phone_number || ''} onChange={handleEditChange} />
          
          <button type="submit">Save Changes</button>
          <button type="button" onClick={() => setIsEditing(false)}>Cancel</button>
        </form>
      ) : (
        customerData && (
          <div>
            <p>Email: {customerData.email}</p>
            <p>Name: {customerData.first_name} {customerData.last_name}</p>
            <p>Address: {customerData.address}</p>
            <p>Phone: {customerData.phone_number}</p>
            <button onClick={() => setIsEditing(true)}>Edit Customer Info</button>
            <h3>Ordered Items</h3>
            <ul>
              {customerData.ordered_items.map(item => (
                <li key={item.id}>
                  Product ID: {item.product_id}, Quantity: {item.quantity}, Order Date: {new Date(item.order_date).toLocaleDateString()}
                </li>
              ))}
            </ul>
          </div>
        )
      )}
    </div>
  );
};

export default CustomerDetails;
