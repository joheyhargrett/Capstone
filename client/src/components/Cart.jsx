import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { delCart } from './indexRR'; 


const Cart = () => {
  const state = useSelector((state) => state.handleCart);
  const dispatch = useDispatch();

  const handleClose = (item) => {
    dispatch(delCart(item));
  };

  const cartItems = (cartItem) => {
    return (
      <div className="px-4 my-5 bg-light rounded-3" key={cartItem.id}>
        <div className="container py-4">
          <button onClick={() => handleClose(cartItem)} className="btn-close float-end" aria-label="Close"></button>
          <div className="row justify-content-center">
            <div className="col-md-4">
              <img src={cartItem.image_url} alt={cartItem.name} height="200px" width="180px" />
            </div>
            <div className="col-md-4">
              <h3>{cartItem.name}</h3>
              <p className="lead fw-bold">${cartItem.price}</p>
              <p className="small">Quantity: {cartItem.qty}</p>
              <p className="lead fw-bold">Total: ${cartItem.price * cartItem.qty}</p>

            </div>
          </div>
        </div>
      </div>
    );
  };

  const emptyCart = () => {
    return (
      <div className="px-4 my-5 bg-light rounded-3 py-5">
        <div className="container py-4">
          <div className="row">
            <h3>Your Cart is Empty</h3>
          </div>
        </div>
      </div>
    );
  };

  const button = () => {
    return (
      <div className="container">
        <div className="row">
          <Link to="/checkout" className="btn btn-outline-primary mb-5 w-25 mx-auto">Proceed To Checkout</Link>
        </div>
      </div>
    );
  };

  return (
    <>
      {state.length === 0 && emptyCart()}
      {state.length !== 0 && state.map(cartItems)}
      {state.length !== 0 && button()}
    </>
  );
};

export default Cart;
