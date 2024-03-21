import React, { useState, useEffect } from 'react';

const AdminPage = () => {
  const [customers, setCustomers] = useState([]);
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [formData, setFormData] = useState({});

  useEffect(() => {
    fetch('http://localhost:5555/customers')
      .then(response => response.json())
      .then(data => setCustomers(data));
  }, []);

  const handleEdit = (customer) => {
    setSelectedCustomer(customer);
    setFormData(customer);
  };

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
      fetch('http://localhost:5555/customers')
        .then(response => response.json())
        .then(data => setCustomers(data));
    });
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleDelete = (id) => {
    fetch(`http://localhost:5555/customers/${id}`, { method: 'DELETE' })
      .then(() => {
        setCustomers(customers.filter(customer => customer.id !== id));
      });
  };

  return (
    <div className="container my-5 border p-4">
      <h1 className="text-center">Admin Dashboard</h1>
      {selectedCustomer ? (
        <div>
          <h2>Edit Customer</h2>
          <form onSubmit={handleSubmit} className="mb-3">
            {Object.entries(formData).map(([key, value]) => (
              <div className="mb-3" key={key}>
                <label className="form-label">{key.replace('_', ' ').toUpperCase()}</label>
                <input 
                  type="text" 
                  className="form-control" 
                  name={key} 
                  value={value} 
                  onChange={handleChange} 
                />
              </div>
            ))}
            <div className="text-center">
              <button type="submit" className="btn btn-primary me-2">Save Changes</button>
              <button type="button" className="btn btn-outline-primary" onClick={() => setSelectedCustomer(null)}>Cancel</button>
            </div>
          </form>
        </div>
      ) : (
        <div>
          <h2>Customers</h2>
          <div className="list-group">
            {customers.map(customer => (
              <div key={customer.id} className="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                {customer.first_name} {customer.last_name} - {customer.email}
                <span>
                  <button className="btn btn-outline-primary me-2" onClick={() => handleEdit(customer)}>Edit</button>
                  <button className="btn btn-outline-primary" onClick={() => handleDelete(customer.id)}>Delete</button>
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminPage;
