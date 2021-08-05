import { combineReducers } from 'redux';
import session from './session'
import { configureStore } from '@reduxjs/toolkit'
import logger from 'redux-logger'


const rootReducer = combineReducers({
  session,
});

export default function configureAppStore(preloadedState) {
  const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
    preloadedState,
    enhancers: [],

  })

  return store
}
// let enhancer;

// if (process.env.NODE_ENV === 'production') {
//   enhancer = applyMiddleware(thunk);
// } else {
//   const logger = require('redux-logger').default;
//   const composeEnhancers =
//     window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
//   enhancer = composeEnhancers(applyMiddleware(thunk, logger));
// }

// const configureStore = (preloadedState) => {
//   return createStore(rootReducer, preloadedState, enhancer);
// };


