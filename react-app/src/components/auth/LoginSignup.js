import ReactCardFlip from 'react-card-flip'
import { useState } from 'react'
import LoginForm from './LoginForm'
import SignUpForm from './SignUpForm'
import './LoginSIgnup.css'

export default function LoginSignup() {

    const [isFlipped, setIsFlipped] = useState(false)

    const handleClick = (e) => {
        e.preventDefault();
        setIsFlipped( !isFlipped )
    }
    return (

              <div className= "outter modal cont">
                <ReactCardFlip isFlipped={isFlipped} flipDirection="horizontal">
                  <div className="signup_cont">
                    <SignUpForm />
                    <span>Already have an account?</span>
                    <button className="submit_btn signup" onClick={handleClick}>SignUp</button>
                  </div>
                  <div className="login_cont">
                    <LoginForm />
                    <span>Don't have an account yet?</span>
                    <button className="submit_btn login" onClick={handleClick}>Login</button>
                  </div>
                </ReactCardFlip>
              </div>
    )
}