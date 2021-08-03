import React from 'react'
import BackgroundSlider from 'react-background-slider'
import img1 from '../../assets/img1.jpg'
import img2 from '../../assets/img2.jpg'
import img3 from '../../assets/img3.jpg'
import img5 from '../../assets/img5.jpg'
import img6 from '../../assets/img6.jpg'
// import img7 from '../../assets/img7.jpg'
// import img8 from '../../assets/img8.jpg'
import img9 from '../../assets/img9.jpg'
import img10 from '../../assets/img10.jpg'
import img11 from '../../assets/img11.jpg'
import './Welcome.css'
import styled, { keyframes } from 'styled-components'


export default function Welcome() {

  const randomIn = (min, max) => Math.floor(Math.random()*(max - min + 1) + min)

  const flickerAnimation = keyframes`
  50% {
    color: white;
    filter: saturate(200%) hue-rotate(20deg);
  }`
  
  const Xsign = styled.p`
      interval: ${randomIn(2000, 4000)};
      display: block;
      color: lightyellow;
      text-shadow: 
        0 0 10px yellow,
        0 0 20px orange,
        0 0 40px brown,
        0 0 80px purple;
      font-family: pacifico;
      will-change: filter, color;
      filter: saturate(60%);
      animation-name: ${flickerAnimation};
      animation-duration: ${ randomIn(2000, 4000)}ms;
      animation-iteration-count: infinite;
      `
  // animation: flicker steps(100) interval ${randomIn(2000, 4000)} infinite;
  // Xsign.addEventListener('webkitAnimationIteration', () => {
  //   mixupInt(intv)
  // })


    return (
        <>
            <div className="intro_div">
                <Xsign>
                  <h1>Welcome!
                    <br/><small>to</small><br/>
                    <strong>Your Wildest Fantasy</strong>
                  </h1>                  
                </Xsign>
            </div>
            <BackgroundSlider images={[img1, img2, img3, img5, img6, img9, img10, img11]} duration={10} transition={2} />
        </>
    )
}