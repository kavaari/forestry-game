import React, { Component } from 'react';
import './App.css';
import MainMenu from './MainMenu';
import MapMenu from './MapMenu';
import Game from './Game';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: 'mainmenu',
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

      // this.setState({
      //   currentView: <MapMenu
      //                  switchView={this.switchView.bind(this)}
      //                  loggedIn={this.state.loggedIn}
      //                  toggleLogin={this.toggleLogin.bind(this)}
      //                  username={this.state.username} />
      // });
//     } else if (newView === 'gameplayview') {
//       var username = "";
//       if (this.state.loggedIn) {
//         username = this.state.username;
//       } else {
//         var rndNumber = Math.floor(Math.random() * 999999) + 1;
//         username = 'guest' + rndNumber.toString();
//       }
//       this.setState({
//         currentView: <Game 
//                        switchView={this.switchView.bind(this)}
//                        loggedIn={this.state.loggedIn}
//                        toggleLogin={this.toggleLogin.bind(this)}
//                        username={username} />
//       });
//     }
//   }
// >>>>>>> 281c98ce9465ae24d39bac35348a8beb48c6d824

      default:
        view = <div>Default</div>;
        break;
    }
    return (
      <div className="App">

        {view}
        
      </div>
    );
  }
}
