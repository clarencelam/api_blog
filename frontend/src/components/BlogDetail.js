import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const BlogDetail = () => {
    const [blog, setBlog] = useState({});



    return(
        <div className='container mt-3'>
            <h1 className='display-2'>title</h1>
            <h2 className="text-muted mt-3">Category: category</h2>
            <h4>month day</h4>
            <div className='mt-5 mb-5' dangerouslySetInnerHTML={createBlog()} />
            <hr />
            <p className='lead mb-5'><Link to='/blog' className='font-weight-bold'>Back to Blogs</Link></p>
        </div>
    );
};

export default BlogDetail;