import React, { Component } from 'react';
import './App.css';
import MainMenu from './MainMenu';
import MapMenu from './MapMenu';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: <MapMenu switchView={this.switchView.bind(this)} />
    }
  }

  switchView(newView) {
    if (newView === 'mainmenu') {

      this.setState({
        currentView: <MainMenu switchView={this.switchView.bind(this)} />
      });

    } else if (newView === 'mapmenu') {

      this.setState({
        currentView: <MapMenu switchView={this.switchView.bind(this)} />
      });
    }    
  }

  render() {
    return (
      <div className="App">

        {this.state.currentView}
        
      </div>
    );
  }
}
