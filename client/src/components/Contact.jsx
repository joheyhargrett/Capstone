import React from 'react';
import './Contact.css';


const Contact = () => {
  return (
    <div className="contact-container">
      <div className="contact-header">
        <h1>Contact Timeless Trends</h1>
      </div>
      <div className="contact-body">
        <p>Have questions about our products or need assistance? We're here to help!</p>

        <div className="contact-info">
          <p><strong>Email:</strong> support@timelesstrends.com</p>
          <p><strong>Phone:</strong>  (404)-567-8900</p>
          <p><strong>Address:</strong> 123 Fashion Ave, Atlanta, GA, 30301, USA</p>
        </div>

        <div className="contact-form">
          <h2>Send Us a Message</h2>
          <form>
            <input type="text" placeholder="Your Name" />
            <input type="email" placeholder="Your Email" />
            <textarea placeholder="Your Message"></textarea>
            <button type="submit">Send Message</button>
          </form>
        </div>

        <div className="social-media">
          <p>Follow us on social media:</p>
          <a href="https://facebook.com/timelesstrends" target="_blank" rel="noopener noreferrer">Facebook</a>
          <a href="https://instagram.com/timelesstrends" target="_blank" rel="noopener noreferrer">Instagram</a>
          <a href="https://twitter.com/timelesstrends" target="_blank" rel="noopener noreferrer">Twitter</a>
        </div>
      </div>
    </div>
  );
}

export default Contact;
