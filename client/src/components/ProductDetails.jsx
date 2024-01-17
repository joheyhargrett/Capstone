import React, { useState, useEffect } from 'react';

const ProductDetails = ({ productId }) => {
  const [product, setProduct] = useState(null);

  useEffect(() => {
    
    fetchProductDetails(productId);
  }, [productId]);

  const fetchProductDetails = async (id) => {
    try {
      const response = await fetch(`http://localhost:5555/products/${id}`);
      if (response.ok) {
        const data = await response.json();
        setProduct(data);
      } else {
        console.error('Failed to fetch product details:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error during fetch:', error);
    }
  };

  const handleUpdateProduct = async (updatedData) => {
    try {
      const response = await fetch(`http://localhost:5555/products/${productId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedData),
      });

      if (response.ok) {
        
        console.log('Product updated successfully!');
      } else {
        console.error('Failed to update product:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error during update:', error);
    }
  };

  const handleDeleteProduct = async () => {
    try {
      const response = await fetch(`http://localhost:5555/products/${productId}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        
        console.log('Product deleted successfully!');
      } else {
        console.error('Failed to delete product:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error during delete:', error);
    }
  };

  return (
    <div>
      {product ? (
        <div>
          <h2>{product.name}</h2>
          <p>Price: ${product.price}</p>
          <p>Description: {product.description}</p>
          <p>Stock: {product.stock}</p>
          <p>Category: {product.category}</p>
          <p>Image: {product.image}</p>
          
          <button onClick={() => handleUpdateProduct({ name: 'Updated Product' })}>
            Update Product
          </button>
          <button onClick={handleDeleteProduct}>Delete Product</button>
        </div>
      ) : (
        <p>Loading product details...</p>
      )}
    </div>
  );
};

export default ProductDetails;
