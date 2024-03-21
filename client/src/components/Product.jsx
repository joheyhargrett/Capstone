import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addCart } from "./indexRR";
import { useParams, Link } from 'react-router-dom';
import Skeleton from 'react-loading-skeleton';

const Product = () => {
  const { id } = useParams();
  const [product, setProduct] = useState([]);
  const [loading, setLoading] = useState(false);

  const dispatch = useDispatch();
  const addProduct = (product) => {
    dispatch(addCart(product));
  }

  useEffect(() => {
    const getProduct = async () => {
      setLoading(true);
      const response = await fetch(`http://localhost:5555/products/${id}`);
      if (response.ok) {
        const data = await response.json();
        console.log(data);
        setProduct(data);
        setLoading(false);
      } else {
        console.error(`Failed to fetch product details: ${response.status}`);
      } 
    }
    getProduct();
  }, [id]);

  const ShowProduct = ({ product }) => {
    // Function to calculate average rating
    const calculateAverageRating = (reviews) => {
      if (!reviews || reviews.length === 0) return 0;
      const total = reviews.reduce((acc, review) => acc + review.rating, 0);
      return (total / reviews.length).toFixed(1); // Keeping one decimal place
    };

    // Calculate the average rating
    const averageRating = calculateAverageRating(product.reviews);

    return(
      <>
        <div className="col-md-6" key={product.id}>
          <img src={product.image_url} alt={product.name} height="600px" width="600px" />
        </div>
        <div className="col-md-6">
          <h4 className="text-uppercase text-black-50">
            {product.category}
          </h4>
          <h1 className="display-5">{product.name}</h1>
          <p className="lead fw-bolder">
            Rating {averageRating} <i className="fa fa-star"></i>
          </p>
          <h3 className="display-6 fw-bold my-4">
            ${product.price}
          </h3>
          <p className="lead">{product.description}</p>
          <button className="btn btn-outline-dark px-3 py-2" onClick={() => addProduct(product)}>
            Add to Cart
          </button>
          <Link to="/cart" className='btn btn-outline-dark ms-2 px-3 py-2'>
            Go to Cart
          </Link>
        </div>
      </>
    );
  }

  return (
    <div>
      <div className="container py-4">
        <div className="row">
          {loading ? <Skeleton /> : <ShowProduct product={product} />}
        </div>
      </div>
    </div>
  );
}

export default Product;
