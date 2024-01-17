import React, { useState, useEffect } from 'react';

const AdminPage = () => {
  const [customers, setCustomers] = useState([]);
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [formData, setFormData] = useState({});

  // Fetch customers from the API
  useEffect(() => {
    fetch('http://localhost:5555/customers')
      .then(response => response.json())
      .then(data => setCustomers(data));
  }, []);

  // Handle customer selection for editing
  const handleEdit = (customer) => {
    setSelectedCustomer(customer);
    setFormData(customer);
  };

  // Update customer details on the server
  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`http://localhost:5555/customers/${selectedCustomer.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    }).then(() => {
      setSelectedCustomer(null);
      // Refresh the customer list after updating
      fetch('http://localhost:5555/customers')
        .then(response => response.json())
        .then(data => setCustomers(data));
    });
  };

  // Handle form changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Delete customer
  const handleDelete = (id) => {
    fetch(`http://localhost:5555/customers/${id}`, { method: 'DELETE' })
      .then(() => {
        setCustomers(customers.filter(customer => customer.id !== id));
      });
  };

  return (
    <div>
      <h1>Admin Dashboard</h1>
      {selectedCustomer ? (
        <div>
          <h2>Edit Customer</h2>
          <form onSubmit={handleSubmit}>
            <input name="email" value={formData.email || ''} onChange={handleChange} />
            <input name="first_name" value={formData.first_name || ''} onChange={handleChange} />
            <input name="last_name" value={formData.last_name || ''} onChange={handleChange} />
            <input name="address" value={formData.address || ''} onChange={handleChange} />
            <input name="phone_number" value={formData.phone_number || ''} onChange={handleChange} />
            <button type="submit">Save Changes</button>
            <button onClick={() => setSelectedCustomer(null)}>Cancel</button>
          </form>
        </div>
      ) : (
        <div>
          <h2>Customers</h2>
          {customers.map(customer => (
            <div key={customer.id}>
              {customer.first_name} {customer.last_name} - {customer.email}
              <button onClick={() => handleEdit(customer)}>Edit</button>
              <button onClick={() => handleDelete(customer.id)}>Delete</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default AdminPage;
