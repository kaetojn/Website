const $ = document.querySelector.bind(document);
const name = $(".name");
const pron = $(".pron");
const tag = $(".tag");
const con1 = $(".contentContainer")
const con2 = $("#skills")
const con3 = $(".project")
const con4 = $(".experiences")
const con5 = $(".allinterests")
const con6 = $(".ig")


function transformLetters() {
	const scroll = window.scrollY;
	name.style.transform = `translate3d(0, ${scroll*2}px, 0) rotateY(${-scroll*0.03}deg)` 
	pron.style.transform = `translate3d(${-scroll*5}px, ${scroll*0.95}px, 0) rotateX(${-scroll*0.1}deg)`;
	tag.style.transform = `translate3d(${scroll*5}px, ${scroll*1.05}px, 0) rotateX(${scroll*0.3}deg)`;

}


//***************************************************************

function trasformcc(){
	const scrollcc = window.scrollY;
	if (scrollcc >= 700){
		con1.style.left = `${-((scrollcc)-680)}vh`;
		//con1.style.right = `${(scrollcc)+520}vh`;

	}
		else{
			con1.style.left = `20vh`;
		}
	}

function cc1(){
	window.removeEventListener('scroll', trasformcc, false);
	con1.style.left = `20vh`;
	setTimeout(cc11, 100);
}

function cc11(){
	window.addEventListener("scroll", trasformcc);
}
//***************************************************************


//***************************************************************
function trasformcc2(){
	const scrollcc = window.scrollY;
	if (scrollcc >= 1400){
		con2.style.left = `${(scrollcc)-1380}vh`;}
	else{
			con2.style.left = `20vh`;
		}
	}
function cc2(){
	window.removeEventListener('scroll', trasformcc2, false);
	con2.style.left = `20vh`;
	setTimeout(cc22, 100);
}
function cc22(){
	window.addEventListener("scroll", trasformcc2);
}
//***************************************************************


//***************************************************************

function trasformcc3(){
	const scrollcc = window.scrollY;
	if (scrollcc >= 1900){
		con3.style.left = `${-((scrollcc)-1880)}vh`;}
		else{
			con3.style.left = `20vh`;
		}
	}

function cc3(){
	window.removeEventListener('scroll', trasformcc3, false);
	con3.style.left = `20vh`;
	setTimeout(cc33, 100);
}
function cc33(){
	window.addEventListener("scroll", trasformcc3);
}
//***************************************************************


//***************************************************************
function trasformcc4(){
	const scrollcc = window.scrollY;
	console.log(scrollcc);
	if (scrollcc >= 2700){
		con4.style.left = `${(scrollcc)-2680}vh`;}
		else{
			con4.style.left = `20vh`;
		}
	}

function cc4(){
	window.removeEventListener('scroll', trasformcc4, false);
	con4.style.left = `20vh`;
	setTimeout(cc44, 100);
}
function cc44(){
	window.addEventListener("scroll", trasformcc4);
}
//***************************************************************


//***************************************************************
function trasformcc5(){
	const scrollcc = window.scrollY;
	if (scrollcc >= 3300){
		con5.style.left = `${-((scrollcc)-3280)}vh`;}
		else{
			con5.style.left = `20vh`;
		}
	}

function cc5(){
	window.removeEventListener('scroll', trasformcc5, false);
	con5.style.left = `20vh`;
	setTimeout(cc55, 100);
}
function cc55(){
	window.addEventListener("scroll", trasformcc5);
}
//***************************************************************


//***************************************************************
function trasformcc6(){
	const scrollcc = window.scrollY;
	if (scrollcc >= 4000){
		con6.style.left = `${((scrollcc)-3980)}vh`;}
		else{
			con6.style.left = `20vh`;
		}
	}

function cc6(){
	window.removeEventListener('scroll', trasformcc6, false);
	con6.style.left = `20vh`;
	setTimeout(cc66, 100);
}
function cc66(){
	window.addEventListener("scroll", trasformcc6);
}
//***************************************************************


window.addEventListener("scroll", transformLetters);
window.addEventListener("scroll", trasformcc);
window.addEventListener("scroll", trasformcc2);
window.addEventListener("scroll", trasformcc3);
window.addEventListener("scroll", trasformcc4);
window.addEventListener("scroll", trasformcc5);
window.addEventListener("scroll", trasformcc6);
