/* global window: true */
import _ from 'lodash'
import { createStore, applyMiddleware ,combineReducers } from 'redux'
import thunk from 'redux-thunk'
import reduxLogger from 'redux-logger'

import {SampleActions, SampleReducer} from './redux-sample'

export const reduxActions = _.assign(
  {},
  SampleActions
)

export const reduxReducers = combineReducers({
  SampleReducer
})

if(!window.store)
{
  // create redux store
  let store = createStore(reduxReducers, applyMiddleware(thunk, reduxLogger))

  // set store and dispatch as global variables
  window.store = store
  window.dispatch = store.dispatch
}