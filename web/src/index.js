import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App.js';
import reportWebVitals from './reportWebVitals.js';
import { BrowserRouter as Router } from 'react-router-dom';
import {Auth0Provider} from '@auth0/auth0-react'

const domain = process.env.REACT_APP_AUTHO_DOMAIN
const clientId = process.env.REACT_APP_AUTHO_CLIENT_ID

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
   <Auth0Provider 
      domain={domain}
      clientId={clientId}
      redirectUri={window.location.origin}
    >
     <Router>
        <App />
      </Router> 
    </Auth0Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();