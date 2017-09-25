import React, { Component } from 'react';
import './LangSelection.css';

export default class LangSelection extends Component {

  render() {
    return (
      <div className="LangSelection"
           style={this.props.style}>

        <div id="lang-sel-flag"></div>

        <div id="lang-sel-text">

          Suomi

        </div>
        
      </div>
    );
  }
}
