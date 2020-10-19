import {increment, decrement, incrementByAmount} from '../reducers/counter';
export {incrementByAmount, decrement, increment};

export const incrementAsync = (amount) => (dispatch) => {
	setTimeout(() => {
		dispatch(incrementByAmount(amount));
	}, 1000);
};

export const selectCount = (state) => state.counter.value;
