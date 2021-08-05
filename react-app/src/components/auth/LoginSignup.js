import ReactCardFlip from 'react-card-flip'
import { useState, useEffect } from 'react'
import LoginForm from './LoginForm'
import SignUpForm from './SignUpForm'

export default function LoginSignup() {

    const [isFlipped, setIsFlipped] = useState(false)

    const handleClick = (e) => {
        e.preventDefault();
        setIsFlipped( !isFlipped )
    }
    return (
        <ReactCardFlip isFlipped={isFlipped} flipDirection="horizontal">
          <div className="login_cont">
            <LoginForm />
            <button onClick={handleClick}>SignUp</button>
          </div>
          <div className="signup_cont">
            <SignUpForm />
            <button onClick={handleClick}>Login</button>
          </div>
        </ReactCardFlip>
    )
}