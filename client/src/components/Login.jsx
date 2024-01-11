import React, { useState, useContext } from 'react'
import { useHistory } from 'react-router-dom'



const Login = () => {
    




    // const handleSubmit = (e) => {
    //     e.preventDefault()
    // }


  return (
    <div>
      <form >
        <h1>Login</h1>
        <label htmlFor="email">Email</label>
        <input type="email" name="email" id="email" value  required placeholder='Enter your email' />
        <label htmlFor="password">Password</label>
        <input type="password" name="password" id="password" value  required placeholder='Enter your password'/>
        <button type="submit">Login</button>
      </form>
    </div>
  )
}

export default Login
