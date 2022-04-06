import React from 'react';
// import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import './index.css';
import Root from "pages"
import {BrowserRouter}  from 'react-router-dom';
// import PostList from 'components/PostList';
// import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );
// const rootElement = document.getElementById('root');
// const root = createRoot(rootElement);
const root = createRoot(document.getElementById("root"));
 
root.render(
  <BrowserRouter>
    <Root/>
    {/* <PostList /> */}
  </BrowserRouter>,
);

//yarn add react-router-dom
//yarn add axios