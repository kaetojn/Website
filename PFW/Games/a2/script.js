var canvasGame = document.getElementById("canvas");
var ctxGame = canvasGame.getContext("2d");

var canvasInfo = document.getElementById("infoBar");
var ctxInfo = canvasInfo.getContext("2d");
ctxInfo.font = "70px ARCADECLASSIC";

var timer;
var timerFunc;
setInterval(draw_score, 100);
var resume;
var foods;
var canvas;
var bugs;
var list_food;
var list_bugs;
var score;
var clock;
var beginning;

game();

function game() {
	"use strict";
    timer = 60;
	clock = 1;
	
	list_bugs = [];
	list_food = [];
    bugs = 0;
	
    score = 0;
    resume = false;
	
    beginning = setInterval(draw_start, 1000);
    new_foods();
	
    timerFunc = setInterval(draw_time, 1000);
    canvas = setInterval(function() { drawGameView() }, 1);
}

function start() {
    var level1 = document.getElementById("level1");
    var level2 = document.getElementById("level2");
    if (typeof(Storage) !== "undefined") {
        window.location = 'Game.html';
    } else {
        alert("Not Supported");
    }
}

function draw_start() {
    if (clock >= 0) {
        ctxGame.clearRect(0, 0, 400, 600);
        ctxGame.save();
        ctxGame.font = "60px ARCADECLASSIC";
        ctxGame.fillStyle = "black";
		
        if (clock === 1) {
            var level = localStorage.getItem("level") === "level1" ? 1 : 2;
            ctxGame.fillText("level " + level, 110, 225, 180);
			
        } else if (clock > 0) {
            ctxGame.fillText(clock, 180, 225, 180);
			
        } else {
            ctxGame.fillText("Begin!", 130, 225, 180);
        }
        ctxGame.restore();
        clock--;
		
    } else {
        changeState();
        clearInterval(beginning);
    }
}

function draw_score() {
    ctxInfo.clearRect(240, 0, 100, 200);
    ctxInfo.fillText("Score: " + score, 200, 100, 100);
}

function draw_time() {
    if (timer >= 0 && resume) {
        ctxInfo.clearRect(0, 0, 100, 200);
        ctxInfo.fillText(timer + " sec", 10, 100, 50);
        timer--;
    } else if (timer < 0) {
        if (score > localStorage.getItem("highestScore" + localStorage.getItem("level"))) {
            localStorage.setItem("highestScore" + localStorage.getItem("level"), score);
        }
        gameOver(true);
    }
}

function changeState() {
    if (!resume) {
        pause();
        resume = true;
    } else if (resume) {
        play();
        resume = false;
    }
}

function pause() {
    ctxInfo.clearRect(100, 0, 100, 200);
    var rectangle = new Path2D();
    rectangle.rect(140, 50, 5, 60);
    rectangle.rect(150, 50, 5, 60);
    ctxInfo.fill(rectangle);
}

function play() {
    ctxInfo.clearRect(100, 0, 100, 200);

    var path = new Path2D();
    path.moveTo(160,80);
    path.lineTo(145,110);
    path.lineTo(145,50);
    ctxInfo.fill(path);
}

function drawGameView() {
    if (!resume) {
        return;
    }

    ctxGame.clearRect(0, 0, 400, 600);

    if (foods == 0) {
        gameOver(false);

        return;
    }

    bugs -= 10;
	
    if (bugs <= 0) {
        list_bugs.push(new Bug());
        bugs = Math.floor(Math.random() * 3000)+1000;
    }

    for (i = 0; i < list_food.length; i++) {
        if (!list_food[i].eaten) {
            list_food[i].draw();
        }
    }

    for (j = 0; j < list_bugs.length; j++) {
        var bug = list_bugs[j];
        bug.move();
    }

    for (i = 0; i < list_bugs.length; i++) {
        var bug1 = list_bugs[i];
        for (j = i + 1; j < list_bugs.length; j++) {
            var bug2 = list_bugs[j];
            if (bug1.alive && bug2.alive && cDist(bug1.xCoord, bug1.yCoord, bug2.xCoord, bug2.yCoord) <= 40) {
                if (bug1.speed == bug2.speed) {
                    if (bug1.xCoord < bug2.xCoord) {
                        bug1.moveBack();
                    } else {
                        bug2.moveBack();
                    }
                } 
            }
        }
    }

    for (j = 0; j < list_bugs.length; j++) {
        var bug = list_bugs[j];
        bug.draw();
    }
}

function gameOver(win) {
    clearInterval(canvas);
    clearInterval(timerFunc);
    

    ctxGame.clearRect(0, 0, 400, 600);

    if (win) {
        if (localStorage.getItem("level") == "level1") {
            localStorage.setItem("level", "level2");

            game();
            return;
        }
    }
    var level;
    if (win && localStorage.getItem("level") == "level2") {
        level = "level1";
    } else {
        level = localStorage.getItem("level");
    }

    if (win) {
        passed_level();
    }

    if (!win) {
        failed_level();
    }

    score_bar();
    score = 0;
    restart_level(level);
    MainMenu();
}

function failed_level() {
    ctxGame.save();
    ctxGame.font = "80px ARCADECLASSIC";
    ctxGame.fillStyle = "red";
    ctxGame.fillText("You failed", 25, 150, 345);
    ctxGame.restore();
}

function passed_level() {
    ctxGame.save();
    ctxGame.font = "80px ARCADECLASSIC";
    ctxGame.fillStyle = "yellow";
    ctxGame.fillText("You Did It", 25, 150, 345);
    ctxGame.restore();
}


function score_bar() {
    ctxGame.save();
    ctxGame.font = "40px ARCADECLASSIC";
    ctxGame.fillStyle = "black";
    ctxGame.fillText("You Scored: " + score + " points", 50, 300, 300);
    ctxGame.restore();
}

function restart_level(level) {
    ctxGame.save();
    ctxGame.font = "30px ARCADECLASSIC";
    ctxGame.fillStyle = "black";
    ctxGame.fillText("Restart", 140, 420, 180);

    window.addEventListener("click", restart, false);
    function restart(event) {
        x = event.pageX - canvasGame.offsetLeft;
        y = event.pageY - canvasGame.offsetTop;
        if (x >= 100 && x <= 300 && y >= 380 && y <= 440) {
            ctxGame.clearRect(0, 0, 400, 600);
            localStorage.setItem("level", level);
            window.removeEventListener('click', restart, false);
            game();
        }
    }
}

function MainMenu() {
    ctxGame.save();
    ctxGame.font = "30px ARCADECLASSIC";
    ctxGame.fillStyle = "black";
    ctxGame.fillText("Main Menu", 127, 525, 180);

    window.addEventListener("click", exit, false);
    function exit(event) {
        x = event.pageX - canvasGame.offsetLeft;
        y = event.pageY - canvasGame.offsetTop;
        if (x >= 100 && x <= 300 && y >= 480 && y <= 540) {
            ctxGame.clearRect(0, 0, 400, 600);
            window.location = "Start.html";
        }
    }
}

function new_foods() {
    for (i = 0; i < 7; i++) {
        var newFood = new food();
        while (newFood.overlapWith()) {
            newFood = new food();
        }
        list_food.push(newFood);
    }
    foods = 7;
}

function food() {
    this.xCoord = Math.floor(Math.random() * (350) + 10);
    this.yCoord = Math.floor(Math.random() * (450) + 130);
    this.eaten = false;

    this.draw = function() {
        var path = new Path2D();
        path.arc(this.xCoord, this.yCoord, 50, 10, 2 * Math.PI, false);
		var img = document.getElementById("apple");
    	ctxGame.drawImage(img, this.xCoord, this.yCoord);
        ctxGame.fillStyle = "white";
        ctxGame.fill(path);
    }

    this.overlapWith = function() {
        for (i = 0; i < list_food.length; i++) {
            if (Math.sqrt(Math.pow(this.xCoord - list_food[i].xCoord, 2) + Math.pow(this.yCoord - list_food[i].yCoord, 2)) <= 20) {
                return true;
            }
        }
        return false;
    }
}

function Bug() {
    this.alive = true;
    this.xCoord = Math.floor(Math.random() * (381) + 10);
    this.yCoord = 0;
    this.opacity = 1;
    this.lastMoveType;
    this.lastRot;
    this.lastMoveX;
    this.lastMoveY;
    this.width = 16;
    this.height = 44;

    this.findNearestFood = function() {
        var minDist = Number.MAX_VALUE;
        var result;
        for (i = 0; i < list_food.length; i++) {
            var food = list_food[i];
            var dist = cDist(this.xCoord, this.yCoord, food.xCoord, food.yCoord);
            if (!food.eaten && dist < minDist) {
                result = food;
                minDist = dist;
            }
        }
        return result;
    }

    this.chooseColor = function() {
        var colorArray = ["black", "red", "orange"];
        var num = Math.random();
        if (num < 0.3) {
            return colorArray[0];
        } else if (0.3 <= num && num < 0.6) {
            return colorArray[1];
        } else {
            return colorArray[2];
        }
    }

    this.getDirection = function() {
        var result = Math.atan2(this.targetFood.yCoord - this.yCoord, this.targetFood.xCoord - this.xCoord) + Math.PI / 2;
        if (result > 2 * Math.PI) {
            result -= 2 * Math.PI
        } else if (result < 0) {
            result += 2 * Math.PI;
        }
        return result;
    }

    this.getSpeed = function() {
        if (this.color == "black") {
            if (localStorage.getItem("level") == "level2") {
                return 0.2;
            } else {
                return 0.15;
            }
        } else if (this.color == "red") {
            if (localStorage.getItem("level") == "level2") {
                return 0.1;
            } else {
                return 0.075;
            }
        } else if (this.color == "orange") {
            if (localStorage.getItem("level") == "level2") {
                return 0.08;
            } else {
                return 0.06;
            }
        }
    }

    this.getScore = function() {
        if (this.color == "black") {
            return 5;
        } else if (this.color == "red") {
            return 3;
        } else if (this.color == "orange") {
            return 1;
        }
    }

    this.color = this.chooseColor();
    this.speed = this.getSpeed();
    this.score = this.getScore();
    this.targetFood = this.findNearestFood();
    this.direction = this.getDirection();

    this.draw = function() {
        ctxGame.save();
        var path = new Path2D();

        ctxGame.fillStyle = this.color;
        ctxGame.strokeStyle = this.color;
        ctxGame.globalAlpha = this.opacity;

        ctxGame.translate(this.xCoord, this.yCoord);
        ctxGame.rotate(this.direction);

        path.arc(0, -10, 4, 0, 5 * Math.PI, false);
        path.ellipse(0, 0, 5, 3, 90 * Math.PI/180, 0, 2 * Math.PI);
        ctxGame.fill(path);

        ctxGame.beginPath();


        ctxGame.stroke();
        ctxGame.restore();
    }

    this.move = function() {
        if (this.alive) {
			
            this.targetFood = this.findNearestFood();
	
            if (this.targetFood == null) {
                return;
            }
            if (cDist(this.xCoord, this.yCoord, this.targetFood.xCoord, this.targetFood.yCoord) < 10) {
                this.targetFood.eaten = true;
                foods--;
            }
            var rightDirection = this.getDirection();
			
            if (Math.abs(this.direction - rightDirection) > 0.1) {
                this.lastMoveType = "rotation";
                this.lastRot = ((rightDirection - this.direction) / 10);
                this.direction += this.lastRot;
				
            } else {
                this.lastMoveType = "forward";
                this.lastMoveX = (Math.sin(this.direction) * this.speed);
                this.lastMoveY = -(Math.cos(this.direction) * this.speed);
                this.xCoord += this.lastMoveX;
                this.yCoord += this.lastMoveY;
            }
        } else {
			
            if (this.opacity > 0.005) {
                this.opacity -= 0.005;
            }
        }
    };

    this.moveBack = function() {
        if (this.lastMoveType === "rotation") {
            this.direction -= this.lastRot;
            this.lastRot = 0;
			
        } else if (this.lastMoveType === "forward") {
            this.xCoord -= this.lastMoveX;
            this.yCoord -= this.lastMoveY;
            this.lastMoveX = 0;
            this.lastMoveY = 0;
        }
    }
}

function cDist(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
}

window.addEventListener("click", doMouseDown, false);
function doMouseDown(event) {
  x = event.pageX - canvasInfo.offsetLeft;
  y = event.pageY - canvasInfo.offsetTop;
  
  if (x >= 190 && x <= 220 && y >= 27 && y <=60) {
     changeState();
  }
}

canvasGame.addEventListener('click', function(evt) {
    x = evt.pageX - canvasGame.offsetLeft;
    y = evt.pageY - canvasGame.offsetTop;
	
    for (i = 0; i < list_bugs.length; i++) {
        var bug = list_bugs[i];
		
        if (bug.alive) {
            var dist = Math.sqrt( Math.pow((x - bug.xCoord), 2) + Math.pow((y- bug.yCoord), 2) );
			
            if (dist <= 30){
                bug.alive = false;
                score += bug.score;
            } 
        }
    }
}, false); 

function level_and_highscore() {
    var level1 = document.getElementById("level1");
    var level2 = document.getElementById("level2");
	
    if (level1.checked) {
        localStorage.setItem("level", level1.value);
		
    } else if (level2.checked) {
        localStorage.setItem("level", level2.value);
    }
    
    var highscore = document.getElementById("score_count");
    highscore.innerHTML = localStorage.getItem("highestScore" + localStorage.getItem("level")) == null ?
        0 : localStorage.getItem("highestScore" + localStorage.getItem("level"));
}

