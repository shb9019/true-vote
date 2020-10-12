import * as actionTypes from '../actions/actionTypes';

const initialState = {
	counter: 0,
};

const reducer = (state = initialState, action) => {
	switch (action.type) {
		case actionTypes.INCREASE:
			return {
				...state,
				counter: state.counter + 1,
			};
		default:
			return state;
	}
};

export default reducer;
