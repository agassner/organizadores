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

	$("#highlight-slide").append('<a href="javascript:void(0);" id="slider-stopper" class="rounded-corners-button">Parar</a>');

	sliderIntervalID = setInterval(function(){
		doMove(panelWidth, tooFar);
	}, delayLength);
	
	$("#slider-stopper").click(function(){
		if ($(this).text() == "Parar") {
			clearInterval(sliderIntervalID);
		 	$(this).text("Iniciar");
		}
		else {
			sliderIntervalID = setInterval(function(){
				doMove(panelWidth, tooFar);
			}, delayLength);
		 	$(this).text("Parar");
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
 * Execute the product slider.
 */
function slideProduct(direction) {
    var $productsMover = $("#products-mover");
    var elementWidth = parseInt($(".products-slide").css("width")) + 10;
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

/**
 * Load the data/content on the slide highlight.
 */
function loadHighlightsSlideContent() {
    var url = "/products/highlights/slide";

    $.get(url, function(data) {
        $.each(data, function(i, item) {
            //var $highlightVertical = $("#highlight-vertical-" + (i + 1));
            //$highlightVertical.find("#highlight-title").text(item.fields.title);
            //$highlightVertical.find("#highlight-link").attr("href", item.fields.link);
            //$highlightVertical.find("#highlight-image").attr("src", "/media/" + item.fields.photo);
            //$highlightVertical.find("#highlight-content").text(item.fields.content);
        });
    });
}

/**
 * Load the data/content on the box highlight.
 */
function loadHighlightsBoxContent() {
    var url = "/products/highlights/box";

    $.get(url, function(data) {
        $.each(data, function(i, item) {
            var $highlightVertical = $("#highlight-vertical-" + (i + 1));
            $highlightVertical.find("#highlight-title").text(item.fields.title);
            $highlightVertical.find("#highlight-link").attr("href", item.fields.link);
            $highlightVertical.find("#highlight-image").attr("src", "/media/" + item.fields.photo);
            $highlightVertical.find("#highlight-content").text(item.fields.content);
        });
        
    });
}

/**
 * Load the data/content on the top list highlight.
 */
function loadHighlightsTopListContent() {
    var url = "/products/highlights/top";

    $.get(url, function(data) {
        var $highlightHorizontal = $("#highlight-horizontal");
        $.each(data, function(i, item) {
            var $productsSlide = $highlightHorizontal.find("#products-slide-" + (i + 1));
            $productsSlide.find("#highlight-link").attr("href", item.fields.link);
            $productsSlide.find("#highlight-image").attr("src", "/media/" + item.fields.photo);
            $productsSlide.find("#highlight-image").attr("alt", item.fields.title);
        });
        
    });
}

/**
 * On load.
 */
$(document).ready(function() {
	startStopSlider();
    loadSlideProduct();
    loadHighlightsSlideContent();
    loadHighlightsBoxContent();
    loadHighlightsTopListContent()
});

