import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import { Navbar } from "./components/Navbar";
import { Login } from "./components/Login";
import { Users } from "./components/Users";

function App() {
  return (
    <Router>
      <Navbar />

      <div className="container p-4">
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/register" component={Users} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
