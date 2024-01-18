import React from 'react';

const Contact = () => {
  return (
    <div className="container my-5">
      <div className="text-center mb-4">
        <h1>Contact Timeless Trends</h1>
        <p>Have questions about our products or need assistance? We're here to help!</p>
      </div>

      <div className="text-center mb-3">
        <p><strong>Email:</strong> support@timelesstrends.com</p>
        <p><strong>Phone:</strong> (404)-567-8900</p>
        <p><strong>Address:</strong> 123 Fashion Ave, Atlanta, GA, 30301, USA</p>
      </div>

      <div className="text-center mb-4">
        <h2>Send Us a Message</h2>
        <form>
          <input type="text" className="form-control mb-2" placeholder="Your Name" />
          <input type="email" className="form-control mb-2" placeholder="Your Email" />
          <textarea className="form-control mb-2" placeholder="Your Message" rows="3"></textarea>
          <div className="d-flex justify-content-center">
            <button type="submit" className="btn btn-primary">Send Message</button>
          </div>
        </form>
      </div>

      <div className="text-center mt-4">
        <p>Follow us on social media:</p>
        <div className="d-flex justify-content-center mb-2">
          <a href="https://facebook.com/timelesstrends" className="btn btn-outline-primary me-2" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-facebook-f"></i> Facebook
          </a>
          <a href="https://instagram.com/timelesstrends" className="btn btn-outline-primary me-2" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-instagram"></i> Instagram
          </a>
          <a href="https://twitter.com/timelesstrends" className="btn btn-outline-primary" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-twitter"></i> Twitter
          </a>
        </div>
      </div>
    </div>
  );
}

export default Contact;
