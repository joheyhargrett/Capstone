import React from "react";
import App from "./components/App";
import "./index.css";
import { createRoot } from "react-dom/client";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/font-awesome/css/font-awesome.min.css';

import { Provider } from 'react-redux';
import  store  from './components/store';






const container = document.getElementById("root");
const root = createRoot(container);

root.render(
    <Provider store={store}>    
        <App />
    </Provider>    
    );

