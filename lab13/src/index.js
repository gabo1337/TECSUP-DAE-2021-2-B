import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Route, Link, BrowserRouter,Routes} from 'react-router-dom';

import App from './App';
import Users from './users';
import Contact from './contact';
import Notfound  from './notfound';
import Tabla from './tabla';

const routing = (
  
  <div>
    
  <BrowserRouter>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href="/">Home </a>
      <a class="nav-item nav-link" href="/usuarios">Usuarios</a>
      <a class="nav-item nav-link" href="/contacto">Contacto</a>
      <a class="nav-item nav-link" href="/tabla">tablas</a>
    </div>
    
  </div>
</nav>

   
    <Routes>
      <Route exact path="/" element={<App />} />
      <Route path="/usuarios" element={<Users />} />
      <Route path="/usuarios/:id" element={<Users />} />
      <Route path="/contacto" element={<Contact />} />
      <Route path="/tabla" element={<Tabla />} />
      <Route path="*" element={<Notfound />} />
    </Routes>
  </BrowserRouter>
</div>

  
  )


  ReactDOM.render(
    routing, 
    document.getElementById('root')
    );
  

