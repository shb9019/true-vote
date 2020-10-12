import React from 'react';
import * as actionCreators from '../../store/actions/index';
import {useSelector, useDispatch} from 'react-redux';

const Home = (props) => {
	const counter = useSelector((state) => state.counter.counter);
	const dispatch = useDispatch();
	return (
		<div>
			<h1>True-Vote</h1>
			counter :{counter}
			<br></br>
			<button onClick={() => dispatch(actionCreators.increase())}>+1</button>
		</div>
	);
};

export default Home;
