import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import NavBarUnlogged from './components/NavBars/NavBar';
// import NavBarLogged from './components/NavBars';
import ProtectedRoute from './components/auth/ProtectedRoute';
// import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/slices/session';
import Welcome from './components/Welcome';
import HomePage from './components/Home';


function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  // const { user }= useSelector(state => state.session.user)

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }


  return (
    <BrowserRouter>
      <NavBarUnlogged />
      <Switch>
        <Route path='/welcome' exact={true}>
          <Welcome />
        </Route>
        <ProtectedRoute path='/home' exact={true} >
          <HomePage/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path='/' exact={true} >
          <h1>My Home Page</h1>
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
