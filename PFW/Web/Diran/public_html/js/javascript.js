/*
 * JAVASCRIPTS
 */

//# XHTML COMPATIBLE -> TARGET="_BLANK"
$("a[rel^='external']").not('.nav').attr("target","_blank");

// Image FadeIn
$('img').each( function(){
	var current = $(this);
	newImage = new Image();
	newImage.src = current.attr('src');
	newImage.onload = function(){
		current.css('opacity', 0).animate({'opacity' : 1}, 'slow').css('background-image', 'none'); 
	};
});

// Royal Slider
jQuery(document).ready(function($) {
	var sliderInstance = new Array();
	var sliderThumb = new Array();
	var sliderNav = new Array();
	var sliderId = false;
	
	$('.slider.autoload').each( function(i){
		sliderInstance[i] = $(this).find('.screen').royalSlider({
			keyboardNavEnabled: true,
			arrowsNav : false,
			autoPlay: {
				enabled: true,
				pauseOnHover: true,
				delay: 7000
			}
		}).data('royalSlider');
		if(sliderInstance[i]){		
			$('.nav .prev a', $(this)).click( function(){
				sliderInstance[i].prev();
				return false;
			});
			$('.nav .next a', $(this)).click( function(){
				sliderInstance[i].next();
				return false;
			});
		}

		sliderThumb[i] = $('.thumb li a', $(this));
		sliderNav[i] = $('.nav', $(this));
		if(sliderInstance[i] && sliderThumb.length > 0){
			sliderThumb[i].click( function(){
				sliderThumb[i].removeClass('focus');
				$(this).addClass('focus');
				sliderId = sliderThumb[i].index($(this));
				sliderInstance[i].goTo(sliderId);
				return false;
			});
			sliderInstance[i].ev.on('rsAfterSlideChange', function() {
				sliderThumb[i].removeClass('focus').removeClass('active').eq(sliderInstance[i].currSlideId).addClass('active');
				navDisabled(sliderNav[i], sliderInstance[i]);
			});
		}
	});
	
	function navDisabled(nav, instance)
	{
		nav.find('a').removeClass('disabled');
		if(instance.currSlideId == 0){
			$('.prev a', nav).addClass('disabled');
		}else if(instance.currSlideId == instance.numSlides-1){
			$('.next a', nav).addClass('disabled');
		}		
	}
});