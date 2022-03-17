import React from 'react';
import { Link } from 'react-router-dom';

const home = () => (
    <div className = 'container'>
        <div class='mt-4'>
        <h1 className="display-4">Welcome.</h1>
        </div>
        <div class='mt-4'>
            <h4>
                This is a blog currently in progress, being built with a Django REST API back-end and React front-end.
            </h4>
        </div>
        <div class='mt-4'>
            <h4>
            <Link className="btn btn-primary btn-lg" to='/blog' role="button">View the blog catalogue here.</Link>
            </h4>
        </div>
    </div>
);

export default home;