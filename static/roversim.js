var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

let width = canvas.width;
let height = canvas.height;
let posx = width / 2;
let posy = height / 2;
let rotation = 0;

let speed = 0;
let turn = 0;

socket.on('set-speed', function (data) {
	speed = data["speed"];
	turn = data["turn"];
});

function clear() {
	ctx.rect(-1, -1, width + 2, height + 2);
	ctx.fillStyle = "white";
	ctx.fill();
	// ctx.closePath();
}

function draw_rover() {
	ctx.save();
	ctx.translate(posx, posy);
	ctx.rotate(rotation * Math.PI / 180);

	ctx.beginPath();
	ctx.fillStyle = "rgb(0,0,0)";
	ctx.rect(-20, -40, 40, 80);
	ctx.fill();
	ctx.stroke();

	ctx.beginPath();
	ctx.fillStyle = "rgb(100,100,255)";
	ctx.rect(10, -40, 10, 20);
	ctx.rect(-20, -40, 10, 20);
	ctx.fill();
	ctx.stroke();

	ctx.restore();
}

function redraw() {
	clear();
	draw_rover();
}

function roversim() {
	rotation += turn;
	if (rotation > 180) rotation -= 360;
	else if (rotation < -180) rotation += 360;
	posy += speed * Math.cos((Math.PI / 180) * rotation * -1);
	posx += speed * Math.sin((Math.PI / 180) * rotation * -1);
	redraw();
	setTimeout(roversim, 10);
}

roversim();