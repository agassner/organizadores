function viewProduct(id) {
    var url = "/products/" + id + "/";
    $.get(url, function(data) {
        var $popin = $("#popin-dialog-modal");
        var product = data[0].fields;
        $popin.dialog({
            width: 600,
			height: 450,
			modal: true,
            title: product.name
		});
        $popin.find("#product-image").attr("src", "/media/" + product.photo);
        $popin.find("#product-text").html(product.full_description.replace(/\r\n/g, '<br/>'));
        $popin.find("#product-price").html("R$ " + product.price);
        $popin.find("#product-link").attr("href", product.buy_link);
    });
}

/**
 * On load.
 */
$(document).ready(function() {
    $("#popin-dialog-modal").hide();
});
