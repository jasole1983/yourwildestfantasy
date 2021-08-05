import { NavLink } from "react-router-dom"
import LogoutButton from "../auth/LogoutButton"
import MessageBoard from "../MessageBoard"

export default function NavBarLogged() {



    return (
        <nav className="header navbar_logged">
          <ul>
            <li>
              <button>
                <NavLink to='/home' exact={true} activeClassName='active'>
                Home
                </NavLink>
              </button>
            </li>
            <li>
              <NavLink to='/<int:leagueid>/messageboard'>
                  MessageBoard
                  <MessageBoard />
              </NavLink>
            </li>
            <li>
              <NavLink to='/<int:userid>/myleagues'>My Leagues</NavLink>
            </li>
            <li>
              <NavLink to='/somepageicantremember'>Can't Remember ATM</NavLink>
            </li>
            <li>
              <LogoutButton />
            </li>
          </ul>
        </nav>
    )
}