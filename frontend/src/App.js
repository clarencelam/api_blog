//import './App.css';
import React from 'react';
import {BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Layout from './hocs/Layout';
import Home from './components/Home';
import Blog from './components/Blog';
import Category from './components/Category';
import BlogDetail from './components/BlogDetail';

const App = () => (
  <Router>
    <Layout>
      <Switch>
        <Route exact path='/welcome' element={Home} />
        <Route exact path='/blog' component={Blog} />
        <Route exact path='/category/:id' component={Category} />
        <Route exact path='/blog/:id' component={BlogDetail} />
      </Switch>
    </Layout>
  </Router>
);

export default App;
