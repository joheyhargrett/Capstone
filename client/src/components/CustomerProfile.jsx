import React, { useState, useEffect } from 'react'


function CustomerProfile() {
    const [customer, setCustomer] = useState({});

    useEffect(() => {
        const fetchCustomer = async () => {
          try {
            const response = await fetch('http://localhost:5555/customer/id');
            if (response.ok) {
              const data = await response.json();
              setCustomer(data);
            } else {
              console.error('Failed to fetch customer:', response.statusText);
            }
          } catch (error) {
            console.error('Error during fetch:', error);
          }
        };
        fetchCustomer();
    })
  return (
    <div>
      <h1>Customer Profile</h1>
      <p>Name: {customer.name}</p>
      <p>Email: {customer.email}</p>
      <p>Address: {customer.address}</p>
      <p>Phone: {customer.phone}</p>
      
      
    </div>
  )
}





export default CustomerProfile

