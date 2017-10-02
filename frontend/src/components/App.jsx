import React, { Component } from 'react';
import './App.css';
import MainMenu from './MainMenu';
import MapMenu from './MapMenu';
import Game from './Game';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: <MainMenu
                     switchView={this.switchView.bind(this)}
                     loggedIn={false}
                     toggleLogin={this.toggleLogin.bind(this)}
                     username="" />,
      loggedIn: false,
      username: ''
    }
  }

  toggleLogin(username) {
    console.log('msg');
    this.setState((prevState) => ({
      loggedIn: !prevState.loggedIn,
      currentView: <MainMenu
                     switchView={this.switchView.bind(this)}
                     loggedIn={!prevState.loggedIn}
                     toggleLogin={this.toggleLogin.bind(this)}
                     username={username} />,
      username: username
    }));
  }

  switchView(newView) {
    if (newView === 'mainmenu') {

      this.setState({
        currentView: <MainMenu
                       switchView={this.switchView.bind(this)}
                       loggedIn={this.state.loggedIn}
                       toggleLogin={this.toggleLogin.bind(this)}
                       username={this.state.username} />
      });

    } else if (newView === 'mapmenu') {

      this.setState({
        currentView: <MapMenu
                       switchView={this.switchView.bind(this)}
                       loggedIn={this.state.loggedIn}
                       toggleLogin={this.toggleLogin.bind(this)}
                       username={this.state.username} />
      });
    } else if (newView === 'gameplayview') {
      var username = "";
      if (this.state.loggedIn) {
        username = this.state.username;
      } else {
        var rndNumber = Math.floor(Math.random() * 999999) + 1;
        username = 'guest' + rndNumber.toString();
      }
      this.setState({
        currentView: <Game 
                       switchView={this.switchView.bind(this)}
                       loggedIn={this.state.loggedIn}
                       toggleLogin={this.toggleLogin.bind(this)}
                       username={username} />
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
