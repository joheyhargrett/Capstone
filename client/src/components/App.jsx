import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { UserProvider } from './UserContext';
import './App.css';
import Home from './Home';
import Login from './Login';
import SignUp from './SignUp';
import NavBar from './NavBar'; 
import About from './About';
import Contact from './Contact';
import Cart from './Cart';
import Products from './Products';
import ErrorPage from './ErrorPage';
import AdminPage from './AdminEdits';
import CustomerDetails from './CustomerProfile';
import Product from './Product';
import CheckOut from './CheckOut';

function App() {
  return (
    <Router>
      <UserProvider>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/SignUp" element={<SignUp />} />
          <Route path="/About" element={<About />} />
          <Route path="/Contact" element={<Contact />} />
          <Route path="/Cart" element={<Cart />} />
          <Route path="/Products" element={<Products />} />
          <Route path="/Admin" element={<AdminPage />} />
          <Route path="/CustomerDetails" element={<CustomerDetails />} />
          <Route path="/Products/:id" element={<Product />} />
          <Route path="/CheckOut" element={<CheckOut />} />
          <Route path="*" element={<ErrorPage />} />
        </Routes>
      </UserProvider>
    </Router>
  );
}

export default App;
