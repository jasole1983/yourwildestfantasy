import { combineReducers } from 'redux';
import session from './slices/session'
import { configureStore } from '@reduxjs/toolkit'
import logger from 'redux-logger'
import postReducer from './slices/messages'
import commentReducer from './slices/CommentSlice'



export default function configureAppStore(preloadedState) {
  const store = configureStore({
    reducer: {
      session,
      post: postReducer,
      comment: commentReducer,
    },
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


