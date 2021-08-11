import { useEffect } from "react";
import { NavLink, Route, Switch } from "react-router-dom";
import { getPosts } from "../../store/slices/Postslice";
import { getComments } from "../../store/slices/Commentslice";
import { useDispatch } from "react-redux";


export default function HomePage() {
    const dispatch = useDispatch()
    // const [tabStatus, setTabStatus] = useState(0)

    useEffect(() => {
        dispatch(getPosts())
        dispatch(getComments())
    }, [dispatch])





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
