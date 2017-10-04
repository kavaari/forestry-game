import React, { Component } from 'react';
import './App.css';
import MainMenu from './MainMenu';
import MapMenu from './MapMenu';
import Game from './Game';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: 'gameplayview',
      loggedIn: false,
      username: '',
      lang: 'fi'
    }
  }

  changeLanguage(newLanguage) {
    this.setState({
      lang: newLanguage
    });
  }

  toggleLogin(username) {
    this.setState((prevState) => ({
      loggedIn: !prevState.loggedIn,
      username: username
    }));
  }

  switchView(newView) {
    this.setState({
      currentView: newView
    });   
  }

  render() {
    var view;
    switch(this.state.currentView) {

      case 'mainmenu':
        view = (
          <MainMenu
            switchView={this.switchView.bind(this)}
            loggedIn={this.state.loggedIn}
            toggleLogin={this.toggleLogin.bind(this)}
            username={this.state.username}
            lang={this.state.lang}
            changeLanguage={this.changeLanguage.bind(this)} />
        );
        break;

      case 'mapmenu':
        view = (
          <MapMenu
            switchView={this.switchView.bind(this)}
            loggedIn={this.state.loggedIn}
            toggleLogin={this.toggleLogin.bind(this)}
            username={this.state.username}
            lang={this.state.lang} />
        );
        break;

      case 'gameplayview':
        var username = "";
        if (this.state.loggedIn) {
          username = this.state.username;
        } else {
          var rndNumber = Math.floor(Math.random() * 999999) + 1;
          username = 'guest' + rndNumber.toString();
        }
        view = (
          <Game 
            switchView={this.switchView.bind(this)}
            loggedIn={this.state.loggedIn}
            toggleLogin={this.toggleLogin.bind(this)}
            username={username} />
        );
        break;

      default:
        view = <div>You should never see this text.</div>;
        break;
    }
    return (
      <div className="App">

        {view}
        
      </div>
    );
  }
}
