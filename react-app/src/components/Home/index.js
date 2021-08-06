import { useState, useEffect } from "react";
import { NavLink, Route, Switch } from "react-router-dom";


export default function HomePage() {

    const [tabStatus, setTabStatus] = useState(0)







    return (
        <>
            <body>
               
                <header><h1>LeagueName</h1></header>    
                <ul className="nav_tab_cont">
                    <li className="TAB one">
                        <button onClick="">MY ROSTER</button>
                    </li>
                    <li className="TAB two">
                        <button onClick="">TRADE</button>
                    </li>
                    <li className="TAB three">
                        <button onClick="">PLAYERS</button>
                    </li>
                    <li className="TAB four">
                        <button onClick="">SCHEDULE</button>
                    </li>
                    <li className="TAB five">
                        <button onClick="">STANDINGS</button>
                    </li>
                </ul>
                <div className="main_focus" >
                    {tabStatus}
                </div>
                
            </body>    

        </>
    )

}
