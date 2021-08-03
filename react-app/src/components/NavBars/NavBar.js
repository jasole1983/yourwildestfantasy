
import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { Modal } from '../../context/Modal'
import LoginSignup from '../auth/LoginSignup'
import './NavBar.css'
import { useDispatch } from 'react-redux';

export default function NavBar () {

  const [showModal, setShowModal] = useState(false)
  const [launchModal, setLaunchModal] = useState('')
                    
  const dispatch = useDispatch()

  const handleClick = (e) => {
    // e.preventDefault()
    setLaunchModal(e.target.side)
    console.log(launchModal)
  }
  
  useEffect( () => {
    
    if (launchModal === 'login'){
      dispatch(setShowModal(true))
      setTimeout(() => (
        dispatch(setLaunchModal(''))
      ), 2000)
    }
    if (launchModal === 'signup'){
      dispatch(setShowModal(true))
      setTimeout(() => (
        dispatch(setLaunchModal(''))
      ), 2000)
    }


  }, [dispatch, showModal, launchModal])


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
              <button className='navbar_btn' onClick={handleClick('login')} side="login">
                Login
              </button>
            </li>
            <li>
              <button className='navbar_btn'onClick={handleClick('signum')} side="signup">
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


