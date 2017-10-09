import * as PIXI from 'pixi.js';
import * as Key from './controls'
import {lerp, distance} from './helpers';


export default class Truck {
  constructor(x, y, stage, routes) {
    this.sprite = PIXI.Sprite.fromImage('/truck.png');
    this.sprite.anchor.set(0.5);

    this.sprite.x = x;
    this.sprite.y = y;

    this.velocity = 5.0;

    this.pointAIndex = 0;
    this.pointBIndex = 1;
    this.pointDelta = 0;
    this.currentRoute = routes[0];
    this.routeSegmentLength = distance(this.currentRoute[this.pointAIndex], this.currentRoute[this.pointBIndex]);
    stage.addChild(this.sprite);
  }

  update(timeDelta) {
    var direction = 0;
    if(Key.up.isDown) {
      direction = 1
    }
    if(Key.down.isDown) {
      direction = -1
    }    

    this.pointDelta += (direction * this.velocity * timeDelta) / this.routeSegmentLength;

    if (this.pointDelta <= 0) {
      this.pointDelta = 0;

      if (this.pointAIndex !== 0) {
        this.pointDelta = 0.99;
        this.pointAIndex--;
        this.pointBIndex--;
        this.routeSegmentLength = distance(this.currentRoute[this.pointAIndex], this.currentRoute[this.pointBIndex]);
      }

    } else if (this.pointDelta >= 1) {
      this.pointDelta = 1;

      if (this.pointBIndex !== this.currentRoute.length - 1) {
        this.pointDelta = 0.01;
        this.pointAIndex++;
        this.pointBIndex++;
        this.routeSegmentLength = distance(this.currentRoute[this.pointAIndex], this.currentRoute[this.pointBIndex]);
      }
    }

    var pA = this.currentRoute[this.pointAIndex];
    var pB = this.currentRoute[this.pointBIndex]
    var point = lerp(this.currentRoute[this.pointAIndex], this.currentRoute[this.pointBIndex], this.pointDelta)
    this.sprite.x = point.x;
    this.sprite.y = point.y;

    this.sprite.rotation = Math.atan2(pB.y - pA.y, pB.x - pA.x) + Math.PI/2;    
  }
}
