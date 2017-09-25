import React from 'react';
import './Button.css';

export default function Button(props) {

  if (props.roundedCorners) {
    props.style.borderRadius = '5px';
  }

  return (
    <div
      className="Button"
      id={props.id}
      style={props.style}
      onClick={props.handleClick} >

    {props.text}
    
    </div>
  );
}
