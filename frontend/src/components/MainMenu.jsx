import React, { Component } from 'react';
import Game from './Game';

export default class MainMenu extends Component {
  render() {
    // Just render the Game component for now
    // TODO: Real implementation
    return (
      <div className="MainMenu">
        <Game />
      </div>
    );
  }
}
