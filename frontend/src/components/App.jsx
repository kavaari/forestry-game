import React, { Component } from 'react';
import './App.css';
import MainMenu from './MainMenu';
import MapMenu from './MapMenu';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: <MainMenu
                     switchView={this.switchView.bind(this)}
                     loggedIn={false}
                     toggleLogin={this.toggleLogin.bind(this)} />,
      loggedIn: false
    }
  }

  toggleLogin() {
    console.log('msg');
    this.setState((prevState) => ({
      loggedIn: !prevState.loggedIn,
      currentView: <MainMenu
                     switchView={this.switchView.bind(this)}
                     loggedIn={!prevState.loggedIn}
                     toggleLogin={this.toggleLogin.bind(this)} />
    }));
  }

  switchView(newView) {
    if (newView === 'mainmenu') {

      this.setState({
        currentView: <MainMenu
                       switchView={this.switchView.bind(this)}
                       loggedIn={this.state.loggedIn}
                       toggleLogin={this.toggleLogin.bind(this)} />
      });

    } else if (newView === 'mapmenu') {

      this.setState({
        currentView: <MapMenu
                       switchView={this.switchView.bind(this)}
                       loggedIn={this.state.loggedIn}
                       toggleLogin={this.toggleLogin.bind(this)} />
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
