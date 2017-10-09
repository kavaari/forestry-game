import * as PIXI from 'pixi.js';
import Truck from './truck';

const MAP = {
  "id": 1,
  "startpoint" : {"x": 200, "y": 500},
  "routes": [
    [
      {"x": 200, "y": 500},
      {"x": 400, "y": 700},
      {"x": 800, "y": 300},
      {"x": 1000, "y": 500},
    ]
  ],
  "logs": [

  ]
}

export default class GameCanvas {
  constructor() {
    var game = new PIXI.Application(window.innerWidth, window.innerHeight, {backgroundColor: 0x7da66e});
    this.update = this.update.bind(this);
    game.ticker.add(this.update);
    var interaction = new PIXI.interaction.InteractionManager(game.renderer);
    var mouseInput = {
      position: {
        x: 0,
        y: 0
      }
    };
    document.getElementById('canvas-game').appendChild(game.view);

    game.stage.pivot.set( MAP.startpoint.x,  MAP.startpoint.y);
    game.stage.position.x += game.renderer.width / 2;
    game.stage.position.y += game.renderer.height / 2;

    game.stage.hitArea = new PIXI.Rectangle(-1000000, -1000000, 1000000000, 1000000000);
    var graphics = new PIXI.Graphics();
    graphics.lineStyle(50, 0xa57d4c, 1);

    for (var i = 0; i < MAP.routes.length; i++) {
      for (var j = 0; j < MAP.routes[i].length; j++) {
        var pos = MAP.routes[i][j];
        if (j === 0) {
          graphics.moveTo(pos.x, pos.y);
        } else {
          graphics.lineTo(pos.x, pos.y);
        }
      }
    }

    graphics.endFill();
    game.stage.addChild(graphics);
    
    game.stage.interactive = true;
    game.stage.pointerdown = function() {
      mouseInput.isDown = true;
    };
    game.stage.pointerup = function() {
      mouseInput.isDown = false;
    };
    game.stage.pointerupoutside = function() {
      mouseInput.isDown = false;
    };

    game.stage.pointermove = function() {
      mouseInput.lastPosition = {x: mouseInput.position.x, y: mouseInput.position.y};
      mouseInput.position = {x: interaction.mouse.global.x, y: interaction.mouse.global.y};
      mouseInput.delta = {x: mouseInput.lastPosition.x - mouseInput.position.x, y: mouseInput.lastPosition.y - mouseInput.position.y};

      if (mouseInput.isDown === true) {
        game.stage.pivot.x +=  mouseInput.delta.x / game.stage.scale.x
        game.stage.pivot.y +=  mouseInput.delta.y / game.stage.scale.y
      }

    }
    
    var mouseWheelEvent = function(event) {
      if ((event.wheelDelta < -1 || event.deltaY > 1) && game.stage.scale.x > 0.5) {
        game.stage.scale.x -=  0.05;
        game.stage.scale.y -=   0.05;
      } else if ((event.wheelDelta > 1 || event.deltaY < -1) && game.stage.scale.x < 3.0) {
        game.stage.scale.x +=  0.05;
        game.stage.scale.y +=  0.05;
      }
    } 

    document.getElementById('canvas-game').addEventListener("mousewheel", mouseWheelEvent, false);

    this.truck = new Truck(MAP.startpoint.x, MAP.startpoint.y, game.stage, MAP.routes);
    this.game = game;
  }

  update(delta)
  {
    this.truck.update(delta)
  }

  destroy()
  {
    this.game.destroy(true);
  }
}
