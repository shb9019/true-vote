import React from 'react';
import * as actionCreators from '../../store/actions/index';
import {useSelector, useDispatch} from 'react-redux';
import Logo from '../../components/logo/Logo';

const Home = (props) => {
	const counter = useSelector((state) => state.counter.counter);
	const dispatch = useDispatch();
	return (
		<div>
			<Logo />
			counter :{counter}
			<br></br>
			<button onClick={() => dispatch(actionCreators.increase())}>+1</button>
		</div>
	);
};

export default Home;
