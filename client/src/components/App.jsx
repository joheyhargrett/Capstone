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
import './About.css';
import AdminPage from './AdminEdits';
import CustomerDetails from './CustomerProfile';

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

          
        </Routes>
      </UserProvider>
    </Router>
  );
}

export default App;
