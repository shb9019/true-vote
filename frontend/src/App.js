import React from 'react';
import './App.css';
import home from './container/home/home';
import {BrowserRouter, Route} from 'react-router-dom';

const App = () => {
	return (
		<div>
			<BrowserRouter>
				<Route path='/' component={home} />
			</BrowserRouter>
		</div>
	);
};

export default App;
