/**
 * Execute the slide movement.
 */
function doMove(panelWidth, tooFar) {
	var leftValue = $("#mover").css("left");
	
	// Fix for IE
	if (leftValue == "auto") {
        leftValue = 0;
    };
	
	var movement = parseFloat(leftValue, 10) - panelWidth;
	
	if (movement == tooFar) {
		$(".slide img").animate({
			"top": -350
		}, function() {
			$("#mover").animate({
				"left": 0
			}, function() {
				$(".slide img").animate({
					"top": 30
				});
			});
		});
	} else {
		$(".slide img").animate({
			"top": -350
		}, function() {
			$("#mover").animate({
				"left": movement
			}, function() {
				$(".slide img").animate({
					"top": 30
				});
			});
		});
	}
}

/**
 * Initialize the start/stop slider.
 */
function startStopSlider() {
    var delayLength = 10000;
	
    var $slide1 = $("#slide-1");

	var panelWidth = $slide1.css("width");
	var panelPaddingLeft = $slide1.css("paddingLeft");
	var panelPaddingRight = $slide1.css("paddingRight");

	panelWidth = parseFloat(panelWidth, 10);
	panelPaddingLeft = parseFloat(panelPaddingLeft, 10);
	panelPaddingRight = parseFloat(panelPaddingRight, 10);

	panelWidth = panelWidth + panelPaddingLeft + panelPaddingRight;
	
	var numPanels = $(".slide").length;
	var tooFar = -(panelWidth * numPanels);
	var totalMoverwidth = numPanels * panelWidth;
	$("#mover").css("width", totalMoverwidth);

	$("#highlight-slide").append('<a href="javascript:void(0);" id="slider-stopper" class="rounded-corners-button">Stop</a>');

	sliderIntervalID = setInterval(function(){
		doMove(panelWidth, tooFar);
	}, delayLength);
	
	$("#slider-stopper").click(function(){
		if ($(this).text() == "Stop") {
			clearInterval(sliderIntervalID);
		 	$(this).text("Start");
		}
		else {
			sliderIntervalID = setInterval(function(){
				doMove(panelWidth, tooFar);
			}, delayLength);
		 	$(this).text("Stop");
		}
		 
	});

}

/**
 * Load some slide product config.
 */
function loadSlideProduct() {
    $("#prev").click(function(){
        slideProduct("prev");
    });

    $("#next").click(function(){
        slideProduct("next");
    });
}

/**
 * Executes a manual slider.
 */
function slideProduct(direction) {
    var $productsMover = $("#products-mover");
    var elementWidth = parseInt($("#products-slide").css("width")) + 10;
    var maxMovement = parseInt($productsMover.css("width")) - elementWidth;
    var position = parseInt($productsMover.css("left"));

    var movement = "0";

    if (direction == "next") {
        if ((position * -1) < maxMovement) {
            movement = "-=" + elementWidth;
        }
    } else if (direction == "prev") {
        if (position < 0) {
            movement = "+=" + elementWidth;
        }
    }

    if (movement != 0) {
        $productsMover.animate({
            left: movement
        });
    }
}

function loadHighlightsBoxContent() {
    var url = "http://localhost/products/highlights/box";

    $.get(url, function(data) {
        $.each(data, function(i, item) {
            var $highlightVertical = $("#highlight-vertical-" + (i + 1));
            $highlightVertical.find("#highlight-title").text(item.fields.title);
            // $highlightVertical.find("#highlight-link").text(item.fields.);
            // $highlightVertical.find("#highlight-image");
            $highlightVertical.find("#highlight-content").text(item.fields.content);
        });
        
    });
}

$(document).ready(function() {
	startStopSlider();
    loadSlideProduct();
    loadHighlightsBoxContent();
});

