import _ from 'lodash'
import * as actions from './actions'

export const initialState = {
  sampleData: 'Sample Data'
}

export const SampleReducer = (state = initialState, _action) => {
  switch(_action.type) {
    case actions.ACTION_SAMPLE:
      return _.defaultsDeep({sampleData: _action.sampleData})
    default:
      return state
  }
}