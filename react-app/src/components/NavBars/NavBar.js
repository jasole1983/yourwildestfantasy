
import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { Modal } from '../../context/Modal'
import LoginSignup from '../auth/LoginSignup'
import './NavBar.css'
// import { useDispatch } from 'react-redux';

export default function NavBarUnlogged () {

  const [showModal, setShowModal] = useState(false)
 


  return (
    <>
        <nav className="header navbar">
          <ul>
            <li>
              <NavLink to='/' exact={true} activeClassName='active'>
                Home
              </NavLink>
            </li>
            <li>
              <button className='navbar_btn' onClick={() => setShowModal(true)}>
                Login
              </button>
            </li>
            <li>
              <button className='navbar_btn'onClick={() => setShowModal(true)}>
                Sign Up
              </button>
            </li>
            <li>
              <button className='navbar_btn'>
                Demo
              </button>
            </li>
            <li>
              <LogoutButton />
            </li>
          </ul>
        </nav>
          {showModal && (
          <Modal onClose={() => setShowModal(false)}>
              <LoginSignup setShowModal={setShowModal}/>
          </Modal> 
        )}
    
    </>   
  );
}


