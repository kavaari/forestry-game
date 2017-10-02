import React, { Component } from 'react';
import Button from './Button';
import './LoginSignupForm.css';

export default class LoginSignupForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentView: 'login',
      username: '',
      password: '',
      email: '',
      message: undefined
    }
  }

  handleInputChange(e) {
    const name = e.target.name;
    const value = e.target.value;

    this.setState({
      [name]: value,
      message: undefined
    });
  }

  handleSignupLinkClick() {
    if (this.state.currentView === 'login') {

      this.setState({
        currentView: 'signup'
      });

    } else {

      this.setState({
        currentView: 'login'
      });
    }
  }

  render() {
    var buttonStyle = {
      margin: 'auto',
      width: 'var(--form-width)',
      backgroundColor: 'var(--jd-yellow)',
      boxShadow: 'var(--menu-shadow-2)'
    };

    var hiddenSubmit = {
      display: 'none'
    };

    var emailField;
    var formButton;
    if (this.state.currentView === 'signup') {
      emailField = (
        <input 
          type="text"
          id="email"
          name="email"
          placeholder="email"
          value={this.state.email}
          onChange={this.handleInputChange.bind(this)} />
      );

      formButton = (
        <Button
          id="button-sign-up"
          text="Sign up"
          style={buttonStyle}
          handleClick={() => this.props.handleClick(this.state.username)} />
      );

    } else {

      formButton = (
        <Button
          id="button-log-in"
          text="Log in"
          style={buttonStyle}
          handleClick={() => this.props.handleClick(this.state.username)} />
      );
    }

    return (
      <div className="LoginForm">

        <div id="login-form">

          {this.state.message ? <div id="message">{this.state.message}</div> : ''}

          <form onSubmit={() => this.props.handleClick(this.state.username)}>

            <input 
              type="text"
              id="username"
              name="username"
              placeholder="username"            
              value={this.state.username}
              onChange={this.handleInputChange.bind(this)} />

            {this.state.currentView === 'signup' ? emailField : ''}

            <input 
              type="password"
              id="password"
              name="password"
              placeholder="password"            
              value={this.state.password}
              onChange={this.handleInputChange.bind(this)} />

            <input type="submit" style={hiddenSubmit} />

          </form>

          {formButton}

        </div>

        <div id="signup-message">

          {this.state.currentView === 'login' ? 'Don\'t have and account? ' : 'Already have an account? '}
          
          <span
            id="signup-link"
            onClick={this.handleSignupLinkClick.bind(this)} >

            {this.state.currentView === 'login' ? 'Sign Up' : 'Log In'}

          </span>
          
          {' here!'}

        </div>

      </div>
    );
  }
}
