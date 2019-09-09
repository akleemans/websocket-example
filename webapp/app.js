console.log("Initializing and connecting websocket...");
let socket = new WebSocket("ws://localhost:5678");
let canvas;
let ctx;
let board;
let mouseIsDown = false;
let startField = null;

const boardParams = {
  startX: 20,
  startY: 20,
  fieldSize: 34,
  dim: {w: 8, h: 8}
};

const actions = {
  out: {
    NEW_GAME: 'NEW_GAME',
    REQUEST_MOVE: 'REQUEST_MOVE'
  },
  in: {
    NEW_GAME: 'NEW_GAME',
    MOVE: 'MOVE'
  }
};

socket.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log("Got message:", message);
  switch (message.action) {
    case actions.in.NEW_GAME:
    case actions.in.MOVE:
    default:
      board = message.data;
      drawBoard();
      break;
  }
};

//////////

const init = () => {
  console.log("Initializing...");
  // setup canvas
  canvas = document.getElementById('gameCanvas');
  ctx = canvas.getContext('2d');

  canvas.addEventListener('mousedown', function (e) {
    mouseIsDown = true;
    startField = getField(e.clientX, e.clientY);
  });

  canvas.addEventListener('mouseup', function (e) {
    let targetField = getField(e.clientX, e.clientY);
    if (startField === targetField - 1 || startField === targetField + 1 ||
      startField === targetField - boardParams.dim.w || startField === targetField + boardParams.dim.w) {
      console.log('neighbor fields!', startField, targetField);
      send(actions.out.REQUEST_MOVE, {from: startField, to: targetField});
    } else {
      console.log('NO neighbors...', startField, targetField);
    }
    // TODO send event
    mouseIsDown = false;
  });
};

const drawBoard = () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < board.length; i++) {
    let shape = board[i];
    let x = (i % boardParams.dim.w) * boardParams.fieldSize;
    let y = ((i - (i % boardParams.dim.w)) / boardParams.dim.w) * boardParams.fieldSize;
    drawShape(boardParams.startX + x, boardParams.startY + y, shape);
  }
};

const drawShape = (x, y, s) => {
  const shapes = {
    'w': {name: 'circle', color: 'white', img: document.getElementById("gem1")},
    'p': {name: 'triangle', color: 'purple', img: document.getElementById("gem2")},
    'r': {name: 'square', color: 'red', img: document.getElementById("gem3")},
    'y': {name: 'rhombus', color: 'yellow', img: document.getElementById("gem4")},
    'o': {name: 'hexagon', color: 'orange', img: document.getElementById("gem5")},
    'g': {name: 'hexagon', color: 'green', img: document.getElementById("gem6")},
    'b': {name: 'diamond', color: 'blue', img: document.getElementById("gem7")}
  };
  let shape = shapes[s];
  ctx.drawImage(shape.img, x, y);
};


const sendButton = () => {
  send(actions.out.NEW_GAME, null);
};

const send = (action, data) => {
  let message = {action, data};
  console.log("sending:", message);
  socket.send(JSON.stringify(message));
};

const getField = (x, y) => {
  x -= canvas.offsetLeft;
  x -= (boardParams.fieldSize / 2);
  x -= boardParams.startX;
  x /= boardParams.fieldSize;
  x = Math.round(x);

  y -= canvas.offsetTop;
  y -= (boardParams.fieldSize / 2);
  y -= boardParams.startY;
  y /= boardParams.fieldSize;
  y = Math.round(y);

  return y * 8 + x;
};
