import React from 'react';
import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import './index.css';
import App from './App';
// import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );
const rootElement = document.getElementById('root');
const root = createRoot(rootElement);
// const root = ReactDOM.createRoot(document.getElementById("root"));
 
root.render(
  <StrictMode>
    <App />
  </StrictMode>,
);