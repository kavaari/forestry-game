import React, { Component } from 'react';
import Button from './Button';
import LangSelection from './LangSelection';
import LoginSignupForm from './LoginSignupForm';
import './MainMenu.css';

export default class MainMenu extends Component {
  constructor(props) {
    super(props);
  }

  handleButtonClick(e) {
    var clicked = e.target.getAttribute('id');

    if (clicked === 'button-start-game') {
      this.props.switchView('mapmenu');
    }
  }

  handleFormClick(username, event) {
    // Set loggedIn for testing purposes
    // TODO: connect to backend

    this.props.toggleLogin(username);
  }

  render() {

    var langSelStyle = {
      position: 'fixed',
      right: '10%',
      top: '5%'
    }
    
    var leftButtonStyle = {
      position: 'fixed',
      left: '10%',
      bottom: '10%'
    }

    var rightButtonStyle = {
      position: 'fixed',
      right: '10%',
      bottom: '10%',
      backgroundColor: 'var(--jd-yellow)'
    }

    var centerElement;
    var startButtonText;
    if (this.props.loggedIn) {

      centerElement = (
        <div id="welcome-message">
          Welcome,<br />
          {this.props.username}
        </div>
      );

      startButtonText = 'Start game';

    } else {

      centerElement = <LoginSignupForm handleClick={this.handleFormClick.bind(this)} />;
      startButtonText = 'Play as guest';
    }

    return (
      <div className="MainMenu">

        <LangSelection style={langSelStyle} />

        {centerElement}

        <Button
          id="button-how-to-play"
          text="How to play"
          style={leftButtonStyle}
          handleClick={this.handleButtonClick.bind(this)} />

        <Button
          id="button-start-game"
          text={startButtonText}
          style={rightButtonStyle}
          handleClick={this.handleButtonClick.bind(this)} />

      </div>
    );
  }
}
