import React, { Component } from 'react';
import './Game.css';

export default class Game extends Component {

  componentDidMount() {
    canvasStuff();
  }

  render() {
    return (
      <div className="Game">
        <canvas id="canvas-game"></canvas>
      </div>
    );
  }
}

// Canvas test code
// TODO: Press delete on this
function canvasStuff() {
  var canvas = document.getElementById('canvas-game');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  window.onresize = function(event) {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  var c = canvas.getContext('2d');

  var mouse = {
    x: undefined,
    y: undefined
  }

  window.addEventListener('mousemove', function(event) {
    mouse.x = event.x;
    mouse.y = event.y;
  });

  function Circle(x, y, r, dx, dy) {
    this.x = x;
    this.y = y;
    this.radius = r;
    this.dx = dx;
    this.dy = dy;

    this.draw = function() {
      c.beginPath();
      c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
      c.strokeStyle = 'red';
      c.stroke();
      c.fill();
    }

    this.update = function() {
      if (this.x + this.radius > window.innerWidth || this.x - this.radius < 0) {
        this.dx = -this.dx;
      }

      if (this.y + this.radius > window.innerHeight || this.y - this.radius < 0) {
        this.dy = -this.dy;
      }

      this.x += this.dx;
      this.y += this.dy;

      // interact
      if (mouse.x - this.x < 50 && 
          mouse.x - this.x > -50 && 
          mouse.y - this.y < 50 &&
          mouse.y - this.y > -50 &&
          this.radius < 50) {
        this.radius += 1;
      } else if (this.radius > 2){
        this.radius -= 1;
      }

      this.draw();
    }
  }

  var circles = [];

  for (var i = 0; i < 1000; i++) {
    circles.push(new Circle(
        Math.random() * (window.innerWidth - 40 * 2) + 40,
        Math.random() * (window.innerHeight - 40 * 2) + 40,
        40,
        (Math.random() - 0.5) * 1,
        (Math.random() - 0.5) * 1
      )
    );
  }

  animate();

  function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0, 0, window.innerWidth, window.innerHeight);

    for (var i = 0; i < circles.length; i++) {
      circles[i].update();
    }
  }
}
