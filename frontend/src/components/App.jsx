import React, { Component } from 'react';
import './App.css';
import MainMenu from './MainMenu';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: <MainMenu />
    }
  }

  switchView(newView) {
    this.setState({
      currentView: newView
    });
  }

  render() {
    return (
      <div className="App">

        {this.state.currentView}
        
      </div>
    );
  }
}
